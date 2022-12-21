# Issue 8779: Categories for polynomial rings

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-04-27 06:19:21

Assignee: nthiery

CC:  sage-combinat

Keywords: polynomial rings, categories


```
sage: QQ[x].categories()
[Category of commutative rings, Category of rings, ...]
```


This list should at least contain `EuclideanDomains()` and `GradedAlgebrasWithBasis(QQ)`. Maybe even `GradedHopfAlgebrasWithBasis(QQ)`.

At that occasion, the various accessors (term, ...) here and in ModulesWithBasis should be made consistent.


---

Comment by jpflori created at 2014-11-14 10:38:30

Has this been superceded by #9944?


---

Comment by tscrim created at 2014-11-14 15:52:29

Partially, but polynomial rings are not yet considered to be graded (we already have this implemented because of the `degree` method).
