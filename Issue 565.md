# Issue 565: memleak in matrix_rational_sparse_allocate_mpq_vector exposed by ModularSymbols(n,sign=1).decomposition()

archive/issues_000565.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello folks,\n\n```\nfor n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\ncauses (among other things) the following:\n\n```\n==5107== 4,536,112 bytes in 567,014 blocks are definitely lost in loss record 2,943 of 2,944\n==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==5107==    by 0x94AD2C1: __gmpq_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==5107==    by 0x210C44C3: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5358)\n==5107==    by 0x210C6041: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6542)\n==5107==    by 0x210C6367: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:84\n63)\n==5107==    by 0x1E21D176: __pyx_mp_ass_subscript_7matrix0_Matrix (matrix0.c:2277)\n==5107==    by 0x480E96: PyEval_EvalFrameEx (ceval.c:1497)\n==5107==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)\n==5107==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)\n==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)\n==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)\n==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)\n```\n\nCheers,\n\nTagged for 2.8.4\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/565\n\n",
    "created_at": "2007-09-02T00:22:06Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "memleak in matrix_rational_sparse_allocate_mpq_vector exposed by ModularSymbols(n,sign=1).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/565",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 4,536,112 bytes in 567,014 blocks are definitely lost in loss record 2,943 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94AD2C1: __gmpq_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x210C44C3: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5358)
==5107==    by 0x210C6041: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6542)
==5107==    by 0x210C6367: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:84
63)
==5107==    by 0x1E21D176: __pyx_mp_ass_subscript_7matrix0_Matrix (matrix0.c:2277)
==5107==    by 0x480E96: PyEval_EvalFrameEx (ceval.c:1497)
==5107==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==5107==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
==5107==    by 0x485025: PyEval_EvalFrameEx (ceval.c:3650)
```

Cheers,

Tagged for 2.8.4

Michael

Issue created by migration from https://trac.sagemath.org/ticket/565





---

archive/issue_comments_002926.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/565#issuecomment-2926",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002927.json:
```json
{
    "body": "Attachment\n\nthis patch fixes a memleak when setting an entry to 0 in a sparse vector",
    "created_at": "2007-09-03T15:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/565#issuecomment-2927",
    "user": "was"
}
```

Attachment

this patch fixes a memleak when setting an entry to 0 in a sparse vector



---

archive/issue_comments_002928.json:
```json
{
    "body": "This is a pretty shocking before and after example!\n\nBEFORE\n\n```\nage: get_memory_usage()\n372.22265625\nsage: m = random_matrix(ZZ, 300, sparse=True)\nsage: get_memory_usage()\n376.92578125\nsage: for i in range(300):\n....:     for j in range(300):\n....:         m[i,j] = 0\n....:\n\nsage: get_memory_usage()\n786.4765625\n```\n\n\n\nA 300 MB memleak!!!\n\nAFTER:\n\n\n```\nsage: get_memory_usage()\n372.23046875\nsage: m = random_matrix(ZZ, 300, sparse=True)\nsage: get_memory_usage()\n376.921875\nsage: for i in range(300):\n....:     for j in range(300):\n....:         m[i,j] = 0\n....:\nsage: get_memory_usage()\n376.921875\n```\n",
    "created_at": "2007-09-03T15:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/565#issuecomment-2928",
    "user": "was"
}
```

This is a pretty shocking before and after example!

BEFORE

```
age: get_memory_usage()
372.22265625
sage: m = random_matrix(ZZ, 300, sparse=True)
sage: get_memory_usage()
376.92578125
sage: for i in range(300):
....:     for j in range(300):
....:         m[i,j] = 0
....:

sage: get_memory_usage()
786.4765625
```



A 300 MB memleak!!!

AFTER:


```
sage: get_memory_usage()
372.23046875
sage: m = random_matrix(ZZ, 300, sparse=True)
sage: get_memory_usage()
376.921875
sage: for i in range(300):
....:     for j in range(300):
....:         m[i,j] = 0
....:
sage: get_memory_usage()
376.921875
```




---

archive/issue_comments_002929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-03T17:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/565#issuecomment-2929",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002930.json:
```json
{
    "body": "William has fixed the huge memleak mentioned above. The patch has also been pushed out to the public repo.\n\nThere is another smaller issue left in add_mpz_vector_init and once we find a proper testcase we will open another ticket for it.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T17:28:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/565#issuecomment-2930",
    "user": "mabshoff"
}
```

William has fixed the huge memleak mentioned above. The patch has also been pushed out to the public repo.

There is another smaller issue left in add_mpz_vector_init and once we find a proper testcase we will open another ticket for it.

Cheers,

Michael



---

archive/issue_comments_002931.json:
```json
{
    "body": "#533 seems related to this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T20:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/565#issuecomment-2931",
    "user": "mabshoff"
}
```

#533 seems related to this ticket.

Cheers,

Michael
