# Issue 530: gmpz leak in Matrix_integer_dense__solve_iml (from matrix/strassen.pyx)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-30 18:47:59

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


---

Comment by mabshoff created at 2007-08-30 18:48:11

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-03 11:11:52

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

Comment by mabshoff created at 2007-09-03 11:23:22

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

Comment by malb created at 2007-09-07 00:16:35

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

Comment by malb created at 2007-09-07 00:19:39

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

Attachment


---

Comment by malb created at 2008-04-05 21:24:17

The attached patch fixes at least one possible leak


---

Comment by robertwb created at 2008-04-06 05:55:59

This patch works fine and solves a potential leak for degenerate matrices, but doesn't look like it solves the problem.


---

Comment by mabshoff created at 2008-04-07 03:05:28

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

Comment by mabshoff created at 2008-04-07 03:06:02

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-07 03:06:02

Resolution: fixed


---

Comment by robertwb created at 2008-04-07 17:28:58

I stand happily corrected.
