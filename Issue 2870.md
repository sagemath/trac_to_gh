# Issue 2870: [with patch, needs review] Various files poorly import calculus.py

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-04-10 05:46:11

Assignee: gfurnish

Various files import specific classes from calculus.py instead of their wrappers, making them too dependent on calculus internals.


---

Attachment


---

Comment by gfurnish created at 2008-04-10 05:47:12

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-10 06:20:43

Looks good to me.


---

Comment by mabshoff created at 2008-04-10 13:36:25

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-10 13:36:25

Resolution: fixed
