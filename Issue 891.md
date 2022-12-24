# Issue 891: [with patch] symmetrica needs to have its deallocation routine called upon exit

archive/issues_000891.json:
```json
{
    "body": "Assignee: mhansen\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/891\n\n",
    "created_at": "2007-10-13T20:44:34Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] symmetrica needs to have its deallocation routine called upon exit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/891",
    "user": "mhansen"
}
```
Assignee: mhansen



Issue created by migration from https://trac.sagemath.org/ticket/891





---

archive/issue_comments_005494.json:
```json
{
    "body": "Attachment [6720.patch](tarball://root/attachments/some-uuid/ticket891/6720.patch) by mabshoff created at 2007-10-13 20:51:04\n\nHere are some statistics: The really big one is\n\n```\n==26643== 80,000 bytes in 1 blocks are still reachable in loss record 1,797 of 1,866\n==26643==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==26643==    by 0xDFD414A: SYM_malloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/build/sage/libs/symmetrica/sy\nmmetrica.so)\n==26643==    by 0xDFD4219: anfang (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/build/sage/libs/symmetrica/symmet\nrica.so)\n==26643==    by 0xDFAF13A: __pyx_f_py_10symmetrica_start (symmetrica.c:6089)\n==26643==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)\n==26643==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==26643==    by 0x4851D1: PyEval_EvalCode (ceval.c:494)\n==26643==    by 0x49B4FE: PyImport_ExecCodeModuleEx (import.c:669)\n==26643==    by 0x49BE0F: load_source_module (import.c:953)\n==26643==    by 0x49C45D: import_submodule (import.c:2394)\n==26643==    by 0x49C920: load_next (import.c:2214)\n==26643==    by 0x49CB7D: import_module_level (import.c:2002)\n```\n\nBut there are a bunch of smaller issues (mostly 8, 16 or 32 bytes)\n\nWithout the patch:\n\n```\n==26643== LEAK SUMMARY:\n==26643==    definitely lost: 0 bytes in 0 blocks.\n==26643==      possibly lost: 198,182 bytes in 521 blocks.\n==26643==    still reachable: 34,535,836 bytes in 16,831 blocks.\n==26643==         suppressed: 0 bytes in 0 blocks.\n```\n\nWith the patch:\n\n```\n==26449== LEAK SUMMARY:\n==26449==    definitely lost: 0 bytes in 0 blocks.\n==26449==      possibly lost: 198,654 bytes in 522 blocks.\n==26449==    still reachable: 34,454,092 bytes in 16,785 blocks.\n==26449==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nEvery byte counts!\n\nCheers,\n\nMichael",
    "created_at": "2007-10-13T20:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/891#issuecomment-5494",
    "user": "mabshoff"
}
```

Attachment [6720.patch](tarball://root/attachments/some-uuid/ticket891/6720.patch) by mabshoff created at 2007-10-13 20:51:04

Here are some statistics: The really big one is

```
==26643== 80,000 bytes in 1 blocks are still reachable in loss record 1,797 of 1,866
==26643==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==26643==    by 0xDFD414A: SYM_malloc (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/build/sage/libs/symmetrica/sy
mmetrica.so)
==26643==    by 0xDFD4219: anfang (in /tmp/Work-mabshoff/sage-2.8.7-alpha0/devel/sage-main/build/sage/libs/symmetrica/symmet
rica.so)
==26643==    by 0xDFAF13A: __pyx_f_py_10symmetrica_start (symmetrica.c:6089)
==26643==    by 0x482FE8: PyEval_EvalFrameEx (ceval.c:3548)
==26643==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==26643==    by 0x4851D1: PyEval_EvalCode (ceval.c:494)
==26643==    by 0x49B4FE: PyImport_ExecCodeModuleEx (import.c:669)
==26643==    by 0x49BE0F: load_source_module (import.c:953)
==26643==    by 0x49C45D: import_submodule (import.c:2394)
==26643==    by 0x49C920: load_next (import.c:2214)
==26643==    by 0x49CB7D: import_module_level (import.c:2002)
```

But there are a bunch of smaller issues (mostly 8, 16 or 32 bytes)

Without the patch:

```
==26643== LEAK SUMMARY:
==26643==    definitely lost: 0 bytes in 0 blocks.
==26643==      possibly lost: 198,182 bytes in 521 blocks.
==26643==    still reachable: 34,535,836 bytes in 16,831 blocks.
==26643==         suppressed: 0 bytes in 0 blocks.
```

With the patch:

```
==26449== LEAK SUMMARY:
==26449==    definitely lost: 0 bytes in 0 blocks.
==26449==      possibly lost: 198,654 bytes in 522 blocks.
==26449==    still reachable: 34,454,092 bytes in 16,785 blocks.
==26449==         suppressed: 0 bytes in 0 blocks.
```


Every byte counts!

Cheers,

Michael



---

archive/issue_comments_005495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T05:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/891#issuecomment-5495",
    "user": "was"
}
```

Resolution: fixed
