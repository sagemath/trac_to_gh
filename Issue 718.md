# Issue 718: still rechable memory: various pyx-files instanciated their own PariInstance

Issue created by migration from https://trac.sagemath.org/ticket/718

Original creator: mabshoff

Original creation time: 2007-09-20 20:34:20

Assignee: mabshoff

Doing a startup + quit with Sage 2.8.4.2 leads to five of the following:

```
==8222== 524,288 bytes in 1 blocks are still reachable in loss record 1,983 of 1,998
==8222==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==8222==    by 0xA6F983A: gpmalloc (in /tmp/Work-mabshoff/sage-2.8.4.3.pre-vg/local/lib/libpari-gmp.so.2)
==8222==    by 0xA6FA8DE: pari_init_opts (in /tmp/Work-mabshoff/sage-2.8.4.3.pre-vg/local/lib/libpari-gmp.so.2)
==8222==    by 0xAA74864: __pyx_f_3gen_12PariInstance___init__ (gen.c:20649)
==8222==    by 0x459220: type_call (typeobject.c:436)
==8222==    by 0x415522: PyObject_Call (abstract.c:1860)
==8222==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==8222==    by 0xAA76BFE: initgen (gen.c:27873)
==8222==    by 0x49E54D: _PyImport_LoadDynamicModule (importdl.c:53)
==8222==    by 0x49C45D: import_submodule (import.c:2394)
==8222==    by 0x49C920: load_next (import.c:2214)
==8222==    by 0x49CB7D: import_module_level (import.c:2002)
```

We should only instantiate one pari instance, so the following culprits ought to import the global pari instance:

```
rings/real_mpfr.pyx:        cdef PariInstance P
rings/real_double.pyx:        cdef sage.libs.pari.gen.PariInstance P = sage.libs.pari.gen.pari
rings/complex_double.pyx:        cdef sage.libs.pari.gen.PariInstance P = sage.libs.pari.gen.pari
rings/complex_double.pyx:        cdef sage.libs.pari.gen.PariInstance P
rings/complex_double.pyx:        cdef sage.libs.pari.gen.PariInstance P
```

This saves about 2.5 MB of memory.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-01 03:28:51

Well, as it turned out the pari only instantiates its stack ones. The problem is caused by some reference not being freed, so it is very likely a Cython issue.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-18 13:32:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-08-27 01:20:02

This is no longer a problem in Sage 3.1.1, so close it as fixed. Who fixed it we will never know :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 01:20:02

Resolution: fixed
