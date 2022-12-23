# Issue 1236: tate pairings on elliptic curves -- add to sage

Issue created by migration from https://trac.sagemath.org/ticket/1236

Original creator: was

Original creation time: 2007-11-21 16:22:42

Assignee: was

CC:  cremona mariah aly.deines jdemeyer


```

Hi, I needed some calculation period benchmark for pairings. I could
not find anything build in, but the following implementation solved my
problem:

http://maths.straylight.co.uk/archives/104
```



---

Comment by was created at 2007-11-21 16:23:28


```

Thanks!  I've made adding this to Sage proper ticket

   http://trac.sagemath.org/sage_trac/ticket/1236

Can you make some sort of GPL-compatible license statement about your code,
if you haven't already?

William
```



---

Comment by was created at 2007-11-21 16:37:58


```
William Stein to sage-support
	
show details 8:35 AM (1 minute ago)
	
	
	
Reply
	
	
On Nov 21, 2007 8:24 AM, Ondrej Certik <ondrej@certik.cz> wrote:
>
> > I think in the long-run Sage will have to completely implement its own solve
> > function, which is better than Maxima's.  Thoughts from Ondrej-sympy would be
> > appreciated here.
>
>
> Isn't solve supposed to return an analylic solution only? Is there an
> analytic solution to this equation? It doesn't seem so to me.

I don't like that meaning for solve, since it is misleading to me, and
is inconsistent. e.g., what about:

sage: solve(x^5 + x^3 + 1, x)
[0 == x^5 + x^3 + 1]

When there is no explicit solution, maxima usually returns something
to explicitly indicate this.

Also, as a data point, Maple returns an approximate solution if
it doesn't find an exact one:

sage: maple.eval('solve(38.40000000*exp(1)^(-1200*t)-9.600000000*exp(1)^(-300*t),
t)')
'.1540327068e-2'

Likewise with Mathematica:

sage: mathematica.eval('Solve[0.004*(9600/E^(1200*t) - 2400/E^(300*t))
## 0, t]')

Solve::ifun: Inverse functions are being used by Solve, so some solutions may
    not be found; use Reduce for complete solution information.

        {{t -> 0.00154033}}


sage: mathematica('x^5 + x^3 + 1 == 0').Solve(x)

{{x -> Root[1 + #1^3 + #1^5 & , 1, 0]},
 {x -> Root[1 + #1^3 + #1^5 & , 2, 0]},
 {x -> Root[1 + #1^3 + #1^5 & , 3, 0]},
 {x -> Root[1 + #1^3 + #1^5 & , 4, 0]}, {x -> Root[1 + #1^3 + #1^5 & , 5, 0]}}



> My thoughts on these issues are still the same - slowly replacing
> Maxima with our own things in Python, that are easy to fix and easy to
> extend. But they need to do the same things as Maxima first (and be as
> fast as Maxima).

Shouldn't we be able to write something that is way faster than Maxima?
What do people even benchmark in the context of calculus?


```



---

Comment by was created at 2007-11-21 17:02:51

disregard above comment


---

Comment by davidloeffler created at 2009-07-20 19:46:14

Assigned to new "elliptic curves" component.


---

Comment by davidloeffler created at 2009-07-20 19:46:14

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:46:14

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-10-09 09:10:53

Remove assignee davidloeffler.


---

Comment by zimmerma created at 2011-08-31 12:32:07

Changing status from new to needs_info.


---

Comment by zimmerma created at 2011-08-31 12:32:07

should this ticket be closed now that #10912 is fixed?

Paul


---

Comment by nestibal created at 2011-09-16 09:23:23

Changing status from needs_info to needs_review.


---

Comment by nestibal created at 2011-09-16 09:23:23

Weil, Tate and ate pairings are know implemented in sage. I think this ticket may be closed.

The reference
  [http://maths.straylight.co.uk/archives/104](http://maths.straylight.co.uk/archives/104)
shows implementation using elliptic net. This is not in sage now but this is not needed for the Tate pairing.


---

Comment by roed created at 2011-11-19 04:27:13

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-11-26 13:03:32

Resolution: duplicate
