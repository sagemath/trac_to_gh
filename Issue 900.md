# Issue 900: both squarefree_decomposition() and square_free_decomposition() methods exist

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-14 23:14:12

Assignee: somebody

`ZZ['x']` polynomials have a square_free_decomposition() method; all polynomials have a squarefree_decomposition() method (as of 2.8.7).  (Yes, I'm the one who added both of them.  I don't know what I was thinking.)

I have a patch for this which I will attach as soon as -testall is finished.



---

Attachment


---

Comment by was created at 2007-10-21 01:10:34

Resolution: fixed
