# Issue 7590: Create Bipartite Graph according to 2 degree sequences

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-12-03 12:40:23

Assignee: rlm

CC:  wdj

Given the sequence of degrees for set A and a sequence of degree for set B, create the corresponding bipartite graph if possible.

Use #7301


---

Comment by ncohen created at 2009-12-04 17:51:26

Here it is !


---

Comment by ncohen created at 2009-12-04 17:51:26

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 17:57:31

Changing status from needs_review to needs_info.


---

Comment by rlm created at 2009-12-15 17:57:31

What is the status of #7301 and this patch? The comments on #7301 are a bit confusing, but at the end it seems as if perhaps this patch should depend on the other version instead of #7301?


---

Comment by ncohen created at 2009-12-16 00:52:59

Well, I'd say this patch is ready for review (as it is written and functional) even though #7301 is not :-)

The discussion in #7301 could lead to a gale_ryser function which does not use GLPK  ( and may be even more efficient ), which is good for everybody :-)

As this function is not so fundamental to Sage, I see no harm in making it wait until #7301 is ready :-)


---

Comment by ncohen created at 2009-12-16 00:52:59

Changing status from needs_info to needs_review.


---

Attachment

Added # optional to some doctests.


---

Comment by rlm created at 2009-12-16 03:01:01

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2009-12-16 03:05:24

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2009-12-16 03:06:36

(This is fine by me once #7301 is ready...)


---

Comment by rlm created at 2010-01-13 09:03:38

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-13 09:04:12

positive review.


---

Comment by rlm created at 2010-01-13 09:04:12

Resolution: fixed


---

Comment by ncohen created at 2010-01-13 09:05:48

Thanks !! :-)
