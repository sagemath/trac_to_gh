# Issue 956: small memleak in the graph_isom code

Issue created by migration from https://trac.sagemath.org/ticket/956

Original creator: mabshoff

Original creation time: 2007-10-21 04:43:26

Assignee: mabshoff

Keywords: graph isom

Valgrinding the code from #939 leads to

```
==9242== LEAK SUMMARY:
==9242==    definitely lost: 25,877 bytes in 3,205 blocks.
==9242==      possibly lost: 318,230 bytes in 908 blocks.
==9242==    still reachable: 43,973,827 bytes in 28,805 blocks.
==9242==         suppressed: 0 bytes in 0 blocks.
```

In detail:

```
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,618 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6100C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD777E: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6942)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==9242==
==9242==
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,619 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD77A4: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6960)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==9242==
==9242==
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,620 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD7791: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6951)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==9242==
==9242==
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,620 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD7791: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6951)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
```



---

Comment by mabshoff created at 2007-10-21 04:43:36

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-21 04:47:26


```
[06:46] <mabshoff> robert___: You need to up the upper bound for the deallocation matching
[06:46] <mabshoff>     # allocate GMP ints
[06:46] <mabshoff>     for i from 0 <= i < n+2:
[06:46] <mabshoff>         mpz_init(Lambda_mpz[i])
[06:46] <mabshoff>         mpz_init_set_si(zf_mpz[i], -1) # correspond to default values of
[06:46] <mabshoff>         mpz_init_set_si(zb_mpz[i], -1) # "infinity"
[06:46] <mabshoff>     # deallocate the MP integers
[06:46] <mabshoff>     for i from 0 <= i < n:
[06:46] <mabshoff>         mpz_clear(Lambda_mpz[i])
[06:46] <mabshoff>         mpz_clear(zf_mpz[i])
[06:46] <mabshoff>         mpz_clear(zb_mpz[i])
```


Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2007-10-22 01:46:25

Please refer to ticket #968


---

Comment by rlm created at 2007-10-22 01:46:25

Resolution: duplicate


---

Comment by mabshoff created at 2007-10-22 07:03:38

Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-22 07:03:38

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2007-10-22 07:03:38

Changing status from closed to reopened.


---

Comment by rlm created at 2007-10-22 16:21:59

PLEASE NOTE -- Don't use the patch here!! Instead, use the ones in #968.


---

Comment by malb created at 2007-10-23 19:58:23

Resolution: duplicate
