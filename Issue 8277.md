# Issue 8277: Using matrix() to convert between sparse and dense.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-02-15 22:01:08

Assignee: hivert

Keywords: sparse matrix conversion

A call to `matrix` does not change the sparsity:

```
    sage: mat = matrix(ZZ, [[1,1],[1,1]], sparse=False)
    sage: type(mat)
    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
    sage: mat2 = matrix(ZZ, mat, sparse=True)
    sage: type(mat2)
    <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>
```



---

Comment by AlexGhitza created at 2010-09-02 10:50:43

Changing component from algebra to linear algebra.


---

Comment by jdemeyer created at 2018-03-01 15:00:46

Resolution: duplicate


---

Comment by jdemeyer created at 2018-03-01 15:00:46

Fixed in #24742.
