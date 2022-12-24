# Issue 3503: pickling certain modular forms segfaults

archive/issues_003503.json:
```json
{
    "body": "Assignee: craigcitro\n\nOn Standard sage-3.0.3 on sage.math:\n\n```\nsage: m = ModularSymbols(250,4,sign=1)\nsage: s = m.cuspidal_submodule().new_subspace().decomposition()\nsage: save(s,'foo.sobj',compress=False)\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nValgrind says:\n\n```\n\n==21080== Invalid write of size 1\n==21080==    at 0x19679A33: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5584)\n==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x8BF3723: save (cPickle.c:2498)\n==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)\n==21080==    by 0x8BF40D4: save (cPickle.c:2407)\n==21080==    by 0x8BF4D57: batch_dict (cPickle.c:1715)\n==21080==  Address 0x3a80eac0 is 0 bytes after a block of size 4,600 alloc'd\n==21080==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==21080==    by 0x196799BB: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5417)\n==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x8BF3723: save (cPickle.c:2498)\n==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)\n==21080==    by 0x8BF40D4: save (cPickle.c:2407)\n```\n\nand\n\n```\n==21080== Invalid read of size 1\n==21080==    at 0x4A1E0F9: strcpy (mc_replace_strmem.c:268)\n==21080==    by 0x19679A90: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5500)\n==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x8BF3723: save (cPickle.c:2498)\n==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)\n==21080==    by 0x8BF40D4: save (cPickle.c:2407)\n==21080==  Address 0x3a80eac0 is 0 bytes after a block of size 4,600 alloc'd\n==21080==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)\n==21080==    by 0x196799BB: __pyx_f_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle_version0 (matrix_integer_dense.c:5417)\n==21080==    by 0x19674A6A: __pyx_pf_4sage_6matrix_20matrix_integer_dense_20Matrix_integer_dense__pickle (matrix_integer_dense.c:5325)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x180B6235: __pyx_pf_4sage_6matrix_7matrix0_6Matrix___reduce__ (matrix0.c:3809)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)\n==21080==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)\n==21080==    by 0x415832: PyObject_Call (abstract.c:1861)\n==21080==    by 0x8BF3723: save (cPickle.c:2498)\n==21080==    by 0x8BF3244: save_tuple (cPickle.c:1384)\n==21080==    by 0x8BF40D4: save (cPickle.c:2407)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3503\n\n",
    "created_at": "2008-06-24T20:29:54Z",
    "labels": [
        "modular forms",
        "blocker",
        "bug"
    ],
    "title": "pickling certain modular forms segfaults",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3503",
    "user": "mabshoff"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/3503





---

archive/issue_comments_024704.json:
```json
{
    "body": "Interestingly enough running the same computation with\n\n```\nsage: m = ModularSymbols(248,4,sign=1)\nsage: s = m.cuspidal_submodule().new_subspace().decomposition()\nsage: save(s,'foo.sobj',compress=False)\n```\n\nvalgrinds clean.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-24T20:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24704",
    "user": "mabshoff"
}
```

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

archive/issue_comments_024705.json:
```json
{
    "body": "Ok, the offending code is this in matrix_integer_dense.pyx:\n\n```\n    cdef _pickle_version0(self):\n        # TODO: *maybe* redo this to use mpz_import and mpz_export\n        # from sec 5.14 of the GMP manual. ??\n        cdef int i, j, len_so_far, m, n\n        cdef char *a\n        cdef char *s, *t, *tmp\n\n        if self._nrows == 0 or self._ncols == 0:\n            data = ''\n        else:\n            n = self._nrows*self._ncols*10\n            s = <char*> sage_malloc(n * sizeof(char))\n            t = s\n            len_so_far = 0\n\n            _sig_on\n            for i from 0 <= i < self._nrows * self._ncols:\n                m = mpz_sizeinbase (self._entries[i], 32)\n                if len_so_far + m + 1 >= n:\n                    # copy to new string with double the size\n                    n = 2*n + m + 1\n                    tmp = <char*> sage_malloc(n * sizeof(char))\n                    strcpy(tmp, s)\n                    sage_free(s)\n                    s = tmp\n                    t = s + len_so_far\n                #endif\n                mpz_get_str(t, 32, self._entries[i])\n                m = strlen(t)\n                len_so_far = len_so_far + m + 1\n                t = t + m\n                t[0] = <char>32\n                t[1] = <char>0\n                t = t + 1\n            _sig_off\n            data = str(s)[:-1]\n            free(s)\n        return data\n```\n\nI would not be surprised if this is an overflow issue. Notice the factor `10` for the computation of `n`. Poking around ....\n\nAccording to valgrind the crash happens in `t[1] = <char>0`\n\nCheers,\n\nMichael",
    "created_at": "2008-06-24T21:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24705",
    "user": "mabshoff"
}
```

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

archive/issue_comments_024706.json:
```json
{
    "body": "ok, the following makes the above case work, but it is not the real fix:\n\n```\ndiff -r 718f333c3aba sage/matrix/matrix_integer_dense.pyx\n--- a/sage/matrix/matrix_integer_dense.pyx\tMon Jun 23 06:15:23 2008 -0700\n+++ b/sage/matrix/matrix_integer_dense.pyx\tTue Jun 24 14:16:26 2008 -0700\n@@ -439,7 +439,7 @@ cdef class Matrix_integer_dense(matrix_d\n         if self._nrows == 0 or self._ncols == 0:\n             data = ''\n         else:\n-            n = self._nrows*self._ncols*10\n+            n = self._nrows*self._ncols*100\n             s = <char*> sage_malloc(n * sizeof(char))\n             t = s\n             len_so_far = 0\n```\n\nSomebody who understands the code needs to rewrite memory management here :)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-24T21:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24706",
    "user": "mabshoff"
}
```

ok, the following makes the above case work, but it is not the real fix:

```
diff -r 718f333c3aba sage/matrix/matrix_integer_dense.pyx
--- a/sage/matrix/matrix_integer_dense.pyx	Mon Jun 23 06:15:23 2008 -0700
+++ b/sage/matrix/matrix_integer_dense.pyx	Tue Jun 24 14:16:26 2008 -0700
@@ -439,7 +439,7 @@ cdef class Matrix_integer_dense(matrix_d
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

archive/issue_comments_024707.json:
```json
{
    "body": "Great work tracking this down Michael!!",
    "created_at": "2008-06-24T21:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24707",
    "user": "was"
}
```

Great work tracking this down Michael!!



---

archive/issue_comments_024708.json:
```json
{
    "body": "Attachment [trac-3503.patch](tarball://root/attachments/some-uuid/ticket3503/trac-3503.patch) by craigcitro created at 2008-06-24 22:24:17",
    "created_at": "2008-06-24T22:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24708",
    "user": "craigcitro"
}
```

Attachment [trac-3503.patch](tarball://root/attachments/some-uuid/ticket3503/trac-3503.patch) by craigcitro created at 2008-06-24 22:24:17



---

archive/issue_comments_024709.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-24T22:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24709",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024710.json:
```json
{
    "body": "Attached patch seems to fix the issue. The problem is that two extra chars were being added to the end of the array, but space was only guaranteed for one. The attached patch fixes it.\n\nCredit to myself and David Roe.",
    "created_at": "2008-06-24T22:25:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24710",
    "user": "craigcitro"
}
```

Attached patch seems to fix the issue. The problem is that two extra chars were being added to the end of the array, but space was only guaranteed for one. The attached patch fixes it.

Credit to myself and David Roe.



---

archive/issue_comments_024711.json:
```json
{
    "body": "BRAVO!\n\nPositive review.  Great work fixing my stupid terrible bug Michael, Craig, and David Roe.",
    "created_at": "2008-06-24T22:28:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24711",
    "user": "was"
}
```

BRAVO!

Positive review.  Great work fixing my stupid terrible bug Michael, Craig, and David Roe.



---

archive/issue_comments_024712.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-24T23:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24712",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024713.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-24T23:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3503",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3503#issuecomment-24713",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
