# Issue 3499: [with patch, needs review] cyclotomic linear algebra: multiplying 1x1 identity matrix by anything fails

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-06-24 00:23:31

Assignee: craigcitro

This fails:


```
sage: N1 = Matrix(CyclotomicField(6), 1, [1])
sage: cf6 = CyclotomicField(6) ; z6 = cf6.0
sage: N2 = Matrix(CyclotomicField(6), 1, 5, [0,1,z6,-z6,-z6+1])
sage: N1*N2
[         0          1      zeta6     -zeta6 -zeta6 + 1]
```


The attached patch fixes it.


---

Comment by craigcitro created at 2008-06-24 00:26:42

Changing status from new to assigned.


---

Attachment

I just realized that this may depend on trac #3495. Sorry.


---

Comment by was created at 2008-06-24 00:47:08


```
sage: N1 = Matrix(CyclotomicField(6), 1, [1]) 
sage: cf6 = CyclotomicField(6) ; z6 = cf6.0 
sage: N2 = Matrix(CyclotomicField(6), 1, 5, [0,1,z6,-z6,-z6+1]) 
sage: N1*N2
[         0          1      zeta6     -zeta6 -zeta6 + 1]
sage: N1 *N1
[1]
sage: N1 = Matrix(CyclotomicField(6), 1, [-1]) 
sage: N1 *N2
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/element.pyx in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11499)()

/Users/was/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5061)()

/Users/was/action.pyx in sage.categories.action.Action._call_c (sage/categories/action.c:1682)()

/Users/was/action.pyx in sage.matrix.action.MatrixMatrixAction._call_c_impl (sage/matrix/action.c:1934)()

/Users/was/matrix_cyclo_dense.pyx in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._matrix_times_matrix_c_impl (sage/matrix/matrix_cyclo_dense.c:3257)()

/Users/was/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense._lift_crt (sage/matrix/matrix_integer_dense.c:26974)()

IndexError: list index out of range
```



---

Comment by craigcitro created at 2008-06-24 01:07:47

part 2


---

Attachment


---

Comment by was created at 2008-06-24 03:09:30

REPORT:  Very good.  Michael -- apply both patches.


---

Comment by mabshoff created at 2008-06-24 03:39:14

Resolution: fixed


---

Comment by mabshoff created at 2008-06-24 03:39:14

Merged both patches in Sage 3.0.4.alpha1
