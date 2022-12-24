# Issue 865: several small memory leak in multi_modular

archive/issues_000865.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello,\nRunning\n\n```\nget_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache(); get_memory_usage()\n```\n\nleads to\n\n```\n==11888== 120 bytes in 15 blocks are definitely lost in loss record 364 of 2,467\n==11888==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==11888==    by 0x6108E17: __gmpz_init_set_ui (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)\n==11888==    by 0x11D57FD4: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2398)\n==11888==    by 0x11D538C0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5940)\n==11888==    by 0x459172: type_call (typeobject.c:422)\n==11888==    by 0x415522: PyObject_Call (abstract.c:1860)\n==11888==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==11888==    by 0x126DE8DA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de\nnse.c:7711)\n==11888==    by 0x415522: PyObject_Call (abstract.c:1860)\n==11888==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==11888==    by 0x126B66BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege\nr_dense.c:5669)\n==11888==    by 0x17AFCD27: __pyx_f_6action_18MatrixMatrixAction__call_c_impl (action.c:1270)\n\n==19224== 24 bytes in 3 blocks are definitely lost in loss record 134 of 2,477\n==19224==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==19224==    by 0x6107C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)\n==19224==    by 0x11D58001: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2425)\n==19224==    by 0x11D538C0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5949)\n==19224==    by 0x459172: type_call (typeobject.c:422)\n==19224==    by 0x415522: PyObject_Call (abstract.c:1860)\n==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==19224==    by 0x126DE8DA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de\nnse.c:7711)\n==19224==    by 0x415522: PyObject_Call (abstract.c:1860)\n==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==19224==    by 0x126B66BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege\nr_dense.c:5669)\n==19224==    by 0x9340519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)\n\n==19224== 24 bytes in 3 blocks are definitely lost in loss record 135 of 2,477\n==19224==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==19224==    by 0x6107C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)\n==19224==    by 0x11D57FF8: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2416)\n==19224==    by 0x11D538C0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5949)\n==19224==    by 0x459172: type_call (typeobject.c:422)\n==19224==    by 0x415522: PyObject_Call (abstract.c:1860)\n==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==19224==    by 0x126DE8DA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de\nnse.c:7711)\n==19224==    by 0x415522: PyObject_Call (abstract.c:1860)\n==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==19224==    by 0x126B66BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege\nr_dense.c:5669)\n==19224==    by 0x9340519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)\n```\n\nbefore patch:\n\n```\n==11888== LEAK SUMMARY:\n==11888==    definitely lost: 549,575 bytes in 60,799 blocks.\n==11888==    indirectly lost: 129,896 bytes in 133 blocks.\n==11888==      possibly lost: 377,982 bytes in 943 blocks.\n==11888==    still reachable: 57,758,573 bytes in 839,594 blocks.\n==11888==         suppressed: 0 bytes in 0 blocks.\n```\n\nafter patch:\n\n```\n==22732==    definitely lost: 549,303 bytes in 60,765 blocks.\n==22732==    indirectly lost: 129,896 bytes in 133 blocks.\n==22732==      possibly lost: 378,414 bytes in 944 blocks.\n==22732==    still reachable: 57,759,394 bytes in 839,604 blocks.\n==22732==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/865\n\n",
    "created_at": "2007-10-12T19:49:32Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "several small memory leak in multi_modular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/865",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Hello,
Running

```
get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache(); get_memory_usage()
```

leads to

```
==11888== 120 bytes in 15 blocks are definitely lost in loss record 364 of 2,467
==11888==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==11888==    by 0x6108E17: __gmpz_init_set_ui (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==11888==    by 0x11D57FD4: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2398)
==11888==    by 0x11D538C0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5940)
==11888==    by 0x459172: type_call (typeobject.c:422)
==11888==    by 0x415522: PyObject_Call (abstract.c:1860)
==11888==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==11888==    by 0x126DE8DA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de
nse.c:7711)
==11888==    by 0x415522: PyObject_Call (abstract.c:1860)
==11888==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==11888==    by 0x126B66BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege
r_dense.c:5669)
==11888==    by 0x17AFCD27: __pyx_f_6action_18MatrixMatrixAction__call_c_impl (action.c:1270)

==19224== 24 bytes in 3 blocks are definitely lost in loss record 134 of 2,477
==19224==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==19224==    by 0x6107C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==19224==    by 0x11D58001: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2425)
==19224==    by 0x11D538C0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5949)
==19224==    by 0x459172: type_call (typeobject.c:422)
==19224==    by 0x415522: PyObject_Call (abstract.c:1860)
==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==19224==    by 0x126DE8DA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de
nse.c:7711)
==19224==    by 0x415522: PyObject_Call (abstract.c:1860)
==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==19224==    by 0x126B66BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege
r_dense.c:5669)
==19224==    by 0x9340519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)

==19224== 24 bytes in 3 blocks are definitely lost in loss record 135 of 2,477
==19224==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==19224==    by 0x6107C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==19224==    by 0x11D57FF8: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2416)
==19224==    by 0x11D538C0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5949)
==19224==    by 0x459172: type_call (typeobject.c:422)
==19224==    by 0x415522: PyObject_Call (abstract.c:1860)
==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==19224==    by 0x126DE8DA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de
nse.c:7711)
==19224==    by 0x415522: PyObject_Call (abstract.c:1860)
==19224==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==19224==    by 0x126B66BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege
r_dense.c:5669)
==19224==    by 0x9340519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)
```

before patch:

```
==11888== LEAK SUMMARY:
==11888==    definitely lost: 549,575 bytes in 60,799 blocks.
==11888==    indirectly lost: 129,896 bytes in 133 blocks.
==11888==      possibly lost: 377,982 bytes in 943 blocks.
==11888==    still reachable: 57,758,573 bytes in 839,594 blocks.
==11888==         suppressed: 0 bytes in 0 blocks.
```

after patch:

```
==22732==    definitely lost: 549,303 bytes in 60,765 blocks.
==22732==    indirectly lost: 129,896 bytes in 133 blocks.
==22732==      possibly lost: 378,414 bytes in 944 blocks.
==22732==    still reachable: 57,759,394 bytes in 839,604 blocks.
==22732==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/865





---

archive/issue_comments_005346.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-12T19:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/865#issuecomment-5346",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005347.json:
```json
{
    "body": "Attachment [Sage-2.8.6-fix-memleak-in-multi_modular.patch](tarball://root/attachments/some-uuid/ticket865/Sage-2.8.6-fix-memleak-in-multi_modular.patch) by mabshoff created at 2007-10-12 19:50:46",
    "created_at": "2007-10-12T19:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/865#issuecomment-5347",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.6-fix-memleak-in-multi_modular.patch](tarball://root/attachments/some-uuid/ticket865/Sage-2.8.6-fix-memleak-in-multi_modular.patch) by mabshoff created at 2007-10-12 19:50:46



---

archive/issue_comments_005348.json:
```json
{
    "body": "Attachment [Sage-2.8.6-fix-memleak-in-multi_modular.2.patch](tarball://root/attachments/some-uuid/ticket865/Sage-2.8.6-fix-memleak-in-multi_modular.2.patch) by mabshoff created at 2007-10-12 21:20:41\n\nOops, sorry for patch #2, it is identical to the previous one. I did a reload on a tab I wanted to close.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-12T21:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/865#issuecomment-5348",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.6-fix-memleak-in-multi_modular.2.patch](tarball://root/attachments/some-uuid/ticket865/Sage-2.8.6-fix-memleak-in-multi_modular.2.patch) by mabshoff created at 2007-10-12 21:20:41

Oops, sorry for patch #2, it is identical to the previous one. I did a reload on a tab I wanted to close.

Cheers,

Michael



---

archive/issue_comments_005349.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T08:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/865#issuecomment-5349",
    "user": "@williamstein"
}
```

Resolution: fixed
