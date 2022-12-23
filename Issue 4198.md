# Issue 4198: [with patch, needs review] matrix_cyclo_dense.pyx leaks in _get_unsafe

archive/issues_004198.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  craigcitro\n\n#3502 added (or exposed?) a small memory leak in matrix_cyclo_dense.pyx's _get_unsafe method. We do not deallocate a tmp mpz in the quick return patch. The attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4198\n\n",
    "created_at": "2008-09-26T02:02:06Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] matrix_cyclo_dense.pyx leaks in _get_unsafe",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4198",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  craigcitro

#3502 added (or exposed?) a small memory leak in matrix_cyclo_dense.pyx's _get_unsafe method. We do not deallocate a tmp mpz in the quick return patch. The attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4198





---

archive/issue_comments_030469.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-26T02:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4198#issuecomment-30469",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030470.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-26T02:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4198#issuecomment-30470",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_030471.json:
```json
{
    "body": "Oops :-)  Patch looks good to me.",
    "created_at": "2008-09-26T02:22:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4198#issuecomment-30471",
    "user": "mhansen"
}
```

Oops :-)  Patch looks good to me.



---

archive/issue_comments_030472.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-26T02:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4198#issuecomment-30472",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030473.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-26T02:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4198#issuecomment-30473",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030474.json:
```json
{
    "body": "The valgrind trace was the following:\n\n```\n==19392== 8 bytes in 1 blocks are definitely lost in loss record 71 of 22,499\n==19392==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)\n==19392==    by 0x6360947: __gmpz_init (in /scratch/mabshoff/release-cycle/sage-3.1.3.alpha1/local/lib/libgmp.so.3.4.1)\n==19392==    by 0x19D0A675: __pyx_f_4sage_6matrix_18matrix_cyclo_dense_18Matrix_cyclo_dense_get_unsafe(__pyx_obj_4sage_6matrix_18matrix_cyclo_dense_Matrix_cyclo_dense*, long, long) (matrix_cyclo_dense.cpp:3773)\n==19392==    by 0x16397A16: __pyx_pf_4sage_6matrix_7matrix1_6Matrix_dense_rows (matrix1.c:3933)\n==19392==    by 0x415832: PyObject_Call (abstract.c:1861)\n==19392==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==19392==    by 0x16392247: __pyx_pf_4sage_6matrix_7matrix1_6Matrix_rows (matrix1.c:3366)\n==19392==    by 0x415832: PyObject_Call (abstract.c:1861)\n==19392==    by 0x164CEEE9: __pyx_pf_4sage_6matrix_7matrix0_6Matrix_linear_combination_of_rows (matrix0.c:10569)\n```\n",
    "created_at": "2008-10-15T13:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4198",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4198#issuecomment-30474",
    "user": "mabshoff"
}
```

The valgrind trace was the following:

```
==19392== 8 bytes in 1 blocks are definitely lost in loss record 71 of 22,499
==19392==    at 0x4A1BE1B: malloc (vg_replace_malloc.c:207)
==19392==    by 0x6360947: __gmpz_init (in /scratch/mabshoff/release-cycle/sage-3.1.3.alpha1/local/lib/libgmp.so.3.4.1)
==19392==    by 0x19D0A675: __pyx_f_4sage_6matrix_18matrix_cyclo_dense_18Matrix_cyclo_dense_get_unsafe(__pyx_obj_4sage_6matrix_18matrix_cyclo_dense_Matrix_cyclo_dense*, long, long) (matrix_cyclo_dense.cpp:3773)
==19392==    by 0x16397A16: __pyx_pf_4sage_6matrix_7matrix1_6Matrix_dense_rows (matrix1.c:3933)
==19392==    by 0x415832: PyObject_Call (abstract.c:1861)
==19392==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==19392==    by 0x16392247: __pyx_pf_4sage_6matrix_7matrix1_6Matrix_rows (matrix1.c:3366)
==19392==    by 0x415832: PyObject_Call (abstract.c:1861)
==19392==    by 0x164CEEE9: __pyx_pf_4sage_6matrix_7matrix0_6Matrix_linear_combination_of_rows (matrix0.c:10569)
```

