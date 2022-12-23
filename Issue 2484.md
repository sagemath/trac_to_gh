# Issue 2484: "Conditional jump" in  QuadDoubleElement __repr__

Issue created by migration from https://trac.sagemath.org/ticket/2484

Original creator: mabshoff

Original creation time: 2008-03-12 08:25:36

Assignee: mabshoff

When doctesting calculus.py memcheck complains about the following:

```
==24858== Conditional jump or move depends on uninitialised value(s)
==24858==    at 0x4A1CA17: strlen (mc_replace_strmem.c:242)
==24858==    by 0x44D65A: PyString_FromString (stringobject.c:108)
==24858==    by 0xC248F88: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (rea
l_rqdf.cpp:5314)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24858==    by 0xC24C11A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5850)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24858==    by 0xC2468BB: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5152)
==24858==    by 0x443279: PyObject_Repr (object.c:361)
==24858==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)
==24858==    by 0x4AC5B8: sys_displayhook (sysmodule.c:114)
==24858== Invalid read of size 1
==24858==    at 0x4A1CA13: strlen (mc_replace_strmem.c:242)
==24858==    by 0x44D65A: PyString_FromString (stringobject.c:108)
==24858==    by 0xC248F88: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (rea
l_rqdf.cpp:5314)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24858==    by 0xC24C11A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5850)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24858==    by 0xC2468BB: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5152)
==24858==    by 0x443279: PyObject_Repr (object.c:361)
==24858==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)
==24858==    by 0x4AC5B8: sys_displayhook (sysmodule.c:114)
==24858==  Address 0x1c89aa29 is 0 bytes after a block of size 65 alloc'd
==24858==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==24858==    by 0xC248F3E: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (rea
l_rqdf.cpp:5278)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24858==    by 0xC24C11A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5850)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24858==    by 0xC2468BB: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5152)
==24858==    by 0x443279: PyObject_Repr (object.c:361)
==24858==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)
==24858==    by 0x4AC5B8: sys_displayhook (sysmodule.c:114)
==24858==    by 0x415542: PyObject_Call (abstract.c:1860)
```


I suspect the above causes occasional unreproducible segfaults in various doctests.

Cheers,

Michael


---

Attachment

The attached patch *should* fix the above valgrind log, but I haven't run valgrind myself to check.  (I did run testall, which passed.)


---

Comment by mabshoff created at 2008-03-14 02:04:19

The patch fixes the issue. Positive review :)


---

Comment by mabshoff created at 2008-03-14 02:06:31

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 02:06:31

Resolution: fixed
