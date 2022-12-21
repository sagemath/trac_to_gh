# Issue 6134: [with patch, needs review] Fix SR coercion issue with numpy.float128

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-05-26 20:07:41

On 32-bit boxes, numpy does not build a float128.


---

Attachment

This applied to my 32-bit rc0 build and fixed the issue for me.  Positive review.


---

Comment by mhansen created at 2009-05-26 20:51:57

Resolution: fixed


---

Comment by mhansen created at 2009-05-26 20:51:57

Merged in 4.0.rc1.
