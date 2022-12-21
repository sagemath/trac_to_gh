# Issue 6120: [with patch, needs review] P(0).total_degree() should return -1 for multivariate polynomial rings

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-05-22 10:43:21

Assignee: malb

CC:  cremona simonking

but it returns `0` now.


---

Attachment


---

Comment by cremona created at 2009-05-22 12:17:48

At the same time we *must* do the same for the degree of univariate polynomials!  there is a degree() function in rings/polynomial/polynomial_element_generic.py which currently returns -1 for deg(0), but there may be other places too -- maybe malb knows if there are others?


---

Comment by malb created at 2009-05-22 13:15:39

I checked a few implementations, they all seem to agree that deg(0) == -1.


---

Comment by AlexGhitza created at 2009-05-30 08:46:23

Looks good, applies (with some fuzz) to 4.0.rc2, and passes doctests in sage/rings/polynomial.


---

Comment by mhansen created at 2009-05-31 23:57:29

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-05-31 23:57:29

Resolution: fixed
