# Issue 614: structure/element.pyx:  non-integral exponents not supported error in doctest

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-09-07 04:32:11

Assignee: mhansen

Bad doctest:
sage: 2r**(SR(2)-1-1r)



---

Attachment

Patch attached.


---

Comment by was created at 2007-09-07 04:34:45

Resolution: fixed
