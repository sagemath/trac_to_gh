# Issue 1561: [with patch] add ._matrix_() and .transpose() to vector/FreeModuleElement.

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-12-18 19:36:47

Assignee: malb

Keywords: matrix vector transpose FreeModuleElement

This makes `matrix(vector(2, 3, 4))` and `transpose(vector(2, 3, 4))` work -- very handy when translating PARI code.


---

Attachment


---

Comment by rlm created at 2007-12-21 22:37:48

Resolution: fixed


---

Comment by rlm created at 2007-12-21 22:37:48

merged in 2.9.1 alpha3
