# Issue 7887: Fast function field arithmetic

Issue created by migration from https://trac.sagemath.org/ticket/7887

Original creator: robertwb

Original creation time: 2010-01-10 00:10:13

Assignee: AlexGhitza

CC:  roed

Wrapping zmod_poly directly should be much faster than the current implementation of Frac(GF(p)['t'])

See also #7585


---

Attachment


---

Attachment

apply on top of previous


---

Comment by ylchapuy created at 2010-01-10 07:58:39

I know it's way to early for review, but maybe you could be inspired by ticket #7857 and implement directly Henrici's algorithms.

Yann


---

Comment by ylchapuy created at 2010-10-20 07:39:55

Changing status from new to needs_review.


---

Comment by ylchapuy created at 2010-10-20 07:39:55

I guess this should be closed as a duplicate of #9051


---

Comment by robertwb created at 2010-10-20 15:53:45

Resolution: duplicate


---

Comment by robertwb created at 2010-10-20 15:53:45

Changing type from defect to enhancement.


---

Comment by robertwb created at 2010-10-20 15:53:45

Correct.
