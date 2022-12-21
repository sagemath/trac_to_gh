# Issue 8743: change_ring on a rational matrix may return self

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-04-22 01:17:21

Assignee: jason, was

CC:  was rbeezer

change_ring on a rational matrix goes against the documentation for the generic change_ring function, which states that a copy is always returned.  This patch fixes this and adds a TestSuite test for it (the advantage of a testsuite test is that this will be run for *every* matrix class, not just the rational matrix class).


---

Comment by jason created at 2010-04-22 01:38:36

Changing status from new to needs_review.


---

Attachment


---

Comment by jsyri created at 2010-05-19 14:01:08

Fixes bug, code seems to be OK, test is included, all tests pass. Positive review.


---

Comment by jsyri created at 2010-05-19 14:01:08

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 01:33:11

Resolution: fixed


---

Comment by robertwb created at 2010-06-06 06:44:31

I understand the ticket is closed, but is there any rational for the current behavior? Seems very inefficient, and returning self should be totally safe for immutable matrices at least.


---

Comment by mhansen created at 2010-06-06 06:58:26

The patch does return self for immutable matrices.
