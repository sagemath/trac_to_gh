# Issue 247: bug in __contains__ for polynomial rings over ZZ

Issue created by migration from https://trac.sagemath.org/ticket/247

Original creator: William Stein

Original creation time: 2007-02-07 04:22:07

Assignee: somebody


```
age: R.<x,y,z,w> = ZZ['x,y,z,w']
sage: i = ideal(x^2 + y^2 - z^2 - w^2, x-y)
sage: j = i^2
sage: j.groebner_basis()
[y^2 - 2*x*y + x^2, y*w^2 + y*z^2 - 2*y^3 - x*w^2 - x*z^2 + 2*x*y^2, w^4 + 2*z^2*w^2 + z^4 - 4*y^2*w^2 - 4*y^2*z^2 + 4*y^4]
sage: y^2 - 2*x*y + x^2 in j
False
sage: 0 in j
False
```


The last two lines are WRONG!!


---

Comment by malb created at 2007-02-07 04:32:55

Changing assignee from somebody to malb.


---

Comment by malb created at 2007-02-07 05:02:39

Resolution: fixed


---

Comment by malb created at 2007-02-07 05:02:39

fixed in r2808
