# Issue 6008: Improved efficiency  of elliptic curve torsion computation

Issue created by migration from https://trac.sagemath.org/ticket/6008

Original creator: cremona

Original creation time: 2009-05-08 16:49:38

Assignee: was

Keywords: elliptic curve torsion

This patch makes an improvement to the efficiency of elliptic curve torsion subgroup computation (over number fields).

I noticed something in the code I wrote which can be improved.  This
is something which was not in Chris Wuthrich's original
implementation, so it is my fault.

Here's what we do:  (1) find an upper bound on the torsion order, i.e.
a positive integer N such that the torsion order is certainly a
divisor of N.  This uses the function _torsion_bound() in
ell_number_field.py.    (2) For each prime dividing N, find a basis
for  the p-primary torsion.  This is done in
_p_primary_torsion_basis() in ell_generic.py.  (3) Put together the
primary parts.

Here's the inefficiency.  In step (2) I ignore the bound we have on
the exponent of each prime.  This wastes time in computing the
p-primary torsion basis.  So I will change the function
_p_primary_torsion_basis() to take an optional parameter which is a
bound on the  exponent of the order (not the exponent of the p-primary
subgroup).

e.g. in Jim's example, the bound is 49 and the actual torion is C7xC7. But when we compute the 7-primary torsion, after finding that the 7-torsion is complete and of order 49, we do not stop, but test 8 points in the 7-torsion subgroup to see if they can be divided further by 7.  that last part is obiously a waste of time since we have already reached the bound.

Before: Jim's example took 12.64s.  After: 9.73s.


---

Comment by stankewicz created at 2009-05-09 18:01:53

Doctests all came out clean.

Moreover the example given took 71 seconds in 3.4.2 on my travel notebook before the patch and 62 seconds after the patch.


---

Comment by cremona created at 2009-05-09 19:24:16

Thanks Jim -- you could give the patch a positive review now, and it might get into Sage 4.0 which is out soon!


---

Comment by stankewicz created at 2009-05-09 21:15:53

Resolution: fixed


---

Comment by stankewicz created at 2009-05-09 21:18:56

Changing status from closed to reopened.


---

Comment by stankewicz created at 2009-05-09 21:18:56

Resolution changed from fixed to 


---

Comment by cremona created at 2009-05-09 21:44:12

Replying to [comment:5 stankewicz]:

Thanks for the positive review.  [Only Michael Abshoff changes the status to "fixed", when the patch has been merged in the next release.]


---

Comment by mabshoff created at 2009-05-10 04:17:52

The hunk in this patch changing `sage/version.py` needs to be removed before merging the patch since it will cause rejects and should have never been part of the patch to begin with ;)

Thanks for reopening - I think it is pretty clear in the trac guidelines not to close tickets, but it happens on occasion by new reviewers.

Cheers,

Michael


---

Attachment

Replace previous one with this


---

Comment by cremona created at 2009-05-10 08:08:02

Replying to [comment:7 mabshoff]:
> The hunk in this patch changing `sage/version.py` needs to be removed before merging the patch since it will cause rejects and should have never been part of the patch to begin with ;)

Done -- I have no idea how that got in there!  Soory

> 
> Thanks for reopening - I think it is pretty clear in the trac guidelines not to close tickets, but it happens on occasion by new reviewers.
> 
> Cheers,
> 
> Michael


---

Comment by mabshoff created at 2009-05-12 21:03:35

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-12 21:03:35

Resolution: fixed
