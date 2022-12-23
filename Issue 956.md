# Issue 956: small memleak in the graph_isom code

archive/issues_000956.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: graph isom\n\nValgrinding the code from #939 leads to\n\n```\n==9242== LEAK SUMMARY:\n==9242==    definitely lost: 25,877 bytes in 3,205 blocks.\n==9242==      possibly lost: 318,230 bytes in 908 blocks.\n==9242==    still reachable: 43,973,827 bytes in 28,805 blocks.\n==9242==         suppressed: 0 bytes in 0 blocks.\n```\n\nIn detail:\n\n```\n==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,618 of 2,792\n==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==9242==    by 0x6100C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)\n==9242==    by 0x17DD777E: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6942)\n==9242==    by 0x415522: PyObject_Call (abstract.c:1860)\n==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==9242==\n==9242==\n==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,619 of 2,792\n==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)\n==9242==    by 0x17DD77A4: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6960)\n==9242==    by 0x415522: PyObject_Call (abstract.c:1860)\n==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==9242==\n==9242==\n==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,620 of 2,792\n==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)\n==9242==    by 0x17DD7791: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6951)\n==9242==    by 0x415522: PyObject_Call (abstract.c:1860)\n==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n==9242==\n==9242==\n==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,620 of 2,792\n==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)\n==9242==    by 0x17DD7791: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6951)\n==9242==    by 0x415522: PyObject_Call (abstract.c:1860)\n==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)\n==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/956\n\n",
    "created_at": "2007-10-21T04:43:26Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "small memleak in the graph_isom code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/956",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Keywords: graph isom

Valgrinding the code from #939 leads to

```
==9242== LEAK SUMMARY:
==9242==    definitely lost: 25,877 bytes in 3,205 blocks.
==9242==      possibly lost: 318,230 bytes in 908 blocks.
==9242==    still reachable: 43,973,827 bytes in 28,805 blocks.
==9242==         suppressed: 0 bytes in 0 blocks.
```

In detail:

```
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,618 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6100C87: __gmpz_init (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD777E: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6942)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==9242==
==9242==
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,619 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD77A4: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6960)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==9242==
==9242==
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,620 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD7791: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6951)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==9242==
==9242==
==9242== 8,456 bytes in 1,057 blocks are definitely lost in loss record 2,620 of 2,792
==9242==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==9242==    by 0x6101D47: __gmpz_init_set_si (in /tmp/Work-mabshoff/sage-2.8.7.1/local/lib/libgmp.so.3.4.1)
==9242==    by 0x17DD7791: __pyx_f_py_10graph_isom_search_tree (graph_isom.c:6951)
==9242==    by 0x415522: PyObject_Call (abstract.c:1860)
==9242==    by 0x481E91: PyEval_EvalFrameEx (ceval.c:3775)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==9242==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==9242==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
```


Issue created by migration from https://trac.sagemath.org/ticket/956





---

archive/issue_comments_005825.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T04:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5825",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005826.json:
```json
{
    "body": "\n```\n[06:46] <mabshoff> robert___: You need to up the upper bound for the deallocation matching\n[06:46] <mabshoff>     # allocate GMP ints\n[06:46] <mabshoff>     for i from 0 <= i < n+2:\n[06:46] <mabshoff>         mpz_init(Lambda_mpz[i])\n[06:46] <mabshoff>         mpz_init_set_si(zf_mpz[i], -1) # correspond to default values of\n[06:46] <mabshoff>         mpz_init_set_si(zb_mpz[i], -1) # \"infinity\"\n[06:46] <mabshoff>     # deallocate the MP integers\n[06:46] <mabshoff>     for i from 0 <= i < n:\n[06:46] <mabshoff>         mpz_clear(Lambda_mpz[i])\n[06:46] <mabshoff>         mpz_clear(zf_mpz[i])\n[06:46] <mabshoff>         mpz_clear(zb_mpz[i])\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T04:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5826",
    "user": "mabshoff"
}
```


```
[06:46] <mabshoff> robert___: You need to up the upper bound for the deallocation matching
[06:46] <mabshoff>     # allocate GMP ints
[06:46] <mabshoff>     for i from 0 <= i < n+2:
[06:46] <mabshoff>         mpz_init(Lambda_mpz[i])
[06:46] <mabshoff>         mpz_init_set_si(zf_mpz[i], -1) # correspond to default values of
[06:46] <mabshoff>         mpz_init_set_si(zb_mpz[i], -1) # "infinity"
[06:46] <mabshoff>     # deallocate the MP integers
[06:46] <mabshoff>     for i from 0 <= i < n:
[06:46] <mabshoff>         mpz_clear(Lambda_mpz[i])
[06:46] <mabshoff>         mpz_clear(zf_mpz[i])
[06:46] <mabshoff>         mpz_clear(zb_mpz[i])
```


Cheers,

Michael



---

archive/issue_comments_005827.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-21T13:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5827",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_005828.json:
```json
{
    "body": "Please refer to ticket #968",
    "created_at": "2007-10-22T01:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5828",
    "user": "rlm"
}
```

Please refer to ticket #968



---

archive/issue_comments_005829.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-10-22T01:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5829",
    "user": "rlm"
}
```

Resolution: duplicate



---

archive/issue_comments_005830.json:
```json
{
    "body": "Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-22T07:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5830",
    "user": "mabshoff"
}
```

Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.

Cheers,

Michael



---

archive/issue_comments_005831.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2007-10-22T07:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5831",
    "user": "mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_005832.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-22T07:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5832",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_005833.json:
```json
{
    "body": "PLEASE NOTE -- Don't use the patch here!! Instead, use the ones in #968.",
    "created_at": "2007-10-22T16:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5833",
    "user": "rlm"
}
```

PLEASE NOTE -- Don't use the patch here!! Instead, use the ones in #968.



---

archive/issue_comments_005834.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-10-23T19:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/956",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/956#issuecomment-5834",
    "user": "malb"
}
```

Resolution: duplicate
