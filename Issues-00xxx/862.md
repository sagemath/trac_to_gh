# Issue 862: [with patch] [tested by cwitty] memory leak: Matrix_modn_sparse

archive/issues_000862.json:
```json
{
    "body": "Assignee: mabshoff\n\nRunning\n\n```\nget_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache(); get_memory_usage()\n```\nleads to\n\n```\n==15091== 219,648 (197,120 direct, 22,528 indirect) bytes in 22 blocks are definitely lost in loss record 2,428 of 2,504\n==15091==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==15091==    by 0x123E8B13: __pyx_tp_new_18matrix_modn_sparse_Matrix_modn_sparse (matrix_modn_sparse.c:2969)\n==15091==    by 0x4597F9: tp_new_wrapper (typeobject.c:4022)\n==15091==    by 0x415522: PyObject_Call (abstract.c:1860)\n==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==15091==    by 0x129A36AD: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__mod_int_c (matrix_integer_sparse.c:7106\n)\n==15091==    by 0x1299FBB3: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__mod_int (matrix_integer_sparse.c:7021)\n==15091==    by 0x415522: PyObject_Call (abstract.c:1860)\n==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==15091==    by 0x1755D847: __pyx_f_4misc_matrix_rational_echelon_form_multimodular (misc.c:12135)\n==15091==    by 0x415522: PyObject_Call (abstract.c:1860)\n==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n```\nBefore the patch:\n\n```\n==11617== LEAK SUMMARY:\n==11617==    definitely lost: 576,207 bytes in 60,771 blocks.\n==11617==    indirectly lost: 130,648 bytes in 227 blocks.\n==11617==      possibly lost: 377,974 bytes in 943 blocks.\n==11617==    still reachable: 57,758,197 bytes in 839,535 blocks.\n==11617==         suppressed: 0 bytes in 0 blocks.\n```\nWith the patch:\n\n```\n==11888==    definitely lost: 549,575 bytes in 60,799 blocks.\n==11888==    indirectly lost: 129,896 bytes in 133 blocks.\n==11888==      possibly lost: 377,982 bytes in 943 blocks.\n==11888==    still reachable: 57,758,573 bytes in 839,594 blocks.\n==11888==         suppressed: 0 bytes in 0 blocks.\n```\n./sage -testall passes on sage.math\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/862\n\n",
    "closed_at": "2007-10-13T07:51:53Z",
    "created_at": "2007-10-12T15:52:05Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] [tested by cwitty] memory leak: Matrix_modn_sparse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/862",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Running

```
get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache(); get_memory_usage()
```
leads to

```
==15091== 219,648 (197,120 direct, 22,528 indirect) bytes in 22 blocks are definitely lost in loss record 2,428 of 2,504
==15091==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==15091==    by 0x123E8B13: __pyx_tp_new_18matrix_modn_sparse_Matrix_modn_sparse (matrix_modn_sparse.c:2969)
==15091==    by 0x4597F9: tp_new_wrapper (typeobject.c:4022)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==15091==    by 0x129A36AD: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__mod_int_c (matrix_integer_sparse.c:7106
)
==15091==    by 0x1299FBB3: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__mod_int (matrix_integer_sparse.c:7021)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==15091==    by 0x1755D847: __pyx_f_4misc_matrix_rational_echelon_form_multimodular (misc.c:12135)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
```
Before the patch:

```
==11617== LEAK SUMMARY:
==11617==    definitely lost: 576,207 bytes in 60,771 blocks.
==11617==    indirectly lost: 130,648 bytes in 227 blocks.
==11617==      possibly lost: 377,974 bytes in 943 blocks.
==11617==    still reachable: 57,758,197 bytes in 839,535 blocks.
==11617==         suppressed: 0 bytes in 0 blocks.
```
With the patch:

```
==11888==    definitely lost: 549,575 bytes in 60,799 blocks.
==11888==    indirectly lost: 129,896 bytes in 133 blocks.
==11888==      possibly lost: 377,982 bytes in 943 blocks.
==11888==    still reachable: 57,758,573 bytes in 839,594 blocks.
==11888==         suppressed: 0 bytes in 0 blocks.
```
./sage -testall passes on sage.math

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/862





---

archive/issue_comments_005310.json:
```json
{
    "body": "Attachment [Sage-2.8.6-fix-memleak-in-Matrix_modn_sparse.patch](tarball://root/attachments/some-uuid/ticket862/Sage-2.8.6-fix-memleak-in-Matrix_modn_sparse.patch) by mabshoff created at 2007-10-13 00:05:39",
    "created_at": "2007-10-13T00:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/862#issuecomment-5310",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.6-fix-memleak-in-Matrix_modn_sparse.patch](tarball://root/attachments/some-uuid/ticket862/Sage-2.8.6-fix-memleak-in-Matrix_modn_sparse.patch) by mabshoff created at 2007-10-13 00:05:39



---

archive/issue_comments_005311.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-13T00:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/862#issuecomment-5311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_002415.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-13T07:51:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/862",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/862#event-2415"
}
```



---

archive/issue_comments_005312.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:51:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/862#issuecomment-5312",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
