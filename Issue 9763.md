# Issue 9763: Change hashing and printing for NumberFieldIdeals

Issue created by migration from https://trac.sagemath.org/ticket/9764

Original creator: jdemeyer

Original creation time: 2010-08-18 21:57:52

Assignee: davidloeffler

CC:  was

This ticket is a fork from #9400.

    * implement hashing for number field ideals that isn't a stupid string repr, hence vastly faster 

    * make number field ideals *not* print in reduced form; this will look uglier, but is massively faster and more sensible for any real applications, as people learned constantly at sage days 22.


---

Comment by jdemeyer created at 2010-08-18 22:00:42

Needs to be rebased to #9343.


---

Comment by jdemeyer created at 2010-08-18 22:00:42

Changing status from new to needs_work.


---

Comment by jdemeyer created at 2010-08-18 22:04:02

Patch against sage-4.5.3.alpha0


---

Attachment


---

Comment by jdemeyer created at 2010-09-16 16:49:36

Changing keywords from "" to "number field ideal hash".


---

Comment by jdemeyer created at 2010-09-16 16:49:36

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-09-16 16:50:56

Patch against sage-4.6.alpha0 + #9400 + #9898 + #9753


---

Comment by davidloeffler created at 2010-09-23 11:18:15

Changing status from needs_review to positive_review.


---

Attachment

I applied this to sage-4.6.alpha1 with #9898 and #9753 installed. Changes look sensible, patch applies fine, and all doctests pass. Positive review.


---

Comment by mpatel created at 2010-09-28 10:56:31

Resolution: fixed
