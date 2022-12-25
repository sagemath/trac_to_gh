# Issue 533: matrix_rational_sparse_allocate_mpq_vector leak (from modular/ssmod/ssmod.py)

archive/issues_000533.json:
```json
{
    "body": "Assignee: mabshoff\n\nFrom Sage 2.8.3rc3:\n\n```\n==24845== 352 bytes in 44 blocks are definitely lost in loss record 1,423 of 2,587\n==24845==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==24845==    by 0x946C2A6: __gmpq_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==24845==    by 0x20EB34C3: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5358)\n==24845==    by 0x20EB51D4: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6394)\n==24845==    by 0x20EB5367: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:8\n463)\n==24845==    by 0x1DF0A336: __pyx_f_7matrix0_6Matrix_add_multiple_of_column_c (matrix0.c:5631)\n==24845==    by 0x1DA89C8B: __pyx_f_7matrix2_6Matrix_hessenbergize (matrix2.c:4699)\n==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24845==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24845==    by 0x1DA86360: __pyx_f_7matrix2_6Matrix_hessenberg_form (matrix2.c:4233)\n==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24845==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/533\n\n",
    "created_at": "2007-08-30T18:51:07Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "matrix_rational_sparse_allocate_mpq_vector leak (from modular/ssmod/ssmod.py)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

From Sage 2.8.3rc3:

```
==24845== 352 bytes in 44 blocks are definitely lost in loss record 1,423 of 2,587
==24845==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==24845==    by 0x946C2A6: __gmpq_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==24845==    by 0x20EB34C3: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5358)
==24845==    by 0x20EB51D4: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6394)
==24845==    by 0x20EB5367: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:8
463)
==24845==    by 0x1DF0A336: __pyx_f_7matrix0_6Matrix_add_multiple_of_column_c (matrix0.c:5631)
==24845==    by 0x1DA89C8B: __pyx_f_7matrix2_6Matrix_hessenbergize (matrix2.c:4699)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24845==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24845==    by 0x1DA86360: __pyx_f_7matrix2_6Matrix_hessenberg_form (matrix2.c:4233)
==24845==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24845==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/533





---

archive/issue_comments_002708.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-30T18:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/533#issuecomment-2708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002709.json:
```json
{
    "body": "With patches 6801 and 6802 this leaks has been but cut by more than half:\n\n```\n==6907== LEAK SUMMARY:\n==6907==    definitely lost: 191,508 bytes in 16,482 blocks.\n==6907==    indirectly lost: 1,128 bytes in 16 blocks.\n==6907==      possibly lost: 327,526 bytes in 908 blocks.\n==6907==    still reachable: 136,860,457 bytes in 22,940 blocks.\n==6907==         suppressed: 0 bytes in 0 blocks.\n```\n\nvs.\n\n```\n==21394== LEAK SUMMARY:\n==21394==    definitely lost: 77,340 bytes in 2,550 blocks.\n==21394==    indirectly lost: 816 bytes in 3 blocks.\n==21394==      possibly lost: 325,374 bytes in 903 blocks.\n==21394==    still reachable: 136,860,401 bytes in 22,935 blocks.\n==21394==         suppressed: 0 bytes in 0 blocks.\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T20:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/533#issuecomment-2709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With patches 6801 and 6802 this leaks has been but cut by more than half:

```
==6907== LEAK SUMMARY:
==6907==    definitely lost: 191,508 bytes in 16,482 blocks.
==6907==    indirectly lost: 1,128 bytes in 16 blocks.
==6907==      possibly lost: 327,526 bytes in 908 blocks.
==6907==    still reachable: 136,860,457 bytes in 22,940 blocks.
==6907==         suppressed: 0 bytes in 0 blocks.
```

vs.

```
==21394== LEAK SUMMARY:
==21394==    definitely lost: 77,340 bytes in 2,550 blocks.
==21394==    indirectly lost: 816 bytes in 3 blocks.
==21394==      possibly lost: 325,374 bytes in 903 blocks.
==21394==    still reachable: 136,860,401 bytes in 22,935 blocks.
==21394==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

Michael



---

archive/issue_comments_002710.json:
```json
{
    "body": "Fixed along the way.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-14T12:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/533#issuecomment-2710",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed along the way.

Cheers,

Michael



---

archive/issue_comments_002711.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T12:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/533",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/533#issuecomment-2711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000572.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-10-14T12:45:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/533",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/533#event-572"
}
```
