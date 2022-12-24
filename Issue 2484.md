# Issue 2484: "Conditional jump" in  QuadDoubleElement __repr__

archive/issues_002484.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen doctesting calculus.py memcheck complains about the following:\n\n```\n==24858== Conditional jump or move depends on uninitialised value(s)\n==24858==    at 0x4A1CA17: strlen (mc_replace_strmem.c:242)\n==24858==    by 0x44D65A: PyString_FromString (stringobject.c:108)\n==24858==    by 0xC248F88: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (rea\nl_rqdf.cpp:5314)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24858==    by 0xC24C11A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5850)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24858==    by 0xC2468BB: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5152)\n==24858==    by 0x443279: PyObject_Repr (object.c:361)\n==24858==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)\n==24858==    by 0x4AC5B8: sys_displayhook (sysmodule.c:114)\n==24858== Invalid read of size 1\n==24858==    at 0x4A1CA13: strlen (mc_replace_strmem.c:242)\n==24858==    by 0x44D65A: PyString_FromString (stringobject.c:108)\n==24858==    by 0xC248F88: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (rea\nl_rqdf.cpp:5314)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24858==    by 0xC24C11A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5850)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24858==    by 0xC2468BB: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5152)\n==24858==    by 0x443279: PyObject_Repr (object.c:361)\n==24858==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)\n==24858==    by 0x4AC5B8: sys_displayhook (sysmodule.c:114)\n==24858==  Address 0x1c89aa29 is 0 bytes after a block of size 65 alloc'd\n==24858==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==24858==    by 0xC248F3E: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___str_no_scientific(_object*, _object*) (rea\nl_rqdf.cpp:5278)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24858==    by 0xC24C11A: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement_str(_object*, _object*) (real_rqdf.cpp:5850)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n==24858==    by 0x47CBE0: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24858==    by 0xC2468BB: __pyx_pf_4sage_5rings_9real_rqdf_17QuadDoubleElement___repr__(_object*) (real_rqdf.cpp:5152)\n==24858==    by 0x443279: PyObject_Repr (object.c:361)\n==24858==    by 0x429B5B: PyFile_WriteObject (fileobject.c:2196)\n==24858==    by 0x4AC5B8: sys_displayhook (sysmodule.c:114)\n==24858==    by 0x415542: PyObject_Call (abstract.c:1860)\n```\n\n\nI suspect the above causes occasional unreproducible segfaults in various doctests.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2484\n\n",
    "created_at": "2008-03-12T08:25:36Z",
    "labels": [
        "memleak",
        "blocker",
        "bug"
    ],
    "title": "\"Conditional jump\" in  QuadDoubleElement __repr__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2484",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/2484





---

archive/issue_comments_016830.json:
```json
{
    "body": "Attachment [trac2484-rqdf-uninit.patch](tarball://root/attachments/some-uuid/ticket2484/trac2484-rqdf-uninit.patch) by cwitty created at 2008-03-14 01:33:41\n\nThe attached patch *should* fix the above valgrind log, but I haven't run valgrind myself to check.  (I did run testall, which passed.)",
    "created_at": "2008-03-14T01:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2484#issuecomment-16830",
    "user": "cwitty"
}
```

Attachment [trac2484-rqdf-uninit.patch](tarball://root/attachments/some-uuid/ticket2484/trac2484-rqdf-uninit.patch) by cwitty created at 2008-03-14 01:33:41

The attached patch *should* fix the above valgrind log, but I haven't run valgrind myself to check.  (I did run testall, which passed.)



---

archive/issue_comments_016831.json:
```json
{
    "body": "The patch fixes the issue. Positive review :)",
    "created_at": "2008-03-14T02:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2484#issuecomment-16831",
    "user": "mabshoff"
}
```

The patch fixes the issue. Positive review :)



---

archive/issue_comments_016832.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T02:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2484#issuecomment-16832",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_016833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T02:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2484#issuecomment-16833",
    "user": "mabshoff"
}
```

Resolution: fixed
