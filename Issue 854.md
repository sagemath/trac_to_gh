# Issue 854: [with patch] memory leak: MultiModularBasis_base_mpz_crt_vec_tail

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-12 00:58:20

Assignee: mabshoff


```
==15091== 24,160 bytes in 3,020 blocks are definitely lost in loss record 2,218 of 2,504
==15091==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==15091==    by 0x6108C60: __gmpz_init_set (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==15091==    by 0x11CD7DC0: __pyx_f_13multi_modular_22MultiModularBasis_base_mpz_crt_vec_tail (multi_modular.c:4543)
==15091==    by 0x11CD2DB9: __pyx_f_13multi_modular_17MultiModularBasis_mpz_crt_vec (multi_modular.c:5435)
==15091==    by 0x1262F7A4: __pyx_f_20matrix_integer_dense__lift_crt (matrix_integer_dense.c:17664)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==15091==    by 0x1265ECF8: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de
nse.c:7916)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==15091==    by 0x126356BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege
r_dense.c:5669)
==15091==    by 0x9341519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)
```



---

Attachment


---

Comment by mabshoff created at 2007-10-12 01:05:04

William,

please check if this is the right way to fix this. "sage -testall" passes on sage.math with the patch applied.

Cheers,

Michael


---

Comment by was created at 2007-10-13 07:28:03

Resolution: fixed
