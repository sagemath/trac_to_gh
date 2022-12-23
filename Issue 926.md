# Issue 926: MPolynomial Iterator

Issue created by migration from https://trac.sagemath.org/ticket/926

Original creator: malb

Original creation time: 2007-10-19 09:59:18

Assignee: malb

SAGE should support iterating over sparse multivariate polynomials like this:

```
sage: P.<x,y,z> = PolynomialRing(QQ,3)
sage: f= 3*x^3*y + 16*x + 7
sage: for c,m in f:
....:     print c,m
....:
3, x^3*y
16, x
7,1
```



---

Comment by robertwb created at 2007-10-20 20:25:08

Changing assignee from malb to robertwb.


---

Attachment


---

Comment by was created at 2007-10-21 03:24:11

Resolution: fixed
