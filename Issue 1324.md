# Issue 1324: 2.8.14: doctest failure in sage/rings/real_rqdf.pyx  on FC6, x86-64

Issue created by migration from https://trac.sagemath.org/ticket/1324

Original creator: mabshoff

Original creation time: 2007-11-28 21:44:15

Assignee: failure

Initially Kate Minola reported the issue in http://groups.google.com/group/sage-support/t/ff6aa3efc272f40b

Valgrind tells us:

```
==6899== Conditional jump or move depends on uninitialised value(s)
==6899==    at 0xC4BCC67: __pyx_f_4sage_5rings_9real_rqdf_17QuadDoubleElement__set(__pyx_obj_4sage_5rings_9real_rqdf_QuadDou
bleElement*, _object*) (real_rqdf.cpp:2521)
==6899==    by 0xC4B6037: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___init__(_object*, _object*, _object*) (real_
rqdf.cpp:4282)
==6899==    by 0x458E40: type_call (typeobject.c:436)
==6899==    by 0x415542: PyObject_Call (abstract.c:1860)
==6899==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==6899==    by 0xC4B94F6: __pyx_pf_4sage_5rings_9real_rqdf_25RealQuadDoubleField_class___call__(_object*, _object*, _object*
) (real_rqdf.cpp:2919)
==6899==    by 0x415542: PyObject_Call (abstract.c:1860)
==6899==    by 0x481AC1: PyEval_EvalFrameEx (ceval.c:3775)
==6899==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==6899==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==6899==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==6899==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)

==6899== Invalid read of size 1
==6899==    at 0x4A1CA13: strlen (mc_replace_strmem.c:242)
==6899==    by 0x44D65A: PyString_FromString (stringobject.c:108)
==6899==    by 0xC4B81B8: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (real
_rqdf.cpp:5315)
==6899==    by 0x415542: PyObject_Call (abstract.c:1860)
==6899==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==6899==    by 0xC4BB34A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5851)
==6899==    by 0x415542: PyObject_Call (abstract.c:1860)
==6899==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==6899==    by 0xC4B595B: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5153)
==6899==    by 0x443279: PyObject_Repr (object.c:361)
==6899==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)
==6899==    by 0x4ABD88: sys_displayhook (sysmodule.c:114)
```


Cheers,

Michael


---

Attachment

The attached patch fixes an off-by-one error in RR->RQDF conversion; the bug had the effect that depending on the stack layout chosen by the compiler, `RealField(53)->RQDF` conversion might always return NaN.  (The code read one past the end of an array on the stack, so it depended on what the compiler allocated after the array.)

It also includes a minor cleanup: "cdef bint isnan" was technically wrong, because we weren't using isnan as a boolean.


---

Comment by cwitty created at 2007-12-07 02:51:39

Changing assignee from failure to cwitty.


---

Comment by mabshoff created at 2007-12-09 09:49:53

Looks good to me. Great work ;)

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-09 12:03:15

Resolution: fixed


---

Comment by mabshoff created at 2007-12-09 12:03:15

Merged in 2.9.alpha2.
