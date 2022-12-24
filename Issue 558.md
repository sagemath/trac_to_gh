# Issue 558: memleak in integer_fast_tp_dealloc exposed by ModularSymbols(n,sign=1).decomposition()

archive/issues_000558.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello folks,\n\n```\nfor n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\ncauses (among other things) the following:\n\n```\n==5107== 1,024 bytes in 128 blocks are definitely lost in loss record 2,196 of 2,944\n==5107==    at 0x4A0590B: realloc (vg_replace_malloc.c:306)\n==5107==    by 0x94A8760: __gmpz_realloc (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==5107==    by 0x1678B012: __pyx_f_7integer_fast_tp_dealloc (integer.c:14595)\n==5107==    by 0x1F4BD7B2: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2222)\n==5107==    by 0x1F4B92A0: __pyx_tp_new_13multi_modular_MultiModularBasis (multi_modular.c:5836)\n==5107==    by 0x45A272: type_call (typeobject.c:422)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den\nse.c:7503)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x204237E0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_integer\n_dense.c:5487)\n```\n\nCheers,\n\nTagged for 2.8.4\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/558\n\n",
    "created_at": "2007-09-02T00:11:40Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "memleak in integer_fast_tp_dealloc exposed by ModularSymbols(n,sign=1).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/558",
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
==5107== 1,024 bytes in 128 blocks are definitely lost in loss record 2,196 of 2,944
==5107==    at 0x4A0590B: realloc (vg_replace_malloc.c:306)
==5107==    by 0x94A8760: __gmpz_realloc (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x1678B012: __pyx_f_7integer_fast_tp_dealloc (integer.c:14595)
==5107==    by 0x1F4BD7B2: __pyx_tp_new_13multi_modular_MultiModularBasis_base (multi_modular.c:2222)
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
```

Cheers,

Tagged for 2.8.4

Michael

Issue created by migration from https://trac.sagemath.org/ticket/558





---

archive/issue_comments_002881.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2881",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002882.json:
```json
{
    "body": "Some progress with the attached patch:\n\n\n```\nsage: d = [ZZ(i**100000 + 1) for i in range(100)]; del d\nsage: get_memory_usage()\n577.11328125\nsage: sage.rings.integer.free_integer_pool()\nsage: get_memory_usage()\n570.2421875\n```\n\n\nbut if the integers are smaller nothing seems to change\n\n\n```\nsage: d = [ZZ(i**10000 + 1) for i in range(100)]; del d\nsage: get_memory_usage()\n571.078125\nsage: sage.rings.integer.free_integer_pool()\nsage: get_memory_usage()\n571.078125\n```\n\n\nfree_integer_pool() is also called on exit() if the attached patch is applied.",
    "created_at": "2007-09-06T18:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2882",
    "user": "@malb"
}
```

Some progress with the attached patch:


```
sage: d = [ZZ(i**100000 + 1) for i in range(100)]; del d
sage: get_memory_usage()
577.11328125
sage: sage.rings.integer.free_integer_pool()
sage: get_memory_usage()
570.2421875
```


but if the integers are smaller nothing seems to change


```
sage: d = [ZZ(i**10000 + 1) for i in range(100)]; del d
sage: get_memory_usage()
571.078125
sage: sage.rings.integer.free_integer_pool()
sage: get_memory_usage()
571.078125
```


free_integer_pool() is also called on exit() if the attached patch is applied.



---

archive/issue_comments_002883.json:
```json
{
    "body": "Attachment [6169.patch](tarball://root/attachments/some-uuid/ticket558/6169.patch) by @malb created at 2007-09-06 18:26:40\n\nwork in progress for freeing the integer pool on exit",
    "created_at": "2007-09-06T18:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2883",
    "user": "@malb"
}
```

Attachment [6169.patch](tarball://root/attachments/some-uuid/ticket558/6169.patch) by @malb created at 2007-09-06 18:26:40

work in progress for freeing the integer pool on exit



---

archive/issue_comments_002884.json:
```json
{
    "body": "Attachment [6170.patch](tarball://root/attachments/some-uuid/ticket558/6170.patch) by @malb created at 2007-09-06 18:48:44\n\nPatch 6170.patch makes sure no new elements are added tot he pool once its free'd.",
    "created_at": "2007-09-06T18:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2884",
    "user": "@malb"
}
```

Attachment [6170.patch](tarball://root/attachments/some-uuid/ticket558/6170.patch) by @malb created at 2007-09-06 18:48:44

Patch 6170.patch makes sure no new elements are added tot he pool once its free'd.



---

archive/issue_comments_002885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T03:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2885",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_002886.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-07T03:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2886",
    "user": "@williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002887.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-07T03:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2887",
    "user": "@williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002888.json:
```json
{
    "body": "This patch seriously breaks SAGE.  Try \n\n```\n    sage -t --verbose coding/linear_code.py\n```\n\non exit SAGE hangs with\n\n\n```\n*** glibc detected *** /home/was/s/local/bin/python: double free or corruption (out): 0x0000000002b75f70 ***\n```\n\n\nIn the official version of SAGE, I'm commenting out the line in all.py that calls the cleanup until\nthis gets fixed.   Note that all the code mentioned above is in the offical repo, but calling\nit is commented out.",
    "created_at": "2007-09-07T03:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2888",
    "user": "@williamstein"
}
```

This patch seriously breaks SAGE.  Try 

```
    sage -t --verbose coding/linear_code.py
```

on exit SAGE hangs with


```
*** glibc detected *** /home/was/s/local/bin/python: double free or corruption (out): 0x0000000002b75f70 ***
```


In the official version of SAGE, I'm commenting out the line in all.py that calls the cleanup until
this gets fixed.   Note that all the code mentioned above is in the offical repo, but calling
it is commented out.



---

archive/issue_comments_002889.json:
```json
{
    "body": "The version I got via `hg_sage.pull()` commented out `clear_mpz_globals()` and not `free_integer_pool()`. `clear_mpz_globals()` is not related (more carefully: should not be related) to this ticket. Also, I ran `make test` and did not run ito the `double free` situation on my 64-bit Core2Duo Linux at least. I'll attach a tiny patch to re-enable `clear_mpz_globals()` on exit.",
    "created_at": "2007-09-07T11:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2889",
    "user": "@malb"
}
```

The version I got via `hg_sage.pull()` commented out `clear_mpz_globals()` and not `free_integer_pool()`. `clear_mpz_globals()` is not related (more carefully: should not be related) to this ticket. Also, I ran `make test` and did not run ito the `double free` situation on my 64-bit Core2Duo Linux at least. I'll attach a tiny patch to re-enable `clear_mpz_globals()` on exit.



---

archive/issue_comments_002890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T11:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2890",
    "user": "@malb"
}
```

Resolution: fixed



---

archive/issue_comments_002891.json:
```json
{
    "body": "Attachment [6253.patch](tarball://root/attachments/some-uuid/ticket558/6253.patch) by @malb created at 2007-09-07 11:11:23",
    "created_at": "2007-09-07T11:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/558",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/558#issuecomment-2891",
    "user": "@malb"
}
```

Attachment [6253.patch](tarball://root/attachments/some-uuid/ticket558/6253.patch) by @malb created at 2007-09-07 11:11:23
