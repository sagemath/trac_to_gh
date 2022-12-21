# Issue 7739: Improvements to AGM

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-12-18 23:57:01

Assignee: AlexGhitza

CC:  cremona

Native (much faster) agm for RDF and CDF, optimized and document agm for RR. 

Inspired by, but somewhat orthogonal to, #7719.



---

Comment by cremona created at 2009-12-20 16:52:57

Look basically good.  Robert, do you want to add the test for a=0 or b=0 or a=-b in the complex_double case, and also perhaps a=0 or b=0 for the real cases?


---

Comment by robertwb created at 2010-01-07 10:50:46

Changing status from new to needs_review.


---

Attachment

Good idea, I added some degenerate tests and refreshed the patch.


---

Attachment

corrects typo in previous patch (which it replaces)


---

Comment by cremona created at 2010-01-07 15:48:53

There's a typo (sgm for agm) in the docstring (line 1944 of complex_double).  I edited the patch to fix that.

Otherwise I'm quite happy -- applies to 4.3 and tests in sage/rings/{real,complex}* all pass.  So: positive review!


---

Comment by cremona created at 2010-01-07 15:48:53

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 08:43:00

Resolution: fixed


---

Comment by robertwb created at 2010-01-13 20:04:50

Thanks.
