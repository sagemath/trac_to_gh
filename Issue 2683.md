# Issue 2683: [with patch, needs review]  Add initial support of k-Schur functions

Issue created by migration from https://trac.sagemath.org/ticket/2683

Original creator: mhansen

Original creation time: 2008-03-27 09:54:26

Assignee: mhansen

CC:  sage-combinat




---

Attachment

The patch also includes some miscellaneous cleanup in permutation.py and partition.py


---

Comment by mhansen created at 2008-03-27 10:04:44

Changing status from new to assigned.


---

Comment by mhansen created at 2008-03-27 10:18:05

Also, note the removal of the ordered partitions and  set partitions code from partition.py was because they were duplicates of code found elsewhere in partition.py


---

Comment by rlm created at 2008-03-28 23:15:03

Applies cleanly to 2.11.alpha1, passes doctests in `sage/combinat.` Looks good!


---

Comment by mabshoff created at 2008-03-29 00:00:19

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 00:00:19

Merged in Sage 2.11.alpah2
