# Issue 2990: sage-3.0.rc1: calculus/functions.py segfault on debian64 xeon vmware image

archive/issues_002990.json:
```json
{
    "body": "Assignee: @williamstein\n\nSame problem every time.  This is new since rc0.\n\n\n```\nwas@debian64:~/build/sage-3.0.rc1$ ./sage -t --gdb devel/sage/sage/calculus/functions.py\nsage -t --gdb devel/sage/sage/calculus/functions.py         ********************************************************************************\nType r at the (gdb) prompt to run the doctests.\nType bt if there is a crash to see a traceback.\n********************************************************************************\nGNU gdb 6.4.90-debian\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"x86_64-linux-gnu\"...Using host libthread_db library \"/lib/libthread_db.so.1\".\n\n(gdb) r\nStarting program: /home/was/build/sage-3.0.rc1/local/bin/python /home/was/build/sage-3.0.rc1/tmp/.doctest_functions.py\n[Thread debugging using libthread_db enabled]\n[New Thread 47336057798496 (LWP 19251)]\n\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread 47336057798496 (LWP 19251)]\nPyObject_GC_Del (op=0x2b0d5d762d40) at Modules/gcmodule.c:161\n161     Modules/gcmodule.c: No such file or directory.\n        in Modules/gcmodule.c\n(gdb)\n(gdb) bt\n#0  PyObject_GC_Del (op=0x2b0d5d762d40) at Modules/gcmodule.c:161\n#1  0x00000000004d050b in meth_dealloc (m=0x2b0d6015f290) at Objects/methodobject.c:126\n#2  0x000000000047fcce in PyEval_EvalFrameEx (f=0x1d6a400,\n    throwflag=<value optimized out>) at Python/ceval.c:3607\n#3  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5e76eb70,\n    globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=2,\n    kws=0x1d540c0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#4  0x0000000000484347 in PyEval_EvalFrameEx (f=0x1d53f30,\n    throwflag=<value optimized out>) at Python/ceval.c:3669\n#5  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5fd80558,\n    globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0,\n    kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836\n#6  0x0000000000484ec2 in PyEval_EvalFrameEx (f=0x1d52ed0,\n    throwflag=<value optimized out>) at Python/ceval.c:494\n#7  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5fd89a08,\n    globals=<value optimized out>, locals=<value optimized out>, args=0x1d57c10,\n    argcount=4, kws=0x1d57c30, kwcount=0, defs=0x0, defcount=0, closure=0x0)\n    at Python/ceval.c:2836\n#8  0x0000000000484347 in PyEval_EvalFrameEx (f=0x1d57a60,\n    throwflag=<value optimized out>) at Python/ceval.c:3669\n#9  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5fd89b70,\n    globals=<value optimized out>, locals=<value optimized out>, args=0x5, argcount=2,\n\n```\n\n\n\nIf test the same file with verbose the problem vanishes.  I'm guessing it is a deallocate on exist issue. \n\nThe problem happens even if output isn't redirected:\n\n```\nwas@debian64:~/build/sage-3.0.rc1$ ./sage -python tmp/.doctest_functions.py \n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2990\n\n",
    "created_at": "2008-04-21T16:47:31Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "sage-3.0.rc1: calculus/functions.py segfault on debian64 xeon vmware image",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2990",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Same problem every time.  This is new since rc0.


```
was@debian64:~/build/sage-3.0.rc1$ ./sage -t --gdb devel/sage/sage/calculus/functions.py
sage -t --gdb devel/sage/sage/calculus/functions.py         ********************************************************************************
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

(gdb) r
Starting program: /home/was/build/sage-3.0.rc1/local/bin/python /home/was/build/sage-3.0.rc1/tmp/.doctest_functions.py
[Thread debugging using libthread_db enabled]
[New Thread 47336057798496 (LWP 19251)]


Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 47336057798496 (LWP 19251)]
PyObject_GC_Del (op=0x2b0d5d762d40) at Modules/gcmodule.c:161
161     Modules/gcmodule.c: No such file or directory.
        in Modules/gcmodule.c
(gdb)
(gdb) bt
#0  PyObject_GC_Del (op=0x2b0d5d762d40) at Modules/gcmodule.c:161
#1  0x00000000004d050b in meth_dealloc (m=0x2b0d6015f290) at Objects/methodobject.c:126
#2  0x000000000047fcce in PyEval_EvalFrameEx (f=0x1d6a400,
    throwflag=<value optimized out>) at Python/ceval.c:3607
#3  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5e76eb70,
    globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=2,
    kws=0x1d540c0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#4  0x0000000000484347 in PyEval_EvalFrameEx (f=0x1d53f30,
    throwflag=<value optimized out>) at Python/ceval.c:3669
#5  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5fd80558,
    globals=<value optimized out>, locals=<value optimized out>, args=0x0, argcount=0,
    kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#6  0x0000000000484ec2 in PyEval_EvalFrameEx (f=0x1d52ed0,
    throwflag=<value optimized out>) at Python/ceval.c:494
#7  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5fd89a08,
    globals=<value optimized out>, locals=<value optimized out>, args=0x1d57c10,
    argcount=4, kws=0x1d57c30, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2836
#8  0x0000000000484347 in PyEval_EvalFrameEx (f=0x1d57a60,
    throwflag=<value optimized out>) at Python/ceval.c:3669
#9  0x0000000000486182 in PyEval_EvalCodeEx (co=0x2b0d5fd89b70,
    globals=<value optimized out>, locals=<value optimized out>, args=0x5, argcount=2,

```



If test the same file with verbose the problem vanishes.  I'm guessing it is a deallocate on exist issue. 

The problem happens even if output isn't redirected:

```
was@debian64:~/build/sage-3.0.rc1$ ./sage -python tmp/.doctest_functions.py 


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



Issue created by migration from https://trac.sagemath.org/ticket/2990





---

archive/issue_comments_020535.json:
```json
{
    "body": "This also happens on my 32-bit Ubuntu and Debian Xeon vmware images.  Exactly the same...",
    "created_at": "2008-04-21T18:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2990#issuecomment-20535",
    "user": "https://github.com/williamstein"
}
```

This also happens on my 32-bit Ubuntu and Debian Xeon vmware images.  Exactly the same...



---

archive/issue_comments_020536.json:
```json
{
    "body": "If I backout what is for me this\n\n```\n# HG changeset patch\n# User Alexandru Ghitza <aghitza@alum.mit.edu>\n# Date 1208737339 14400\n# Node ID e6249f4ffb3917dc2317eb0019654b8f0b486cb0\n# Parent  89932dbf4a767b51e2a538533f4a980079e8371e\n[mq]: wronskian_constants.patch\n```\n\n\nthen the segfaults disappear. \n\nSince that changeset is pure python, the underlying cause must be deeper, and it just happens\nto be the case that this exposes some issue.\n\nWilliam",
    "created_at": "2008-04-21T18:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2990#issuecomment-20536",
    "user": "https://github.com/williamstein"
}
```

If I backout what is for me this

```
# HG changeset patch
# User Alexandru Ghitza <aghitza@alum.mit.edu>
# Date 1208737339 14400
# Node ID e6249f4ffb3917dc2317eb0019654b8f0b486cb0
# Parent  89932dbf4a767b51e2a538533f4a980079e8371e
[mq]: wronskian_constants.patch
```


then the segfaults disappear. 

Since that changeset is pure python, the underlying cause must be deeper, and it just happens
to be the case that this exposes some issue.

William



---

archive/issue_comments_020537.json:
```json
{
    "body": "I cannot reproduce this either with rc1 on sage.math nor with your rc1 build on debian64:\n\n```\n==30663== Memcheck, a memory error detector.\n==30663== Copyright (C) 2002-2008, and GNU GPL'd, by Julian Seward et al.\n==30663== Using LibVEX rev 1812, a library for dynamic binary translation.\n==30663== Copyright (C) 2004-2008, and GNU GPL'd, by OpenWorks LLP.\n==30663== Using valgrind-3.4.0.SVN, a dynamic binary instrumentation framework.\n==30663== Copyright (C) 2000-2008, and GNU GPL'd, by Julian Seward et al.\n==30663== For more details, rerun with: -v\n==30663==\n==30663== My PID = 30663, parent PID = 30662.  Prog and args are:\n==30663==    /scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/python\n==30663==    /scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/.doctest_functions.py\n==30663==\n--30663-- DWARF2 CFI reader: unhandled CFI instruction 0:10\n--30663-- DWARF2 CFI reader: unhandled CFI instruction 0:10\n==30663==\n==30663== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 570 from 2)\n==30663== malloc/free: in use at exit: 34,573,886 bytes in 218,151 blocks.\n==30663== malloc/free: 920,111 allocs, 701,960 frees, 211,580,807 bytes allocated.\n==30663== For counts of detected errors, rerun with: -v\n==30663== searching for pointers to 218,151 not-freed blocks.\n==30663== checked 39,313,256 bytes.\n==30663==\n==30663== LEAK SUMMARY:\n==30663==    definitely lost: 242,945 bytes in 3,868 blocks.\n==30663==      possibly lost: 328,992 bytes in 940 blocks.\n==30663==    still reachable: 34,001,949 bytes in 213,343 blocks.\n==30663==         suppressed: 0 bytes in 0 blocks.\n==30663== Rerun with --leak-check=full to see details of leaked memory.\n```\n\nI checked the hg log and the patches applied are identical. So far nobody else has been able to reproduce this.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-22T03:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2990#issuecomment-20537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I cannot reproduce this either with rc1 on sage.math nor with your rc1 build on debian64:

```
==30663== Memcheck, a memory error detector.
==30663== Copyright (C) 2002-2008, and GNU GPL'd, by Julian Seward et al.
==30663== Using LibVEX rev 1812, a library for dynamic binary translation.
==30663== Copyright (C) 2004-2008, and GNU GPL'd, by OpenWorks LLP.
==30663== Using valgrind-3.4.0.SVN, a dynamic binary instrumentation framework.
==30663== Copyright (C) 2000-2008, and GNU GPL'd, by Julian Seward et al.
==30663== For more details, rerun with: -v
==30663==
==30663== My PID = 30663, parent PID = 30662.  Prog and args are:
==30663==    /scratch/mabshoff/release-cycle/sage-3.0.rc1/local/bin/python
==30663==    /scratch/mabshoff/release-cycle/sage-3.0.rc1/tmp/.doctest_functions.py
==30663==
--30663-- DWARF2 CFI reader: unhandled CFI instruction 0:10
--30663-- DWARF2 CFI reader: unhandled CFI instruction 0:10
==30663==
==30663== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 570 from 2)
==30663== malloc/free: in use at exit: 34,573,886 bytes in 218,151 blocks.
==30663== malloc/free: 920,111 allocs, 701,960 frees, 211,580,807 bytes allocated.
==30663== For counts of detected errors, rerun with: -v
==30663== searching for pointers to 218,151 not-freed blocks.
==30663== checked 39,313,256 bytes.
==30663==
==30663== LEAK SUMMARY:
==30663==    definitely lost: 242,945 bytes in 3,868 blocks.
==30663==      possibly lost: 328,992 bytes in 940 blocks.
==30663==    still reachable: 34,001,949 bytes in 213,343 blocks.
==30663==         suppressed: 0 bytes in 0 blocks.
==30663== Rerun with --leak-check=full to see details of leaked memory.
```

I checked the hg log and the patches applied are identical. So far nobody else has been able to reproduce this.

Thoughts?

Cheers,

Michael



---

archive/issue_events_006815.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-22T04:40:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2990",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2990#event-6815"
}
```



---

archive/issue_comments_020538.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-22T04:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2990#issuecomment-20538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020539.json:
```json
{
    "body": "Attachment [sage-2990.patch](tarball://root/attachments/some-uuid/ticket2990/sage-2990.patch) by mabshoff created at 2008-04-22 04:40:19\n\nMerged in Sage 3.0.final",
    "created_at": "2008-04-22T04:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2990#issuecomment-20539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-2990.patch](tarball://root/attachments/some-uuid/ticket2990/sage-2990.patch) by mabshoff created at 2008-04-22 04:40:19

Merged in Sage 3.0.final
