# Issue 919: creation of p-adic rings uses O(n^2) memory

Issue created by migration from https://trac.sagemath.org/ticket/919

Original creator: roed

Original creation time: 2007-10-18 14:51:33

Assignee: roed

Keywords: padics

Upon creation, p-adic rings currently cache powers of p from 0 up to their precision cap.  This uses O(n^2) space, and is very unfriendly to someone who wants to use a capped relative ring with very high precision in order to never run into the precision cap.


---

Comment by roed created at 2007-10-19 22:09:17

Fixes the problem, adds some functionality for padic extensions


---

Attachment


---

Comment by was created at 2007-10-20 18:00:00

Resolution: fixed


---

Comment by was created at 2007-10-20 18:00:00

I've applied this.
