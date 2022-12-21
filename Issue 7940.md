# Issue 7940: real_mpfr: fix docstring so ref manual builds

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-01-16 03:17:42

Assignee: AlexGhitza

CC:  kcrisman

A triple quote `"""` in real_mpfr.pyx needs to be converted to `r"""`.  This patch does that.  Otherwise, the reference manual fails to build.



---

Attachment

if I put a long enough description here, it will be longer than the patch itself...


---

Comment by rlm created at 2010-01-16 03:46:06

Changing status from new to needs_review.


---

Comment by rlm created at 2010-01-16 03:46:22

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-16 03:46:32

Resolution: fixed
