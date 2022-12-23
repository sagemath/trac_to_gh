# Issue 1235: bug solving equations using maxima

Issue created by migration from https://trac.sagemath.org/ticket/1235

Original creator: was

Original creation time: 2007-11-21 16:08:22

Assignee: was


```
On Nov 20, 2007 12:28 PM, Ted Kosan <ted.kosan@gmail.com> wrote:
> Does anyone have any thoughts on why the solve() function this program
> returns an empty list?:
> 
> sage: var('t')
> sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t))
> - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) -
> 2400*e^(-(300*t)))^2
> sage: print a(t=.000411)
> sage: show(plot(a,0,.002),xmin=0, xmax=.002)
> sage: solve(a==0,t)

Maxima stupidly decides there is no solution.  This is clearly a bug.  This
is the sort of bug in Sage that is very difficult for us to fix since it's really
a bug in Maxima, and it's entirely possible that maxima developers would
not even call it a bug.  But clearly it is, since it's a mathematically incorrect result. 

Here's what happens when you try this in Maxima directly:

sage: !maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.41 (2006-10-13)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) solve(0.004*(8*%e^-(300*t)-8*%e^-(1200*t))*(720000*%e^-(300*t)-11520000*%e^-(1200*t))+0.004*(9600*%e^-(1200*t)-2400*%e^-(300*t))^2=0, t)
;
`rat' replaced 0.004 by 1/250 = 0.004
`rat' replaced 0.004 by 1/250 = 0.004
(%o1)                                 []


I strongly encourage you to report this to the maxima list, if you agree that it is
a bug in Maxima. 

I think in the long-run Sage will have to completely implement its own solve
function, which is better than Maxima's.  Thoughts from Ondrej-sympy would be
appreciated here. 

> And why the solve() function in this program hangs?:
> 
> sage: var('t')
> sage: v = 0.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))
> sage: show(plot(v,0,.002),xmin=0,xmax = .002)
> sage: solve(v == 0,t)

Here maxima also gives the wrong answer:

sage: maxima(v == 0)
0.004*(9600*%e^-(1200*t)-2400*%e^-(300*t))=0
sage: maxima(v == 0).solve(t)
[]

Just to emphasize that in my opinion this is *definitely* a bug,
I've entered this into the tracker:

```



---

Comment by was created at 2007-11-21 17:03:01


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

Comment by was created at 2007-11-27 15:10:51

The following is relevant:


```
sage: var('t')
sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t)) - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))^2
sage: from scipy.optimize import brentq
sage: # Given two points x, y such that a(x) and a(y) have different sign, this
sage: # brentq uses "inverse quadratic extrapolation" to find a root of a in the
sage: # interval [x,y].  It has lots of extra tolerance and other options.
sage: brentq(a, 0, 0.002)
0.00041105140493493411
sage: show(plot(a,0,.002),xmin=0, xmax=.002)
```



---

Comment by was created at 2007-11-27 15:14:31


```
I don't know.  However, Ted, what do you think of the following, i.e.,
it is a way in Sage to solve your problem which is probably pretty
clean and flexible, and could certainly made a little more student
friendly?

sage: var('t')
sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t))
- 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) -
2400*e^(-(300*t)))^2
sage: from scipy.optimize import brentq
sage: # Given two points x, y such that a(x) and a(y) have different sign, this
sage: # brentq uses "inverse quadratic extrapolation" to find a root of a in the
sage: # interval [x,y].  It has lots of extra tolerance and other options.
sage: brentq(a, 0, 0.002)
0.00041105140493493411
sage: show(plot(a,0,.002),xmin=0, xmax=.002)

I.e., what we provide an numerical_root method so that
    a.numerical_root(x,y)
would fine a numerical root of a in the interval [x,y], if it exists?
It could be built on brentq.  The main thing we would have to add
is some sort of analysis to find x', y' in the interval so that a(x')
has different sign from a(y'), i.e., decide if there is a sign switch,
which could be doable for many analytically defined functions at least.
```



---

Attachment


---

Attachment

Seems good to me. Tested the patch (both parts).
It appears to work robustly in the cases I tried.


---

Comment by mabshoff created at 2007-12-09 13:15:52

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 13:15:52

Merged in 2.9.alpha2.


---

Attachment

This fixes a doctest failure on Redhat Linux 32-bit.


---

Comment by was created at 2007-12-10 15:34:40

Resolution changed from fixed to 


---

Comment by was created at 2007-12-10 15:34:40

Changing status from closed to reopened.


---

Comment by was created at 2007-12-10 15:34:40

Changing priority from major to blocker.


---

Comment by mabshoff created at 2007-12-10 21:02:06

Resolution: fixed


---

Comment by mabshoff created at 2007-12-10 21:02:06

Merged trac-1235-doctest_fix.patch   in 2.9.alpha5.
