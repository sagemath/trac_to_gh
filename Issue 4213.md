# Issue 4213: Bug in Permutations(n, k)

Issue created by migration from https://trac.sagemath.org/ticket/4213

Original creator: anakha

Original creation time: 2008-09-28 21:26:17

Assignee: mhansen

CC:  sage-combinat


```
sage: list(Permutations([1,2,3,4,5], 4))

[ ...
 [2, 3, 1, 5],
 [2, 3, 3, 1],
 [2, 3, 3, 4],
 [2, 3, 3, 5],
 [2, 3, 4, 1],
 ...
 [3, 2, 1, 5],
 [3, 2, 2, 1],
 [3, 2, 2, 4],
 [3, 2, 2, 5],
 [3, 2, 4, 1],
 ...
 [4, 2, 1, 5],
 [4, 2, 2, 1],
 [4, 2, 2, 3],
 [4, 2, 2, 5],
 [4, 2, 3, 1],
 ...
 [5, 2, 1, 4],
 [5, 2, 2, 1],
 [5, 2, 2, 3],
 [5, 2, 2, 4],
 [5, 2, 3, 1],
```


Only the buggy parts are shown.

This does not occur for lists smaller that 5 or when len(n) == k.


---

Attachment


---

Comment by mhansen created at 2008-09-28 21:51:59

Changing status from new to assigned.


---

Comment by anakha created at 2008-09-28 22:13:38

Passes tests and fixes the problem on my end.


---

Comment by mabshoff created at 2008-09-29 02:14:23

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-29 02:14:23

Resolution: fixed
