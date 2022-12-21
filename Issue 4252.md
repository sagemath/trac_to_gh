# Issue 4252: Arrangements / PermutationsNK iterator is broken

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2008-10-07 19:40:10

Assignee: mhansen

CC:  sage-combinat


```
sage: Arrangements(range(5),4).count()
116
sage: len(list(sage.combinat.permutation.PermutationsNK(5,4).iterator()))
116
sage: factorial(5)/factorial(5-4)
120
```


They should all be 120. This also doesn't work for the pairs: (4,4), (5, 4), (5, 5), (6, 4), (6, 5), (6, 6), ....


---

Comment by mhansen created at 2008-10-07 19:55:12

This is a duplicate of #4213 which has been fixed in 3.1.3.


---

Comment by mhansen created at 2008-10-07 19:55:12

Resolution: duplicate
