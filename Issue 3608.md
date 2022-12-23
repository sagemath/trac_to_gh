# Issue 3608: optimize.py: "Invalid read of size 8"

archive/issues_003608.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mkoeppe kcrisman\n\n\n```\n==21694== Invalid read of size 8\n==21694==    at 0x21C720A0: Matrix_NewFromArrayStruct (dense.c:244)\n==21694==    by 0x21C751EE: matrix_new (dense.c:499)\n==21694==    by 0x45E48A: type_call (typeobject.c:422)\n==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==21694==    by 0x4952F3: do_call (ceval.c:3784)\n==21694==    by 0x494BAA: call_function (ceval.c:3596)\n==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)\n==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)\n==21694==    by 0x494E7C: fast_function (ceval.c:3669)\n==21694==    by 0x494B91: call_function (ceval.c:3594)\n==21694==    by 0x491174: PyEval_EvalFrameEx (ceval.c:2272)\n==21694==    by 0x492E64: PyEval_EvalCodeEx (ceval.c:2836)\n==21694==  Address 0x57a1be0 is 0 bytes after a block of size 16 alloc'd\n==21694==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==21694==    by 0x44969A: PyMem_Malloc (object.c:2010)\n==21694==    by 0x1D033292: array_struct_get (arrayobject.c:6409)\n==21694==    by 0x4EA584: getset_get (descrobject.c:146)\n==21694==    by 0x448569: PyObject_GenericGetAttr (object.c:1312)\n==21694==    by 0x447F0B: PyObject_GetAttr (object.c:1127)\n==21694==    by 0x447CB3: PyObject_GetAttrString (object.c:1069)\n==21694==    by 0x21C71DCC: Matrix_NewFromArrayStruct (dense.c:191)\n==21694==    by 0x21C751EE: matrix_new (dense.c:499)\n==21694==    by 0x45E48A: type_call (typeobject.c:422)\n==21694==    by 0x41B0FA: PyObject_Call (abstract.c:1861)\n==21694==    by 0x4952F3: do_call (ceval.c:3784)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3608\n\n",
    "created_at": "2008-07-08T11:53:08Z",
    "labels": [
        "memleak",
        "blocker",
        "bug"
    ],
    "title": "optimize.py: \"Invalid read of size 8\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3608",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  mkoeppe kcrisman


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

archive/issue_comments_025486.json:
```json
{
    "body": "If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.",
    "created_at": "2009-06-15T23:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25486",
    "user": "was"
}
```

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.



---

archive/issue_comments_025487.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2009-06-15T23:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25487",
    "user": "was"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_025488.json:
```json
{
    "body": "totally unclear. Can we close as obsolete ?",
    "created_at": "2020-07-02T13:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25488",
    "user": "chapoton"
}
```

totally unclear. Can we close as obsolete ?



---

archive/issue_comments_025489.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-02T13:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25489",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025490.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-02T14:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25490",
    "user": "mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025491.json:
```json
{
    "body": "ancient valgrind report, outdated",
    "created_at": "2020-07-02T14:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25491",
    "user": "mkoeppe"
}
```

ancient valgrind report, outdated



---

archive/issue_comments_025492.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-02T14:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3608",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3608#issuecomment-25492",
    "user": "chapoton"
}
```

Resolution: invalid
