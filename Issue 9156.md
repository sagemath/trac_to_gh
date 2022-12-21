# Issue 9156: Add real() and imag() methods to Integer and Rational

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-06-06 08:17:05

Assignee: AlexGhitza

This is useful for consistently handling elements of ZZ, QQ, RR, and CC. 


---

Attachment


---

Comment by robertwb created at 2010-06-06 08:20:22

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-06-06 17:32:32

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-06-06 17:32:32

A little, but very pleasant change, I find it very annoying when simpler objects don't have "part-accessing methods" of more complicated ones. All doctests pass.


---

Comment by mhansen created at 2010-06-06 19:22:11

Resolution: fixed
