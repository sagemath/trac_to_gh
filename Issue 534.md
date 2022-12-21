# Issue 534: matrix_modn_sparse_Matrix_modn_sparse leak (from modular/ssmod/ssmod.py)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-30 18:52:22

Assignee: mabshoff

From Sage 2.8.3rc3:

```
==24845== 32,608 (30,120 direct, 2,488 indirect) bytes in 25 blocks are definitely lost in loss record 2,491 of 2,587
==24845==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==24845==    by 0x1FCAF14A: __pyx_tp_new_18matrix_modn_sparse_Matrix_modn_sparse (matrix_modn_sparse.c:2810)
==24845==    by 0x45A272: type_call (typeobject.c:422)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24845==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==24845==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==24845==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==24845==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==24845==    by 0x4CFED0: function_call (funcobject.c:517)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24845==    by 0x41BE0C: instancemethod_call (classobject.c:2497)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 18:52:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-14 11:59:37

Fixed along the way, probably with my other modular memleak fixes.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-14 12:45:32

Resolution: fixed
