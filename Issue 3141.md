# Issue 3141: [with patch, needs review] Doctest coverage 100% for crypto.mq.mpolynomialsystem

archive/issues_003141.json:
```json
{
    "body": "Assignee: failure\n\nSome small mostly simple fixes are also included.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3141\n\n",
    "created_at": "2008-05-09T10:42:39Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] Doctest coverage 100% for crypto.mq.mpolynomialsystem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3141",
    "user": "https://github.com/malb"
}
```
Assignee: failure

Some small mostly simple fixes are also included.

Issue created by migration from https://trac.sagemath.org/ticket/3141





---

archive/issue_comments_021756.json:
```json
{
    "body": "Attachment [mpolynomiasystem_fixes.patch](tarball://root/attachments/some-uuid/ticket3141/mpolynomiasystem_fixes.patch) by @malb created at 2008-05-09 10:42:54",
    "created_at": "2008-05-09T10:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21756",
    "user": "https://github.com/malb"
}
```

Attachment [mpolynomiasystem_fixes.patch](tarball://root/attachments/some-uuid/ticket3141/mpolynomiasystem_fixes.patch) by @malb created at 2008-05-09 10:42:54



---

archive/issue_comments_021757.json:
```json
{
    "body": "On sage.math I see a reproducible segfault:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha0$ ./sage -t -long devel/sage/sage/matrix/matrix2.pyx\nsage -t -long devel/sage/sage/matrix/matrix2.pyx            \n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [3.2 s]\n```\n\nThe bachtrace doesn't look very useful:\n\n```\n(gdb) r\nStarting program: /scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/local/bin/python /scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/tmp/.doctest_matrix2.py\n[Thread debugging using libthread_db enabled]\n[New Thread 47955376648032 (LWP 2035)]\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 47955376648032 (LWP 2035)]\n0x00002b9d92c3a118 in __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (o=0x2b9d92733b90) at sage/matrix/matrix_symbolic_dense.c:5748\n5748      Py_XDECREF(p->__variables);\n(gdb) bt\n#0  0x00002b9d92c3a118 in __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (o=0x2b9d92733b90) at sage/matrix/matrix_symbolic_dense.c:5748\n#1  0x000000000043e91b in insertdict (mp=0x65b1d0, key=0x2b9d7ab5ccc0, hash=12160036574, value=0x621b40) at Objects/dictobject.c:416\n#2  0x000000000044032c in PyDict_SetItem (op=0x65b1d0, key=0x2b9d7ab5ccc0, value=0x621b40) at Objects/dictobject.c:641\n#3  0x00000000004439ea in PyObject_GenericSetAttr (obj=0x2b9d7ab32c58, name=0x2b9d7ab5ccc0, value=0x621b40) at Objects/object.c:1431\n#4  0x0000000000442ea7 in PyObject_SetAttr (v=0x2b9d7ab32c58, name=0x2b9d7ab5ccc0, value=0x621b40) at Objects/object.c:1183\n#5  0x000000000044317d in PyObject_SetAttrString (v=0x2b9d7ab32c58, name=<value optimized out>, w=0x621b40) at Objects/object.c:1097\n#6  0x00000000004ad5a5 in sys_displayhook (self=<value optimized out>, o=0x2b9d92733c20) at Python/sysmodule.c:105\n#7  0x0000000000415823 in PyObject_Call (func=0x2b9d92c18800, arg=0x14df810, kw=0x5b1b435b1b435b1b) at Objects/abstract.c:1861\n#8  0x000000000047db21 in PyEval_CallObjectWithKeywords (func=0x2b9d7ab3f440, arg=0x2b9d92c13150, kw=0x0) at Python/ceval.c:3442\n#9  0x000000000048396a in PyEval_EvalFrameEx (f=0x2212b30, throwflag=<value optimized out>) at Python/ceval.c:1531\n#10 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d9274c8a0, globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, \n    defcount=0, closure=0x0) at Python/ceval.c:2836\n#11 0x0000000000484ec2 in PyEval_EvalFrameEx (f=0x16bceb0, throwflag=<value optimized out>) at Python/ceval.c:494\n#12 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7e517120, globals=<value optimized out>, locals=<value optimized out>, args=0x1e35d00, argcount=4, kws=0x1e35d20, kwcount=0, \n    defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#13 0x0000000000484347 in PyEval_EvalFrameEx (f=0x1e35b50, throwflag=<value optimized out>) at Python/ceval.c:3669\n#14 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7e5173f0, globals=<value optimized out>, locals=<value optimized out>, args=0x5, argcount=2, kws=0x6c6bc0, kwcount=0, \n    defs=0x2b9d7e54eba8, defcount=3, closure=0x0) at Python/ceval.c:2836\n#15 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6c69d0, throwflag=<value optimized out>) at Python/ceval.c:3669\n#16 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7e51a648, globals=<value optimized out>, locals=<value optimized out>, args=0x9, argcount=1, kws=0x6bfd48, kwcount=3, \n    defs=0x2b9d7e552668, defcount=9, closure=0x0) at Python/ceval.c:2836\n#17 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6bfbc0, throwflag=<value optimized out>) at Python/ceval.c:3669\n#18 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7b44b210, globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, \n    defcount=0, closure=0x0) at Python/ceval.c:2836\n#19 0x0000000000486422 in PyEval_EvalCode (co=0x2b9d92c18800, globals=0x14df810, locals=0x5b1b435b1b435b1b) at Python/ceval.c:494\n#20 0x00000000004a78ee in PyRun_FileExFlags (fp=0x650010, filename=0x7fff2ff90d22 \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/tmp/.doctest_matrix2.py\", \n    start=<value optimized out>, globals=0x673600, locals=0x673600, closeit=1, flags=0x7fff2ff90830) at Python/pythonrun.c:1273\n#21 0x00000000004a7b80 in PyRun_SimpleFileExFlags (fp=0x650010, filename=0x7fff2ff90d22 \"/scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/tmp/.doctest_matrix2.py\", closeit=1, \n    flags=0x7fff2ff90830) at Python/pythonrun.c:879\n#22 0x0000000000412160 in Py_Main (argc=<value optimized out>, argv=0x7fff2ff90948) at Modules/main.c:523\n#23 0x00002b9d7b0ea4ca in __libc_start_main () from /lib/libc.so.6\n#24 0x000000000041169a in _start () at ../sysdeps/x86_64/elf/start.S:113\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T04:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

On sage.math I see a reproducible segfault:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha0$ ./sage -t -long devel/sage/sage/matrix/matrix2.pyx
sage -t -long devel/sage/sage/matrix/matrix2.pyx            

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [3.2 s]
```

The bachtrace doesn't look very useful:

```
(gdb) r
Starting program: /scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/local/bin/python /scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/tmp/.doctest_matrix2.py
[Thread debugging using libthread_db enabled]
[New Thread 47955376648032 (LWP 2035)]

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47955376648032 (LWP 2035)]
0x00002b9d92c3a118 in __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (o=0x2b9d92733b90) at sage/matrix/matrix_symbolic_dense.c:5748
5748      Py_XDECREF(p->__variables);
(gdb) bt
#0  0x00002b9d92c3a118 in __pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense (o=0x2b9d92733b90) at sage/matrix/matrix_symbolic_dense.c:5748
#1  0x000000000043e91b in insertdict (mp=0x65b1d0, key=0x2b9d7ab5ccc0, hash=12160036574, value=0x621b40) at Objects/dictobject.c:416
#2  0x000000000044032c in PyDict_SetItem (op=0x65b1d0, key=0x2b9d7ab5ccc0, value=0x621b40) at Objects/dictobject.c:641
#3  0x00000000004439ea in PyObject_GenericSetAttr (obj=0x2b9d7ab32c58, name=0x2b9d7ab5ccc0, value=0x621b40) at Objects/object.c:1431
#4  0x0000000000442ea7 in PyObject_SetAttr (v=0x2b9d7ab32c58, name=0x2b9d7ab5ccc0, value=0x621b40) at Objects/object.c:1183
#5  0x000000000044317d in PyObject_SetAttrString (v=0x2b9d7ab32c58, name=<value optimized out>, w=0x621b40) at Objects/object.c:1097
#6  0x00000000004ad5a5 in sys_displayhook (self=<value optimized out>, o=0x2b9d92733c20) at Python/sysmodule.c:105
#7  0x0000000000415823 in PyObject_Call (func=0x2b9d92c18800, arg=0x14df810, kw=0x5b1b435b1b435b1b) at Objects/abstract.c:1861
#8  0x000000000047db21 in PyEval_CallObjectWithKeywords (func=0x2b9d7ab3f440, arg=0x2b9d92c13150, kw=0x0) at Python/ceval.c:3442
#9  0x000000000048396a in PyEval_EvalFrameEx (f=0x2212b30, throwflag=<value optimized out>) at Python/ceval.c:1531
#10 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d9274c8a0, globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, 
    defcount=0, closure=0x0) at Python/ceval.c:2836
#11 0x0000000000484ec2 in PyEval_EvalFrameEx (f=0x16bceb0, throwflag=<value optimized out>) at Python/ceval.c:494
#12 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7e517120, globals=<value optimized out>, locals=<value optimized out>, args=0x1e35d00, argcount=4, kws=0x1e35d20, kwcount=0, 
    defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#13 0x0000000000484347 in PyEval_EvalFrameEx (f=0x1e35b50, throwflag=<value optimized out>) at Python/ceval.c:3669
#14 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7e5173f0, globals=<value optimized out>, locals=<value optimized out>, args=0x5, argcount=2, kws=0x6c6bc0, kwcount=0, 
    defs=0x2b9d7e54eba8, defcount=3, closure=0x0) at Python/ceval.c:2836
#15 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6c69d0, throwflag=<value optimized out>) at Python/ceval.c:3669
#16 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7e51a648, globals=<value optimized out>, locals=<value optimized out>, args=0x9, argcount=1, kws=0x6bfd48, kwcount=3, 
    defs=0x2b9d7e552668, defcount=9, closure=0x0) at Python/ceval.c:2836
#17 0x0000000000484347 in PyEval_EvalFrameEx (f=0x6bfbc0, throwflag=<value optimized out>) at Python/ceval.c:3669
#18 0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b9d7b44b210, globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, 
    defcount=0, closure=0x0) at Python/ceval.c:2836
#19 0x0000000000486422 in PyEval_EvalCode (co=0x2b9d92c18800, globals=0x14df810, locals=0x5b1b435b1b435b1b) at Python/ceval.c:494
#20 0x00000000004a78ee in PyRun_FileExFlags (fp=0x650010, filename=0x7fff2ff90d22 "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/tmp/.doctest_matrix2.py", 
    start=<value optimized out>, globals=0x673600, locals=0x673600, closeit=1, flags=0x7fff2ff90830) at Python/pythonrun.c:1273
#21 0x00000000004a7b80 in PyRun_SimpleFileExFlags (fp=0x650010, filename=0x7fff2ff90d22 "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha0/tmp/.doctest_matrix2.py", closeit=1, 
    flags=0x7fff2ff90830) at Python/pythonrun.c:879
#22 0x0000000000412160 in Py_Main (argc=<value optimized out>, argv=0x7fff2ff90948) at Modules/main.c:523
#23 0x00002b9d7b0ea4ca in __libc_start_main () from /lib/libc.so.6
#24 0x000000000041169a in _start () at ../sysdeps/x86_64/elf/start.S:113
```


Cheers,

Michael



---

archive/issue_comments_021758.json:
```json
{
    "body": "I cannot reproduce this bug on my 64-bit Linux box (my notebook). Since the segfault is in `__pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense` I wonder if your setup is FUBAR? I can't see anything interesting in Valgrind either.",
    "created_at": "2008-06-23T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21758",
    "user": "https://github.com/malb"
}
```

I cannot reproduce this bug on my 64-bit Linux box (my notebook). Since the segfault is in `__pyx_tp_dealloc_4sage_6matrix_21matrix_symbolic_dense_Matrix_symbolic_dense` I wonder if your setup is FUBAR? I can't see anything interesting in Valgrind either.



---

archive/issue_comments_021759.json:
```json
{
    "body": "My setup passed all tests before and after removing that patch. I will try again and do a \"-ba\" just in case I hit some odd dependency issue, but I am 100% that the issue on sage.math is real.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T21:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21759",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

My setup passed all tests before and after removing that patch. I will try again and do a "-ba" just in case I hit some odd dependency issue, but I am 100% that the issue on sage.math is real.

Cheers,

Michael



---

archive/issue_comments_021760.json:
```json
{
    "body": "After a \"-ba\" all tests pass, so it is back to positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-24T01:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

After a "-ba" all tests pass, so it is back to positive review.

Cheers,

Michael



---

archive/issue_comments_021761.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-24T01:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1



---

archive/issue_events_003357.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-24T01:29:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3141#event-3357"
}
```



---

archive/issue_comments_021762.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-24T01:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3141",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3141#issuecomment-21762",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
