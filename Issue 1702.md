# Issue 1702: memleak in fplll.[pyx|pxi] in "void ZZ_mat_delete"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-06 16:25:13

Assignee: malb

While valgrinding the `fplll.pyx` doctest I came across the following:

```
==15667== 19,200 (12,800 direct, 6,400 indirect) bytes in 800 blocks are definitely lost in loss record 7,374 of 7,520
==15667==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==15667==    by 0x1B643D99: __pyx_pf_4sage_4libs_5fplll_5fplll_6FP_LLL___new__(_object*, _object*, _object*) (fplll.cpp:1677
)
==15667==    by 0x1B643F24: __pyx_tp_new_4sage_4libs_5fplll_5fplll_FP_LLL(_typeobject*, _object*, _object*) (fplll.cpp:4211)
==15667==    by 0x458D92: type_call (typeobject.c:422)
==15667==    by 0x415542: PyObject_Call (abstract.c:1860)
==15667==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==15667==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==15667==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==15667==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==15667==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==15667==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==15667==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
```

The problem is in fplll.pxi:

```
 void ZZ_mat_delete "delete "(ZZ_mat *mem)
```

It doesn't clear the mpzs allocated in fplll.pyx's `__new__`:

```
    def __new__(self, Matrix_integer_dense A):
        cdef int i,j
        self._lattice = ZZ_mat_new(A._nrows,A._ncols)

        cdef Z_NR *t

        for i from 0 <= i < A._nrows:
            for j from 0 <= j < A._ncols:
                t = Z_NR_new()
                t.set_mpz_t(A._matrix[i][j])
                self._lattice.Set(i,j,t[0])

    def __dealloc__(self):
        """
        Destroy internal data.
        """
        ZZ_mat_delete(self._lattice)
```

Should be easy enough to fix.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-06 23:45:34

Patch looks good. `sage -testall` passes. Some statistics:
Before:

```
=15667== LEAK SUMMARY:
==15667==    definitely lost: 12,800 bytes in 800 blocks.
==15667==    indirectly lost: 6,400 bytes in 800 blocks.
==15667==      possibly lost: 257,447 bytes in 773 blocks.
==15667==    still reachable: 29,391,420 bytes in 182,453 blocks.
==15667==         suppressed: 0 bytes in 0 blocks.
```

After:

```
==19108== LEAK SUMMARY:
==19108==    definitely lost: 0 bytes in 0 blocks.
==19108==      possibly lost: 257,447 bytes in 773 blocks.
==19108==    still reachable: 29,391,404 bytes in 182,452 blocks.
==19108==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-07 16:30:06

Resolution: fixed


---

Comment by mabshoff created at 2008-01-07 16:30:06

Merged in 2.10.alpha0
