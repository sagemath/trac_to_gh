# Issue 1092: small memleaks exposed by ntl_ZZ_pE (from 2.8.12.alpha0)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-04 00:02:14

Assignee: mabshoff

ntl_ZZ_pE.py

```
==4443== 104 (8 direct, 96 indirect) bytes in 1 blocks are definitely lost in loss record 33 of 1,883
==4443==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4443==    by 0x5C41AB6: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)
==4443==    by 0xCE6A067: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:2514)
==4443==    by 0xCE6889E: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:1661
)
==4443==    by 0x415522: PyObject_Call (abstract.c:1860)
==4443==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==4443==    by 0x4589BF: object_reduce_ex (typeobject.c:2786)
==4443==    by 0x415522: PyObject_Call (abstract.c:1860)
==4443==    by 0x76F0743: save (cPickle.c:2495)
==4443==    by 0x76F2597: cpm_dumps (cPickle.c:2577)
==4443==    by 0x415522: PyObject_Call (abstract.c:1860)
==4443==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)

==4443== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 84 of 1,883
==4443==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==4443==    by 0x5C41AB6: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/sage-2.8.11/devel/sage-main/c_lib/libcsage.so)
==4443==    by 0xCE6A067: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:2514)
==4443==    by 0xCE67C49: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_p
E.cpp:2554)
==4443==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4443==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4443==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==4443==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==4443==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
```



---

Comment by mabshoff created at 2008-01-07 18:09:35

With Sage 2.10.alpha0 I get:

```
==26597== 104 (8 direct, 96 indirect) bytes in 1 blocks are definitely lost in loss record 1,466 of 7,536
==26597==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==26597==    by 0x5C41A76: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcs
age.so)
==26597==    by 0xCC170F7: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:4203)
==26597==    by 0xCC1592E: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE___reduce__(_object*, _object*) (ntl_ZZ_pE.cpp:312
6)
==26597==    by 0x415542: PyObject_Call (abstract.c:1860)
==26597==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==26597==    by 0x4585DF: object_reduce_ex (typeobject.c:2786)
==26597==    by 0x415542: PyObject_Call (abstract.c:1860)
==26597==    by 0x7AEF743: save (cPickle.c:2495)
==26597==    by 0x7AF1597: cpm_dumps (cPickle.c:2577)
==26597==    by 0x415542: PyObject_Call (abstract.c:1860)
==26597==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)

==26597== 136 (8 direct, 128 indirect) bytes in 1 blocks are definitely lost in loss record 3,065 of 7,536
==26597==    at 0x4A1C344: operator new(unsigned long) (vg_replace_malloc.c:227)
==26597==    by 0x5C41A76: ZZ_pE_to_ZZ_pX (in /tmp/Work-mabshoff/release-cycle/sage-2.9.3.rc1ish/devel/sage-main/c_lib/libcs
age.so)
==26597==    by 0xCC170F7: __pyx_f_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX (ntl_ZZ_pE.cpp:4203)
==26597==    by 0xCC14CD9: __pyx_pf_4sage_4libs_3ntl_9ntl_ZZ_pE_9ntl_ZZ_pE_get_as_ZZ_pX_doctest(_object*, _object*) (ntl_ZZ_
pE.cpp:4259)
==26597==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26597==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26597==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==26597==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==26597==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
```

Leak Summary:

```
==26597==    definitely lost: 16 bytes in 2 blocks.
==26597==    indirectly lost: 224 bytes in 4 blocks.
==26597==      possibly lost: 255,295 bytes in 769 blocks.
==26597==    still reachable: 29,400,323 bytes in 182,486 blocks.
==26597==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-01-08 00:29:44

Nice catch. Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-08 02:03:16

Resolution: fixed


---

Comment by mabshoff created at 2008-01-08 02:03:16

Merge in 2.10.alpha0
