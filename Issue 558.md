# Issue 558: memleak in integer_fast_tp_dealloc exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 00:11:40

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 1,024 bytes in 128 blocks are definitely lost in loss record 2,196 of 2,944
==5107==    at 0x4A0590B: realloc (vg_replace_malloc.c:306)
==5107==    by 0x94A8760: __gmpz_realloc (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x1678B012: __pyx_f_7integer_fast_tp_dealloc (integer.c:14595)
==5107==    by 0x1F4BD7B2: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2222)
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
```

Cheers,

Tagged for 2.8.4

Michael


---

Comment by mabshoff created at 2007-09-02 00:29:32

Changing status from new to assigned.


---

Comment by malb created at 2007-09-06 18:25:56

Some progress with the attached patch:


```
sage: d = [ZZ(i**100000 + 1) for i in range(100)]; del d
sage: get_memory_usage()
577.11328125
sage: sage.rings.integer.free_integer_pool()
sage: get_memory_usage()
570.2421875
```


but if the integers are smaller nothing seems to change


```
sage: d = [ZZ(i**10000 + 1) for i in range(100)]; del d
sage: get_memory_usage()
571.078125
sage: sage.rings.integer.free_integer_pool()
sage: get_memory_usage()
571.078125
```


free_integer_pool() is also called on exit() if the attached patch is applied.


---

Attachment

work in progress for freeing the integer pool on exit


---

Attachment

Patch 6170.patch makes sure no new elements are added tot he pool once its free'd.


---

Comment by was created at 2007-09-07 03:11:55

Resolution: fixed


---

Comment by was created at 2007-09-07 03:49:50

Resolution changed from fixed to 


---

Comment by was created at 2007-09-07 03:49:50

Changing status from closed to reopened.


---

Comment by was created at 2007-09-07 03:52:37

This patch seriously breaks SAGE.  Try 

```
    sage -t --verbose coding/linear_code.py
```

on exit SAGE hangs with


```
*** glibc detected *** /home/was/s/local/bin/python: double free or corruption (out): 0x0000000002b75f70 ***
```


In the official version of SAGE, I'm commenting out the line in all.py that calls the cleanup until
this gets fixed.   Note that all the code mentioned above is in the offical repo, but calling
it is commented out.


---

Comment by malb created at 2007-09-07 11:10:13

The version I got via `hg_sage.pull()` commented out `clear_mpz_globals()` and not `free_integer_pool()`. `clear_mpz_globals()` is not related (more carefully: should not be related) to this ticket. Also, I ran `make test` and did not run ito the `double free` situation on my 64-bit Core2Duo Linux at least. I'll attach a tiny patch to re-enable `clear_mpz_globals()` on exit.


---

Comment by malb created at 2007-09-07 11:10:13

Resolution: fixed


---

Attachment
