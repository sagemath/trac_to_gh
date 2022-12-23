# Issue 5179: Delete __getslice__ from matrices

Issue created by migration from https://trac.sagemath.org/ticket/5179

Original creator: jason

Original creation time: 2009-02-04 18:31:44

Assignee: was

`__getslice__` has been deprecated for a long time in Python.  This patch adds equivalent functionality to `__getitem__`, which is where the functionality should be.


---

Attachment


---

Comment by jason created at 2009-02-04 18:33:50

I thought I opened another ticket for this issue and posted a patch there, but I cannot find it at all.  If there is another ticket open at this time with a patch, this ticket and patch supersedes it.


---

Comment by cwitty created at 2009-02-05 05:00:42

Code looks good, all doctests pass.

Positive review.


---

Comment by mabshoff created at 2009-02-05 10:49:34

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-05 10:49:34

Resolution: fixed
