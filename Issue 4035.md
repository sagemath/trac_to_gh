# Issue 4035: [with patch, needs review] fix optional doctests for multivariate polynomials

Issue created by migration from https://trac.sagemath.org/ticket/4035

Original creator: malb

Original creation time: 2008-09-01 09:55:46

Assignee: malb

CC:  mhansen

See attached patch.


---

Attachment

Gary, can you review this (I'm asking you since it involves M2)


---

Comment by mabshoff created at 2008-09-04 00:22:05

I assume this ticket depends on the series of changes you made starting with the number field support? As is the patch does not apply.

Cheers,

Michael


---

Comment by malb created at 2008-09-04 01:17:17

yeah, that could be.


---

Comment by malb created at 2008-09-20 15:47:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-26 21:39:02

Unfortunately this patch has bitrotted:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha1/devel/sage$ patch -p1 < trac_4035_m2_optional_doctests.patch 
patching file sage/rings/polynomial/multi_polynomial.pyx
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 60.
Hunk #2 succeeded at 1659 (offset 58 lines).
Hunk #3 succeeded at 1883 (offset 64 lines).
Hunk #4 FAILED at 2031.
2 out of 4 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/rings/polynomial/multi_polynomial_ring.py
```


Mike: Once it is rebased can you review it?

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 16:16:22

Fixed via the patch at #4420.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 16:16:22

Resolution: fixed
