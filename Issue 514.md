# Issue 514: memory leak in  _solve_iml(self, Matrix_integer_dense B, right=True)

Issue created by migration from https://trac.sagemath.org/ticket/514

Original creator: mabshoff

Original creation time: 2007-08-29 17:47:38

Assignee: was

Hello,

I got the following leak while looking at #454 further:

```
==9632== 3,416,000 (2,196,032 direct, 1,219,968 indirect) bytes in 110 blocks are definitely lost in loss record 2,823 of 2,
824
==9632==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==9632==    by 0x203196F8: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__solve_iml (matrix_integer_dense.c:13639)
==9632==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==9632==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==9632==    by 0x203018C0: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__rational_echelon_via_solve (matrix_integer
_dense.c:14916)
==9632==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==9632==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==9632==    by 0x20BA375D: __pyx_f_21matrix_rational_dense_21Matrix_rational_dense__echelon_form_padic (matrix_rational_dens
e.c:8784)
==9632==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==9632==    by 0x47DB71: PyEval_CallObjectWithKeywords (ceval.c:3433)
==9632==    by 0x20B7D01B: __pyx_f_21matrix_rational_dense_21Matrix_rational_dense_echelon_form (matrix_rational_dense.c:852
3)
==9632==    by 0x485A8A: PyEval_EvalFrameEx (ceval.c:3564)
```


The problem starts at line 1857 of sage/matrix/matrix_integer_dense.pyx:

```
            if m == 0 or n == 0:
                return self.new_matrix(nrows = n, ncols = m), Integer(1)

            mp_N = <mpz_t *> sage_malloc( n * m * sizeof(mpz_t) ) [line 1857]
            for i from 0 <= i < n * m:
                mpz_init( mp_N[i] )
```

Then after the computation has finished we try to deallocate in line 1884, specifically line 1887:

```
        M = Matrix_integer_dense.__new__(Matrix_integer_dense, P, None, None, None)
        for i from 0 <= i < n*m:
            mpz_init_set(M._entries[i], mp_N[i])
            mpz_clear(mp_N[i]) [line 1887]
        M._initialized = True
```

The code certainly looks correct, but somehow things do go wrong. I don't like the look of "<mpz_t*> sage_alloc" Any ideas?

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-29 17:53:23

Changing component from algebraic geometry to basic arithmetic.


---

Comment by mabshoff created at 2007-08-29 17:53:23

Changing assignee from was to somebody.


---

Comment by mabshoff created at 2007-08-29 20:32:49

Changing assignee from somebody to was.


---

Comment by mabshoff created at 2007-08-29 20:32:49

Changing priority from major to blocker.


---

Comment by mabshoff created at 2007-08-29 20:32:49

The following patch fixes the issue:

```
diff -r c6efa3a2146a sage/matrix/matrix_integer_dense.pyx
--- a/sage/matrix/matrix_integer_dense.pyx      Wed Aug 29 00:26:58 2007 -0700
+++ b/sage/matrix/matrix_integer_dense.pyx      Wed Aug 29 21:25:49 2007 +0200
@@ -1885,6 +1885,7 @@ cdef class Matrix_integer_dense(matrix_d
         for i from 0 <= i < n*m:
             mpz_init_set(M._entries[i], mp_N[i])
             mpz_clear(mp_N[i])
+        sage_free(mp_N)
         M._initialized = True

         D = PY_NEW(Integer)
```

Fix by malb, verification by mabshoff.

The patch is also at http://fsmath.mathematik.uni-dortmund.de/~mabshoff/patches/sage-2.8.3alpha2-fix-memleak-ticket-514.patch

Cheers,

Michael


---

Comment by was created at 2007-08-29 23:34:10

Resolution: fixed
