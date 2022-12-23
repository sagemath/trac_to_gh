# Issue 154: gfan -- something wrong

Issue created by migration from https://trac.sagemath.org/ticket/154

Original creator: was

Original creation time: 2006-10-26 20:37:48

Assignee: was


```
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: i = ideal([x + y - 1])
sage: g = i.groebner_fan()
sage: g.tropical_basis()
Traceback (most recent call last):
...
KeyError: 'Dimension of homogeneity space'
```



---

Comment by was created at 2007-01-19 11:39:47

Resolution: fixed


---

Comment by was created at 2007-01-19 11:39:47

This is now fixed.
