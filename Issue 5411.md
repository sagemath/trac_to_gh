# Issue 5411: QuadraticForm: implement clifford_invariant and replace hasse_conductor with clifford_conductor

Issue created by migration from https://trac.sagemath.org/ticket/5411

Original creator: tornaria

Original creation time: 2009-03-01 15:30:07

Assignee: gonzalo

The `hasse_invariant` of a quadratic form doesn't match the standard invariant (brauer class) for quaternion algebras (e.g. for ternary quadratic forms, the ramification of the corresponding quaternion algebra).

The `clifford_invariant` can defined in terms of the clifford algebra of the quadratic form. See Lam (AMS GSM 67) p. 117 for the definition, and p. 119 for the formula relating it to the Hasse invariant.

It also has the property that hyperbolic spaces have `clifford_invariant == +1` at all primes.

It also makes more sense to define a `clifford_conductor` instead of a `hasse_conductor` as the product of all the primes with `clifford_invariant == -1`.


---

Attachment


---

Comment by tornaria created at 2009-03-01 16:00:23

same file with correct name


---

Attachment


---

Comment by tornaria created at 2009-03-01 16:04:31

Changing assignee from gonzalo to tornaria.


---

Comment by tornaria created at 2009-03-01 16:04:31

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-02 03:41:54

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 03:50:20

Jon expressed some further wishes, so "needs review" again for now :-)

Cheers,

Michael


---

Comment by tornaria created at 2009-03-02 04:10:00

replaces previous patch --- this one doesn't remove hasse_conductor


---

Attachment

The new patch (2nd patch) preserves `hasse_conductor` as requested by Jon, and it also fixes the imports in `quadratic_form.py`, so it is meant to be applied on top of #5403.


---

Comment by jonhanke created at 2009-03-02 05:13:05

Looks good.  Positive review.


---

Comment by mabshoff created at 2009-03-02 06:37:17

Resolution: fixed


---

Comment by mabshoff created at 2009-03-02 06:37:17

Merged trac_5411.clifford_invariant.2nd.patch in Sage 3.4.rc0.

Cheers,

Michael
