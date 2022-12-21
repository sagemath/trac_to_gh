# Issue 9421: desolve mixes user parameters and integration constants

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-07-03 13:56:02

Assignee: burcin

CC:  robert.marik kcrisman

Consider

```
sage: var('t')
sage: x=function('x',t)
sage: var('c')
sage: desolve(diff(x,t)+2*x==t^2-2*t+c,x,ivar=t).expand()
c*e^(-2*t) + 1/2*t^2 + 1/2*c - 3/2*t + 3/4
```

Here the first occurrence of `c` is an integration constant,
whereas the second one is the parameter in the ODE:

```
sage: var('d')
sage: desolve(diff(x,t)+2*x==t^2-2*t+d,x,ivar=t).expand()
c*e^(-2*t) + 1/2*t^2 + 1/2*d - 3/2*t + 3/4
```

In case the ODE contains `c`, desolve should choose another
name for the integration constant.


---

Comment by robert.marik created at 2010-07-04 15:52:27

This is a part of more general problem which has been reported in #6882.


---

Attachment


---

Comment by zimmerma created at 2013-08-25 13:27:12

Changing status from new to needs_review.


---

Comment by zimmerma created at 2013-08-25 13:27:12

waiting for the general problem to be solved, the attached patch prints a warning if the given equation contains the variable `c`.

Paul


---

Comment by rws created at 2014-03-25 10:15:21

I will OK this if you have a look at #8734 in turn, please 8)  See also #16007


---

Comment by rws created at 2014-03-25 10:15:21

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2014-03-25 21:07:37

thus should we have a dependency on #8734?

Paul


---

Comment by rws created at 2014-03-26 04:42:26

Replying to [comment:7 zimmerma]:
> thus should we have a dependency on #8734?

Then everything waits for that review, which could take forever. But I want the warning now.


---

Comment by nbruin created at 2014-03-26 05:48:15

You might want to consider this one too:

```
sage: desolve(diff(f(x),x,x)-f(x),f(x))
k2*e^(-x) + k1*e^x
```

We can recognize the variables as distinct before they are converted from maxima:

```
sage: function('f',x)
f(x)
sage: var('c')
c
sage: V=diff(f(x),x)-f(x)+c
sage: v=maxima_calculus(V)
sage: v.ode2(f(x),x)
'f(x)=(c*%e^-x+%c)*%e^x
sage: v.ode2(f(x),x).ecl()
<ECL: ((MEQUAL SIMP) ((%F SIMP) $X)
 ((MTIMES SIMP)
  ((MPLUS SIMP) $%C
   ((MTIMES SIMP) $C ((MEXPT SIMP) $%E ((MTIMES SIMP) -1 $X))))
  ((MEXPT SIMP) $%E $X)))>
```

so perhaps the right solution is to warn when sage's "forget the %" causes a name collision (with the righter solution being: making sage's "forget the %" more intelligent, so that collisions can be avoided)


---

Comment by rws created at 2014-03-26 16:03:24

With #16007 the output is now

```
sage: sage: x=function('x',t)
sage: sage: var('c')
c
sage: sage: desolve(diff(x,t)+2*x==t^2-2*t+c,x,ivar=t).expand()
1/2*t^2 + _C*e^(-2*t) + 1/2*c - 3/2*t + 3/4

sage: desolve(diff(f(x),x,x)-f(x),f(x))
_K2*e^(-x) + _K1*e^x
```

As that's a simple and fine solution instead of a warning or an extended patch I would be glad if someone could review that one-liner.


---

Comment by vbraun created at 2014-03-31 15:03:53

Resolution: duplicate
