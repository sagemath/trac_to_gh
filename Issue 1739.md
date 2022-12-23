# Issue 1739: [with patch] "Use of uninitialised value of size 8" in binary_code.pyx

Issue created by migration from https://trac.sagemath.org/ticket/1739

Original creator: mabshoff

Original creation time: 2008-01-10 02:32:59

Assignee: mabshoff

When valgrinding binary_code.pyx I came across the following:

```
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)
==24968==    by 0x1BB80160: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7119)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Use of uninitialised value of size 8
==24968==    at 0x4FFCEF0: _itoa_word (in /lib/libc-2.3.6.so)
==24968==    by 0x50001AF: vfprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)
==24968==    by 0x42DECC: int_repr (intobject.c:437)
==24968==    by 0x443519: _PyObject_Str (object.c:406)
==24968==    by 0x4435BA: PyObject_Str (object.c:426)
==24968==    by 0x44D88F: string_new (stringobject.c:3892)
==24968==    by 0x458D92: type_call (typeobject.c:422)
==24968==    by 0x415542: PyObject_Call (abstract.c:1860)
==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x4FFCEFA: _itoa_word (in /lib/libc-2.3.6.so)
==24968==    by 0x50001AF: vfprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)
==24968==    by 0x42DECC: int_repr (intobject.c:437)
==24968==    by 0x443519: _PyObject_Str (object.c:406)
==24968==    by 0x4435BA: PyObject_Str (object.c:426)
==24968==    by 0x44D88F: string_new (stringobject.c:3892)
==24968==    by 0x458D92: type_call (typeobject.c:422)
==24968==    by 0x415542: PyObject_Call (abstract.c:1860)
==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x50006B0: vfprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)
==24968==    by 0x42DECC: int_repr (intobject.c:437)
==24968==    by 0x443519: _PyObject_Str (object.c:406)
==24968==    by 0x4435BA: PyObject_Str (object.c:426)
==24968==    by 0x44D88F: string_new (stringobject.c:3892)
==24968==    by 0x458D92: type_call (typeobject.c:422)
==24968==    by 0x415542: PyObject_Call (abstract.c:1860)
==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x4FFF36B: vfprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)
==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)
==24968==    by 0x42DECC: int_repr (intobject.c:437)
==24968==    by 0x443519: _PyObject_Str (object.c:406)
==24968==    by 0x4435BA: PyObject_Str (object.c:426)
==24968==    by 0x44D88F: string_new (stringobject.c:3892)
==24968==    by 0x458D92: type_call (typeobject.c:422)
==24968==    by 0x415542: PyObject_Call (abstract.c:1860)
==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968== 
==24968== Use of uninitialised value of size 8
==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)
==24968==    by 0x1BB80160: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7119)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)
==24968==    by 0x1BB80482: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7222)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Use of uninitialised value of size 8
==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)
==24968==    by 0x1BB80482: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7222)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)
==24968==    by 0x1BB806FF: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7325)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)
==24968==    by 0x1BB809DB: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7428)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Use of uninitialised value of size 8
==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)
==24968==    by 0x1BB809DB: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7428)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)
==24968==    by 0x1BB80C94: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7531)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Use of uninitialised value of size 8
==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)
==24968==    by 0x1BB80C94: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7531)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Conditional jump or move depends on uninitialised value(s)
==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)
==24968==    by 0x1BB80E8C: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7634)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Use of uninitialised value of size 8
==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)
==24968==    by 0x1BB80E8C: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7634)
==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)
==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)
==24968== 
==24968== Invalid free() / delete / delete[]
==24968==    at 0x4A1B74A: free (vg_replace_malloc.c:320)
==24968==    by 0x43FE9A: dict_dealloc (dictobject.c:847)
==24968==    by 0x43FE9A: dict_dealloc (dictobject.c:847)
==24968==    by 0x499E5B: _PyImport_Fini (import.c:229)
==24968==    by 0x4A5D66: Py_Finalize (pythonrun.c:419)
==24968==    by 0x4A58AA: handle_system_exit (pythonrun.c:1616)
==24968==    by 0x4A5AA8: PyErr_PrintEx (pythonrun.c:1062)
==24968==    by 0x4A62B6: PyRun_SimpleFileExFlags (pythonrun.c:976)
==24968==    by 0x4120FF: Py_Main (main.c:523)
==24968==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)
==24968==  Address 0x585fb90 is 32 bytes inside a block of size 80 alloc'd
==24968==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==24968==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)
==24968==    by 0x454C29: PyType_GenericAlloc (typeobject.c:454)
==24968==    by 0x9762350: __pyx_tp_new_4sage_9structure_7element_Element (element.c:22358)
==24968==    by 0xAA2204A: __pyx_tp_new_4sage_5rings_7integer_Integer (integer.c:20161)
==24968==    by 0x458D92: type_call (typeobject.c:422)
==24968==    by 0x415542: PyObject_Call (abstract.c:1860)
==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24968==    by 0xAA20616: initinteger (integer.c:21119)
==24968==    by 0x49E17D: _PyImport_LoadDynamicModule (importdl.c:53)
==24968==    by 0x49C08D: import_submodule (import.c:2394)
==24968==    by 0x49C550: load_next (import.c:2214)
==24968== 
==24968== ERROR SUMMARY: 422 errors from 16 contexts (suppressed: 521 from 2)
==24968== malloc/free: in use at exit: 29,698,561 bytes in 183,508 blocks.
==24968== malloc/free: 872,747 allocs, 689,240 frees, 227,576,259 bytes allocated.
==24968== For counts of detected errors, rerun with: -v
==24968== searching for pointers to 183,508 not-freed blocks.
==24968== checked 34,408,912 bytes.
```


The patch that I will attach shortly will fix the issue.

Cheers,

Michael


---

Attachment

fixes the problem


---

Attachment

documents the fix


---

Comment by mabshoff created at 2008-01-10 19:41:55

Ok, Robert's fix to my fix is the correct one. Peer review is good ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 19:47:34

Resolution: fixed


---

Comment by mabshoff created at 2008-01-10 19:47:34

Merged both of rlm's patches in Sage 2.10.alpha2.


---

Comment by bascorp2 created at 2010-05-26 08:42:57

[brand x pictures](http://top20search.biz/)
