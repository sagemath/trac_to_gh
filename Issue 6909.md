# Issue 6909: [with patch, needs review]

Issue created by migration from https://trac.sagemath.org/ticket/6909

Original creator: malb

Original creation time: 2009-09-09 16:36:50

Assignee: malb

Implement a couple of functions using the new libsingular functions interface (#6628).


---

Attachment

The attached patch
 * implements a Pythonic interface to the Singular options 
 * fixes a bug where local orderings were not used correctly 
 * switches `groebner_basis()` and `elimination_ideal()` to libsingular.

For most functions on multivariate polynomial ideals we first need to wrap libSingular lists since many functions return lists. This would require an updated SPKG.


---

Comment by PolyBoRi created at 2009-10-05 12:34:27

Hi,
I spent 10 minutes reading the code and like it (this is not a formal review).
Cheers,
Michael


---

Comment by burcin created at 2009-10-11 15:04:48

rebased to 4.1.2.rc0


---

Comment by burcin created at 2009-10-11 15:07:46

Changing status from needs_review to positive_review.


---

Attachment

Positive review.

Apply only attachment:trac_6909-libsingular_more_functions.patch, which is a rebase of Martin's patch to 4.1.2.rc0.


---

Comment by mhansen created at 2009-10-16 04:59:39

Resolution: fixed
