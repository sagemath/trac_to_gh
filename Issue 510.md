# Issue 510: IPython crashes on "import sage.rings.real_mpfr"

archive/issues_000510.json:
```json
{
    "body": "Assignee: was\n\nImporting the module sage.rings.real_mpfr in IPython causes a segfault with the backtrace included below. SAGE itself doesn't report any errors in this case.\n\n```\nIn [2]: import sage.rings.real_mpfr\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread -1210221920 (LWP 28996)]\n0xb0d29b0e in __pyx_f_9real_mpfr_9RealField___init__ (__pyx_v_self=0xb0dc625c, \n    __pyx_args=0xb0ce242c, __pyx_kwds=0x0) at sage/rings/real_mpfr.c:1128\n1128      Py_INCREF(__pyx_v_rnd);\n(gdb) bt\n#0  0xb0d29b0e in __pyx_f_9real_mpfr_9RealField___init__ (\n    __pyx_v_self=0xb0dc625c, __pyx_args=0xb0ce242c, __pyx_kwds=0x0)\n    at sage/rings/real_mpfr.c:1128\n#1  0x0809c2f3 in type_call (type=0xb0d88d40, args=0xb0ce242c, kwds=0x0)\n    at Objects/typeobject.c:436\n#2  0x0805a0a7 in PyObject_Call (func=0x0, arg=0xb0ce242c, kw=0x0)\n    at Objects/abstract.c:1860\n#3  0x080c0c50 in PyEval_EvalFrameEx (f=0x83964ec, throwflag=0)\n    at Python/ceval.c:3775\n#4  0x080c564a in PyEval_EvalFrameEx (f=0x8392a9c, throwflag=0)\n    at Python/ceval.c:3650\n#5  0x080c639b in PyEval_EvalCodeEx (co=0xb0dd0ad0, globals=0xb0d9fc64, \n    locals=0x0, args=0xb0d963f8, argcount=2, kws=0x0, kwcount=0, \n    defs=0xb0ce2478, defcount=1, closure=0x0) at Python/ceval.c:2831\n```\n\n\nYou can use the patch included in #509 to run IPython under gdb.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/510\n\n",
    "created_at": "2007-08-29T10:57:35Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "IPython crashes on \"import sage.rings.real_mpfr\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/510",
    "user": "burcin"
}
```
Assignee: was

Importing the module sage.rings.real_mpfr in IPython causes a segfault with the backtrace included below. SAGE itself doesn't report any errors in this case.

```
In [2]: import sage.rings.real_mpfr

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1210221920 (LWP 28996)]
0xb0d29b0e in __pyx_f_9real_mpfr_9RealField___init__ (__pyx_v_self=0xb0dc625c, 
    __pyx_args=0xb0ce242c, __pyx_kwds=0x0) at sage/rings/real_mpfr.c:1128
1128      Py_INCREF(__pyx_v_rnd);
(gdb) bt
#0  0xb0d29b0e in __pyx_f_9real_mpfr_9RealField___init__ (
    __pyx_v_self=0xb0dc625c, __pyx_args=0xb0ce242c, __pyx_kwds=0x0)
    at sage/rings/real_mpfr.c:1128
#1  0x0809c2f3 in type_call (type=0xb0d88d40, args=0xb0ce242c, kwds=0x0)
    at Objects/typeobject.c:436
#2  0x0805a0a7 in PyObject_Call (func=0x0, arg=0xb0ce242c, kw=0x0)
    at Objects/abstract.c:1860
#3  0x080c0c50 in PyEval_EvalFrameEx (f=0x83964ec, throwflag=0)
    at Python/ceval.c:3775
#4  0x080c564a in PyEval_EvalFrameEx (f=0x8392a9c, throwflag=0)
    at Python/ceval.c:3650
#5  0x080c639b in PyEval_EvalCodeEx (co=0xb0dd0ad0, globals=0xb0d9fc64, 
    locals=0x0, args=0xb0d963f8, argcount=2, kws=0x0, kwcount=0, 
    defs=0xb0ce2478, defcount=1, closure=0x0) at Python/ceval.c:2831
```


You can use the patch included in #509 to run IPython under gdb.


Issue created by migration from https://trac.sagemath.org/ticket/510





---

archive/issue_comments_002561.json:
```json
{
    "body": "This is not so much a bug as something that hasn't been implemented -- or even thought about yet.  It doesn't make sense to just load any random module into SAGE, since certain modules assume certain other modules have been imported first.  E.g., import sage.math first and the rest works fine:\n\n\n```\n\nIn [1]: import sage.all\n\nIn [2]: import sage.rings.real_mpfr\n\n```\n\n\nIn short, importing particular random modules without having import sage.all\nfirst is *not* supported at present.  It would be a good enhancement to implement\nsomething to force sage.all to be imported or something...",
    "created_at": "2007-08-31T20:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2561",
    "user": "was"
}
```

This is not so much a bug as something that hasn't been implemented -- or even thought about yet.  It doesn't make sense to just load any random module into SAGE, since certain modules assume certain other modules have been imported first.  E.g., import sage.math first and the rest works fine:


```

In [1]: import sage.all

In [2]: import sage.rings.real_mpfr

```


In short, importing particular random modules without having import sage.all
first is *not* supported at present.  It would be a good enhancement to implement
something to force sage.all to be imported or something...



---

archive/issue_comments_002562.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-31T20:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2562",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_002563.json:
```json
{
    "body": "Changing component from algebraic geometry to interfaces.",
    "created_at": "2007-09-07T05:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2563",
    "user": "craigcitro"
}
```

Changing component from algebraic geometry to interfaces.



---

archive/issue_comments_002564.json:
```json
{
    "body": "I would consider this bug report to be invalid - see the explanation by was above, so it should be closed as invalid. Any opinioins?\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T19:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2564",
    "user": "mabshoff"
}
```

I would consider this bug report to be invalid - see the explanation by was above, so it should be closed as invalid. Any opinioins?

Cheers,

Michael



---

archive/issue_comments_002565.json:
```json
{
    "body": "\n```\n[21:42] <wstein> mabshoff -- close 510 as invalid.\n[21:42] <mabshoff> ok\n```\n",
    "created_at": "2008-02-17T21:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2565",
    "user": "mabshoff"
}
```


```
[21:42] <wstein> mabshoff -- close 510 as invalid.
[21:42] <mabshoff> ok
```




---

archive/issue_comments_002566.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-17T21:02:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2566",
    "user": "mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_002567.json:
```json
{
    "body": "I think this should still remain as an enhancement request, maybe in the sage-wishlist target.\n\nThe reason we get a segfault by importing `sage.rings.real_mpfr` before `sage.all` is that `sage.all` calls some initialization function for this library. From a software design point of view, this initialization should be handled closer to the place the library is used, possibly in the `__init__.py` of the corresponding wrapper. Then users will be able to import this module without worrying about importing `sage.all` and waiting to initialize many components they don't care about.\n\nEven the fact that we don't know which initialization function needs to be called to fix the segfault is enough to regard this as a bug in the wrapper. Since nobody cares enough to look into this at the moment, we should at least keep note of it as an enhancement request which we could take up, once we have the time.\n\nSo I suggest we reopen this, and maybe resolve to `wontfix` instead of `invalid` next time.",
    "created_at": "2008-02-18T08:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2567",
    "user": "burcin"
}
```

I think this should still remain as an enhancement request, maybe in the sage-wishlist target.

The reason we get a segfault by importing `sage.rings.real_mpfr` before `sage.all` is that `sage.all` calls some initialization function for this library. From a software design point of view, this initialization should be handled closer to the place the library is used, possibly in the `__init__.py` of the corresponding wrapper. Then users will be able to import this module without worrying about importing `sage.all` and waiting to initialize many components they don't care about.

Even the fact that we don't know which initialization function needs to be called to fix the segfault is enough to regard this as a bug in the wrapper. Since nobody cares enough to look into this at the moment, we should at least keep note of it as an enhancement request which we could take up, once we have the time.

So I suggest we reopen this, and maybe resolve to `wontfix` instead of `invalid` next time.



---

archive/issue_comments_002568.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-02-18T13:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2568",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002569.json:
```json
{
    "body": "ok, I am convinced for now. If you can come up with a better summary for the bug please change it.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T13:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2569",
    "user": "mabshoff"
}
```

ok, I am convinced for now. If you can come up with a better summary for the bug please change it.

Cheers,

Michael



---

archive/issue_comments_002570.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-02-18T13:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2570",
    "user": "mabshoff"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_002571.json:
```json
{
    "body": "fix some circular imports in sage.rings.real_mpfr",
    "created_at": "2008-05-10T19:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2571",
    "user": "burcin"
}
```

fix some circular imports in sage.rings.real_mpfr



---

archive/issue_comments_002572.json:
```json
{
    "body": "Attachment\n\nattachment:510_real_mpfr_imports.patch fixes the problem reported in the original report. With this patch, \n\n```\nimport sage.rings.complex_field\n```\n\nstill fails because of similar errors. I'll write a script which imports each file in the tree individually and see if I can fix the errors.",
    "created_at": "2008-05-10T19:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2572",
    "user": "burcin"
}
```

Attachment

attachment:510_real_mpfr_imports.patch fixes the problem reported in the original report. With this patch, 

```
import sage.rings.complex_field
```

still fails because of similar errors. I'll write a script which imports each file in the tree individually and see if I can fix the errors.



---

archive/issue_comments_002573.json:
```json
{
    "body": "This ticket should be renamed and the patch that currently exists should be reviewed and hopefully merged. Since the patch is a little old it might have gone stale, but hopefully not.\n\nIf a test script exists we should definitely fix all the problems that it detects, but those problems should be handled via new tickets.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T11:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2573",
    "user": "mabshoff"
}
```

This ticket should be renamed and the patch that currently exists should be reviewed and hopefully merged. Since the patch is a little old it might have gone stale, but hopefully not.

If a test script exists we should definitely fix all the problems that it detects, but those problems should be handled via new tickets.

Cheers,

Michael



---

archive/issue_comments_002574.json:
```json
{
    "body": "Amazingly this patch still applies with some fuzz to my current 3.1.3.alpha2 merge tree:\n\n```\nage-3.1.3.alpha2/devel/sage$ patch -p1 --dry-run < 510_real_mpfr_imports.patch\\?format\\=raw \npatching file sage/rings/real_double.pxd\npatching file sage/rings/real_double.pyx\nHunk #2 succeeded at 1088 (offset 9 lines).\npatching file sage/rings/real_mpfr.pyx\nHunk #1 succeeded at 132 (offset 6 lines).\nHunk #2 succeeded at 158 (offset 6 lines).\nHunk #3 succeeded at 237 with fuzz 2 (offset 18 lines).\nHunk #4 succeeded at 468 (offset 63 lines).\nHunk #5 succeeded at 1879 (offset 191 lines).\npatching file sage/rings/real_rqdf.pxd\npatching file sage/rings/real_rqdf.pyx\nHunk #3 succeeded at 1263 (offset 4 lines).\n```\n\nI did not try to compile, but I consider this encouraging.",
    "created_at": "2008-09-30T12:22:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2574",
    "user": "mabshoff"
}
```

Amazingly this patch still applies with some fuzz to my current 3.1.3.alpha2 merge tree:

```
age-3.1.3.alpha2/devel/sage$ patch -p1 --dry-run < 510_real_mpfr_imports.patch\?format\=raw 
patching file sage/rings/real_double.pxd
patching file sage/rings/real_double.pyx
Hunk #2 succeeded at 1088 (offset 9 lines).
patching file sage/rings/real_mpfr.pyx
Hunk #1 succeeded at 132 (offset 6 lines).
Hunk #2 succeeded at 158 (offset 6 lines).
Hunk #3 succeeded at 237 with fuzz 2 (offset 18 lines).
Hunk #4 succeeded at 468 (offset 63 lines).
Hunk #5 succeeded at 1879 (offset 191 lines).
patching file sage/rings/real_rqdf.pxd
patching file sage/rings/real_rqdf.pyx
Hunk #3 succeeded at 1263 (offset 4 lines).
```

I did not try to compile, but I consider this encouraging.



---

archive/issue_comments_002575.json:
```json
{
    "body": "Attachment\n\nscript to test if importing a random module from the sage library returns an error",
    "created_at": "2008-10-15T16:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2575",
    "user": "burcin"
}
```

Attachment

script to test if importing a random module from the sage library returns an error



---

archive/issue_comments_002576.json:
```json
{
    "body": "Changing component from interfaces to misc.",
    "created_at": "2008-10-15T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2576",
    "user": "burcin"
}
```

Changing component from interfaces to misc.



---

archive/issue_comments_002577.json:
```json
{
    "body": "attachment:sage-test-import imports all modules in the given source tree, and prints out those which raise an error.",
    "created_at": "2008-10-15T16:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2577",
    "user": "burcin"
}
```

attachment:sage-test-import imports all modules in the given source tree, and prints out those which raise an error.



---

archive/issue_comments_002578.json:
```json
{
    "body": "I just tried attachment:510_real_mpfr_imports.patch. It still applies, and fixes the original problem reported, as I wrote in comment:7 previously.\n\nThe script attachment:sage-test-import lists many other problems of this kind, but feel free to apply this patch, and move the script to another ticket.",
    "created_at": "2008-10-15T17:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2578",
    "user": "burcin"
}
```

I just tried attachment:510_real_mpfr_imports.patch. It still applies, and fixes the original problem reported, as I wrote in comment:7 previously.

The script attachment:sage-test-import lists many other problems of this kind, but feel free to apply this patch, and move the script to another ticket.



---

archive/issue_comments_002579.json:
```json
{
    "body": "Positive review on the patch. I also added the sage-test-import script to the local/bin repo. \n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T03:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2579",
    "user": "mabshoff"
}
```

Positive review on the patch. I also added the sage-test-import script to the local/bin repo. 

Cheers,

Michael



---

archive/issue_comments_002580.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T03:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2580",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002581.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-27T03:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/510#issuecomment-2581",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1
