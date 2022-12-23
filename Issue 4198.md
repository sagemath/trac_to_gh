# Issue 4198: [with patch, needs review] matrix_cyclo_dense.pyx leaks in _get_unsafe

Issue created by migration from https://trac.sagemath.org/ticket/4198

Original creator: mabshoff

Original creation time: 2008-09-26 02:02:06

Assignee: mabshoff

CC:  craigcitro

#3502 added (or exposed?) a small memory leak in matrix_cyclo_dense.pyx's _get_unsafe method. We do not deallocate a tmp mpz in the quick return patch. The attached patch fixes that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 02:02:11

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-09-26 02:22:23

Oops :-)  Patch looks good to me.


---

Comment by mabshoff created at 2008-09-26 02:23:13

Resolution: fixed


---

Comment by mabshoff created at 2008-09-26 02:23:13

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-10-15 13:04:55

The valgrind trace was the following:

```
==19392== 8 bytes in 1 blocks are definitely lost in loss record 71 of 22,499
==19392==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==19392==    by 0x6360947: __gmpz_init (in /scratch/mabshoff/release-cycle/sage-3.1.3.alpha1/local/lib/libgmp.so.3.4.1)
==19392==    by 0x19D0A675: __pyx_f_4sage_6matrix_18matrix_cyclo_dense_18Matrix_cyclo_dense_get_unsafe(__pyx_obj_4sage_6matrix_18matrix_cyclo_dense_Matrix_cyclo_dense*, long, long) (matrix_cyclo_dense.cpp:3773)
==19392==    by 0x16397A16: __pyx_pf_4sage_6matrix_7matrix1_6Matrix_dense_rows (matrix1.c:3933)
==19392==    by 0x415832: PyObject_Call (abstract.c:1861)
==19392==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==19392==    by 0x16392247: __pyx_pf_4sage_6matrix_7matrix1_6Matrix_rows (matrix1.c:3366)
==19392==    by 0x415832: PyObject_Call (abstract.c:1861)
==19392==    by 0x164CEEE9: __pyx_pf_4sage_6matrix_7matrix0_6Matrix_linear_combination_of_rows (matrix0.c:10569)
```

