# Issue 530: gmpz leak in Matrix_integer_dense__solve_iml (from matrix/strassen.pyx)

archive/issues_000530.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is from Sage 2.8.3rc3:\n\n```\n==24738== 24 bytes in 3 blocks are definitely lost in loss record 528 of 2,259\n==24738==    at 0x4A05809: malloc (vg_replace_malloc.c:149)\n==24738==    by 0x9161697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)\n==24738==    by 0x20106299: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__solve_iml (matrix_integer_dense.c:13452)\n==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24738==    by 0x200EF8C0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__rational_echelon_via_solve (matrix_intege\nr_dense.c:14925)\n==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24738==    by 0x2098F422: __pyx_f_21matrix_rational_dense_21Matrix_rational_dense__echelonize_padic (matrix_rational_dense\n.c:9284)\n==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)\n==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==24738==    by 0x2096BBF2: __pyx_f_21matrix_rational_dense_21Matrix_rational_dense_echelonize (matrix_rational_dense.c:8277\n)\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/530\n\n",
    "created_at": "2007-08-30T18:47:59Z",
    "labels": [
        "component: memleak",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "gmpz leak in Matrix_integer_dense__solve_iml (from matrix/strassen.pyx)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is from Sage 2.8.3rc3:

```
==24738== 24 bytes in 3 blocks are definitely lost in loss record 528 of 2,259
==24738==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==24738==    by 0x9161697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==24738==    by 0x20106299: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__solve_iml (matrix_integer_dense.c:13452)
==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24738==    by 0x200EF8C0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__rational_echelon_via_solve (matrix_intege
r_dense.c:14925)
==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24738==    by 0x2098F422: __pyx_f_21matrix_rational_dense_21Matrix_rational_dense__echelonize_padic (matrix_rational_dense
.c:9284)
==24738==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==24738==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==24738==    by 0x2096BBF2: __pyx_f_21matrix_rational_dense_21Matrix_rational_dense_echelonize (matrix_rational_dense.c:8277
)
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/530





---

archive/issue_comments_002690.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-30T18:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002691.json:
```json
{
    "body": "The problem is at:\n\n```\n  /* \"/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/matrix/matrix_integer_dense.pyx\":1842\n *             return B, self[0,0]\n *\n *         mpz_init(mp_D)             # <<<<<<<<<<<<<<\n *\n *\n */\n  mpz_init(__pyx_v_mp_D);\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T11:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem is at:

```
  /* "/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/matrix/matrix_integer_dense.pyx":1842
 *             return B, self[0,0]
 *
 *         mpz_init(mp_D)             # <<<<<<<<<<<<<<
 *
 *
 */
  mpz_init(__pyx_v_mp_D);
```


Cheers,

Michael



---

archive/issue_comments_002692.json:
```json
{
    "body": "But mp_D is also cleared:\n\n```\n  /* \"/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/matrix/matrix_integer_dense.pyx\":1893\n *\n *         D = PY_NEW(Integer)\n *         mpz_set(D.value, mp_D)             # <<<<<<<<<<<<<<\n *         mpz_clear(mp_D)\n *\n */\n  mpz_set(__pyx_v_D->value,__pyx_v_mp_D);\n\n  /* \"/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/matrix/matrix_integer_dense.pyx\":1894\n *         D = PY_NEW(Integer)\n *         mpz_set(D.value, mp_D)\n *         mpz_clear(mp_D)             # <<<<<<<<<<<<<<\n *\n *         return M,D\n */\n  mpz_clear(__pyx_v_mp_D);\n```\n\nIs this a reference counting issue maybe?\n\nCheers,\n\nMichael",
    "created_at": "2007-09-03T11:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

But mp_D is also cleared:

```
  /* "/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/matrix/matrix_integer_dense.pyx":1893
 *
 *         D = PY_NEW(Integer)
 *         mpz_set(D.value, mp_D)             # <<<<<<<<<<<<<<
 *         mpz_clear(mp_D)
 *
 */
  mpz_set(__pyx_v_D->value,__pyx_v_mp_D);

  /* "/tmp/Work2/sage-2.8.3.rc3/devel/sage-main/sage/matrix/matrix_integer_dense.pyx":1894
 *         D = PY_NEW(Integer)
 *         mpz_set(D.value, mp_D)
 *         mpz_clear(mp_D)             # <<<<<<<<<<<<<<
 *
 *         return M,D
 */
  mpz_clear(__pyx_v_mp_D);
```

Is this a reference counting issue maybe?

Cheers,

Michael



---

archive/issue_comments_002693.json:
```json
{
    "body": "Consider these two closely related examples:\n\nThis one leaks:\n\n```\nsage: A = matrix(ZZ,4,4,[0, 1, -2, -1, -1, 1, 0, 2, 2, 2, 2, -1, 0, 2, 2, 1])\nsage: B = matrix(ZZ,3,4, [-1, 1, 1, 0, 2, 0, -2, -1, 0, -2, -2, -2])\nsage: C =A._solve_iml(B,right=False);\nsage: C\n([  6 -18 -15  27]\n[  0  24  24 -36]\n[  4 -12  -6  -2], 12)\nsage: del C\n```\n\n\nWhile this one doesn't:\n\n```\nsage: A = matrix(ZZ,4,4,[0, 1, -2, -1, -1, 1, 0, 2, 2, 2, 2, -1, 0, 2, 2, 1])\nsage: B = matrix(ZZ,3,4, [-1, 1, 1, 0, 2, 0, -2, -1, 0, -2, -2, -2])\nsage: C =A._solve_iml(B,right=False);\nsage: del C\n```\n",
    "created_at": "2007-09-07T00:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2693",
    "user": "https://github.com/malb"
}
```

Consider these two closely related examples:

This one leaks:

```
sage: A = matrix(ZZ,4,4,[0, 1, -2, -1, -1, 1, 0, 2, 2, 2, 2, -1, 0, 2, 2, 1])
sage: B = matrix(ZZ,3,4, [-1, 1, 1, 0, 2, 0, -2, -1, 0, -2, -2, -2])
sage: C =A._solve_iml(B,right=False);
sage: C
([  6 -18 -15  27]
[  0  24  24 -36]
[  4 -12  -6  -2], 12)
sage: del C
```


While this one doesn't:

```
sage: A = matrix(ZZ,4,4,[0, 1, -2, -1, -1, 1, 0, 2, 2, 2, 2, -1, 0, 2, 2, 1])
sage: B = matrix(ZZ,3,4, [-1, 1, 1, 0, 2, 0, -2, -1, 0, -2, -2, -2])
sage: C =A._solve_iml(B,right=False);
sage: del C
```




---

archive/issue_comments_002694.json:
```json
{
    "body": "Also:\n\n```\nsage: A = matrix(ZZ,4,4,[0, 1, -2, -1, -1, 1, 0, 2, 2, 2, 2, -1, 0, 2, 2, 1])\nsage: B = matrix(ZZ,3,4, [-1, 1, 1, 0, 2, 0, -2, -1, 0, -2, -2, -2])\nsage: C =A._solve_iml(B,right=False);\nsage: c = str(C)\nsage: del c\nsage: del C\n```\n\ndoesn't leak either.",
    "created_at": "2007-09-07T00:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2694",
    "user": "https://github.com/malb"
}
```

Also:

```
sage: A = matrix(ZZ,4,4,[0, 1, -2, -1, -1, 1, 0, 2, 2, 2, 2, -1, 0, 2, 2, 1])
sage: B = matrix(ZZ,3,4, [-1, 1, 1, 0, 2, 0, -2, -1, 0, -2, -2, -2])
sage: C =A._solve_iml(B,right=False);
sage: c = str(C)
sage: del c
sage: del C
```

doesn't leak either.



---

archive/issue_comments_002695.json:
```json
{
    "body": "Attachment [trac_530.patch](tarball://root/attachments/some-uuid/ticket530/trac_530.patch) by @malb created at 2008-04-05 21:23:17",
    "created_at": "2008-04-05T21:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2695",
    "user": "https://github.com/malb"
}
```

Attachment [trac_530.patch](tarball://root/attachments/some-uuid/ticket530/trac_530.patch) by @malb created at 2008-04-05 21:23:17



---

archive/issue_comments_002696.json:
```json
{
    "body": "The attached patch fixes at least one possible leak",
    "created_at": "2008-04-05T21:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2696",
    "user": "https://github.com/malb"
}
```

The attached patch fixes at least one possible leak



---

archive/issue_comments_002697.json:
```json
{
    "body": "This patch works fine and solves a potential leak for degenerate matrices, but doesn't look like it solves the problem.",
    "created_at": "2008-04-06T05:55:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2697",
    "user": "https://github.com/robertwb"
}
```

This patch works fine and solves a potential leak for degenerate matrices, but doesn't look like it solves the problem.



---

archive/issue_comments_002698.json:
```json
{
    "body": "Yes, it does solve the problem. Before (this is on 2.11)\n\n```\n==9512== LEAK SUMMARY:\n==9512==    definitely lost: 272 bytes in 5 blocks.\n==9512==    indirectly lost: 3,468 bytes in 5 blocks.\n==9512==      possibly lost: 280,842 bytes in 844 blocks.\n==9512==    still reachable: 31,649,013 bytes in 194,687 blocks.\n==9512==         suppressed: 0 bytes in 0 blocks.\n```\n\nAfter:\n\n```\n==9728== LEAK SUMMARY:\n==9728==    definitely lost: 248 bytes in 2 blocks.\n==9728==    indirectly lost: 3,468 bytes in 5 blocks.\n==9728==      possibly lost: 280,842 bytes in 844 blocks.\n==9728==    still reachable: 31,649,045 bytes in 194,689 blocks.\n==9728==         suppressed: 0 bytes in 0 blocks.\n```\n\nThe now no longer missing 24 bytes in three blocks is exactly what malb fixed. w00t\n\nEnthusiastic positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T03:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, it does solve the problem. Before (this is on 2.11)

```
==9512== LEAK SUMMARY:
==9512==    definitely lost: 272 bytes in 5 blocks.
==9512==    indirectly lost: 3,468 bytes in 5 blocks.
==9512==      possibly lost: 280,842 bytes in 844 blocks.
==9512==    still reachable: 31,649,013 bytes in 194,687 blocks.
==9512==         suppressed: 0 bytes in 0 blocks.
```

After:

```
==9728== LEAK SUMMARY:
==9728==    definitely lost: 248 bytes in 2 blocks.
==9728==    indirectly lost: 3,468 bytes in 5 blocks.
==9728==      possibly lost: 280,842 bytes in 844 blocks.
==9728==    still reachable: 31,649,045 bytes in 194,689 blocks.
==9728==         suppressed: 0 bytes in 0 blocks.
```

The now no longer missing 24 bytes in three blocks is exactly what malb fixed. w00t

Enthusiastic positive review.

Cheers,

Michael



---

archive/issue_comments_002699.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T03:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_002700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T03:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2700",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000569.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-07T03:06:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/530#event-569"
}
```



---

archive/issue_comments_002701.json:
```json
{
    "body": "I stand happily corrected.",
    "created_at": "2008-04-07T17:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/530#issuecomment-2701",
    "user": "https://github.com/robertwb"
}
```

I stand happily corrected.
