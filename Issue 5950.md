# Issue 5950: OSX: Add check code so that x86 and ppc builds print sane error message

Issue created by migration from https://trac.sagemath.org/ticket/5950

Original creator: mabshoff

Original creation time: 2009-04-30 21:50:58

Assignee: mabshoff

-bdist should add something analog to the SSE flags on Linux so that if someone tried to run a ppc build on an x86 it aborts with a sane error message instead of just blowing up.

Cheers,

Michael


---

Comment by kcrisman created at 2015-01-05 16:09:38

Dup (or at least asking very similar question that should be solved at the same time, not _exact_ dup) of the slightly more-detailed #6414.


---

Comment by kcrisman created at 2015-01-05 16:09:38

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-01-05 16:09:43

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-13 01:16:05

Resolution: duplicate
