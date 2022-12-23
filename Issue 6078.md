# Issue 6078: Add compatibility functions with deprecation warnings for QF code after doctest patch

Issue created by migration from https://trac.sagemath.org/ticket/6078

Original creator: tornaria

Original creation time: 2009-05-19 00:53:35

Assignee: tbd

The patches at #5954, #6037 and #6040 bring doctest coverage for quadratic forms up to 100%. In this patch series some functions were removed or renamed, so we should add compatibility functions.

These are the functions I propose we should handle:
 - count_modp__by_gauss_sum renamed to count_modp_solutions__by_Gauss_sum.
 - count_local_type was renamed to count_congruence_solutions.
 - count_local_good_type was renamed to count_congruence_solutions__good_type.
 - count_local_zero_type was renamed to count_congruence_solutions__zero_type. 
 - count_local_bad_type was renamed to count_congruence_solutions__bad_type. 
 - count_local_bad_typeI was renamed to count_congruence_solutions__bad_type_I. 
 - count_local_bad_typeII was renamed to count_congruence_solutions__bad_type_II.
 - GHY_mass_maximal was renamed to GHY_mass__maximal.


---

Comment by tornaria created at 2009-05-19 00:55:28

Note, there are other functions which were removed, but most of them were not implemented, or wrongly implemented, badly or no documented, etc. It really makes no sense to keep them around.


---

Comment by mabshoff created at 2009-05-19 00:56:11

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-05-19 00:56:11

Changing assignee from tbd to justin.


---

Comment by mabshoff created at 2009-05-19 00:56:11

Changing component from algebra to quadratic forms.


---

Comment by was created at 2009-05-28 06:53:20

This isn't critical for 4.0.


---

Comment by was created at 2009-06-15 23:31:12

I don't see the point in doing this, since quadratic forms was only in Sage for a very short amount of time before making this API change.


---

Comment by was created at 2009-06-15 23:31:12

Resolution: invalid
