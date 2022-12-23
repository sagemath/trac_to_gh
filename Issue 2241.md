# Issue 2241: Leak in totallyreal_rel.py

Issue created by migration from https://trac.sagemath.org/ticket/2241

Original creator: mabshoff

Original creation time: 2008-02-21 00:36:17

Assignee: craigcitro

The ticket is different than #2239. 

The issue seems to be in the coercion code somewhere:

```
==25102== 164,280 bytes in 4,107 blocks are definitely lost in loss record 8,413 of 8,436
==25102==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==25102==    by 0xC90D42B: __pyx_f_4sage_5rings_11real_double_fast_tp_new (real_double.c:10022)
==25102==    by 0xC9065CA: __pyx_f_4sage_5rings_11real_double_17RealDoubleElement__mul_c_impl (real_double.c:5041)
==25102==    by 0xA08ECD3: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:16691)
==25102==    by 0x41580C: binary_op1 (abstract.c:398)
==25102==    by 0x418F47: PyNumber_Multiply (abstract.c:669)
==25102==    by 0x6D9512D: op_mul (operator.c:73)
==25102==    by 0x415542: PyObject_Call (abstract.c:1860)
==25102==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==25102==    by 0xA2F21BF: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5155)
==25102==    by 0xA08EE41: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:8882)
==25102==    by 0x415861: binary_op1 (abstract.c:404)
```


Cheers,

Michael


---

Comment by jvoight created at 2008-02-29 20:07:54

I don't know how to read this.  Will a similar approach as in #2239 fix this memleak?  (In totallyreal_rel.py, numpy.roots is called on an array of floats instead of ints...)

JV


---

Comment by mabshoff created at 2008-09-15 04:43:31

This issue has been fixed some time prior to Sage 3.1.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-15 04:43:31

Resolution: fixed
