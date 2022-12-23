# Issue 2541: [with patch, needs review] Fixes bugs in binary_codes.pyx

Issue created by migration from https://trac.sagemath.org/ticket/2541

Original creator: rlm

Original creation time: 2008-03-16 03:05:25

Assignee: rlm

This also makes the automorphism group calculator return the size of the group.


---

Attachment

This may fix one of the issues mentioned in #2514. At the very least it adds doctests that show that if there still is a problem, it isn't in `binary_code.pyx`.


---

Comment by mhansen created at 2008-03-16 03:41:57

Applies and passes tests for me.


---

Comment by mabshoff created at 2008-03-16 04:15:24

I will remove the colorful language once I merge this patch :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 04:39:49

Merged in Sage 2.10.4.rc0 (minus one line ;)


---

Comment by mabshoff created at 2008-03-16 04:39:49

Resolution: fixed
