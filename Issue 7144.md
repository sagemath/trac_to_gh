# Issue 7144: desolve does not use contrib_ode

Issue created by migration from https://trac.sagemath.org/ticket/7144

Original creator: robert.marik

Original creation time: 2009-10-06 20:18:17

Assignee: burcin

The following code fails

```
y=function('y',x)
eqn=x*diff(y,x)^2-(1+x*y)*diff(y,x)+y == 0
desolve(eqn,y)
```

However, Maxima is able to produce the solution using contrib_ode command. If ode2 fails, Sage should call contrib_ode

maxima commands

```
load('contrib_ode)$
eqn:x*'diff(y,x)^2-(1+x*y)*'diff(y,x)+y=0;
contrib_ode(eqn,y,x);
```



---

Comment by robert.marik created at 2009-10-07 11:43:08

Resolution: duplicate


---

Comment by mvngu created at 2009-10-14 17:11:17

Closed as duplicate of #6479.
