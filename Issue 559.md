# Issue 559: memleak in multi_modular_MultiModularBasis_base exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from https://trac.sagemath.org/ticket/559

Original creator: mabshoff

Original creation time: 2007-09-02 00:14:35

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 1,056 bytes in 132 blocks are definitely lost in loss record 2,208 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x1F4BD6EF: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2324)
==5107==    by 0x1F4B92A0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5836)
==5107==    by 0x45A272: type_call (typeobject.c:422)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den
se.c:7503)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x204237E0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_integer
_dense.c:5487)
==5107==    by 0xDFD6878: __pyx_f_7element_6Matrix__matrix_times_matrix_c (element.c:11483)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-09-02 00:29:41

Changing status from new to assigned.


---

Attachment


---

Comment by burcin created at 2007-09-21 01:12:36

The following code causes similar errors:


```
A = random_matrix(ZZ, 100, 200, density=.001)
B = random_matrix(ZZ, 200, 100, density=.001)
C = A*B
del A, B, C
```


The first chunk of the attached fixes these. The second chunk is useful for #561.

Unfortunately, this isn't enough to reduce all the noise MultiModularBasis makes while running


```
m = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache();
```



---

Comment by mabshoff created at 2007-10-14 23:02:14

Patch will be submitted by me as a mercurial patch.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-15 02:21:24

Resolution: fixed


---

Comment by mabshoff created at 2007-10-15 02:21:24

As it turns out the part of the patch the fixed this ticket was wrong and coincidentally I already fixed this with another patch. The part of the patch that fixes #561 is valid. I will post that patch with credit to burcin there.

Cheers,

Michael
