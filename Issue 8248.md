# Issue 8248: Small improvement in checking for elliptic curve isogenies

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-02-12 11:00:54

Assignee: cremona

CC:  wuthrich

Keywords: isogenies

When an isogeny is constructed from a kernel polynomial, by default (unless check=False) it is checked whether the given kernel polynomial divides the appropriate division polynomial.  This is expensive when the degree is large (e.g. 163!).

We provide a small patch which does this checking more efficiently.

The example in the patch which now takes 20s, used to take many minutes.


---

Attachment

Applies to 4.3.2


---

Comment by wuthrich created at 2010-02-15 15:10:14

Applies fine to 4.3.3.aplha0.
All tests pass. (execpt heegner.py, which has nothing to do with this patch).

Thanks, John, for this improvement.

Chris.


---

Comment by wuthrich created at 2010-02-15 15:10:14

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-02-15 15:10:32

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 00:12:35

Resolution: fixed
