# Issue 854: [with patch] memory leak: MultiModularBasis_base_mpz_crt_vec_tail

archive/issues_000854.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n==15091== 24,160 bytes in 3,020 blocks are definitely lost in loss record 2,218 of 2,504\n==15091==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)\n==15091==    by 0x6108C60: __gmpz_init_set (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)\n==15091==    by 0x11CD7DC0: __pyx_f_13multi_modular_22MultiModularBasis_base_mpz_crt_vec_tail (multi_modular.c:4543)\n==15091==    by 0x11CD2DB9: __pyx_f_13multi_modular_17MultiModularBasis_mpz_crt_vec (multi_modular.c:5435)\n==15091==    by 0x1262F7A4: __pyx_f_20matrix_integer_dense__lift_crt (matrix_integer_dense.c:17664)\n==15091==    by 0x415522: PyObject_Call (abstract.c:1860)\n==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==15091==    by 0x1265ECF8: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de\nnse.c:7916)\n==15091==    by 0x415522: PyObject_Call (abstract.c:1860)\n==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==15091==    by 0x126356BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege\nr_dense.c:5669)\n==15091==    by 0x9341519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/854\n\n",
    "created_at": "2007-10-12T00:58:20Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "[with patch] memory leak: MultiModularBasis_base_mpz_crt_vec_tail",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
==15091== 24,160 bytes in 3,020 blocks are definitely lost in loss record 2,218 of 2,504
==15091==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==15091==    by 0x6108C60: __gmpz_init_set (in /tmp/Work-mabshoff/sage-2.8.6/local/lib/libgmp.so.3.4.1)
==15091==    by 0x11CD7DC0: __pyx_f_13multi_modular_22MultiModularBasis_base_mpz_crt_vec_tail (multi_modular.c:4543)
==15091==    by 0x11CD2DB9: __pyx_f_13multi_modular_17MultiModularBasis_mpz_crt_vec (multi_modular.c:5435)
==15091==    by 0x1262F7A4: __pyx_f_20matrix_integer_dense__lift_crt (matrix_integer_dense.c:17664)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==15091==    by 0x1265ECF8: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__multiply_multi_modular (matrix_integer_de
nse.c:7916)
==15091==    by 0x415522: PyObject_Call (abstract.c:1860)
==15091==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==15091==    by 0x126356BA: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__matrix_times_matrix_c_impl (matrix_intege
r_dense.c:5669)
==15091==    by 0x9341519: __pyx_f_7element_6Matrix___mul__ (element.c:9950)
```


Issue created by migration from https://trac.sagemath.org/ticket/854





---

archive/issue_comments_005279.json:
```json
{
    "body": "Attachment [Sage-2.8.6-fix-memleak-in-MultiModularBasis.patch](tarball://root/attachments/some-uuid/ticket854/Sage-2.8.6-fix-memleak-in-MultiModularBasis.patch) by mabshoff created at 2007-10-12 01:03:42",
    "created_at": "2007-10-12T01:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/854#issuecomment-5279",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.8.6-fix-memleak-in-MultiModularBasis.patch](tarball://root/attachments/some-uuid/ticket854/Sage-2.8.6-fix-memleak-in-MultiModularBasis.patch) by mabshoff created at 2007-10-12 01:03:42



---

archive/issue_comments_005280.json:
```json
{
    "body": "William,\n\nplease check if this is the right way to fix this. \"sage -testall\" passes on sage.math with the patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-12T01:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/854#issuecomment-5280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William,

please check if this is the right way to fix this. "sage -testall" passes on sage.math with the patch applied.

Cheers,

Michael



---

archive/issue_comments_005281.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/854",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/854#issuecomment-5281",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000966.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-13T07:28:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/854",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/854#event-966"
}
```
