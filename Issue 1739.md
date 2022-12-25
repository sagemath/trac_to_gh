# Issue 1739: [with patch] "Use of uninitialised value of size 8" in binary_code.pyx

archive/issues_001739.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen valgrinding binary_code.pyx I came across the following:\n\n```\n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)\n==24968==    by 0x1BB80160: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7119)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Use of uninitialised value of size 8\n==24968==    at 0x4FFCEF0: _itoa_word (in /lib/libc-2.3.6.so)\n==24968==    by 0x50001AF: vfprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)\n==24968==    by 0x42DECC: int_repr (intobject.c:437)\n==24968==    by 0x443519: _PyObject_Str (object.c:406)\n==24968==    by 0x4435BA: PyObject_Str (object.c:426)\n==24968==    by 0x44D88F: string_new (stringobject.c:3892)\n==24968==    by 0x458D92: type_call (typeobject.c:422)\n==24968==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x4FFCEFA: _itoa_word (in /lib/libc-2.3.6.so)\n==24968==    by 0x50001AF: vfprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)\n==24968==    by 0x42DECC: int_repr (intobject.c:437)\n==24968==    by 0x443519: _PyObject_Str (object.c:406)\n==24968==    by 0x4435BA: PyObject_Str (object.c:426)\n==24968==    by 0x44D88F: string_new (stringobject.c:3892)\n==24968==    by 0x458D92: type_call (typeobject.c:422)\n==24968==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x50006B0: vfprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)\n==24968==    by 0x42DECC: int_repr (intobject.c:437)\n==24968==    by 0x443519: _PyObject_Str (object.c:406)\n==24968==    by 0x4435BA: PyObject_Str (object.c:426)\n==24968==    by 0x44D88F: string_new (stringobject.c:3892)\n==24968==    by 0x458D92: type_call (typeobject.c:422)\n==24968==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x4FFF36B: vfprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x50217E9: vsnprintf (in /lib/libc-2.3.6.so)\n==24968==    by 0x4A37C9: PyOS_snprintf (mysnprintf.c:65)\n==24968==    by 0x42DECC: int_repr (intobject.c:437)\n==24968==    by 0x443519: _PyObject_Str (object.c:406)\n==24968==    by 0x4435BA: PyObject_Str (object.c:426)\n==24968==    by 0x44D88F: string_new (stringobject.c:3892)\n==24968==    by 0x458D92: type_call (typeobject.c:422)\n==24968==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24968==    by 0x1BB80195: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7123)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968== \n==24968== Use of uninitialised value of size 8\n==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)\n==24968==    by 0x1BB80160: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7119)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)\n==24968==    by 0x1BB80482: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7222)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Use of uninitialised value of size 8\n==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)\n==24968==    by 0x1BB80482: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7222)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)\n==24968==    by 0x1BB806FF: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7325)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)\n==24968==    by 0x1BB809DB: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7428)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Use of uninitialised value of size 8\n==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)\n==24968==    by 0x1BB809DB: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7428)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)\n==24968==    by 0x1BB80C94: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7531)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Use of uninitialised value of size 8\n==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)\n==24968==    by 0x1BB80C94: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7531)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Conditional jump or move depends on uninitialised value(s)\n==24968==    at 0x42E35E: PyInt_FromLong (intobject.c:87)\n==24968==    by 0x1BB80E8C: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7634)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Use of uninitialised value of size 8\n==24968==    at 0x42E360: PyInt_FromLong (intobject.c:88)\n==24968==    by 0x1BB80E8C: __pyx_pf_4sage_6coding_11binary_code_14PartitionStack_print_data (binary_code.c:7634)\n==24968==    by 0x482C18: PyEval_EvalFrameEx (ceval.c:3548)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x4838F4: PyEval_EvalFrameEx (ceval.c:494)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968==    by 0x48328C: PyEval_EvalFrameEx (ceval.c:3660)\n==24968==    by 0x484B6A: PyEval_EvalCodeEx (ceval.c:2831)\n==24968== \n==24968== Invalid free() / delete / delete[]\n==24968==    at 0x4A1B74A: free (vg_replace_malloc.c:320)\n==24968==    by 0x43FE9A: dict_dealloc (dictobject.c:847)\n==24968==    by 0x43FE9A: dict_dealloc (dictobject.c:847)\n==24968==    by 0x499E5B: _PyImport_Fini (import.c:229)\n==24968==    by 0x4A5D66: Py_Finalize (pythonrun.c:419)\n==24968==    by 0x4A58AA: handle_system_exit (pythonrun.c:1616)\n==24968==    by 0x4A5AA8: PyErr_PrintEx (pythonrun.c:1062)\n==24968==    by 0x4A62B6: PyRun_SimpleFileExFlags (pythonrun.c:976)\n==24968==    by 0x4120FF: Py_Main (main.c:523)\n==24968==    by 0x4FD94C9: (below main) (in /lib/libc-2.3.6.so)\n==24968==  Address 0x585fb90 is 32 bytes inside a block of size 80 alloc'd\n==24968==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==24968==    by 0x4B0079: _PyObject_GC_Malloc (gcmodule.c:1321)\n==24968==    by 0x454C29: PyType_GenericAlloc (typeobject.c:454)\n==24968==    by 0x9762350: __pyx_tp_new_4sage_9structure_7element_Element (element.c:22358)\n==24968==    by 0xAA2204A: __pyx_tp_new_4sage_5rings_7integer_Integer (integer.c:20161)\n==24968==    by 0x458D92: type_call (typeobject.c:422)\n==24968==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24968==    by 0x47C480: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24968==    by 0xAA20616: initinteger (integer.c:21119)\n==24968==    by 0x49E17D: _PyImport_LoadDynamicModule (importdl.c:53)\n==24968==    by 0x49C08D: import_submodule (import.c:2394)\n==24968==    by 0x49C550: load_next (import.c:2214)\n==24968== \n==24968== ERROR SUMMARY: 422 errors from 16 contexts (suppressed: 521 from 2)\n==24968== malloc/free: in use at exit: 29,698,561 bytes in 183,508 blocks.\n==24968== malloc/free: 872,747 allocs, 689,240 frees, 227,576,259 bytes allocated.\n==24968== For counts of detected errors, rerun with: -v\n==24968== searching for pointers to 183,508 not-freed blocks.\n==24968== checked 34,408,912 bytes.\n```\n\n\nThe patch that I will attach shortly will fix the issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1739\n\n",
    "created_at": "2008-01-10T02:32:59Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch] \"Use of uninitialised value of size 8\" in binary_code.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1739",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/1739





---

archive/issue_comments_010971.json:
```json
{
    "body": "Attachment [uninit.patch](tarball://root/attachments/some-uuid/ticket1739/uninit.patch) by @rlmill created at 2008-01-10 19:05:36\n\nfixes the problem",
    "created_at": "2008-01-10T19:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1739#issuecomment-10971",
    "user": "https://github.com/rlmill"
}
```

Attachment [uninit.patch](tarball://root/attachments/some-uuid/ticket1739/uninit.patch) by @rlmill created at 2008-01-10 19:05:36

fixes the problem



---

archive/issue_comments_010972.json:
```json
{
    "body": "Attachment [uninit-doc.patch](tarball://root/attachments/some-uuid/ticket1739/uninit-doc.patch) by @rlmill created at 2008-01-10 19:06:25\n\ndocuments the fix",
    "created_at": "2008-01-10T19:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1739#issuecomment-10972",
    "user": "https://github.com/rlmill"
}
```

Attachment [uninit-doc.patch](tarball://root/attachments/some-uuid/ticket1739/uninit-doc.patch) by @rlmill created at 2008-01-10 19:06:25

documents the fix



---

archive/issue_comments_010973.json:
```json
{
    "body": "Ok, Robert's fix to my fix is the correct one. Peer review is good ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-01-10T19:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1739#issuecomment-10973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, Robert's fix to my fix is the correct one. Peer review is good ;)

Cheers,

Michael



---

archive/issue_events_004217.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-10T19:47:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1739#event-4217"
}
```



---

archive/issue_comments_010974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-10T19:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1739#issuecomment-10974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010975.json:
```json
{
    "body": "Merged both of rlm's patches in Sage 2.10.alpha2.",
    "created_at": "2008-01-10T19:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1739#issuecomment-10975",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both of rlm's patches in Sage 2.10.alpha2.



---

archive/issue_comments_010976.json:
```json
{
    "body": "[brand x pictures](http://top20search.biz/)",
    "created_at": "2010-05-26T08:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1739#issuecomment-10976",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp2"
}
```

[brand x pictures](http://top20search.biz/)
