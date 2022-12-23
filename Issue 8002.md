# Issue 8002: remove dead code from sage-ptest

Issue created by migration from https://trac.sagemath.org/ticket/8002

Original creator: wjp

Original creation time: 2010-01-19 19:13:52

Assignee: tbd

The `sage-ptest` parallel doctesting script has some dead code in it: a function `run` that's unused, and a `-sage` flag that triggers a call to a no longer existing `sage-doctest_tex` script.

I'm attaching a patch that cleans this up, and as a side effect allows `sage-ptest` to test files with a `.sage` extension.


---

Attachment


---

Comment by wjp created at 2010-01-19 19:26:23

Changing status from new to needs_review.


---

Comment by rbeezer created at 2010-01-21 01:09:57

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-01-21 01:09:57

Written as advertised, `run()` routine is never called, `doctest_tex` is no longer shipped as part of Sage.

Applies cleanly and works fine in limited testing.

Positive review.


---

Comment by mvngu created at 2010-01-23 10:23:46

Merged in script repository.


---

Comment by mvngu created at 2010-01-23 10:23:46

Resolution: fixed
