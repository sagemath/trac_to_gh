# Issue 7396: Disjoint unions of enumerated sets.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-05 15:46:33

Assignee: hivert

CC:  sage-combinat

Keywords: Disjoint union, enumerated sets

The patch implement the disjoint union of a family of enumerated sets. It allows in particular to deal with infinite unions such as in 

```
sage: DisjointUnionEnumeratedSets(
...       Family(NonNegativeIntegers(), Permutations))
Disjoint union of Lazy family (Permutations(i))_{i in Non negative integers}
```


Florent


---

Attachment


---

Comment by hivert created at 2009-11-05 16:26:15

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-11-05 16:28:03

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2009-11-05 16:28:03

Patch good to go (we polished it together:-))!


---

Comment by mhansen created at 2009-11-19 16:58:39

Resolution: fixed
