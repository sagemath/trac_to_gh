# Issue 419: row reduction for matrices over multivariate polynomial rings

Issue created by migration from https://trac.sagemath.org/ticket/419

Original creator: malb

Original creation time: 2007-08-10 15:26:18

Assignee: was

Consider


```
sage: P.<x,y> = PolynomialRing(GF(2),2)
sage: A = Matrix(P,2,2,[1,x,x,x+1]); A

[    1     x]
[    x x + 1]

```


`A.echelon_form()` returns the identity matrix because it computes the reduced echelon form over a fraction field and not over the polynomial ring.  However, SINGULAR has a (educational == slow) `rowred` command to perform row reduction as far as this is possible over the polynomial ring. This behaviour is desired in several applications and thus it should be ported to SAGE.

In fact, I've got an implementation/port of this already (c.f. https://sage.math.washington.edu:8102/home/pub/35/) it just needs to be named and included with SAGE.


---

Comment by malb created at 2007-08-10 19:38:13

Changing status from new to assigned.


---

Comment by malb created at 2007-08-10 19:38:13

Changing assignee from was to malb.


---

Comment by malb created at 2007-09-03 13:55:30

fixed in 2.8.3


---

Comment by malb created at 2007-09-03 13:55:30

Resolution: fixed
