# Issue 3608: optimize.py: "Invalid read of size 8"

Issue created by migration from https://trac.sagemath.org/ticket/3608

Original creator: mabshoff

Original creation time: 2008-07-08 11:53:08

Assignee: mabshoff

CC:  mkoeppe kcrisman


```
==21694== Invalid read of size 8
==21694==    at 0x21C720A0: Matrix_NewFromArrayStruct (dense.c:244)
==21694==    by 0x21C751EE: matrix_new (dense.c:499)
==21694==    by 0x45E48A: type_call (typeobject.c:422)
==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==21694==    by 0x4952F3: do_call (ceval.c:3784)
==21694==    by 0x494BAA: call_function (ceval.c:3596)
==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)
==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==21694==    by 0x494E7C: fast_function (ceval.c:3669)
==21694==    by 0x494B91: call_function (ceval.c:3594)
==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)
==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==21694==  Address 0x57a1be0 is 0 bytes after a block of size 16 alloc'd
==21694==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==21694==    by 0x44969A: PyMem_Malloc (object.c:2010)
==21694==    by 0x1D033292: array_struct_get (arrayobject.c:6409)
==21694==    by 0x4EA584: getset_get (descrobject.c:146)
==21694==    by 0x448569: PyObject_GenericGetAttr (object.c:1312)
==21694==    by 0x447F0B: PyObject_GetAttr (object.c:1127)
==21694==    by 0x447CB3: PyObject_GetAttrString (object.c:1069)
==21694==    by 0x21C71DCC: Matrix_NewFromArrayStruct (dense.c:191)
==21694==    by 0x21C751EE: matrix_new (dense.c:499)
==21694==    by 0x45E48A: type_call (typeobject.c:422)
==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==21694==    by 0x4952F3: do_call (ceval.c:3784)
```



---

Comment by was created at 2009-06-15 23:22:00

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by was created at 2009-06-15 23:22:00

Changing priority from blocker to major.


---

Comment by chapoton created at 2020-07-02 13:29:46

totally unclear. Can we close as obsolete ?


---

Comment by chapoton created at 2020-07-02 13:29:46

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-07-02 14:05:02

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2020-07-02 14:05:02

ancient valgrind report, outdated


---

Comment by chapoton created at 2020-07-02 14:10:00

Resolution: invalid
