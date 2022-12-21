# Issue 3293: [with patch, needs review] MPolynomialRing_generic.random_element returns tuple when degree=0

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-05-24 18:00:26

Assignee: burcin

Attached patch changes `MPolynomialRing_generic.random_element` so that a random element from the base ring is returned when a degree 0 polynomial is requested.


---

Attachment

fix for MPolynomialRing_generic.random_element


---

Comment by mhansen created at 2008-05-24 20:50:46

Looks good to me.


---

Comment by mabshoff created at 2008-05-25 03:27:14

Resolution: fixed


---

Comment by mabshoff created at 2008-05-25 03:27:14

Merged in Sage 3.0.3.alpha0
