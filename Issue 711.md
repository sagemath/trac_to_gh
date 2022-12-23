# Issue 711: control-c and singular interface -- it doesn't quit singular for real.

Issue created by migration from https://trac.sagemath.org/ticket/711

Original creator: was

Original creation time: 2007-09-20 18:19:40

Assignee: was


```
sage: P = PolynomialRing(QQ,10,'x')
sage:  I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis()
Interrupting Singular...
Interrupting Singular...

<type 'exceptions.TypeError'>: Restarting Singular (WARNING: all variables defined in previous session are now invalid)
```

but singular is still running!


---

Comment by was created at 2007-09-21 01:01:07

Resolution: fixed
