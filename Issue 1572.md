# Issue 1572: binary in graphs/graph_fast.pyx leaks like a sieve

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-20 04:51:09

Assignee: mabshoff

Running `devel/sage/sage/graphs/graph_database.py` leads to:

```
==28008== LEAK SUMMARY:
==28008==    definitely lost: 373,192 bytes in 55,057 blocks.
==28008==      possibly lost: 330,333 bytes in 980 blocks.
==28008==    still reachable: 43,708,225 bytes in 20,919 blocks.
==28008==         suppressed: 0 bytes in 0 blocks.
```

Specifically:

```
==28008== 152,864 bytes in 27,528 blocks are definitely lost in loss record 2,812 of 2,879
==28008==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==28008==    by 0x6160485: __gmpz_get_str (in /tmp/Work-mabshoff/sage-2.9/local/lib/libgmp.so.3.4.1)
==28008==    by 0x1863AAC2: __pyx_pf_4sage_6graphs_10graph_fast_binary (graph_fast.c:2002)
==28008==    by 0x415522: PyObject_Call (abstract.c:1860)
==28008==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==28008==    by 0x1864155A: __pyx_pf_4sage_6graphs_10graph_fast_R_inverse (graph_fast.c:2939)
==28008==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==28008==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==28008==    by 0x4CE527: function_call (funcobject.c:517)
==28008==    by 0x415522: PyObject_Call (abstract.c:1860)
==28008==    by 0x41BC42: instancemethod_call (classobject.c:2497)
==28008==    by 0x415522: PyObject_Call (abstract.c:1860)

==28008== 220,200 bytes in 27,525 blocks are definitely lost in loss record 2,815 of 2,879
==28008==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==28008==    by 0x6160C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.9/local/lib/libgmp.so.3.4.1)
==28008==    by 0x1863AA91: __pyx_pf_4sage_6graphs_10graph_fast_binary (graph_fast.c:1983)
==28008==    by 0x415522: PyObject_Call (abstract.c:1860)
==28008==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==28008==    by 0x1864155A: __pyx_pf_4sage_6graphs_10graph_fast_R_inverse (graph_fast.c:2939)
==28008==    by 0x483031: PyEval_EvalFrameEx (ceval.c:3564)
==28008==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==28008==    by 0x4CE527: function_call (funcobject.c:517)
==28008==    by 0x415522: PyObject_Call (abstract.c:1860)
==28008==    by 0x41BC42: instancemethod_call (classobject.c:2497)
==28008==    by 0x415522: PyObject_Call (abstract.c:1860)
```

The patch that will be attached shortly reduces that to:

```
==28989== LEAK SUMMARY:
==28989==    definitely lost: 128 bytes in 4 blocks.
==28989==      possibly lost: 330,809 bytes in 981 blocks.
==28989==    still reachable: 43,707,313 bytes in 20,902 blocks.
==28989==         suppressed: 0 bytes in 0 blocks.
```

It passes testall.

Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2007-12-20 18:16:57

Merged in 2.9.1 alpha2


---

Comment by rlm created at 2007-12-20 18:16:57

Resolution: fixed
