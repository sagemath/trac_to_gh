# Issue 5370: [with patch, needs review] copy for matrix_double_dense

Issue created by migration from https://trac.sagemath.org/ticket/5370

Original creator: ylchapuy

Original creation time: 2009-02-25 10:50:15

Assignee: was

no __copy__ defined for matrix_double_dense, add it.


---

Attachment


---

Comment by ylchapuy created at 2009-02-25 10:58:55

apply patch after #5362


---

Attachment


---

Comment by mhansen created at 2009-02-25 18:26:26

Looks good. I updated the patch to the new docstring format.

Apply only trac-5370-copy-matrix_double_dense.2.patch


---

Comment by mabshoff created at 2009-02-28 17:10:10

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 17:10:10

Merged trac-5370-copy-matrix_double_dense.2.patch only in Sage 3.4.rc0.

Cheers,

Michael
