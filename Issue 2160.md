# Issue 2160: leftovers from python to cython translation

Issue created by migration from https://trac.sagemath.org/ticket/2160

Original creator: jsp

Original creation time: 2008-02-14 17:42:19

Assignee: was

In matrix/matrix_integer_dense.pyx and matrix//matrix_rational_dense.pyx we delete the line:

tmp = []

because tmp is never used




---

Attachment


---

Comment by mabshoff created at 2008-02-14 21:32:40

Patch looks good.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 21:33:22

Resolution: fixed


---

Comment by mabshoff created at 2008-02-14 21:33:22

Merged in Sage 2.10.2.alpha0
