# Issue 2644: doctest failures in matrix_real_double_dense

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-03-22 14:39:47

Assignee: was

On 2.11alpha0, the doctest for `__invert__` randomly fails


---

Attachment

patch against 2.11alpha


---

Comment by dfdeshom created at 2008-03-22 15:37:24

Here is a patch against 2.11alpha0


---

Comment by dfdeshom created at 2008-03-22 15:38:07

Changing assignee from was to dfdeshom.


---

Comment by AlexGhitza created at 2008-03-22 15:48:21

Looks good and tests fine.


---

Comment by mabshoff created at 2008-03-22 19:13:30

Yep, I think this is the right way to fix this. It is clear from the context that the inversion of the matrix should fail and am somewhat surprised that the numerical noise is large enough that the determinant of a rank deficient matrix like A in this example is not even close to zero.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 19:14:21

Merged in Sage 2.11.alpha1


---

Comment by mabshoff created at 2008-03-22 19:14:21

Resolution: fixed
