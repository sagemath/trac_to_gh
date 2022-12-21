# Issue 7474: [with patch, needs review]Expose some more functionality of fmz_poly

Issue created by migration from Trac.

Original creator: mraum

Original creation time: 2009-11-16 17:15:41

Assignee: mraum

Keywords: flint, fmpz_poly, integers

This makes the FLINT wrapper in sage.libs.flint.fmpz_poly handle big integers correctly and exposes shifts and derivatives.


---

Attachment


---

Comment by mhansen created at 2009-11-17 07:34:44

Looks good to me.


---

Comment by mhansen created at 2009-11-17 07:34:44

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-11-17 07:38:54

Actually, the derivative of 1 + 2*x + 6*x^2 should be [2, 12] and not [4, 18].  With this change the tests pass.


---

Comment by mhansen created at 2009-11-17 07:38:54

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-17 07:41:26

Resolution: fixed


---

Attachment
