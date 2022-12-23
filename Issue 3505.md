# Issue 3505: change ints to Py_ssize_t in various pickling code in sage/matrix

archive/issues_003505.json:
```json
{
    "body": "Assignee: craigcitro\n\nThere are several places where we use `cdef int i, j` to index into a matrix, where we should be using `Py_ssize_t`, such as `matrix_integer_dense.pyx` in the `pickle_version_0` code. Also in `matrix_rational_dense.pyx`, maybe others.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3505\n\n",
    "created_at": "2008-06-24T23:11:22Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "change ints to Py_ssize_t in various pickling code in sage/matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3505",
    "user": "craigcitro"
}
```
Assignee: craigcitro

There are several places where we use `cdef int i, j` to index into a matrix, where we should be using `Py_ssize_t`, such as `matrix_integer_dense.pyx` in the `pickle_version_0` code. Also in `matrix_rational_dense.pyx`, maybe others.



Issue created by migration from https://trac.sagemath.org/ticket/3505


