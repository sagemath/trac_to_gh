# Issue 7920: Common numerical matrix base class

Issue created by migration from Trac.

Original creator: dagss

Original creation time: 2010-01-13 14:19:12

Assignee: was

Currently, Matrix_double_dense inherits from Matrix_dense and Matrix_double_sparse from Matrix_sparse. However numerical matrices share a lot compared to other matrices and should probably have a common base class:

 - Docstrings of numerical decompositions should likely be shared
 - `solve_right` implementation should be shared
 - Even if one matrix uses SuiteSparse and another LAPACK for making decompositions, the code for using those decompositions to find solutions, and iteratively improve the solutions, can be shared
 - In general, a place to put docstrings and examples with terminology more familiar to numerical users

Luckily, Matrix_dense/sparse offers little in terms of implementation for numerical matrices (the exception is the hash value -- which is useless for numerical matrices anyway, but should be implemented).

In the future, there might be diagonal, Hermitian, triangular, banded etc. matrices, and then it makes even more sense to change the hierarchy, so that sparse/dense isn't a superclass.

So, this ticket should result in:
 - Introduce Matrix_numerical
 - Change the base class of Matrix_double_dense and Matrix_double_sparse to Matrix_numerical
 - A `Matrix_numerical.solve_right` centered around matrix decompositions

Incidentally, this is likely to result in:
 - A proper pickle implementation for dense double matrices (just pickle the NumPy array; and read back the dtype on unpickle)
 - Loosing the Matrix_real_double_dense and Matrix_complex_double_dense subclasses -- these serve no real purpose at all, and prevents introducing e.g. efficient dense lower-triangular matrices and so on. (Remember to keep stubs aliased to Matrix_double_dense for unpickling backward compatability)


---

Attachment


---

Comment by dagss created at 2010-01-13 14:25:02

Changing status from new to needs_work.


---

Comment by dagss created at 2010-01-13 14:25:02

The patch is very much unfinished. There's some stuff that likely belongs to a seperate patch. The interesting part is matrix_numerical.pyx, and the fact that Matrix_double_sparse is "converted" to it as a base class.


---

Comment by dagss created at 2010-01-13 14:29:35

Changing type from defect to task.
