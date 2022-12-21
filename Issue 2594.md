# Issue 2594: [with patch, needs review] MPolynomial_polydict __floordiv__ wrong arithmetic

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-03-19 11:56:35

Assignee: malb

The __floordiv__ special implementation for monomials throws away coefficients.


```
sage: R.<x,y,z>=ZZ[]
sage: f=3*x^2-1
sage: f//x
x
```


A patch is attached to fix this along with some other coercion issues.


---

Attachment

Patch looks good.


---

Comment by mabshoff created at 2008-03-19 23:38:07

Merged in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-19 23:38:07

Resolution: fixed
