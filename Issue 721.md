# Issue 721: refactoring ell_rational_field

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2007-09-20 22:32:45

Assignee: roed

ell_rational_field is too big.  I therefore propose the following changes.

1.  Create an ell_nf as a common parent for ell_rational_field and ell_number_field.  Factor up as many functions as possible.

2.  Create an Lseries_ell class in sage/schemes/elliptic_curves/lseries_ell.py, and factor out the L-series functions to there (Lseries_dokchitser, Lseries_sympow, Lseries_sympow_derivs, Lseries_zeros, Lseries_zeros_in_interval, Lseries_values_along_line, Lseries_twist_values, Lseries_twist_zeros, Lseries_at1, Lseries_deriv_at1, Lseries, Lseries_extended, L1_vanishes, Lratio, ).

3.  Create a Sha_group class (inheriting from AbelianGroup).  Move the functions (sha_an_numerical, sha_an, sha_an_padic, sha_p_primary_bound, two_selmer_shabound, shabound_kolyvagin, shabound_kato, shabound) to this new class.


---

Comment by dmharvey created at 2007-09-20 22:37:07

please apply #635 before doing this!


---

Comment by roed created at 2007-10-01 19:36:57

Splits ell_rational_field, work in progress on Tate's algorithm


---

Attachment

THIS is the one you *really* want to apply!


---

Comment by was created at 2007-10-02 03:52:10

Resolution: fixed


---

Comment by was created at 2007-10-02 04:08:21

Actually, the patch I just posted is completely broken.  Re-opening the ticket!


---

Comment by was created at 2007-10-02 04:08:21

Resolution changed from fixed to 


---

Comment by was created at 2007-10-02 04:08:21

Changing status from closed to reopened.


---

Comment by was created at 2007-10-04 17:54:22

Do not apply any of the above patches yet!!!!


---

Attachment

This one is even better.


---

Comment by mabshoff created at 2007-10-13 03:11:38

Hello,

the patch doesn't apply cleanly to 2.8.6, so please rebase and try again.

You should also delete obsolte version of the patch.

Cheers,

Michael


---

Comment by roed created at 2007-10-13 07:34:29

Bundled against 2.8.6, with additional material (added ntl ZZ_pE and ZZ_pEX)


---

Attachment


---

Comment by was created at 2007-10-13 07:46:08

Resolution: fixed
