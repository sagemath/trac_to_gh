# Issue 3706: [with patch; positive review] segfault in matrix2.pyx

archive/issues_003706.json:
```json
{
    "body": "Assignee: @williamstein\n\nOn the debian64 vmware image we have a segfault when doctesting matrix2.pyx:\n\n```\nwas@debian64:~/build/sage-3.0.6.rc0$ ./sage -t devel/sage/sage/matrix/matrix2.pyx \nsage -t  devel/sage/sage/matrix/matrix2.pyx                 \n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [15.6 s]\nexit code: 768\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/matrix/matrix2.pyx\nTotal time for all tests: 15.6 seconds\nwas@debian64:~/build/sage-3.0.6.rc0$ \n```\n\nHere's the gdb output.  The segfault doesn't get hit when doing --verbose.\n\n```\nwas@debian64:~/build/sage-3.0.6.rc0$ ./sage -t --gdb devel/sage/sage/matrix/matrix2.pyx\nsage -t --gdb devel/sage/sage/matrix/matrix2.pyx            ********************************************************************************\nType r at the (gdb) prompt to run the doctests.\nType bt if there is a crash to see a traceback.\n********************************************************************************\nGNU gdb 6.4.90-debian\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"x86_64-linux-gnu\"...Using host libthread_db library \"/lib/libthread_db.so.1\".\n\n(gdb) bt\nNo stack.\n(gdb) r\nStarting program: /home/was/build/sage-3.0.6.rc0/local/bin/python /home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\n[Thread debugging using libthread_db enabled]\n[New Thread 47351804546912 (LWP 12929)]\n*** glibc detected *** double free or corruption (fasttop): 0x0000000002032b00 ***\n\nProgram received signal SIGABRT, Aborted.\n[Switching to Thread 47351804546912 (LWP 12929)]\n0x00002b10f35c607b in raise () from /lib/libc.so.6\n(gdb) bt\n#0  0x00002b10f35c607b in raise () from /lib/libc.so.6\n#1  0x00002b10f35c784e in abort () from /lib/libc.so.6\n#2  0x00002b10f35fc629 in __fsetlocking () from /lib/libc.so.6\n#3  0x00002b10f3603193 in mallopt () from /lib/libc.so.6\n#4  0x00002b10f360321e in free () from /lib/libc.so.6\n#5  0x00002b1102e2aee3 in __pyx_tp_dealloc_4sage_6matrix_20matrix_integer_dense_Matrix_integer_dense (o=0x2b110a598170)\n    at sage/matrix/matrix_integer_dense.c:4887\n#6  0x00000000004d050b in meth_dealloc (m=0x2b110a571248) at Objects/methodobject.c:126\n#7  0x00002b110192d5a2 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_list (__pyx_v_self=<value optimized out>,\n    unused=<value optimized out>) at sage/matrix/matrix0.c:1788\n#8  0x0000000000415823 in PyObject_Call (func=0x3281, arg=0x3281, kw=0x6) at Objects/abstract.c:1861\n#9  0x00002b1101945fa3 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_str (__pyx_v_self=0x2b110a598170, unused=<value optimized out>)\n    at sage/matrix/matrix0.c:5075\n#10 0x0000000000415823 in PyObject_Call (func=0x3281, arg=0x3281, kw=0x6) at Objects/abstract.c:1861\n#11 0x00002b1101936bcc in __pyx_pf_4sage_6matrix_7matrix0_6Matrix___repr__ (__pyx_v_self=0x2b110a598170) at sage/matrix/matrix0.c:4766\n#12 0x00000000004433fa in PyObject_Repr (v=0x2b110a598170) at Objects/object.c:361\n#13 0x0000000000429ebc in PyFile_WriteObject (v=0x2b110a598170, f=0x2b110895ee18, flags=0) at Objects/fileobject.c:2195\n#14 0x00000000004ad619 in sys_displayhook (self=<value optimized out>, o=0x2b110a598170) at Python/sysmodule.c:114\n#15 0x0000000000415823 in PyObject_Call (func=0x3281, arg=0x3281, kw=0x6) at Objects/abstract.c:1861\n#16 0x000000000047db21 in PyEval_CallObjectWithKeywords (func=0x2b10f3008440, arg=0x2b1109e95250, kw=0x0) at Python/ceval.c:3442\n#17 0x000000000048396a in PyEval_EvalFrameEx (f=0x2529d50, throwflag=<value optimized out>) at Python/ceval.c:1531\n#18 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b1109eaa6c0, globals=<value optimized out>, locals=<value optimized out>, args=0x0,\n    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#19 0x0000000000484ec2 in PyEval_EvalFrameEx (f=0x2489dc0, throwflag=<value optimized out>) at Python/ceval.c:494\n#20 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f602feb8, globals=<value optimized out>, locals=<value optimized out>,\n    args=0x2457300, argcount=4, kws=0x2457320, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#21 0x0000000000484347 in PyEval_EvalFrameEx (f=0x2457150, throwflag=<value optimized out>) at Python/ceval.c:3669\n#22 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f60350a8, globals=<value optimized out>, locals=<value optimized out>, args=0x5,\n    argcount=2, kws=0x6c5760, kwcount=0, defs=0x2b10f6064f68, defcount=3, closure=0x0) at Python/ceval.c:2836\n#23 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6c5570, throwflag=<value optimized out>) at Python/ceval.c:3669\n#24 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f6035a08, globals=<value optimized out>, locals=<value optimized out>, args=0x9,\n    argcount=1, kws=0x6c99d8, kwcount=3, defs=0x2b10f6052668, defcount=9, closure=0x0) at Python/ceval.c:2836\n#25 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6c9850, throwflag=<value optimized out>) at Python/ceval.c:3669\n#26 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f390fc60, globals=<value optimized out>, locals=<value optimized out>, args=0x0,\n    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#27 0x0000000000486422 in PyEval_EvalCode (co=0x3281, globals=0x3281, locals=0x6) at Python/ceval.c:494\n#28 0x00000000004a78ee in PyRun_FileExFlags (fp=0x650010,\n    filename=0x7fffb7ac843f \"/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\", start=<value optimized out>, globals=0x673540,\n    locals=0x673540, closeit=1, flags=0x7fffb7ac7ab0) at Python/pythonrun.c:1273\n#29 0x00000000004a7b80 in PyRun_SimpleFileExFlags (fp=0x650010,\n    filename=0x7fffb7ac843f \"/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\", closeit=1, flags=0x7fffb7ac7ab0)\n    at Python/pythonrun.c:879\n#30 0x0000000000412160 in Py_Main (argc=<value optimized out>, argv=0x7fffb7ac7bc8) at Modules/main.c:523\n#31 0x00002b10f35b34ca in __libc_start_main () from /lib/libc.so.6\n#32 0x000000000041169a in _start () at ../sysdeps/x86_64/elf/start.S:113\n(gdb) \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3706\n\n",
    "closed_at": "2008-07-28T11:00:13Z",
    "created_at": "2008-07-22T07:58:17Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with patch; positive review] segfault in matrix2.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3706",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

On the debian64 vmware image we have a segfault when doctesting matrix2.pyx:

```
was@debian64:~/build/sage-3.0.6.rc0$ ./sage -t devel/sage/sage/matrix/matrix2.pyx 
sage -t  devel/sage/sage/matrix/matrix2.pyx                 

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [15.6 s]
exit code: 768
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/matrix/matrix2.pyx
Total time for all tests: 15.6 seconds
was@debian64:~/build/sage-3.0.6.rc0$ 
```

Here's the gdb output.  The segfault doesn't get hit when doing --verbose.

```
was@debian64:~/build/sage-3.0.6.rc0$ ./sage -t --gdb devel/sage/sage/matrix/matrix2.pyx
sage -t --gdb devel/sage/sage/matrix/matrix2.pyx            ********************************************************************************
Type r at the (gdb) prompt to run the doctests.
Type bt if there is a crash to see a traceback.
********************************************************************************
GNU gdb 6.4.90-debian
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu"...Using host libthread_db library "/lib/libthread_db.so.1".

(gdb) bt
No stack.
(gdb) r
Starting program: /home/was/build/sage-3.0.6.rc0/local/bin/python /home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py
[Thread debugging using libthread_db enabled]
[New Thread 47351804546912 (LWP 12929)]
*** glibc detected *** double free or corruption (fasttop): 0x0000000002032b00 ***

Program received signal SIGABRT, Aborted.
[Switching to Thread 47351804546912 (LWP 12929)]
0x00002b10f35c607b in raise () from /lib/libc.so.6
(gdb) bt
#0  0x00002b10f35c607b in raise () from /lib/libc.so.6
#1  0x00002b10f35c784e in abort () from /lib/libc.so.6
#2  0x00002b10f35fc629 in __fsetlocking () from /lib/libc.so.6
#3  0x00002b10f3603193 in mallopt () from /lib/libc.so.6
#4  0x00002b10f360321e in free () from /lib/libc.so.6
#5  0x00002b1102e2aee3 in __pyx_tp_dealloc_4sage_6matrix_20matrix_integer_dense_Matrix_integer_dense (o=0x2b110a598170)
    at sage/matrix/matrix_integer_dense.c:4887
#6  0x00000000004d050b in meth_dealloc (m=0x2b110a571248) at Objects/methodobject.c:126
#7  0x00002b110192d5a2 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_list (__pyx_v_self=<value optimized out>,
    unused=<value optimized out>) at sage/matrix/matrix0.c:1788
#8  0x0000000000415823 in PyObject_Call (func=0x3281, arg=0x3281, kw=0x6) at Objects/abstract.c:1861
#9  0x00002b1101945fa3 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_str (__pyx_v_self=0x2b110a598170, unused=<value optimized out>)
    at sage/matrix/matrix0.c:5075
#10 0x0000000000415823 in PyObject_Call (func=0x3281, arg=0x3281, kw=0x6) at Objects/abstract.c:1861
#11 0x00002b1101936bcc in __pyx_pf_4sage_6matrix_7matrix0_6Matrix___repr__ (__pyx_v_self=0x2b110a598170) at sage/matrix/matrix0.c:4766
#12 0x00000000004433fa in PyObject_Repr (v=0x2b110a598170) at Objects/object.c:361
#13 0x0000000000429ebc in PyFile_WriteObject (v=0x2b110a598170, f=0x2b110895ee18, flags=0) at Objects/fileobject.c:2195
#14 0x00000000004ad619 in sys_displayhook (self=<value optimized out>, o=0x2b110a598170) at Python/sysmodule.c:114
#15 0x0000000000415823 in PyObject_Call (func=0x3281, arg=0x3281, kw=0x6) at Objects/abstract.c:1861
#16 0x000000000047db21 in PyEval_CallObjectWithKeywords (func=0x2b10f3008440, arg=0x2b1109e95250, kw=0x0) at Python/ceval.c:3442
#17 0x000000000048396a in PyEval_EvalFrameEx (f=0x2529d50, throwflag=<value optimized out>) at Python/ceval.c:1531
#18 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b1109eaa6c0, globals=<value optimized out>, locals=<value optimized out>, args=0x0,
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#19 0x0000000000484ec2 in PyEval_EvalFrameEx (f=0x2489dc0, throwflag=<value optimized out>) at Python/ceval.c:494
#20 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f602feb8, globals=<value optimized out>, locals=<value optimized out>,
    args=0x2457300, argcount=4, kws=0x2457320, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#21 0x0000000000484347 in PyEval_EvalFrameEx (f=0x2457150, throwflag=<value optimized out>) at Python/ceval.c:3669
#22 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f60350a8, globals=<value optimized out>, locals=<value optimized out>, args=0x5,
    argcount=2, kws=0x6c5760, kwcount=0, defs=0x2b10f6064f68, defcount=3, closure=0x0) at Python/ceval.c:2836
#23 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6c5570, throwflag=<value optimized out>) at Python/ceval.c:3669
#24 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f6035a08, globals=<value optimized out>, locals=<value optimized out>, args=0x9,
    argcount=1, kws=0x6c99d8, kwcount=3, defs=0x2b10f6052668, defcount=9, closure=0x0) at Python/ceval.c:2836
#25 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6c9850, throwflag=<value optimized out>) at Python/ceval.c:3669
#26 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b10f390fc60, globals=<value optimized out>, locals=<value optimized out>, args=0x0,
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#27 0x0000000000486422 in PyEval_EvalCode (co=0x3281, globals=0x3281, locals=0x6) at Python/ceval.c:494
#28 0x00000000004a78ee in PyRun_FileExFlags (fp=0x650010,
    filename=0x7fffb7ac843f "/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py", start=<value optimized out>, globals=0x673540,
    locals=0x673540, closeit=1, flags=0x7fffb7ac7ab0) at Python/pythonrun.c:1273
#29 0x00000000004a7b80 in PyRun_SimpleFileExFlags (fp=0x650010,
    filename=0x7fffb7ac843f "/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py", closeit=1, flags=0x7fffb7ac7ab0)
    at Python/pythonrun.c:879
#30 0x0000000000412160 in Py_Main (argc=<value optimized out>, argv=0x7fffb7ac7bc8) at Modules/main.c:523
#31 0x00002b10f35b34ca in __libc_start_main () from /lib/libc.so.6
#32 0x000000000041169a in _start () at ../sysdeps/x86_64/elf/start.S:113
(gdb) 
```

Issue created by migration from https://trac.sagemath.org/ticket/3706





---

archive/issue_comments_026245.json:
```json
{
    "body": "gdb says:\n\n```\n#0  0x00002b8b47bf407b in raise () from /lib/libc.so.6\n#1  0x00002b8b47bf584e in abort () from /lib/libc.so.6\n#2  0x00002b8b47c2a629 in __fsetlocking () from /lib/libc.so.6\n#3  0x00002b8b47c31193 in mallopt () from /lib/libc.so.6\n#4  0x00002b8b47c3121e in free () from /lib/libc.so.6\n#5  0x00002b8b57656ace in __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense___dealloc__ (__pyx_v_self=0x2b8b5ee41170) at sage/matrix/matrix_integer_dense.c:4896\n#6  0x00002b8b576b87d0 in __pyx_tp_dealloc_4sage_6matrix_20matrix_integer_dense_Matrix_integer_dense (o=0x2b8b5ee41170) at sage/matrix/matrix_integer_dense.c:29687\n#7  0x00000000004f1afd in meth_dealloc (m=0x2b8b5ee1a2d8) at Objects/methodobject.c:126\n#8  0x00002b8b561339c2 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_list (__pyx_v_self=0x2b8b5ee41170, unused=0x0) at sage/matrix/matrix0.c:1788\n#9  0x00000000004f1914 in PyCFunction_Call (func=0x2b8b5ee3bb00, arg=0x2b8b47629050, kw=0x0) at Objects/methodobject.c:82\n#10 0x000000000041b08f in PyObject_Call (func=0x2b8b5ee3bb00, arg=0x2b8b47629050, kw=0x0) at Objects/abstract.c:1861\n#11 0x00002b8b5613d7b2 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_str (__pyx_v_self=0x2b8b5ee41170, unused=0x0) at sage/matrix/matrix0.c:5075\n#12 0x00000000004f1914 in PyCFunction_Call (func=0x2b8b5ee3b8c0, arg=0x2b8b47629050, kw=0x0) at Objects/methodobject.c:82\n#13 0x000000000041b08f in PyObject_Call (func=0x2b8b5ee3b8c0, arg=0x2b8b47629050, kw=0x0) at Objects/abstract.c:1861\n#14 0x00002b8b5613c831 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix___repr__ (__pyx_v_self=0x2b8b5ee41170) at sage/matrix/matrix0.c:4766\n#15 0x000000000044646b in PyObject_Repr (v=0x2b8b5ee41170) at Objects/object.c:361\n#16 0x000000000042bb6d in PyFile_WriteObject (v=0x2b8b5ee41170, f=0x2b8b5d1fdea8, flags=0) at Objects/fileobject.c:2195\n#17 0x00000000004c2b39 in sys_displayhook (self=0x0, o=0x2b8b5ee41170) at Python/sysmodule.c:114\n#18 0x00000000004f198d in PyCFunction_Call (func=0x2b8b47636440, arg=0x2b8b5e739250, kw=0x0) at Objects/methodobject.c:93\n#19 0x000000000041b08f in PyObject_Call (func=0x2b8b47636440, arg=0x2b8b5e739250, kw=0x0) at Objects/abstract.c:1861\n#20 0x0000000000494ed3 in PyEval_CallObjectWithKeywords (func=0x2b8b47636440, arg=0x2b8b5e739250, kw=0x0) at Python/ceval.c:3442\n#21 0x000000000048f25e in PyEval_EvalFrameEx (f=0x2557be0, throwflag=0) at Python/ceval.c:1531\n#22 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b5e7506c0, globals=0x1e26ee0, locals=0x1e26ee0, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#23 0x000000000048bf06 in PyEval_EvalCode (co=0x2b8b5e7506c0, globals=0x1e26ee0, locals=0x1e26ee0) at Python/ceval.c:494\n#24 0x0000000000497145 in exec_statement (f=0x24b7b50, prog=0x2b8b5e7506c0, globals=0x1e26ee0, locals=0x1e26ee0) at Python/ceval.c:4177\n#25 0x000000000048f9e2 in PyEval_EvalFrameEx (f=0x24b7b50, throwflag=0) at Python/ceval.c:1666\n#26 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b4a679eb8, globals=0x8714a0, locals=0x0, args=0x2485090, argcount=4, kws=0x24850b0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#27 0x00000000004959f7 in fast_function (func=0x2b8b4a6c0398, pp_stack=0x7fff63498338, n=4, na=4, nk=0) at Python/ceval.c:3669\n#28 0x000000000049570c in call_function (pp_stack=0x7fff63498338, oparg=3) at Python/ceval.c:3594\n#29 0x0000000000491cef in PyEval_EvalFrameEx (f=0x2484ee0, throwflag=0) at Python/ceval.c:2272\n#30 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b4a67e0a8, globals=0x8714a0, locals=0x0, args=0x6f91d0, argcount=2, kws=0x6f91e0, kwcount=0, defs=0x2b8b4a6aef68, defcount=3, closure=0x0) at Python/ceval.c:2836\n#31 0x00000000004959f7 in fast_function (func=0x2b8b4a6c0500, pp_stack=0x7fff63498818, n=2, na=2, nk=0) at Python/ceval.c:3669\n#32 0x000000000049570c in call_function (pp_stack=0x7fff63498818, oparg=1) at Python/ceval.c:3594\n#33 0x0000000000491cef in PyEval_EvalFrameEx (f=0x6f8ff0, throwflag=0) at Python/ceval.c:2272\n#34 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b4a67ea08, globals=0x8714a0, locals=0x0, args=0x71e8f0, argcount=1, kws=0x71e8f8, kwcount=3, defs=0x2b8b4a69c6e8, defcount=9, closure=0x0) at Python/ceval.c:2836\n#35 0x00000000004959f7 in fast_function (func=0x2b8b4a6bd758, pp_stack=0x7fff63498cf8, n=7, na=1, nk=3) at Python/ceval.c:3669\n#36 0x000000000049570c in call_function (pp_stack=0x7fff63498cf8, oparg=769) at Python/ceval.c:3594\n#37 0x0000000000491cef in PyEval_EvalFrameEx (f=0x71e770, throwflag=0) at Python/ceval.c:2272\n#38 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b47f3dc60, globals=0x6a1540, locals=0x6a1540, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#39 0x000000000048bf06 in PyEval_EvalCode (co=0x2b8b47f3dc60, globals=0x6a1540, locals=0x6a1540) at Python/ceval.c:494\n#40 0x00000000004bcc55 in run_mod (mod=0x73fb18, filename=0x7fff6349a323 \"/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\", globals=0x6a1540, locals=0x6a1540, flags=0x7fff63499300, arena=0x685890)\n    at Python/pythonrun.c:1273\n#41 0x00000000004bcbdf in PyRun_FileExFlags (fp=0x67e010, filename=0x7fff6349a323 \"/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\", start=257, globals=0x6a1540, locals=0x6a1540, closeit=1, flags=0x7fff63499300)\n    at Python/pythonrun.c:1259\n#42 0x00000000004bbae6 in PyRun_SimpleFileExFlags (fp=0x67e010, filename=0x7fff6349a323 \"/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\", closeit=1, flags=0x7fff63499300) at Python/pythonrun.c:879\n#43 0x00000000004bb345 in PyRun_AnyFileExFlags (fp=0x67e010, filename=0x7fff6349a323 \"/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py\", closeit=1, flags=0x7fff63499300) at Python/pythonrun.c:698\n#44 0x00000000004126f8 in Py_Main (argc=2, argv=0x7fff63499478) at Modules/main.c:523\n#45 0x0000000000411843 in main (argc=2, argv=0x7fff63499478) at ./Modules/python.c:23\n```",
    "created_at": "2008-07-24T05:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3706#issuecomment-26245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

gdb says:

```
#0  0x00002b8b47bf407b in raise () from /lib/libc.so.6
#1  0x00002b8b47bf584e in abort () from /lib/libc.so.6
#2  0x00002b8b47c2a629 in __fsetlocking () from /lib/libc.so.6
#3  0x00002b8b47c31193 in mallopt () from /lib/libc.so.6
#4  0x00002b8b47c3121e in free () from /lib/libc.so.6
#5  0x00002b8b57656ace in __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense___dealloc__ (__pyx_v_self=0x2b8b5ee41170) at sage/matrix/matrix_integer_dense.c:4896
#6  0x00002b8b576b87d0 in __pyx_tp_dealloc_4sage_6matrix_20matrix_integer_dense_Matrix_integer_dense (o=0x2b8b5ee41170) at sage/matrix/matrix_integer_dense.c:29687
#7  0x00000000004f1afd in meth_dealloc (m=0x2b8b5ee1a2d8) at Objects/methodobject.c:126
#8  0x00002b8b561339c2 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_list (__pyx_v_self=0x2b8b5ee41170, unused=0x0) at sage/matrix/matrix0.c:1788
#9  0x00000000004f1914 in PyCFunction_Call (func=0x2b8b5ee3bb00, arg=0x2b8b47629050, kw=0x0) at Objects/methodobject.c:82
#10 0x000000000041b08f in PyObject_Call (func=0x2b8b5ee3bb00, arg=0x2b8b47629050, kw=0x0) at Objects/abstract.c:1861
#11 0x00002b8b5613d7b2 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix_str (__pyx_v_self=0x2b8b5ee41170, unused=0x0) at sage/matrix/matrix0.c:5075
#12 0x00000000004f1914 in PyCFunction_Call (func=0x2b8b5ee3b8c0, arg=0x2b8b47629050, kw=0x0) at Objects/methodobject.c:82
#13 0x000000000041b08f in PyObject_Call (func=0x2b8b5ee3b8c0, arg=0x2b8b47629050, kw=0x0) at Objects/abstract.c:1861
#14 0x00002b8b5613c831 in __pyx_pf_4sage_6matrix_7matrix0_6Matrix___repr__ (__pyx_v_self=0x2b8b5ee41170) at sage/matrix/matrix0.c:4766
#15 0x000000000044646b in PyObject_Repr (v=0x2b8b5ee41170) at Objects/object.c:361
#16 0x000000000042bb6d in PyFile_WriteObject (v=0x2b8b5ee41170, f=0x2b8b5d1fdea8, flags=0) at Objects/fileobject.c:2195
#17 0x00000000004c2b39 in sys_displayhook (self=0x0, o=0x2b8b5ee41170) at Python/sysmodule.c:114
#18 0x00000000004f198d in PyCFunction_Call (func=0x2b8b47636440, arg=0x2b8b5e739250, kw=0x0) at Objects/methodobject.c:93
#19 0x000000000041b08f in PyObject_Call (func=0x2b8b47636440, arg=0x2b8b5e739250, kw=0x0) at Objects/abstract.c:1861
#20 0x0000000000494ed3 in PyEval_CallObjectWithKeywords (func=0x2b8b47636440, arg=0x2b8b5e739250, kw=0x0) at Python/ceval.c:3442
#21 0x000000000048f25e in PyEval_EvalFrameEx (f=0x2557be0, throwflag=0) at Python/ceval.c:1531
#22 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b5e7506c0, globals=0x1e26ee0, locals=0x1e26ee0, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#23 0x000000000048bf06 in PyEval_EvalCode (co=0x2b8b5e7506c0, globals=0x1e26ee0, locals=0x1e26ee0) at Python/ceval.c:494
#24 0x0000000000497145 in exec_statement (f=0x24b7b50, prog=0x2b8b5e7506c0, globals=0x1e26ee0, locals=0x1e26ee0) at Python/ceval.c:4177
#25 0x000000000048f9e2 in PyEval_EvalFrameEx (f=0x24b7b50, throwflag=0) at Python/ceval.c:1666
#26 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b4a679eb8, globals=0x8714a0, locals=0x0, args=0x2485090, argcount=4, kws=0x24850b0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#27 0x00000000004959f7 in fast_function (func=0x2b8b4a6c0398, pp_stack=0x7fff63498338, n=4, na=4, nk=0) at Python/ceval.c:3669
#28 0x000000000049570c in call_function (pp_stack=0x7fff63498338, oparg=3) at Python/ceval.c:3594
#29 0x0000000000491cef in PyEval_EvalFrameEx (f=0x2484ee0, throwflag=0) at Python/ceval.c:2272
#30 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b4a67e0a8, globals=0x8714a0, locals=0x0, args=0x6f91d0, argcount=2, kws=0x6f91e0, kwcount=0, defs=0x2b8b4a6aef68, defcount=3, closure=0x0) at Python/ceval.c:2836
#31 0x00000000004959f7 in fast_function (func=0x2b8b4a6c0500, pp_stack=0x7fff63498818, n=2, na=2, nk=0) at Python/ceval.c:3669
#32 0x000000000049570c in call_function (pp_stack=0x7fff63498818, oparg=1) at Python/ceval.c:3594
#33 0x0000000000491cef in PyEval_EvalFrameEx (f=0x6f8ff0, throwflag=0) at Python/ceval.c:2272
#34 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b4a67ea08, globals=0x8714a0, locals=0x0, args=0x71e8f0, argcount=1, kws=0x71e8f8, kwcount=3, defs=0x2b8b4a69c6e8, defcount=9, closure=0x0) at Python/ceval.c:2836
#35 0x00000000004959f7 in fast_function (func=0x2b8b4a6bd758, pp_stack=0x7fff63498cf8, n=7, na=1, nk=3) at Python/ceval.c:3669
#36 0x000000000049570c in call_function (pp_stack=0x7fff63498cf8, oparg=769) at Python/ceval.c:3594
#37 0x0000000000491cef in PyEval_EvalFrameEx (f=0x71e770, throwflag=0) at Python/ceval.c:2272
#38 0x00000000004939df in PyEval_EvalCodeEx (co=0x2b8b47f3dc60, globals=0x6a1540, locals=0x6a1540, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#39 0x000000000048bf06 in PyEval_EvalCode (co=0x2b8b47f3dc60, globals=0x6a1540, locals=0x6a1540) at Python/ceval.c:494
#40 0x00000000004bcc55 in run_mod (mod=0x73fb18, filename=0x7fff6349a323 "/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py", globals=0x6a1540, locals=0x6a1540, flags=0x7fff63499300, arena=0x685890)
    at Python/pythonrun.c:1273
#41 0x00000000004bcbdf in PyRun_FileExFlags (fp=0x67e010, filename=0x7fff6349a323 "/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py", start=257, globals=0x6a1540, locals=0x6a1540, closeit=1, flags=0x7fff63499300)
    at Python/pythonrun.c:1259
#42 0x00000000004bbae6 in PyRun_SimpleFileExFlags (fp=0x67e010, filename=0x7fff6349a323 "/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py", closeit=1, flags=0x7fff63499300) at Python/pythonrun.c:879
#43 0x00000000004bb345 in PyRun_AnyFileExFlags (fp=0x67e010, filename=0x7fff6349a323 "/home/was/build/sage-3.0.6.rc0/tmp/.doctest_matrix2.py", closeit=1, flags=0x7fff63499300) at Python/pythonrun.c:698
#44 0x00000000004126f8 in Py_Main (argc=2, argv=0x7fff63499478) at Modules/main.c:523
#45 0x0000000000411843 in main (argc=2, argv=0x7fff63499478) at ./Modules/python.c:23
```



---

archive/issue_comments_026246.json:
```json
{
    "body": "Attachment [sage-3706.patch](tarball://root/attachments/some-uuid/ticket3706/sage-3706.patch) by @williamstein created at 2008-07-25 19:44:43",
    "created_at": "2008-07-25T19:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3706#issuecomment-26246",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3706.patch](tarball://root/attachments/some-uuid/ticket3706/sage-3706.patch) by @williamstein created at 2008-07-25 19:44:43



---

archive/issue_comments_026247.json:
```json
{
    "body": "The patch fixes the issue. As William mentioned there seems to be trouble with weak references and the current Cython. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-28T10:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3706#issuecomment-26247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch fixes the issue. As William mentioned there seems to be trouble with weak references and the current Cython. Positive review.

Cheers,

Michael



---

archive/issue_events_008484.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-28T11:00:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3706",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3706#event-8484"
}
```



---

archive/issue_comments_026248.json:
```json
{
    "body": "Merged in Sage 3.0.6.final",
    "created_at": "2008-07-28T11:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3706#issuecomment-26248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.6.final



---

archive/issue_comments_026249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-28T11:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3706#issuecomment-26249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
