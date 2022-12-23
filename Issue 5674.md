# Issue 5674: [with patch, needs review] Enhanced handling of elliptic curve twists

Issue created by migration from https://trac.sagemath.org/ticket/5674

Original creator: cremona

Original creation time: 2009-04-03 11:09:11

Assignee: was

CC:  wuthrich

Keywords: elliptic curve twist

The patch does the following related things:

    1. Implements in ell_generic functions is_quadratic_twist(), is_quartic_twist(), is_sextic_twist(), which detect twists between curves (returning the appropriate twisting paramenter)
    2. Deprecates the EllipticCurve(j) constructor, replacing it with EllipticCurve_from_j(j).  Over Q this gives the minimal twist, i.e. a curve with the correct j and minimal conductor.
    3. Rewrites the function minimal_quadratic_twist() introduced in #4667 to use the previous function, with extra work in case j=0, 1728 since we need the minimal __quadratic__ twist, not the minimal twist.

There is likely to be a necessary change to documentation (pages 38 and 39 of the tutorial) which have not yet been made.

The patch is based on 3.4.1.alpha0 + patches at #4667.
I have tested all files in sage/schemes/elliptic_curves.  There are two failures in sha_tate which I do not understand, so I am posting the patch anyway.



---

Attachment

apply to 3.4.1.apha0 + #4667 patches


---

Comment by cremona created at 2009-04-03 11:14:00

Resolution: duplicate


---

Comment by cremona created at 2009-04-03 11:14:00

Sorry I must have pressed too many buttons...
