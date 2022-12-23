# Issue 6301: implement the Hadamard product of two matrices

Issue created by migration from https://trac.sagemath.org/ticket/6301

Original creator: ncalexan

Original creation time: 2009-06-15 16:12:18

Assignee: was

CC:  rbeezer ylchapuy

Keywords: Hadamard matrix product

That is, given a matrix A and another matrix B (of the same dimensions), form C such that C[i, j] = A[i, j] * B[i, j].


---

Comment by rbeezer created at 2009-07-14 22:32:27

Changing type from defect to enhancement.


---

Comment by rbeezer created at 2009-07-14 22:32:27

Patch overview:

`elementwise_product()` in `matrix2.pyx` checks inputs for proper sizes, and coerces base rings, etc.

Then two versions of `_elementwise_product()` (in `matrix_dense.pyx` and `matrix_sparse.pyx`) take over and do the actual work in what should be a fairly efficient manner, given the generality implied.  

More efficient implementations are certainly possible for more specialized classes.  The intent here is to begin with a correct and general implementation that is moderately efficient, primarily to make the functionality available in Sage.


---

Comment by rbeezer created at 2009-07-14 22:32:27

Changing keywords from "Hadamard matrix product" to "elementwise Hadamard matrix product".


---

Attachment


---

Comment by jason created at 2009-07-19 07:25:16

Nice work!  This all looks great.  Doctests in these files pass as well.  Positive review.


---

Comment by mvngu created at 2009-07-19 14:50:06

Resolution: fixed
