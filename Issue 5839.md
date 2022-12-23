# Issue 5839: [with patch, needs review] MPolynomialRing_libsingular __dealloc__ is buggy, can lead to crash

Issue created by migration from https://trac.sagemath.org/ticket/5839

Original creator: cwitty

Original creation time: 2009-04-20 22:22:09

Assignee: cwitty

CC:  malb

In `__dealloc__`, if currRing is NULL on entry, then currRing will be the ring we just deleted on exit.  The patch fixes this bug, so that currRing never points to freed memory.

It took me quite a while to come up with a small reproducible test case for the problem; here it is.  (This test case is also in the patch, as a doctest.)

```
import gc
from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
R1 = MPolynomialRing_libsingular(GF(5), 2, ('x', 'y'), TermOrder('degrevlex', 2))
R2 = MPolynomialRing_libsingular(GF(11), 2, ('x', 'y'), TermOrder('degrevlex', 2))
R3 = MPolynomialRing_libsingular(GF(13), 2, ('x', 'y'), TermOrder('degrevlex', 2))
gc.collect()
foo = R1.gen(0)
del foo
del R1
gc.collect()
del R2
gc.collect()
del R3
gc.collect()
```




---

Attachment

Doctests pass, patch reads good.


---

Comment by mabshoff created at 2009-04-22 07:27:55

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 07:27:55

Resolution: fixed


---

Comment by mabshoff created at 2009-04-22 07:47:32

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-04-22 07:47:32

Mmmh, I seem to be seeing random doctest failure with 3.4.1 + only this patch merged, so I am reopening this ticket for now. Can someone do extensive testing on sage.math to see if they can reproduce it?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-22 07:47:32

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-04-22 18:35:08

Ok, given that this causes issues for me I am changing it to 'needs work' for now.

Cheers,

Michael


---

Comment by cwitty created at 2009-04-22 19:13:48

What sort of errors?  (Crashes?  Wrong answers?  Any particular files?)


---

Comment by mabshoff created at 2009-05-08 00:49:14

I have come to believe that the issues I saw were due to other issues, so I am reinstating the positive review. But I will do some more extensive testing before merging this. Sorry for the noise.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-14 05:16:49

Resolution: fixed


---

Comment by mabshoff created at 2009-05-14 05:16:49

Merged in Sage 4.0.alpha0.

Cheers,

Michael
