# Issue 3608: optimize.py: "Invalid read of size 8"

archive/issues_003608.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @mkoeppe @kcrisman\n\n```\n==21694== Invalid read of size 8\n==21694==    at 0x21C720A0: Matrix_NewFromArrayStruct (dense.c:244)\n==21694==    by 0x21C751EE: matrix_new (dense.c:499)\n==21694==    by 0x45E48A: type_call (typeobject.c:422)\n==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==21694==    by 0x4952F3: do_call (ceval.c:3784)\n==21694==    by 0x494BAA: call_function (ceval.c:3596)\n==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)\n==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)\n==21694==    by 0x494E7C: fast_function (ceval.c:3669)\n==21694==    by 0x494B91: call_function (ceval.c:3594)\n==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)\n==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)\n==21694==  Address 0x57a1be0 is 0 bytes after a block of size 16 alloc'd\n==21694==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==21694==    by 0x44969A: PyMem_Malloc (object.c:2010)\n==21694==    by 0x1D033292: array_struct_get (arrayobject.c:6409)\n==21694==    by 0x4EA584: getset_get (descrobject.c:146)\n==21694==    by 0x448569: PyObject_GenericGetAttr (object.c:1312)\n==21694==    by 0x447F0B: PyObject_GetAttr (object.c:1127)\n==21694==    by 0x447CB3: PyObject_GetAttrString (object.c:1069)\n==21694==    by 0x21C71DCC: Matrix_NewFromArrayStruct (dense.c:191)\n==21694==    by 0x21C751EE: matrix_new (dense.c:499)\n==21694==    by 0x45E48A: type_call (typeobject.c:422)\n==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==21694==    by 0x4952F3: do_call (ceval.c:3784)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3608\n\n",
    "created_at": "2008-07-08T11:53:08Z",
    "labels": [
        "component: memleak",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optimize.py: \"Invalid read of size 8\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @mkoeppe @kcrisman

```
==21694== Invalid read of size 8
==21694==    at 0x21C720A0: Matrix_NewFromArrayStruct (dense.c:244)
==21694==    by 0x21C751EE: matrix_new (dense.c:499)
==21694==    by 0x45E48A: type_call (typeobject.c:422)
==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==21694==    by 0x4952F3: do_call (ceval.c:3784)
==21694==    by 0x494BAA: call_function (ceval.c:3596)
==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)
==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==21694==    by 0x494E7C: fast_function (ceval.c:3669)
==21694==    by 0x494B91: call_function (ceval.c:3594)
==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)
==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)
==21694==  Address 0x57a1be0 is 0 bytes after a block of size 16 alloc'd
==21694==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==21694==    by 0x44969A: PyMem_Malloc (object.c:2010)
==21694==    by 0x1D033292: array_struct_get (arrayobject.c:6409)
==21694==    by 0x4EA584: getset_get (descrobject.c:146)
==21694==    by 0x448569: PyObject_GenericGetAttr (object.c:1312)
==21694==    by 0x447F0B: PyObject_GetAttr (object.c:1127)
==21694==    by 0x447CB3: PyObject_GetAttrString (object.c:1069)
==21694==    by 0x21C71DCC: Matrix_NewFromArrayStruct (dense.c:191)
==21694==    by 0x21C751EE: matrix_new (dense.c:499)
==21694==    by 0x45E48A: type_call (typeobject.c:422)
==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)
==21694==    by 0x4952F3: do_call (ceval.c:3784)
```

Issue created by migration from https://trac.sagemath.org/ticket/3608





---

archive/issue_comments_025435.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25435",
    "user": "https://github.com/williamstein"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_events_008265.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8265"
}
```



---

archive/issue_events_008266.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8266"
}
```



---

archive/issue_events_008267.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8267"
}
```



---

archive/issue_events_008268.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8268"
}
```



---

archive/issue_events_008269.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8269"
}
```



---

archive/issue_events_008270.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8270"
}
```



---

archive/issue_events_008271.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8271"
}
```



---

archive/issue_events_008272.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-02T13:29:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8272"
}
```



---

archive/issue_events_008273.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-02T13:29:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8273"
}
```



---

archive/issue_comments_025436.json:
```json
{
    "body": "totally unclear. Can we close as obsolete ?",
    "created_at": "2020-07-02T13:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25436",
    "user": "https://github.com/fchapoton"
}
```

totally unclear. Can we close as obsolete ?



---

archive/issue_comments_025437.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-02T13:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25437",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025438.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-02T14:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25438",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025439.json:
```json
{
    "body": "ancient valgrind report, outdated",
    "created_at": "2020-07-02T14:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25439",
    "user": "https://github.com/mkoeppe"
}
```

ancient valgrind report, outdated



---

archive/issue_comments_025440.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-02T14:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25440",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_008274.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-02T14:10:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3608#event-8274"
}
```
