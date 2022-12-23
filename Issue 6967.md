# Issue 6967: @parallel -- dramatically improve by rewriting with fork directly, using files, timeouts, controlling interfaces, etc.

Issue created by migration from https://trac.sagemath.org/ticket/6967

Original creator: was

Original creation time: 2009-09-20 10:43:46

Assignee: cwitty




---

Comment by was created at 2009-09-20 11:01:17

first usable version


---

Attachment


---

Comment by mpatel created at 2009-11-18 23:30:18

Should we also allow each child process to pull off a large chunk of the input (e.g., from a deque), when it's more efficient?  Determine the chunk size dynamically, a la `timeit`?


---

Comment by was created at 2010-01-18 04:10:34

Changing type from enhancement to defect.


---

Comment by was created at 2010-01-18 04:10:34

This fixes *major* bugs in `@`parallel sucking.   Without this, `@`parallel gets confused by Sage-isms, preparsing, state, etc., and really hasn't taken off as a result.  This fixes all that.


---

Comment by was created at 2010-01-18 12:16:29

Changing status from new to needs_review.


---

Comment by was created at 2010-01-18 12:16:29

This also fixes a very serious bug in sage.interfaces.quit which will lead to zombie processes being left around, and improves doctest coverage.


---

Attachment


---

Attachment


---

Comment by rlm created at 2010-01-19 02:44:24

Awesome!!!


---

Comment by rlm created at 2010-01-19 02:44:24

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 04:07:33

Resolution: fixed
