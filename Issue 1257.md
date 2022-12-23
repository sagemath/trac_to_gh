# Issue 1257: [with patch] multi_polynomial_libsingular.pyx "random" segfault

Issue created by migration from https://trac.sagemath.org/ticket/1257

Original creator: cwitty

Original creation time: 2007-11-25 03:46:59

Assignee: was

`MPolynomialRing_libsingular.__dealloc__` changes the global Singular "current ring" to its wrapped ring, and then deletes the ring.  Since `__dealloc__` can get called at essentially random times (it can be called by the Python garbage collector, which can be called on any Python memory allocation), this means that at any time the Singular "current ring" may be changed to an invalid, deleted ring.

My patch changes the "current ring" back to its old value, after deleting the wrapped ring.


---

Attachment


---

Comment by was created at 2007-11-25 05:03:23

Looks very good to me.


---

Comment by was created at 2007-11-25 05:37:06

Resolution: fixed
