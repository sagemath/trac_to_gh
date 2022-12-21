# Issue 561: memleak in MultiModularBasis_base__extend_moduli_to_height_c exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 00:18:20

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 2,128 bytes in 133 blocks are definitely lost in loss record 2,338 of 2,944
==5107==    at 0x4A0590B: realloc (vg_replace_malloc.c:306)
==5107==    by 0x94A8760: __gmpz_realloc (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x94A55E8: __gmpz_mul_2exp (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x1F4BF558: __pyx_f_13multi_modular_22MultiModularBasis_base__extend_moduli_to_height_c (multi_modular.c:2760
)
==5107==    by 0x1F4BEA56: __pyx_f_13multi_modular_22MultiModularBasis_base__extend_moduli_to_height (multi_modular.c:2688)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x1F4BD032: __pyx_f_13multi_modular_22MultiModularBasis_base___init__ (multi_modular.c:2618)
==5107==    by 0x45A321: type_call (typeobject.c:436)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den
se.c:7503)
```

Cheers,

Tagged for 2.8.4

Michael


---

Comment by mabshoff created at 2007-09-02 00:30:00

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-14 23:01:57

patch is attached to #559, but will be submitted by me as a mercurial patch.

Cheers,

Michael


---

Attachment

burcin's fix extracted from the patch for #559


---

Comment by was created at 2007-10-20 19:10:57

Resolution: fixed
