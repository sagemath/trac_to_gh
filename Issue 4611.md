# Issue 4611: deprecate sqrt_approx

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-25 07:11:51

Assignee: somebody

This is should be folded into the sqrt(...) function by passing a non-None prec. This exists, e.g. in sage.rings.Rational


---

Attachment


---

Comment by malb created at 2009-01-24 08:44:58

Patch looks good and doctests pass.


---

Comment by mabshoff created at 2009-01-24 19:54:56

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:54:56

Resolution: fixed
