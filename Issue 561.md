# Issue 561: memleak in MultiModularBasis_base__extend_moduli_to_height_c exposed by ModularSymbols(n,sign=1).decomposition()

archive/issues_000561.json:
```json
{
    "body": "Assignee: mabshoff\n\nHello folks,\n\n```\nfor n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()\n```\n\ncauses (among other things) the following:\n\n```\n==5107== 2,128 bytes in 133 blocks are definitely lost in loss record 2,338 of 2,944\n==5107==    at 0x4A0590B: realloc (vg_replace_malloc.c:306)\n==5107==    by 0x94A8760: __gmpz_realloc (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==5107==    by 0x94A55E8: __gmpz_mul_2exp (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==5107==    by 0x1F4BF558: __pyx_f_13multi_modular_22MultiModularBasis_base__extend_moduli_to_height_c (multi_modular.c:2760\n)\n==5107==    by 0x1F4BEA56: __pyx_f_13multi_modular_22MultiModularBasis_base__extend_moduli_to_height (multi_modular.c:2688)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x1F4BD032: __pyx_f_13multi_modular_22MultiModularBasis_base___init__ (multi_modular.c:2618)\n==5107==    by 0x45A321: type_call (typeobject.c:436)\n==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den\nse.c:7503)\n```\n\nCheers,\n\nTagged for 2.8.4\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/561\n\n",
    "created_at": "2007-09-02T00:18:20Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "memleak in MultiModularBasis_base__extend_moduli_to_height_c exposed by ModularSymbols(n,sign=1).decomposition()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/561",
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
==5107== 2,128 bytes in 133 blocks are definitely lost in loss record 2,338 of 2,944
==5107==    at 0x4A0590B: realloc (vg_replace_malloc.c:306)
==5107==    by 0x94A8760: __gmpz_realloc (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x94A55E8: __gmpz_mul_2exp (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x1F4BF558: __pyx_f_13multi_modular_22MultiModularBasis_base__extend_moduli_to_height_c (multi_modular.c:2760
)
==5107==    by 0x1F4BEA56: __pyx_f_13multi_modular_22MultiModularBasis_base__extend_moduli_to_height (multi_modular.c:2688)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x1F4BD032: __pyx_f_13multi_modular_22MultiModularBasis_base___init__ (multi_modular.c:2618)
==5107==    by 0x45A321: type_call (typeobject.c:436)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==5107==    by 0x2041FF67: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_den
se.c:7503)
```

Cheers,

Tagged for 2.8.4

Michael

Issue created by migration from https://trac.sagemath.org/ticket/561





---

archive/issue_comments_002907.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-02T00:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/561#issuecomment-2907",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002908.json:
```json
{
    "body": "patch is attached to #559, but will be submitted by me as a mercurial patch.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-14T23:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/561#issuecomment-2908",
    "user": "mabshoff"
}
```

patch is attached to #559, but will be submitted by me as a mercurial patch.

Cheers,

Michael



---

archive/issue_comments_002909.json:
```json
{
    "body": "Attachment [sage-2.8.7.rc1-fix-small-memleaks-in_MultiModularBasis_base.patch](tarball://root/attachments/some-uuid/ticket561/sage-2.8.7.rc1-fix-small-memleaks-in_MultiModularBasis_base.patch) by mabshoff created at 2007-10-16 02:56:58\n\nburcin's fix extracted from the patch for #559",
    "created_at": "2007-10-16T02:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/561#issuecomment-2909",
    "user": "mabshoff"
}
```

Attachment [sage-2.8.7.rc1-fix-small-memleaks-in_MultiModularBasis_base.patch](tarball://root/attachments/some-uuid/ticket561/sage-2.8.7.rc1-fix-small-memleaks-in_MultiModularBasis_base.patch) by mabshoff created at 2007-10-16 02:56:58

burcin's fix extracted from the patch for #559



---

archive/issue_comments_002910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T19:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/561#issuecomment-2910",
    "user": "@williamstein"
}
```

Resolution: fixed
