# Issue 1273: [with patch] implement complex root isolation

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-25 21:33:03

Assignee: somebody

I'm attaching a patch that implements complex root isolation for exact polynomials.  It uses a fairly inefficient strategy (find the roots using numpy or Pari, then verify them using interval arithmetic), but it does work.


---

Attachment


---

Comment by cwitty created at 2007-11-25 21:34:27

I forgot to mention... this patch depends on the patch from #1270, which must be applied first.


---

Comment by rlm created at 2007-11-30 05:27:25

Fast!


---

Comment by mabshoff created at 2007-12-01 10:58:01

Merged in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 10:58:01

Resolution: fixed
