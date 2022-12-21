# Issue 974: [with spkg] small memleak in nullspace.c in IML

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-23 18:09:18

Assignee: mabshoff

When valgrinding doctest_matrix2.py the following pops up:

```
==4692== 24 bytes in 3 blocks are definitely lost in loss record 124 of 2,497
==4692==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==4692==    by 0x6161E17: __gmpz_init_set_ui (in /tmp/Work-mabshoff/sage-2.8.8/local/lib/libgmp.so.3.4.1)
==4692==    by 0x12A95A43: nullspaceMP (nullspace.c:253)
==4692==    by 0x1293CCA8: __pyx_f_py_20matrix_integer_dense_20Matrix_integer_dense__rational_kernel_iml (matrix_integer_den
se.c:14391)
==4692==    by 0x415522: PyObject_Call (abstract.c:1860)
==4692==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4692==    by 0x12DC1975: __pyx_f_py_21matrix_rational_dense_21Matrix_rational_dense_kernel (matrix_rational_dense.c:7921)
==4692==    by 0x415522: PyObject_Call (abstract.c:1860)
==4692==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4692==    by 0x1139F1A2: __pyx_f_py_7matrix2_6Matrix_kernel_on (matrix2.c:6781)
==4692==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==4692==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```

I fixed the issue in IML and "-testall" passes. The new IML spkg is at

http://sage.math.washington.edu/home/mabshoff/iml-1.0.1.p7.spkg

Before the patch:

```
==4692== LEAK SUMMARY:
==4692==    definitely lost: 6,200 bytes in 147 blocks.
==4692==    indirectly lost: 5,184 bytes in 156 blocks.
==4692==      possibly lost: 377,206 bytes in 906 blocks.
==4692==    still reachable: 37,402,075 bytes in 21,242 blocks.
==4692==         suppressed: 0 bytes in 0 blocks.
```

After the patch:

```
==10896== LEAK SUMMARY:
==10896==    definitely lost: 6,160 bytes in 142 blocks.
==10896==    indirectly lost: 5,184 bytes in 156 blocks.
==10896==      possibly lost: 376,725 bytes in 905 blocks.
==10896==    still reachable: 37,402,500 bytes in 21,245 blocks.
==10896==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-23 18:10:05

Changing status from new to assigned.


---

Comment by malb created at 2007-10-23 19:42:15

applied to 2.8.9.alpha0


---

Comment by malb created at 2007-10-23 19:42:19

Resolution: fixed
