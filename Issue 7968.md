# Issue 7968: doctest failure in heegner.py (Sage-4.3.1.rc0)

Issue created by migration from https://trac.sagemath.org/ticket/7968

Original creator: GeorgSWeber

Original creation time: 2010-01-17 19:34:31

Assignee: tbd

On cicero, Fedora 12, 32-bit, Pentium 4,
and also on cleo, Red Hat Enterprise Linux Server 5.3, 64-bit, IA-64,
as well as on Mac OS X 10.4, Core2Duo, 32 bit:

[mvngu`@`cicero sage-4.3.1.rc0]$ ./sage -t -long
devel/sage-main/sage/schemes/elliptic_curves/heegner.py
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/tmp/mvngu/sage-4.3.1.rc0/devel/sage-main/sage/schemes/elliptic_curves/heegner.py",
line 1486:
    sage: s.__cmp__(0)
Expected:
    -1
Got:
    1
**********************************************************************


---

Comment by GeorgSWeber created at 2010-01-17 19:37:15

Is this "just" some refactoring fallout?
Anyone any ideas??
(Fixing the doctest by itself is obviously trivial ...)


---

Attachment


---

Comment by was created at 2010-01-17 22:41:37

Changing priority from major to blocker.


---

Comment by was created at 2010-01-17 22:41:37

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-01-17 22:44:24

Changing status from needs_review to positive_review.


---

Comment by craigcitro created at 2010-01-17 22:44:24

Yep, this looks good. As William pointed out to me when I asked, the issue is just that the ordering is random -- so just having the doctest confirm that they're not equal is the right thing to do.


---

Comment by rlm created at 2010-01-18 22:26:34

Resolution: fixed
