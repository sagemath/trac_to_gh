# Issue 532: mkfr leak in RealField (from matrix/strassen.pyx)

Issue created by migration from https://trac.sagemath.org/ticket/532

Original creator: mabshoff

Original creation time: 2007-08-30 18:50:02

Assignee: mabshoff

From Sage 2.8.3rc3:

```
==24738== 16 bytes in 1 blocks are possibly lost in loss record 525 of 2,259
==24738==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==24738==    by 0x165368BD: mpfr_init2 (in /tmp/Work2/sage-2.8.3.rc3/devel/sage-main/build/sage/rings/real_mpfr.so)
==24738==    by 0x16503260: __pyx_f_9real_mpfr_9RealField___init__ (real_mpfr.c:1410)
==24738==    by 0x45A321: type_call (typeobject.c:436)
==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24738==    by 0x18836269: initpolynomial_element (polynomial_element.c:21764)
==24738==    by 0x49F762: _PyImport_LoadDynamicModule (importdl.c:53)
==24738==    by 0x49D63E: import_submodule (import.c:2394)
==24738==    by 0x49DB11: load_next (import.c:2214)
==24738==    by 0x49DD6E: import_module_level (import.c:2002)
==24738==    by 0x49E1A4: PyImport_ImportModuleLevel (import.c:2066)
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 18:50:08

Changing status from new to assigned.


---

Comment by cwitty created at 2007-10-11 22:02:38

Resolution: invalid


---

Comment by cwitty created at 2007-10-11 22:02:38

This is because polynomial_element.pyx has a global (well, module-level) variable holding a RealField:

```
RR = RealField()
```

(As a module-level variable, this never gets freed.)

Each RealField holds two RealNumbers (._zero_element and ._one_element), so they never get freed either.
