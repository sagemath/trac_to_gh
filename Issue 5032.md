# Issue 5032: dividing a sparse matrix by a scalar gives a dense matrix, but multiplying gives a sparse one

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-20 05:59:45

Assignee: was

This is a bug:

```
sage: A = matrix(ZZ, 2, [1..4], sparse=True)
sage: type(A*1)
<type 'sage.matrix.matrix_integer_sparse.Matrix_integer_sparse'>
sage: type(A/1)
<type 'sage.matrix.matrix_rational_dense.Matrix_rational_dense'>
```



---

Comment by robertwb created at 2009-01-20 07:04:24

This is because it creates the matrix space over the fraction field when division is done, and I agree that it is a bug that the sparce flag doesn't get passed on. In contrast 


```
sage: A = matrix(QQ, 2, [1..4], sparse=True)
sage: type(A)
<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
sage: type(A/1)
<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
```


What needs to change is 


```
File:           /Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py
Definition:     MS.construction(self)
Source:
    def construction(self):
        from sage.categories.pushout import MatrixFunctor
        return MatrixFunctor(self.__nrows, self.__ncols), self.base_ring()
```


It should read


```
        return MatrixFunctor(self.__nrows, self.__ncols, is_sparse=self.is_sparse), self.base_ring()
```



---

Attachment


---

Comment by rlm created at 2009-01-23 15:02:03

I was right in the middle of tracking this down when you posted the patch, so I figured I'd review it right away. ;)


---

Comment by mabshoff created at 2009-01-24 14:31:31

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 14:31:31

Merged in Sage 3.3.alpha2
