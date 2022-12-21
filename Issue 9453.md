# Issue 9453: Implement Aurifeuillian factorization

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-07-08 14:12:32

Assignee: tbd

Implement Aurifeuillian factorization of integers, see
http://mathworld.wolfram.com/AurifeuilleanFactorization.html


---

Comment by aapitzsch created at 2010-12-08 10:06:55

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2010-12-08 10:06:55

#5945 has to be applied first because of the new factorint.pyx module.


---

Comment by jdemeyer created at 2010-12-08 10:16:55

Obviously, it should be implemented in general, not only for bases 2,3 and 5...


---

Comment by aapitzsch created at 2010-12-22 16:55:09

Depends on #5945

Here is a more general version.


---

Attachment

Depends on #5945 and #10623


---

Comment by mariah created at 2011-06-15 14:18:11

Changing status from needs_review to positive_review.


---

Comment by mariah created at 2011-06-15 14:18:11

Applied patch to sage-4.7.1.alpha2 and did 'make testlong'.  All tests passed.  Positive review!


---

Comment by jdemeyer created at 2011-07-22 17:06:00

Resolution: fixed
