# Issue 621: memory still reachable in matrix_integer_dense_Matrix_integer_dense

archive/issues_000621.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is caused when running Sage 2.8.3.6+malb's fix for #566:\n\n```\nfor i in range(3):\n    get_memory_usage()\n    m = ModularSymbols(501,2).decomposition(3); \n    del m; ModularSymbols_clear_cache(); \n    get_memory_usage()\n```\n\nand results in \n\n```\n==8920== LEAK SUMMARY:\n==8920==    definitely lost: 1,518,830 bytes in 183,739 blocks.\n==8920==    indirectly lost: 288,408 bytes in 610 blocks.\n==8920==      possibly lost: 489,439 bytes in 1,002 blocks.\n==8920==    still reachable: 160,311,066 bytes in 872,845 blocks.\n==8920==         suppressed: 0 bytes in 0 blocks.\n```\n\nThe exact problem:\n\n```\n==8920== 2,603,712 bytes in 5 blocks are still reachable in loss record 2,370 of 2,372\n==8920==    at 0x4A05A66: malloc (vg_replace_malloc.c:207)\n==8920==    by 0x205E1766: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense___new__ (matrix_integer_dense.c:2966)\n==8920==    by 0x205E1BE0: __pyx_tp_new_20matrix_integer_dense_Matrix_integer_dense (matrix_integer_dense.c:17692)\n==8920==    by 0x45A272: type_call (typeobject.c:422)\n==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==8920==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)\n==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)\n==8920==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)\n==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)\n==8920==    by 0x4CFF37: function_call (funcobject.c:517)\n==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==8920==    by 0x41BE0C: instancemethod_call (classobject.c:2497)\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/621\n\n",
    "created_at": "2007-09-07T17:00:57Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "memory still reachable in matrix_integer_dense_Matrix_integer_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/621",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is caused when running Sage 2.8.3.6+malb's fix for #566:

```
for i in range(3):
    get_memory_usage()
    m = ModularSymbols(501,2).decomposition(3); 
    del m; ModularSymbols_clear_cache(); 
    get_memory_usage()
```

and results in 

```
==8920== LEAK SUMMARY:
==8920==    definitely lost: 1,518,830 bytes in 183,739 blocks.
==8920==    indirectly lost: 288,408 bytes in 610 blocks.
==8920==      possibly lost: 489,439 bytes in 1,002 blocks.
==8920==    still reachable: 160,311,066 bytes in 872,845 blocks.
==8920==         suppressed: 0 bytes in 0 blocks.
```

The exact problem:

```
==8920== 2,603,712 bytes in 5 blocks are still reachable in loss record 2,370 of 2,372
==8920==    at 0x4A05A66: malloc (vg_replace_malloc.c:207)
==8920==    by 0x205E1766: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense___new__ (matrix_integer_dense.c:2966)
==8920==    by 0x205E1BE0: __pyx_tp_new_20matrix_integer_dense_Matrix_integer_dense (matrix_integer_dense.c:17692)
==8920==    by 0x45A272: type_call (typeobject.c:422)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==8920==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==8920==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==8920==    by 0x4CFF37: function_call (funcobject.c:517)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==8920==    by 0x41BE0C: instancemethod_call (classobject.c:2497)
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/621





---

archive/issue_comments_003190.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-07T17:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3190",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003191.json:
```json
{
    "body": "The problem still exists with 2.8.6.2, but the amount of memory leak has been reduced:\n\n```\n==22180== LEAK SUMMARY:\n==22180==    definitely lost: 1,451,674 bytes in 182,329 blocks.\n==22180==    indirectly lost: 388,888 bytes in 398 blocks.\n==22180==      possibly lost: 358,750 bytes in 871 blocks.\n==22180==    still reachable: 71,069,104 bytes in 1,284,795 blocks.\n==22180==         suppressed: 0 bytes in 0 blocks.\n```\n\nCheers,\n\nM ichael",
    "created_at": "2007-10-21T04:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3191",
    "user": "mabshoff"
}
```

The problem still exists with 2.8.6.2, but the amount of memory leak has been reduced:

```
==22180== LEAK SUMMARY:
==22180==    definitely lost: 1,451,674 bytes in 182,329 blocks.
==22180==    indirectly lost: 388,888 bytes in 398 blocks.
==22180==      possibly lost: 358,750 bytes in 871 blocks.
==22180==    still reachable: 71,069,104 bytes in 1,284,795 blocks.
==22180==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

M ichael



---

archive/issue_comments_003192.json:
```json
{
    "body": "With 2.8.8 we finally get a large reduction to the definitely lost because there three memleak fixes finally went in:\n\n```\n==6590== LEAK SUMMARY:\n==6590==    definitely lost: 11,810 bytes in 372 blocks.\n==6590==    indirectly lost: 385,232 bytes in 380 blocks.\n==6590==      possibly lost: 362,078 bytes in 872 blocks.\n==6590==    still reachable: 70,576,384 bytes in 1,284,822 blocks.\n==6590==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T18:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3192",
    "user": "mabshoff"
}
```

With 2.8.8 we finally get a large reduction to the definitely lost because there three memleak fixes finally went in:

```
==6590== LEAK SUMMARY:
==6590==    definitely lost: 11,810 bytes in 372 blocks.
==6590==    indirectly lost: 385,232 bytes in 380 blocks.
==6590==      possibly lost: 362,078 bytes in 872 blocks.
==6590==    still reachable: 70,576,384 bytes in 1,284,822 blocks.
==6590==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael



---

archive/issue_comments_003193.json:
```json
{
    "body": "It looks like the ModularSymbols_clear_cache() does nothing:\n\n```\nmabshoff@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.11, Release Date: 2007-11-02                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: for i in range(3):\n....:         print \"start: \", get_memory_usage()\n....:     m = ModularSymbols(501,2).decomposition(3);\n....:     del m;\n....:     print \"deleted m: \", get_memory_usage()\n....:     ModularSymbols_clear_cache();\n....:     print \"cache cleaned: \", get_memory_usage()\n....:\nstart:  329.03515625\ndeleted m:  379.66015625\ncache cleaned:  379.66015625\nstart:  379.66015625\ndeleted m:  391.63671875\ncache cleaned:  391.63671875\nstart:  391.63671875\ndeleted m:  401.21484375\ncache cleaned:  401.21484375\n```\n\nI had a quick look at the code and we play with weak references there, so that might be the cause. Same applies to #620.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-03T14:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3193",
    "user": "mabshoff"
}
```

It looks like the ModularSymbols_clear_cache() does nothing:

```
mabshoff@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.11, Release Date: 2007-11-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: for i in range(3):
....:         print "start: ", get_memory_usage()
....:     m = ModularSymbols(501,2).decomposition(3);
....:     del m;
....:     print "deleted m: ", get_memory_usage()
....:     ModularSymbols_clear_cache();
....:     print "cache cleaned: ", get_memory_usage()
....:
start:  329.03515625
deleted m:  379.66015625
cache cleaned:  379.66015625
start:  379.66015625
deleted m:  391.63671875
cache cleaned:  391.63671875
start:  391.63671875
deleted m:  401.21484375
cache cleaned:  401.21484375
```

I had a quick look at the code and we play with weak references there, so that might be the cause. Same applies to #620.

Cheers,

Michael



---

archive/issue_comments_003194.json:
```json
{
    "body": "This is still there, but seems *so* similar to #620 that we should probably close this one.  Anyone interested in attacking them separately could still do so.",
    "created_at": "2013-06-12T21:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3194",
    "user": "@kcrisman"
}
```

This is still there, but seems *so* similar to #620 that we should probably close this one.  Anyone interested in attacking them separately could still do so.



---

archive/issue_comments_003195.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-12T21:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3195",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_003196.json:
```json
{
    "body": "Essentially a dup of #620 since the exact same code is causing the memleak in both of them.",
    "created_at": "2013-06-12T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3196",
    "user": "@kcrisman"
}
```

Essentially a dup of #620 since the exact same code is causing the memleak in both of them.



---

archive/issue_comments_003197.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-12T21:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3197",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_003198.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-06-19T12:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/621#issuecomment-3198",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
