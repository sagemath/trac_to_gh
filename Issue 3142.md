# Issue 3142: [with patch, needs review] MPolynomialIdeal.homogenize bugfix

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-05-09 10:44:15

Assignee: malb

homogenization could fail if the first polynomial in the list is homogenious but later polynomials aren't.


---

Attachment

Patch is good and passes doctests. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 13:40:09

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 13:40:09

Merged in Sage 3.0.2.alpha0
