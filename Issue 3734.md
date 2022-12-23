# Issue 3734: inverse() fails for 0 by 0 matrices

Issue created by migration from https://trac.sagemath.org/ticket/3734

Original creator: cremona

Original creation time: 2008-07-28 09:36:29

Assignee: was

As reported to sage-devel on 2008-07-19:


```
Puzzle question:  find a matrix with rank 0 but determinant 1:

sage: type(M)
<type 'sage.matrix.matrix_generic_dense.Matrix_generic_dense'>
sage: M.rank()
0
sage: M.determinant()
1.00000000000000

Answer:  M is 0x0:
sage: M
[]
sage: [M.nrows(), M.ncols()]
[0, 0]

Now I am happy with all that (since I am computing regulators of
elliptic curves which may have rank 0).  And with this:
sage: M.is_invertible()
True
but then disappointed by this:
sage: M.inverse()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/john/sage-3.0.4/<ipython console> in <module>()

/home/john/sage-3.0.4/matrix2.pyx in
sage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19932)()

/home/john/sage-3.0.4/matrix0.pyx in
sage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:14525)()

/home/john/sage-3.0.4/matrix0.pyx in
sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:3129)()

IndexError: matrix index out of range
```


The matrix inversion code should catch this case and return the same matrix.



---

Attachment


---

Comment by cremona created at 2008-07-29 00:37:20

Before:

```
sage: MatrixSpace(ZZ,0,0)(0).inverse()  
[]
sage: MatrixSpace(QQ,0,0)(0).inverse()
[]
sage: MatrixSpace(RR,0,0)(0).inverse()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/john/sage-3.0.4/<ipython console> in <module>()

/home/john/sage-3.0.4/matrix2.pyx in sage.matrix.matrix2.Matrix.inverse (sage/matrix/matrix2.c:19932)()

/home/john/sage-3.0.4/matrix0.pyx in sage.matrix.matrix0.Matrix.__invert__ (sage/matrix/matrix0.c:14525)()

/home/john/sage-3.0.4/matrix0.pyx in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:3129)()

IndexError: matrix index out of range
```


After applying sage-trac3734.patch:

```
sage: MatrixSpace(ZZ,0,0)(0).inverse()
[]
sage: MatrixSpace(QQ,0,0)(0).inverse()
[]
sage: MatrixSpace(RR,0,0)(0).inverse()
[]
```


Patch was based on 3.0.4


---

Comment by dfdeshom created at 2008-07-30 17:04:50

Patch looks good to me.


---

Comment by mabshoff created at 2008-07-30 22:49:30

Resolution: fixed


---

Comment by mabshoff created at 2008-07-30 22:49:30

Merged in Sage 3.1.alpha0
