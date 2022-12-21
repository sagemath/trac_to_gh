# Issue 1385: Re-organize number field element inheritance hierarchy

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-12-03 20:32:39

Assignee: was

Currently the base NumberFieldElement class requires NTL. However, the quadratic number field elements, and (in the future) FLINT-based number field classes won't use NTL at all, but things need to be split out to make this clean. 


---

Comment by AlexGhitza created at 2009-01-23 07:06:17

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-20 19:54:03

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:54:03

Changing component from number theory to number fields.


---

Comment by jdemeyer created at 2011-10-09 11:09:45

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2011-10-09 11:09:45

I don't see any reason to change things at the moment.  If we really re-implement number fields, that would be the correct time to change this.  Proposing to close as "wontfix".


---

Comment by davidloeffler created at 2011-10-09 17:18:23

I agree. Let's close this.


---

Comment by davidloeffler created at 2011-10-09 17:18:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-10-09 20:43:32

Resolution: invalid
