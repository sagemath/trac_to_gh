# Issue 7839: Failure to coerce q^(-1) into its own LaurentPolynomialRing

Issue created by migration from https://trac.sagemath.org/ticket/7839

Original creator: bump

Original creation time: 2010-01-04 04:47:29

Assignee: AlexGhitza

CC:  sage-combinat

Consider:


```
sage: P.<q> = LaurentPolynomialRing(QQ)
sage: q in P
True
sage: P(q)
q
sage: q^(-1) in P
True
sage: P(q^(-1))
```


The last statement raises an exception.


---

Comment by mhansen created at 2010-01-19 21:55:38

This is a duplicate of #3617 which should be fixed soon.


---

Comment by mhansen created at 2010-01-19 21:55:38

Resolution: duplicate
