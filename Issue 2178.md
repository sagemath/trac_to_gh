# Issue 2178: latex2html does not like $+$

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-02-16 15:55:18

Assignee: cwitty

Bill Purvis points out (http://groups.google.com/group/sage-support/browse_thread/thread/9531e60cda199e6d#) a problem in the reference manual that seems to be caused by latex2html doing the wrong thing with $+$.

I'll have a patch for this problem shortly.


---

Comment by cwitty created at 2008-02-16 16:11:38

Changing status from new to assigned.


---

Attachment

The attached patch avoids the problem.  It also patches docstrings that create TeX errors on my laptop, so that I can actually build the refman.


---

Comment by mabshoff created at 2008-02-16 18:14:12

We do not use `\mathbb` since it doesn't work with jsmath. Patch looks good.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 18:15:58

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 18:15:58

Merged in Sage 2.10.2.alpha1
