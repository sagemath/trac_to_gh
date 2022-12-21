# Issue 8535: Various interval field improvements

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-03-14 09:12:29

Assignee: AlexGhitza

Bisection, plotting, max/min, and some doctests.


---

Attachment


---

Comment by robertwb created at 2010-04-28 05:09:38

Changing status from new to needs_review.


---

Comment by jason created at 2010-05-14 19:05:09

Nice job on making good doctests.  Looks good.  One question, though: in the bisection methods, why did you round things using RNDZ, instead of RNDU or RNDD?


---

Comment by jason created at 2010-05-14 19:13:06

Doctests pass on rings/*.py[x].  So positive review if RNDZ is the correct thing to do when bisecting intervals.


---

Comment by robertwb created at 2010-05-15 21:15:32

I don't think either RNDU or RNDD would be the right thing to use here--who's to say that the upper or lower interval should always get the extra half ulp? Maybe RNDN would have been a better choice, I'll post a new patch.


---

Comment by jason created at 2010-05-15 21:32:43

Replying to [comment:4 robertwb]:
> I don't think either RNDU or RNDD would be the right thing to use here--who's to say that the upper or lower interval should always get the extra half ulp? Maybe RNDN would have been a better choice, I'll post a new patch. 

I agree, after thinking about it.  I also agree that RNDN would be a better choice.


---

Comment by robertwb created at 2010-05-15 21:35:35

Same as previous, but uses GMP_RNDN rather than GMP_RNDZ


---

Attachment

Patch attached.


---

Comment by robertwb created at 2010-06-07 19:54:39

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-06-07 19:54:39

Replying to [comment:3 jason]:
> Doctests pass on rings/*.py[x].  So positive review if RNDZ is the correct thing to do when bisecting intervals.

OK, I'm setting this to positive review then.


---

Comment by cremona created at 2010-06-29 06:17:04

Note: only apply the second patch, not both!


---

Comment by mpatel created at 2010-07-20 09:20:18

Resolution: fixed
