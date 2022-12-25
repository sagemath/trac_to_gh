# Issue 564: memleak in matrix_integer_sparse_allocate_mpz_vector exposed by ModularSymbols(n,sign=1).decomposition()

archive/issues_000564.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello folks,\n\n```\nfor n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\ncauses (among other things) the following:\n\n```\n==5107== 90,320 bytes in 11,290 blocks are definitely lost in loss record 2,811 of 2,944\n==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==5107==    by 0x20A67143: __pyx_f_21matrix_integer_sparse_allocate_mpz_vector (matrix_integer_sparse.c:1202)\n==5107==    by 0x20A684BF: __pyx_f_21matrix_integer_sparse_add_mpz_vector_init (matrix_integer_sparse.c:1315)\n==5107==    by 0x20A6D054: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__add_c_impl (matrix_integer_sparse.c:6549\n)\n==5107==    by 0xDFE08FD: __pyx_f_7element_13ModuleElement__add_c (element.c:3986)\n==5107==    by 0xDFCF2E8: __pyx_f_7element_13ModuleElement___add__ (element.c:3888)\n==5107==    by 0x41596C: binary_op1 (abstract.c:398)\n==5107==    by 0x416ADB: PyNumber_InPlaceAdd (abstract.c:744)\n==5107==    by 0x27D10EBA: __pyx_f_4misc_matrix_rational_echelon_form_multimodular (misc.c:12816)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n\n```\n\nCheers,\n\nTagged for 2.8.4\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/564\n\n",
    "created_at": "2007-09-02T00:21:14Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "memleak in matrix_integer_sparse_allocate_mpz_vector exposed by ModularSymbols(n,sign=1).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/564",
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
==5107== 90,320 bytes in 11,290 blocks are definitely lost in loss record 2,811 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x20A67143: __pyx_f_21matrix_integer_sparse_allocate_mpz_vector (matrix_integer_sparse.c:1202)
==5107==    by 0x20A684BF: __pyx_f_21matrix_integer_sparse_add_mpz_vector_init (matrix_integer_sparse.c:1315)
==5107==    by 0x20A6D054: __pyx_f_21matrix_integer_sparse_21Matrix_integer_sparse__add_c_impl (matrix_integer_sparse.c:6549
)
==5107==    by 0xDFE08FD: __pyx_f_7element_13ModuleElement__add_c (element.c:3986)
==5107==    by 0xDFCF2E8: __pyx_f_7element_13ModuleElement___add__ (element.c:3888)
==5107==    by 0x41596C: binary_op1 (abstract.c:398)
==5107==    by 0x416ADB: PyNumber_InPlaceAdd (abstract.c:744)
==5107==    by 0x27D10EBA: __pyx_f_4misc_matrix_rational_echelon_form_multimodular (misc.c:12816)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)

```

Cheers,

Tagged for 2.8.4

Michael

Issue created by migration from https://trac.sagemath.org/ticket/564





---

archive/issue_comments_002908.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/564#issuecomment-2908",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002909.json:
```json
{
    "body": "Attachment [6081.patch](tarball://root/attachments/some-uuid/ticket564/6081.patch) by @williamstein created at 2007-09-03 15:19:43\n\nThis fixes the memleak in + or - for sparse matrix arithmetic.",
    "created_at": "2007-09-03T15:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/564#issuecomment-2909",
    "user": "https://github.com/williamstein"
}
```

Attachment [6081.patch](tarball://root/attachments/some-uuid/ticket564/6081.patch) by @williamstein created at 2007-09-03 15:19:43

This fixes the memleak in + or - for sparse matrix arithmetic.



---

archive/issue_comments_002910.json:
```json
{
    "body": "\n```\n[17:17] <mabshoff> I am running the above with range(10,30) to save some time.\n[17:22] <mabshoff> It works:\n[17:22] <mabshoff> Without the patch:\n[17:22] <mabshoff> ==8165== LEAK SUMMARY:\n[17:22] <mabshoff> ==8165==    definitely lost: 144,790 bytes in 12,251 blocks.\n[17:22] <mabshoff> ==8165==    indirectly lost: 22,800 bytes in 532 blocks.\n[17:22] <mabshoff> ==8165==      possibly lost: 392,214 bytes in 1,010 blocks.\n[17:22] <mabshoff> With the patch:\n[17:22] <mabshoff> ==8132== LEAK SUMMARY:\n[17:22] <mabshoff> ==8132==    definitely lost: 141,107 bytes in 11,827 blocks.\n[17:22] <mabshoff> ==8132==    indirectly lost: 22,155 bytes in 531 blocks.\n[17:22] <mabshoff> ==8132==      possibly lost: 392,982 bytes in 1,012 blocks.\n```\n\nThis ticket should be closed.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T15:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/564#issuecomment-2910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[17:17] <mabshoff> I am running the above with range(10,30) to save some time.
[17:22] <mabshoff> It works:
[17:22] <mabshoff> Without the patch:
[17:22] <mabshoff> ==8165== LEAK SUMMARY:
[17:22] <mabshoff> ==8165==    definitely lost: 144,790 bytes in 12,251 blocks.
[17:22] <mabshoff> ==8165==    indirectly lost: 22,800 bytes in 532 blocks.
[17:22] <mabshoff> ==8165==      possibly lost: 392,214 bytes in 1,010 blocks.
[17:22] <mabshoff> With the patch:
[17:22] <mabshoff> ==8132== LEAK SUMMARY:
[17:22] <mabshoff> ==8132==    definitely lost: 141,107 bytes in 11,827 blocks.
[17:22] <mabshoff> ==8132==    indirectly lost: 22,155 bytes in 531 blocks.
[17:22] <mabshoff> ==8132==      possibly lost: 392,982 bytes in 1,012 blocks.
```

This ticket should be closed.

Cheers,

Michael



---

archive/issue_events_000610.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-03T17:27:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/564#event-610"
}
```



---

archive/issue_comments_002911.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-03T17:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/564#issuecomment-2911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002912.json:
```json
{
    "body": "There is another smaller issue left in add_mpz_vector_init and once we find a proper testcase we will open another ticket for it.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T17:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/564#issuecomment-2912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There is another smaller issue left in add_mpz_vector_init and once we find a proper testcase we will open another ticket for it.

Cheers,

Michael



---

archive/issue_comments_002913.json:
```json
{
    "body": "#533 seems related to this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T20:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/564#issuecomment-2913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#533 seems related to this ticket.

Cheers,

Michael
