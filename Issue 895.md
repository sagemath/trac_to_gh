# Issue 895: [with patch] .inverse() method for matrices

Issue created by migration from https://trac.sagemath.org/ticket/895

Original creator: mhansen

Original creation time: 2007-10-13 23:47:18

Assignee: mhansen




---

Attachment

This patch needs some work:

  1. It should be in matrix2.pyx not matrix_dense.pyx, so it will be available to both sparse and dense matrices.

  2. It should call m.__invert__() instead of do m**(-1).      Or it could call ~m, which is the Python notation for __invert__.

  3. The docstring should also mention doing ~m.

William


---

Attachment

Upadated patch -- use the last one and ignore the first one.


---

Comment by was created at 2007-10-21 03:34:41

Resolution: fixed


---

Comment by was created at 2007-10-21 03:34:46

Resolution changed from fixed to 


---

Comment by was created at 2007-10-21 03:34:46

Changing status from closed to reopened.


---

Comment by malb created at 2007-10-23 19:48:42

applied to 2.8.9.alpha0


---

Comment by malb created at 2007-10-23 19:48:42

Resolution: fixed
