# Issue 1812: [with patch] doctest coverage for finite_field_givaro up to 100%

Issue created by migration from https://trac.sagemath.org/ticket/1812

Original creator: malb

Original creation time: 2008-01-17 22:40:53

Assignee: tba

besides this, this patch also removes the redundant `K.is_prime` method, sorry for the mess. It can easily be re-added though but this time in `FiniteField_generic` instead of in every implementation.


---

Attachment


---

Comment by mhansen created at 2008-01-21 04:12:33

Looks good to me.


---

Comment by mabshoff created at 2008-01-21 04:22:42

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 04:22:42

Resolution: fixed
