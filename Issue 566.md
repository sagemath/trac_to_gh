# Issue 566: gmpz leak in gmp.pxi

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 00:36:11

Assignee: mabshoff

Hello,

every piece of code that includes gmp.pxi leaks at least one gmpz:

```
  /* "/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/rings/../ext/gmp.pxi":66
 * cdef mpq_t tmp
 * mpz_init(u);  mpz_init(v); mpz_init(q)
 * mpz_init(u0); mpz_init(u1); mpz_init(u2)             # <<<<<<<<<<<<<<
 * mpz_init(v0); mpz_init(v1); mpz_init(v2)
 * mpz_init(t0); mpz_init(t1); mpz_init(t2)
 */
  mpz_init(__pyx_v_8rational_u0);
```

Valgrind says:

```
==25825== 8 bytes in 1 blocks are still reachable in loss record 349 of 2,539
==25825==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==25825==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==25825==    by 0x169D8914: initrational (rational.c:10891)
==25825==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==25825==    by 0x49D63E: import_submodule (import.c:2394)
==25825==    by 0x49DB11: load_next (import.c:2214)
==25825==    by 0x49DD6E: import_module_level (import.c:2002)
==25825==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
==25825==    by 0x47D5D8: builtin___import__ (bltinmodule.c:47)
==25825==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==25825==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==25825==    by 0x480BD3: PyEval_EvalFrameEx (ceval.c:2063)
```

This leak is usually 8 bytes only, so this counts as noise.

Cheers,

Michael




---

Comment by mabshoff created at 2007-09-02 00:36:22

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-02 23:50:15


```
[00:58] <sage> No -- there is a separate copy of the entire gmp.pxi in each file that includes it.
[00:58] <sage> It's not shared at all.
[00:59] <sage> Some of gmp.pxi should be moved to c_lib, i.e., to libsage.so
[00:59] <mabshoff> So the *.pxi are really includes.
[00:59] <sage> Then it would all be shared.
```


After the move we need to define a cleanup routine and call that routine from sage/all.py

Cheers,

Michael


---

Attachment


---

Comment by was created at 2007-09-07 03:16:38

Resolution: fixed


---

Comment by was created at 2007-09-07 06:01:08

Changing status from closed to reopened.


---

Comment by was created at 2007-09-07 06:01:08

Resolution changed from fixed to 


---

Comment by was created at 2007-09-07 06:01:08

This actually crashes numerous doctests, e.g., modular/modsym/space.py.

I've posted (to the official repo) this patch, but with a following patch
that modifies a few lines of gmp.pxi to *disable* the effects of this patch.
So you should pull the lates (hg_sage.pull()), then edit gmp.pxi to re-enable
this patch, then build, then do this many times:

```
sage`@`modular:~/d/sage/sage/modular/modsym$ sage -t space.py
```


You'll see numerous memory allocation errors.


---

Comment by malb created at 2007-09-07 10:51:59

Fixed in attached `segfault-fix.patch`. The problem was that vector_times_matrix in Matrix_rational_dense used the global `mpz_t y` locally as `mpq_t` and cleared it.


---

Attachment


---

Comment by was created at 2007-09-07 18:38:35

Resolution: fixed
