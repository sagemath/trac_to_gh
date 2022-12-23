# Issue 5193: [with patch, needs review] maximum allowed matrix size is too big

Issue created by migration from https://trac.sagemath.org/ticket/5193

Original creator: cwitty

Original creation time: 2009-02-06 03:11:31

Assignee: was

On a 32-bit computer, `MatrixSpace` will let you create a matrix space with up to 2<sup>32</sup>-1 rows or columns.  But we use Py_ssize_t for matrix indices, which can only hold numbers up to 2<sup>31</sup>-1.

Patch attached; all doctests pass on a 64-bit computer, and .../matrix_space.py doctests pass on a 32-bit computer.


---

Attachment

I think the reasoning is that Py_ssize_t is a signed integer to allow for negative indices.


---

Comment by jason created at 2009-02-06 08:23:42

Yep, the reasoning is explained in the patch.  Doctests in matrixspace.py pass on my 32 bit computer.  Positive review.


---

Comment by mabshoff created at 2009-02-06 22:28:39

Merged in Sage 3.3.alpha6.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-06 22:28:39

Resolution: fixed
