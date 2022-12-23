# Issue 4545: better fix for mixing @parallel with numerical constant preparsing

Issue created by migration from https://trac.sagemath.org/ticket/4545

Original creator: craigcitro

Original creation time: 2008-11-18 09:37:40

Assignee: cwitty

As noted on #4312, ``@`parallel` and the new preprocessing of constants don't play together very well. The fix at #4312 provides *a* fix, but a better fix is needed.


---

Comment by klee created at 2021-09-28 16:14:11

Changing status from new to needs_review.


---

Comment by klee created at 2021-09-28 16:14:11

Apparently the problem just went away.


---

Comment by @kliem created at 2021-09-29 09:05:12

New commits:


---

Comment by klee created at 2021-09-30 03:33:01

Changing status from needs_review to positive_review.


---

Comment by klee created at 2021-09-30 03:33:01

Okay.


---

Comment by @kliem created at 2021-09-30 06:59:23

Thank you.


---

Comment by vbraun created at 2021-10-09 11:10:12

Resolution: fixed
