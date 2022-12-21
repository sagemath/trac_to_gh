# Issue 3507: fix major efficiency/performance bug in sparse linear algebra matrix multiply

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-25 01:46:19

Assignee: was

a * b for a, b sparse matrices over QQ was VASTLY too slow because of a stupid bug.


---

Attachment


---

Comment by craigcitro created at 2008-06-25 01:56:46

Looks good.


---

Comment by mabshoff created at 2008-06-25 02:47:25

Resolution: fixed


---

Comment by mabshoff created at 2008-06-25 02:47:25

Merged in Sage 3.0.4.alpha1
