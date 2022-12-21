# Issue 4579: [with patch, needs review] put mpz_longlong functions in c_lib

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-22 00:42:03

Assignee: somebody




---

Attachment


---

Comment by cwitty created at 2008-11-23 03:37:39

This patch removes mpz_set_longlong from integer.pyx; but Sage 3.2 doesn't have that function in integer.pyx at all (in fact, I can't find it anywhere).  Does this depend on some other patch that hasn't been applied yet?


---

Comment by cwitty created at 2008-11-23 04:32:08

mabshoff points out that #4564 is the patch I was missing.


---

Comment by cwitty created at 2008-11-23 05:43:52

Patch looks good; doctests pass.

Positive review.


---

Comment by mabshoff created at 2008-11-23 06:43:16

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-23 06:43:16

Resolution: fixed
