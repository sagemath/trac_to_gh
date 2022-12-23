# Issue 3745: calculus -- bug in solve

Issue created by migration from https://trac.sagemath.org/ticket/3745

Original creator: was

Original creation time: 2008-07-30 12:45:59

Assignee: gfurnish


```
On Tue, Jul 29, 2008 at 6:05 PM, jamlatino <medrano.antonio@gmail.com> wrote:
>
> While working on the video tutorial for Sage I tried the following
> equation:
>
> (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) - (2*cos(x)*sin(x) -
> sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))
>
> if I use find_root in the interval 1,2 I get the following answer:
> 1.9106332362490561
>
> but when I use solve to find the solution I get
> [x == pi, x == pi/2, x == 0]
>
> pi/2 is 1.57, but when I try find_root in the interval 1.5,1.6 it
> tells me that the equation has no zero in that interval, can someone
> explain??

This appears to me to be a bug as pi/2 is not a solution.
If you do the following it is pretty clear that the 0's are
at 0, 1.9..., etc. and not at pi/2:

sage: f = (sin(x) - 8*cos(x)*sin(x))*(sin(x)^2 + cos(x)) -
(2*cos(x)*sin(x) - sin(x))*(-2*sin(x)^2 + 2*cos(x)^2 - cos(x))
sage: f(pi/2)
-1
sage: f.plot(-1,4)

Sage finds the numerical 0's using a numerical root
finder (from scipy).

Sage finds the exact solutions by calling the computer
algebra system Maxima, which indeed strangely claims that pi/2 is a solution:

(%i1) solve((sin(x)-8*cos(x)*sin(x))*(sin(x)^2+cos(x))-(2*cos(x)*sin(x)-sin(x))*(-2*sin(x)^2+2*cos(x)^2-cos(x))=0,
x);

`solve' is using arc-trig functions to get a solution.
Some solutions will be lost.
                                        %pi
(%o1)                      [x = %pi, x = ---, x = 0]
                                         2

It looks like this might be a bug in Maxima's solve function.

There's not much for me to do besides:
  * report this to the maxima folks (I've cc'd Robert Dodier
in this email),
  * completely rewrite Sage's solve to not use Maxima.

From Robert Dodier:


Yup, that's a bug, all right ... I'll make a bug report.

>    * completely rewrite Sage's solve to not use Maxima.

Well, if you do that, please write it in pure Python so it is easier
to translate to Lisp.

Maxima's code for solving equations has more than a few bugs,
and it's not clear what classes of problems it can handle, nor is
it clear what method is used for each class, and there certainly
are interesting and useful equations which it just can't handle.
All of this motivates a complete rewrite. Not that I'm volunteering;
not yet, anyway.

FWIW

Robert Dodier
```


I think we need to rewrite solve for Sage.  Any volunteers?  It will have to wait until we change to use either "Gary's symbolics" or "Sympy" for Sage's symbolics, since the current symbolics likely don't support enough to make implementing solve practical.


---

Comment by rlm created at 2008-08-13 00:10:30

Also:

```
sage: var('a b c')
sage: eqn1 = a - exp((-pi*b)/sqrt(1-b)) == 0
sage: eqn2 = c - atan(2*b*sqrt(1/(sqrt(4*b^4+1) - 2*b^2)))==0
sage: solve([eqn1,eqn2,a==0.1975],b,c,a) 
[]
```



---

Comment by rlm created at 2008-08-13 04:39:04

And even:

```
sage: var('a,b,c,d')
sage: m = matrix(2,[a,b,c,d])
sage: i2=identity_matrix(SR,2)
sage: eqlist=[(m*m).list()[i] - i2.list()[i] for i in range(4)]
sage: solve(eqlist,a,b,c,d) 
Traceback (most recent call last):
...
ValueError: Unable to solve [b*c + a^2 - 1, b*d + a*b, c*d + a*c, d^2 + b*c - 1] for (a, b, c, d)
```



---

Comment by kcrisman created at 2009-09-15 18:40:19

Note this particular bug is still in Maxima as of 5.19.1.  More bugs (but also lots more correct answers) have been introduced in the last year, and other bugs  have been fixed.  Writing a solve from scratch still looks very hard.


---

Comment by kcrisman created at 2009-12-24 03:27:53

Update from Maxima 5.20.1 in Sage:

```
sage: sage: var('a,b,c,d')
(a, b, c, d)
sage: sage: m = matrix(2,[a,b,c,d])
sage: sage: i2=identity_matrix(SR,2)
sage: sage: eqlist=[(m*m).list()[i] - i2.list()[i] for i in range(4)]
sage: sage: solve(eqlist,a,b,c,d) 
[a^2 + b*c - 1, a*b + b*d, a*c + c*d, b*c + d^2 - 1]
```

so this one seems to be working now, at least in the sense that it doesn't throw an error.  

The second one now causes a hang.

And the first one is still there :(


---

Comment by was created at 2009-12-24 20:33:42

<irrelevant rant>
We should write our own native solve from scratch.  Depending on maxima for solve is silly, for several reasons:

  * For algebraic systems we could do much better using Groebner basis and singular. 

  * Coefficients for symbolic expressions can be in many base rings that don't even make sense to Maxima.

</irrelevant rant>


---

Comment by kcrisman created at 2013-01-20 01:42:12

It could be worth trying these with #13364.


---

Comment by kcrisman created at 2014-11-21 13:36:08

https://sourceforge.net/p/maxima/bugs/2846/


---

Comment by kcrisman created at 2014-11-21 13:59:11

The one in comment:1 hangs for me as before, but upon Ctrl-C it does give `[]`.  For what it's worth.  Though in Maxima I got 

```
(%i1) solve([a - exp((-pi*b)/sqrt(1-b)) = 0, c - atan(2*b*sqrt(1/(sqrt(4*b^4+1) - 2*b^2)))=0,a=0.1975],[b,c,a]);

rat: replaced -0.1975 by -79/400 = -0.1975
(%o1)                                 []
```

almost immediately.  So I'm not sure why it hangs.  Is there even a solution to that?  It seems quite arbitrary.


---

Comment by kcrisman created at 2014-11-21 13:59:58

> https://sourceforge.net/p/maxima/bugs/2846/
By the way, in the original report which has been erased, a Maxima dev suggested he'd reported this, so perhaps this is redundant, but I don't know where it would be.


---

Comment by zonova created at 2016-11-27 01:02:09

I would like to point out that this bug still exists, 7 years later. There were a couple other cases of maxima's solve giving an incorrect answer (for eg, giving 0 when the function is undefined at 0). I am interested in studying this problem, does anyone have any recommendations on what would make for a better equation solver? And, if possible, some information on why Maxima's isn't great?


---

Comment by kcrisman created at 2016-11-28 15:46:51

Basically, the short answer is that solving in general cases isn't easy.  The long answer is that Maxima's is reasonable but often has small changes that impact other things.  You are likely to get some response on the Maxima email list if you mention this bug.  But writing a new one from scratch isn't a good idea; on the other hand, perhaps [sympy](http://www.sympy.org/en/index.html)'s solver is now ready to swap in for Maxima's in Sage, I don't know.  We do have both available.
