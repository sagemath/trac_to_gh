# Issue 3503: pickling certain modular forms segfaults

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-24 20:29:54

Assignee: craigcitro

On Standard sage-3.0.3 on sage.math:

```
sage: m = ModularSymbols(250,4,sign=1)
sage: s = m.cuspidal_submodule().new_subspace().decomposition()
sage: save(s,'foo.sobj',compress=False)
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

Valgrind says:

```

==21080== Invalid write of size 1
==21080==    at 0x19679A33: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5584)
==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x8BF3723: save (cPickle.c:2498)
==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)
==21080==    by 0x8BF40D4: save (cPickle.c:2407)
==21080==    by 0x8BF4D57: batch_dict (cPickle.c:1715)
==21080==  Address 0x3a80eac0 is 0 bytes after a block of size 4,600 alloc'd
==21080==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==21080==    by 0x196799BB: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5417)
==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x8BF3723: save (cPickle.c:2498)
==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)
==21080==    by 0x8BF40D4: save (cPickle.c:2407)
```

and

```
==21080== Invalid read of size 1
==21080==    at 0x4A1E0F9: strcpy (mc_replace_strmem.c:268)
==21080==    by 0x19679A90: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5500)
==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x8BF3723: save (cPickle.c:2498)
==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)
==21080==    by 0x8BF40D4: save (cPickle.c:2407)
==21080==  Address 0x3a80eac0 is 0 bytes after a block of size 4,600 alloc'd
==21080==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==21080==    by 0x196799BB: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5417)
==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==21080==    by 0x415832: PyObject_Call (abstract.c:1861)
==21080==    by 0x8BF3723: save (cPickle.c:2498)
==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)
==21080==    by 0x8BF40D4: save (cPickle.c:2407)
```



---

Comment by mabshoff created at 2008-06-24 20:55:49

Interestingly enough running the same computation with

```
sage: m = ModularSymbols(248,4,sign=1)
sage: s = m.cuspidal_submodule().new_subspace().decomposition()
sage: save(s,'foo.sobj',compress=False)
```

valgrinds clean.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-24 21:14:18

Ok, the offending code is this in matrix_integer_dense.pyx:

```
    cdef _pickle_version0(self):
        # TODO: *maybe* redo this to use mpz_import and mpz_export
        # from sec 5.14 of the GMP manual. ??
        cdef int i, j, len_so_far, m, n
        cdef char *a
        cdef char *s, *t, *tmp

        if self._nrows == 0 or self._ncols == 0:
            data = ''
        else:
            n = self._nrows*self._ncols*10
            s = <char*> sage_malloc(n * sizeof(char))
            t = s
            len_so_far = 0

            _sig_on
            for i from 0 <= i < self._nrows * self._ncols:
                m = mpz_sizeinbase (self._entries[i], 32)
                if len_so_far + m + 1 >= n:
                    # copy to new string with double the size
                    n = 2*n + m + 1
                    tmp = <char*> sage_malloc(n * sizeof(char))
                    strcpy(tmp, s)
                    sage_free(s)
                    s = tmp
                    t = s + len_so_far
                #endif
                mpz_get_str(t, 32, self._entries[i])
                m = strlen(t)
                len_so_far = len_so_far + m + 1
                t = t + m
                t[0] = <char>32
                t[1] = <char>0
                t = t + 1
            _sig_off
            data = str(s)[:-1]
            free(s)
        return data
```

I would not be surprised if this is an overflow issue. Notice the factor `10` for the computation of `n`. Poking around ....

According to valgrind the crash happens in `t[1] = <char>0`

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-24 21:18:17

ok, the following makes the above case work, but it is not the real fix:

```
diff -r 718f333c3aba sage/matrix/matrix_integer_dense.pyx
--- a/sage/matrix/matrix_integer_dense.pyx	Mon Jun 23 06:15:23 2008 -0700
+++ b/sage/matrix/matrix_integer_dense.pyx	Tue Jun 24 14:16:26 2008 -0700
`@``@` -439,7 +439,7 `@``@` cdef class Matrix_integer_dense(matrix_d
         if self._nrows == 0 or self._ncols == 0:
             data = ''
         else:
-            n = self._nrows*self._ncols*10
+            n = self._nrows*self._ncols*100
             s = <char*> sage_malloc(n * sizeof(char))
             t = s
             len_so_far = 0
```

Somebody who understands the code needs to rewrite memory management here :)

Cheers,

Michael


---

Comment by was created at 2008-06-24 21:32:14

Great work tracking this down Michael!!


---

Attachment


---

Comment by craigcitro created at 2008-06-24 22:25:13

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-06-24 22:25:13

Attached patch seems to fix the issue. The problem is that two extra chars were being added to the end of the array, but space was only guaranteed for one. The attached patch fixes it.

Credit to myself and David Roe.


---

Comment by was created at 2008-06-24 22:28:55

BRAVO!

Positive review.  Great work fixing my stupid terrible bug Michael, Craig, and David Roe.


---

Comment by mabshoff created at 2008-06-24 23:33:10

Resolution: fixed


---

Comment by mabshoff created at 2008-06-24 23:33:10

Merged in Sage 3.0.4.alpha1
