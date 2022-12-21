# Issue 1732: block matrix construction

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-01-09 08:24:23

Assignee: was

CC:  dfdeshom@gmail.com


```
Is there a way to construct block matrices in SAGE?
Not just the "block_sum", "augment" and "stack" functions.

As an example, let A, B, C, D be matrices and i want to construct a
matrix like E=[[A,B],[C,D]]

Such a feature would be very nice.

-vgermrk-

```



---

Attachment


---

Attachment

Much expanded functionality due to discussion at http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg08958.html

See the docstrings in the patch for many examples.


---

Comment by robertwb created at 2008-01-11 03:14:47

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-01-11 03:14:47

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-11 03:25:57

more memory friendly for constant entries


---

Attachment

Just wanted to point out that this patch works great for me, both for block diagonal matrices and for creating block matrices from lists.


---

Comment by mabshoff created at 2008-01-15 03:10:47

I merged all three patches into Sage 2.10.alpha3


---

Comment by mabshoff created at 2008-01-15 03:10:47

Resolution: fixed
