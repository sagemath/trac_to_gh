# Issue 534: matrix_modn_sparse_Matrix_modn_sparse leak (from modular/ssmod/ssmod.py)

archive/issues_000534.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom Sage 2.8.3rc3:\n\n```\n==24845== 32,608 (30,120 direct, 2,488 indirect) bytes in 25 blocks are definitely lost in loss record 2,491 of 2,587\n==24845==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==24845==    by 0x1FCAF14A: __pyx_tp_new_18matrix_modn_sparse_Matrix_modn_sparse (matrix_modn_sparse.c:2810)\n==24845==    by 0x45A272: type_call (typeobject.c:422)\n==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24845==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)\n==24845==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)\n==24845==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)\n==24845==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)\n==24845==    by 0x4CFED0: function_call (funcobject.c:517)\n==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24845==    by 0x41BE0C: instancemethod_call (classobject.c:2497)\n==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/534\n\n",
    "created_at": "2007-08-30T18:52:22Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "matrix_modn_sparse_Matrix_modn_sparse leak (from modular/ssmod/ssmod.py)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/534",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

From Sage 2.8.3rc3:

```
==24845== 32,608 (30,120 direct, 2,488 indirect) bytes in 25 blocks are definitely lost in loss record 2,491 of 2,587
==24845==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==24845==    by 0x1FCAF14A: __pyx_tp_new_18matrix_modn_sparse_Matrix_modn_sparse (matrix_modn_sparse.c:2810)
==24845==    by 0x45A272: type_call (typeobject.c:422)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24845==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==24845==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==24845==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==24845==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==24845==    by 0x4CFED0: function_call (funcobject.c:517)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24845==    by 0x41BE0C: instancemethod_call (classobject.c:2497)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/534





---

archive/issue_comments_002712.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-30T18:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/534#issuecomment-2712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002713.json:
```json
{
    "body": "Fixed along the way, probably with my other modular memleak fixes.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-14T11:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/534#issuecomment-2713",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed along the way, probably with my other modular memleak fixes.

Cheers,

Michael



---

archive/issue_events_000573.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-10-14T12:45:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/534#event-573"
}
```



---

archive/issue_comments_002714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T12:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/534#issuecomment-2714",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
