# Issue 3908: [with patch, needs review] fix major memory leak in fast_float

archive/issues_003908.json:
```json
{
    "body": "Assignee: jkantor\n\nCurrently there is a major memory leak in fast_float because it uses `__del__` instead of `__dealloc__`.  (Python uses `__del__`, Cython uses `__dealloc__`.)\n\nBefore:\n\n```\nsage: from sage.ext.fast_eval import fast_float_constant\nsage: get_memory_usage()\n117.859375\nsage: print sum([fast_float_constant(3.0)] * 2000)\n<sage.ext.fast_eval.FastDoubleFunc object at 0xb7ab4b54>\nsage: get_memory_usage()\n163.6328125\n```\n\n\nAfter:\n\n```\nsage: from sage.ext.fast_eval import fast_float_constant\nsage: get_memory_usage()\n117.859375\nsage: print sum([fast_float_constant(3.0)] * 2000)\n<sage.ext.fast_eval.FastDoubleFunc object at 0xb7b18b54>\nsage: get_memory_usage()\n117.98828125\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3908\n\n",
    "created_at": "2008-08-20T02:57:54Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] fix major memory leak in fast_float",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3908",
    "user": "cwitty"
}
```
Assignee: jkantor

Currently there is a major memory leak in fast_float because it uses `__del__` instead of `__dealloc__`.  (Python uses `__del__`, Cython uses `__dealloc__`.)

Before:

```
sage: from sage.ext.fast_eval import fast_float_constant
sage: get_memory_usage()
117.859375
sage: print sum([fast_float_constant(3.0)] * 2000)
<sage.ext.fast_eval.FastDoubleFunc object at 0xb7ab4b54>
sage: get_memory_usage()
163.6328125
```


After:

```
sage: from sage.ext.fast_eval import fast_float_constant
sage: get_memory_usage()
117.859375
sage: print sum([fast_float_constant(3.0)] * 2000)
<sage.ext.fast_eval.FastDoubleFunc object at 0xb7b18b54>
sage: get_memory_usage()
117.98828125
```



Issue created by migration from https://trac.sagemath.org/ticket/3908





---

archive/issue_comments_027958.json:
```json
{
    "body": "Attachment [trac3908-fast_float-memleak.patch](tarball://root/attachments/some-uuid/ticket3908/trac3908-fast_float-memleak.patch) by cwitty created at 2008-08-20 02:58:54",
    "created_at": "2008-08-20T02:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3908#issuecomment-27958",
    "user": "cwitty"
}
```

Attachment [trac3908-fast_float-memleak.patch](tarball://root/attachments/some-uuid/ticket3908/trac3908-fast_float-memleak.patch) by cwitty created at 2008-08-20 02:58:54



---

archive/issue_comments_027959.json:
```json
{
    "body": "This patch actually makes it worse: Before:\n\n```\n==12210== LEAK SUMMARY:\n==12210==    definitely lost: 152,380 bytes in 5,433 blocks.\n==12210==      possibly lost: 338,476 bytes in 965 blocks.\n==12210==    still reachable: 34,336,340 bytes in 211,430 blocks.\n==12210==         suppressed: 300,797 bytes in 4,764 blocks.\n```\n\nAfter:\n\n```\n==25373== LEAK SUMMARY:\n==25373==    definitely lost: 311,287 bytes in 5,364 blocks.\n==25373==      possibly lost: 338,986 bytes in 969 blocks.\n==25373==    still reachable: 34,331,200 bytes in 211,437 blocks.\n==25373==         suppressed: 0 bytes in 0 blocks.\n==25373== Rerun with --leak-check=full to see details of leaked memory.\n```\n\n\n:(\n\nCheers,\n\nMichael",
    "created_at": "2008-08-20T18:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3908#issuecomment-27959",
    "user": "mabshoff"
}
```

This patch actually makes it worse: Before:

```
==12210== LEAK SUMMARY:
==12210==    definitely lost: 152,380 bytes in 5,433 blocks.
==12210==      possibly lost: 338,476 bytes in 965 blocks.
==12210==    still reachable: 34,336,340 bytes in 211,430 blocks.
==12210==         suppressed: 300,797 bytes in 4,764 blocks.
```

After:

```
==25373== LEAK SUMMARY:
==25373==    definitely lost: 311,287 bytes in 5,364 blocks.
==25373==      possibly lost: 338,986 bytes in 969 blocks.
==25373==    still reachable: 34,331,200 bytes in 211,437 blocks.
==25373==         suppressed: 0 bytes in 0 blocks.
==25373== Rerun with --leak-check=full to see details of leaked memory.
```


:(

Cheers,

Michael



---

archive/issue_comments_027960.json:
```json
{
    "body": "Mmmh, it seems that having suppression enabled only works with --leak-check=full, so I need to investigate here.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-20T18:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3908#issuecomment-27960",
    "user": "mabshoff"
}
```

Mmmh, it seems that having suppression enabled only works with --leak-check=full, so I need to investigate here.

Cheers,

Michael



---

archive/issue_comments_027961.json:
```json
{
    "body": "Positive review. It does not fix all the issue, but it reduces the problem significantly:\n\n```\n==12941== LEAK SUMMARY:\n==12941==    definitely lost: 7,300 bytes in 600 blocks.\n==12941==    indirectly lost: 3,483 bytes in 5 blocks.\n==12941==      possibly lost: 338,598 bytes in 964 blocks.\n==12941==    still reachable: 34,339,261 bytes in 211,436 blocks.\n==12941==         suppressed: 300,797 bytes in 4,764 blocks.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-08-20T19:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3908#issuecomment-27961",
    "user": "mabshoff"
}
```

Positive review. It does not fix all the issue, but it reduces the problem significantly:

```
==12941== LEAK SUMMARY:
==12941==    definitely lost: 7,300 bytes in 600 blocks.
==12941==    indirectly lost: 3,483 bytes in 5 blocks.
==12941==      possibly lost: 338,598 bytes in 964 blocks.
==12941==    still reachable: 34,339,261 bytes in 211,436 blocks.
==12941==         suppressed: 300,797 bytes in 4,764 blocks.
```


Cheers,

Michael



---

archive/issue_comments_027962.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-21T18:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3908#issuecomment-27962",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027963.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-21T18:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3908#issuecomment-27963",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha0
