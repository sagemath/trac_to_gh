# Issue 4289: EllipticCurve behaviour

Issue created by migration from https://trac.sagemath.org/ticket/4289

Original creator: ljpk

Original creation time: 2008-10-14 21:30:29

Assignee: was

If one types in
`EllipticCurve(1,2)`
then one gets

`Elliptic Curve defined by y^2  = x^3 + 5181*x - 5965058 over Rational Field`

this seemingly unrelated curve has j-invariant 1 and the 2 is ignored. Could the EllipticCurve function test for the presence of two numerical inputs and either raise an error or cast it to
`EllipticCurve([1,2])`?


---

Comment by robertwb created at 2008-10-14 21:34:09

This should be an easy fix.


---

Attachment


---

Comment by robertwb created at 2008-10-14 21:42:45

I think raising an error is the most consistent thing to do.


---

Comment by zimmerma created at 2008-10-15 07:37:08

Positive review. I notice there is no doctest for EllipticCurve(j). It would be good to add one.
Also the doc is inconsistent wrt 'Returns' vs 'Return'.


---

Comment by wuthrich created at 2008-10-15 09:54:20

This trac and the last comment is linked to the old Ticket #128.
As noted there, we should remove `EllipticCurve(j)` from the possible ways of defining an elliptic curve anyway.


---

Comment by mabshoff created at 2008-10-15 20:29:53

Merged in Sage 3.1.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-15 20:29:53

Resolution: fixed
