# Issue 2501: [with patch, needs review] SBox class for Sage

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-03-12 18:05:16

Assignee: malb

The attached patch adds a class SBox to the module `sage.crypto.mq` which offers basic functionality to work with cryptographic substitution boxes like:
 * substitution (obviously)
 * difference distribution and linear approximation matrices
 * multivariate polynomial system generation
 * univariate polynomial interpolation

It might be a bit controversial if this functionality should go in (it is not math but applied math), so here are some points in favour:
 * Sage has a `sage.crypto` module with LFSRs and such.
 * `SBox` supports (algebraic) cryptanalysis by simplifying experiments with ciphers and algebraic aspects of cryptography is an application of Sage (Sage was advertised for this application in the past)
 * Some people have expressed (some) interest in such a class.


---

Attachment


---

Comment by was created at 2008-03-12 18:10:09

> It might be a bit controversial if this functionality  should go in (it is not math but applied math)

It's not controversial at all, in my opinion -- this should *definitely* go in.

"Applied math" belongs squarely within the mission of Sage, and S-Box's most certainly do.


---

Comment by mhansen created at 2008-03-15 21:35:05

Applies to 2.10.4.alpha0 and passes tests after #2444 is applied.


---

Comment by mabshoff created at 2008-03-15 22:58:48

Merged in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-15 22:58:48

Resolution: fixed
