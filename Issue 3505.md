# Issue 3505: change ints to Py_ssize_t in various pickling code in sage/matrix

Issue created by migration from https://trac.sagemath.org/ticket/3505

Original creator: craigcitro

Original creation time: 2008-06-24 23:11:22

Assignee: craigcitro

There are several places where we use `cdef int i, j` to index into a matrix, where we should be using `Py_ssize_t`, such as `matrix_integer_dense.pyx` in the `pickle_version_0` code. Also in `matrix_rational_dense.pyx`, maybe others.


