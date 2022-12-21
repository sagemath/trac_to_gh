# Issue 3372: expand on (x+y)^n fails for non-commutative (x,y) [new symbolics]

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-06-05 19:33:16

Assignee: gfurnish


```
sage: var('x,y', MatrixSpace(QQ, 5, 5))
(x, y)
sage: ((x+y)^3).expand()
x^3 + x*y*x + y*x*x + x*y^2 + y*x^2 + x*y*y + y*x*y + y^3
```


This is the wrong answer (it has two terms `x*y*y` and `x*y^2`, when only one should exist; and it does not have an `x^2*y`); also, this answer is printed poorly (`x*y*y + ... + x*y^2` should simplify to `2*x*y^2 + ...`).


---

Comment by gfurnish created at 2008-07-18 10:39:27

Fixed in sage-symbolics commit 10238.  This was caused by an out of order list reordering while creating a symbolic product.


---

Comment by gfurnish created at 2008-07-18 10:39:27

Resolution: fixed


---

Comment by was created at 2008-08-23 08:14:14

Milestone sage-symbolics deleted
