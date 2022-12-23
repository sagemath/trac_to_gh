# Issue 7755: Auto-detect SageNB install path when building documentation

Issue created by migration from https://trac.sagemath.org/ticket/7755

Original creator: mpatel

Original creation time: 2009-12-24 05:15:55

Assignee: mvngu

CC:  jhpalmieri

We should update the "docbuild" configuration so that Sphinx can locate jsMath.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/9db6f5df45bc05cc), #7467.


---

Comment by mpatel created at 2009-12-24 05:24:53

Auto-detect jsMath path.  Based on timdumol's comment at #7467.  sage repo.


---

Comment by jhpalmieri created at 2009-12-24 06:24:13

Changing status from new to needs_review.


---

Attachment

Looks good.  Here's a slightly different patch to do the same thing, just making os.path.join do more of the work.  I'm committing it in your name (I just edited the patch file) and I'm giving it a positive review.


---

Comment by jhpalmieri created at 2009-12-24 06:24:27

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-12-24 06:24:51

use this one instead


---

Comment by was created at 2009-12-24 07:11:50

Resolution: fixed


---

Attachment

Merged into sage-4.3.rc2.
