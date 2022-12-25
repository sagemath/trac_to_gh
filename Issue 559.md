# Issue 559: memleak in multi_modular_MultiModularBasis_base exposed by ModularSymbols(n,sign=1).decomposition()

archive/issues_000559.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello folks,\n\n```\nfor n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\ncauses (among other things) the following:\n\n```\n==5107== 1,056 bytes in 132 blocks are definitely lost in loss record 2,208 of 2,944\n==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==5107==    by 0x1F4BD6EF: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2324)\n==5107==    by 0x1F4B92A0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5836)\n==5107==    by 0x45A272: type_call (typeobject.c:422)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den\nse.c:7503)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x204237E0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_integer\n_dense.c:5487)\n==5107==    by 0xDFD6878: __pyx_f_7element_6Matrix__matrix_times_matrix_c (element.c:11483)\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/559\n\n",
    "created_at": "2007-09-02T00:14:35Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "memleak in multi_modular_MultiModularBasis_base exposed by ModularSymbols(n,sign=1).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 1,056 bytes in 132 blocks are definitely lost in loss record 2,208 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x1F4BD6EF: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2324)
==5107==    by 0x1F4B92A0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5836)
==5107==    by 0x45A272: type_call (typeobject.c:422)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den
se.c:7503)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x204237E0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_integer
_dense.c:5487)
==5107==    by 0xDFD6878: __pyx_f_7element_6Matrix__matrix_times_matrix_c (element.c:11483)
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/559





---

archive/issue_comments_002880.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/559#issuecomment-2880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_001489.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-07T04:46:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/559#event-1489"
}
```



---

archive/issue_comments_002881.json:
```json
{
    "body": "Attachment [multi_modular_memleak.patch](tarball://root/attachments/some-uuid/ticket559/multi_modular_memleak.patch) by @burcin created at 2007-09-21 01:07:08",
    "created_at": "2007-09-21T01:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/559#issuecomment-2881",
    "user": "https://github.com/burcin"
}
```

Attachment [multi_modular_memleak.patch](tarball://root/attachments/some-uuid/ticket559/multi_modular_memleak.patch) by @burcin created at 2007-09-21 01:07:08



---

archive/issue_comments_002882.json:
```json
{
    "body": "The following code causes similar errors:\n\n\n```\nA = random_matrix(ZZ, 100, 200, density=.001)\nB = random_matrix(ZZ, 200, 100, density=.001)\nC = A*B\ndel A, B, C\n```\n\n\nThe first chunk of the attached fixes these. The second chunk is useful for #561.\n\nUnfortunately, this isn't enough to reduce all the noise MultiModularBasis makes while running\n\n\n```\nm = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache();\n```\n",
    "created_at": "2007-09-21T01:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/559#issuecomment-2882",
    "user": "https://github.com/burcin"
}
```

The following code causes similar errors:


```
A = random_matrix(ZZ, 100, 200, density=.001)
B = random_matrix(ZZ, 200, 100, density=.001)
C = A*B
del A, B, C
```


The first chunk of the attached fixes these. The second chunk is useful for #561.

Unfortunately, this isn't enough to reduce all the noise MultiModularBasis makes while running


```
m = ModularSymbols(501,2).decomposition(3); del m; ModularSymbols_clear_cache();
```




---

archive/issue_events_001490.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-14T23:02:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/559#event-1490"
}
```



---

archive/issue_events_001491.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-14T23:02:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/559#event-1491"
}
```



---

archive/issue_comments_002883.json:
```json
{
    "body": "Patch will be submitted by me as a mercurial patch.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-14T23:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/559#issuecomment-2883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch will be submitted by me as a mercurial patch.

Cheers,

Michael



---

archive/issue_events_001492.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-15T02:21:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/559#event-1492"
}
```



---

archive/issue_comments_002884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-15T02:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/559#issuecomment-2884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002885.json:
```json
{
    "body": "As it turns out the part of the patch the fixed this ticket was wrong and coincidentally I already fixed this with another patch. The part of the patch that fixes #561 is valid. I will post that patch with credit to burcin there.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-15T02:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/559#issuecomment-2885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

As it turns out the part of the patch the fixed this ticket was wrong and coincidentally I already fixed this with another patch. The part of the patch that fixes #561 is valid. I will post that patch with credit to burcin there.

Cheers,

Michael



---

archive/issue_events_001493.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-15T02:21:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/559#event-1493"
}
```



---

archive/issue_events_001494.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-15T02:21:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/559",
    "milestone": "sage-2.8.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/559#event-1494"
}
```
