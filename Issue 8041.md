# Issue 8041: docstring for XGCD has Sphinx errors "Unknown control sequence '\*'" in sage-4.3.1

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-22 15:31:55

Assignee: AlexGhitza

Subject says it all.  In the notebook type `XGCD?` and get errors. 


---

Comment by was created at 2010-01-22 15:34:40

Changing status from new to needs_review.


---

Attachment


---

Comment by jhpalmieri created at 2010-01-22 16:11:51

Positive review for was's patch.  Here's another patch fixing the same and similar issues.


---

Attachment

apply on top of other patch


---

Comment by AlexGhitza created at 2010-01-23 01:03:29

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-01-23 01:03:29

Looks good (applies, passes tests, the built documentation is ok).


---

Comment by mvngu created at 2010-01-23 07:03:59

Resolution: fixed
