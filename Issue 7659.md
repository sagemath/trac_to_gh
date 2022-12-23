# Issue 7659: fix tests in documentation after pynac printing changes

Issue created by migration from https://trac.sagemath.org/ticket/7659

Original creator: burcin

Original creation time: 2009-12-11 13:31:52

Assignee: mvngu

Attached patch fixes minor doctest errors in documentation caused by #7406 in 4.3.rc0.




---

Attachment

doctest fixes


---

Comment by burcin created at 2009-12-11 13:35:43

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2009-12-11 23:30:28

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2009-12-11 23:30:28

Looks good and fixes the problems.


---

Comment by mhansen created at 2009-12-14 16:05:47

Resolution: fixed


---

Comment by jhpalmieri created at 2009-12-22 19:02:24

This is a duplicate of #7747 (or rather, #7747 is a duplicate of this one).  The patch in #7747 does a little more; can we merge that one instead?


---

Comment by burcin created at 2009-12-22 22:55:32

Replying to [comment:5 jhpalmieri]:
> This is a duplicate of #7747 (or rather, #7747 is a duplicate of this one).  The patch in #7747 does a little more; can we merge that one instead?

AFAICT by looking at comment:3, this patch was merged. The patch on #7747 should be rebased in this case.


---

Comment by mhansen created at 2009-12-23 13:26:43

I've backed out this patch, and am merging the one at #7747 instead.


---

Comment by burcin created at 2009-12-23 13:49:26

I don't see why you couldn't just merge the patch at #7747 on top of this one, and ignored the failed hunks.
