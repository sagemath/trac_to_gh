# Issue 6037: Major Upgrade to QuadraticForm Local Density Routines

Issue created by migration from Trac.

Original creator: jonhanke

Original creation time: 2009-05-14 10:03:59

Assignee: justin

CC:  mabshoff wstein tornaria

Completely rewritten and doctested Local densities routines according to a consistent interface (and algorithms) described in the attached PDF file.

Patch to follow very shortly!


---

Comment by jonhanke created at 2009-05-14 10:05:49

Description of the inputs and algorithms used in QF local density routines


---

Attachment


---

Attachment


---

Attachment

LaTeX file used to create the PDF writeup


---

Comment by tornaria created at 2009-05-19 00:30:33

Looks nice. For the record, the following exported member functions (of QuadraticForm) have been renamed/removed:
 - `reindex_vector_from_extraction` was removed
 - `count_modp__by_gauss_sum` was renamed to `count_modp_solutions__by_Gauss_sum`.
 - `local_good_density_congruence_even__experimental` was removed.
 - `VecIncrement__deprecated` was removed.
 - `local_solution_type__deprecated` was removed.
 - `CountAllLocalTypesNaive__deprecated` was removed.
 - `count_local_type` was renamed to `count_congruence_solutions`.
 - `count_local_good_type` was renamed to `count_congruence_solutions__good_type`.
 - `count_local_zero_type` was renamed to `count_congruence_solutions__zero_type`.
 - `count_local_bad_type` was renamed to `count_congruence_solutions__bad_type`.
 - `count_local_bad_typeI` was renamed to `count_congruence_solutions__bad_type_I`.
 - `count_local_bad_typeII` was renamed to `count_congruence_solutions__bad_type_II`.
 - `local_good_density` was removed.
 - `local_zero_density` was removed.
 - `local_bad_density` was removed.
 - `local_badI_density` was removed.
 - `local_badII_density` was removed.

I think the `__deprecated` and `__experimental` functions need no comment. For the renamed functions, though, it may be nice to add a compatibility wrapper with deprecation warning... (where and how?)

Jon, internal routines should be using names starting with an underscore (that's the python convention).


---

Comment by mabshoff created at 2009-05-19 00:38:04

Merged patch-2__QF_local_densities__3.4.1.patch in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 00:38:04

Resolution: fixed
