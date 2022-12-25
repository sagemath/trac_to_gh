# Issue 781: Matrix from Matrix_integer_dense() blows up (Dup of 799 for formatting)

archive/issues_000781.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf I create a matrix with Matrix_integer_dense(), and try to display it, sage blows chunks. It appears to happen inside the gmp library. This is with 2.8.5.1 on a Core 2 Duo (Mac OS X, 10.4.10).\n\nTwo different examples, printing the whole matrix:\n\n\n```\nsage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense\nsage: a = Matrix_integer_dense.new(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)\nsage: a.ncols() 3 sage: a.nrows() 3 sage: a\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_INVALID_ADDRESS at address: 0x013af000 0x00777991 in gmpn_copyi ()\n\n(gdb) bt\n#0 0x00777991 in gmpn_copyi ()\n#1 0x0075c4a0 in gmpz_set ()\nPrevious frame inner to this frame (corrupt stack?)\n```\n\n\nand printing a single entry:\n\n```\nsage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense\nsage: a = Matrix_integer_dense.new(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)\nsage: for i in range(a.nrows()):\n    ...: for j in range(a.ncols()):\n        ...: print a[i,j] ...:\n0\npython(16613) malloc: *** vm_allocate(size=1680302080) failed (error code=3)\npython(16613) malloc: *** error: can't allocate region\npython(16613) malloc: *** set a breakpoint in szone_error to debug\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_PROTECTION_FAILURE at address: 0x00000000\n0x0076a0b7 in gmpn_sqr_basecase ()\n(gdb)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/781\n\n",
    "created_at": "2007-10-02T02:41:13Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "Matrix from Matrix_integer_dense() blows up (Dup of 799 for formatting)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/781",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

If I create a matrix with Matrix_integer_dense(), and try to display it, sage blows chunks. It appears to happen inside the gmp library. This is with 2.8.5.1 on a Core 2 Duo (Mac OS X, 10.4.10).

Two different examples, printing the whole matrix:


```
sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: a = Matrix_integer_dense.new(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
sage: a.ncols() 3 sage: a.nrows() 3 sage: a

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x013af000 0x00777991 in gmpn_copyi ()

(gdb) bt
#0 0x00777991 in gmpn_copyi ()
#1 0x0075c4a0 in gmpz_set ()
Previous frame inner to this frame (corrupt stack?)
```


and printing a single entry:

```
sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: a = Matrix_integer_dense.new(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
sage: for i in range(a.nrows()):
    ...: for j in range(a.ncols()):
        ...: print a[i,j] ...:
0
python(16613) malloc: *** vm_allocate(size=1680302080) failed (error code=3)
python(16613) malloc: *** error: can't allocate region
python(16613) malloc: *** set a breakpoint in szone_error to debug

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x00000000
0x0076a0b7 in gmpn_sqr_basecase ()
(gdb)
```


Issue created by migration from https://trac.sagemath.org/ticket/781





---

archive/issue_comments_004654.json:
```json
{
    "body": "And, by '799', I mean '779'",
    "created_at": "2007-10-02T02:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4654",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

And, by '799', I mean '779'



---

archive/issue_comments_004655.json:
```json
{
    "body": "I will look into this, valgrind might turn up something interesting.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-04T19:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will look into this, valgrind might turn up something interesting.

Cheers,

Michael



---

archive/issue_comments_004656.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-10-04T19:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_events_002151.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-04T19:51:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/781#event-2151"
}
```



---

archive/issue_comments_004657.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-18T11:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004658.json:
```json
{
    "body": "Interestingly enough this works under valgrind:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense\nsage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)\nsage: for i in range(a.nrows()):\n....:     for j in range(a.ncols()):\n....:         print a[i,j]\n....:\n0\n0\n0\n0\n0\n0\n0\n0\n0\nsage:\nExiting SAGE (CPU time 0m20.94s, Wall time 1m7.20s).\n```\n\nI will have a look at the logs and hopefully fix this during Bug Day 4.\n| SAGE Version 2.8.7.rc1, Release Date: 2007-10-14                   |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2007-10-18T11:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Interestingly enough this works under valgrind:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
sage: for i in range(a.nrows()):
....:     for j in range(a.ncols()):
....:         print a[i,j]
....:
0
0
0
0
0
0
0
0
0
sage:
Exiting SAGE (CPU time 0m20.94s, Wall time 1m7.20s).
```

I will have a look at the logs and hopefully fix this during Bug Day 4.
| SAGE Version 2.8.7.rc1, Release Date: 2007-10-14                   |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_004659.json:
```json
{
    "body": "There are a bunch of the following:\n\n```\n==32632== Conditional jump or move depends on uninitialised value(s)\n==32632==    at 0x6116EC4: __gmpn_get_str (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)\n==32632==    by 0x60FF327: __gmpz_get_str (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)\n==32632==    by 0xB961F7C: __pyx_f_py_7integer_7Integer_str (integer.c:3896)\n==32632==    by 0x415522: PyObject_Call (abstract.c:1860)\n==32632==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==32632==    by 0xB95D4AB: __pyx_f_py_7integer_7Integer___repr__ (integer.c:3691)\n==32632==    by 0x443299: _PyObject_Str (object.c:406)\n==32632==    by 0x443A08: internal_print (object.c:426)\n==32632==    by 0x42999C: PyFile_WriteObject (fileobject.c:2178)\n==32632==    by 0x481C0C: PyEval_EvalFrameEx (ceval.c:1561)\n==32632==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==32632==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n==32632==\n==32632== Use of uninitialised value of size 8\n==32632==    at 0x6116EA0: __gmpn_get_str (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)\n==32632==    by 0x7: ???\n==32632==    by 0xB961F7C: __pyx_f_py_7integer_7Integer_str (integer.c:3896)\n==32632==    by 0x415522: PyObject_Call (abstract.c:1860)\n==32632==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)\n==32632==    by 0xB95D4AB: __pyx_f_py_7integer_7Integer___repr__ (integer.c:3691)\n==32632==    by 0x443299: _PyObject_Str (object.c:406)\n==32632==    by 0x443A08: internal_print (object.c:426)\n==32632==    by 0x42999C: PyFile_WriteObject (fileobject.c:2178)\n==32632==    by 0x481C0C: PyEval_EvalFrameEx (ceval.c:1561)\n==32632==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)\n==32632==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)\n```\n\nBut I am not even sure if you are supposed to call the matrix constructor this way. I will investigate.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-18T11:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are a bunch of the following:

```
==32632== Conditional jump or move depends on uninitialised value(s)
==32632==    at 0x6116EC4: __gmpn_get_str (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)
==32632==    by 0x60FF327: __gmpz_get_str (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)
==32632==    by 0xB961F7C: __pyx_f_py_7integer_7Integer_str (integer.c:3896)
==32632==    by 0x415522: PyObject_Call (abstract.c:1860)
==32632==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==32632==    by 0xB95D4AB: __pyx_f_py_7integer_7Integer___repr__ (integer.c:3691)
==32632==    by 0x443299: _PyObject_Str (object.c:406)
==32632==    by 0x443A08: internal_print (object.c:426)
==32632==    by 0x42999C: PyFile_WriteObject (fileobject.c:2178)
==32632==    by 0x481C0C: PyEval_EvalFrameEx (ceval.c:1561)
==32632==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==32632==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
==32632==
==32632== Use of uninitialised value of size 8
==32632==    at 0x6116EA0: __gmpn_get_str (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)
==32632==    by 0x7: ???
==32632==    by 0xB961F7C: __pyx_f_py_7integer_7Integer_str (integer.c:3896)
==32632==    by 0x415522: PyObject_Call (abstract.c:1860)
==32632==    by 0x47C850: PyEval_CallObjectWithKeywords (ceval.c:3433)
==32632==    by 0xB95D4AB: __pyx_f_py_7integer_7Integer___repr__ (integer.c:3691)
==32632==    by 0x443299: _PyObject_Str (object.c:406)
==32632==    by 0x443A08: internal_print (object.c:426)
==32632==    by 0x42999C: PyFile_WriteObject (fileobject.c:2178)
==32632==    by 0x481C0C: PyEval_EvalFrameEx (ceval.c:1561)
==32632==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==32632==    by 0x483CC4: PyEval_EvalFrameEx (ceval.c:494)
```

But I am not even sure if you are supposed to call the matrix constructor this way. I will investigate.

Cheers,

Michael



---

archive/issue_comments_004660.json:
```json
{
    "body": "As is the code posted doesn't work:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.8.1, Release Date: 2007-10-21                     |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense\nsage: sage: a = Matrix_integer_dense.new(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/tmp/Work-mabshoff/sage-2.8.8/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: type object 'sage.matrix.matrix_integer_dense.Matrix_integer_de' has no attribute 'new'\n```\n\nIf I call\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.8.1, Release Date: 2007-10-21                     |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense\nsage: sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)\n```\n\nit works, but I am not certain I get the whole picture here. In any case the code clearly states that it is for internal use only and the elements are not initialized:\n\n```\n\n    def __new__(self, parent, entries, coerce, copy):\n        \"\"\"\n        Create and allocate memory for the matrix.  Does not actually initialize\n        any of the memory.\n\n        INPUT:\n            parent, entries, coerce, copy -- as for __init__.\n\n        EXAMPLES:\n            sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense\n            sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)\n            sage: type(a)\n            <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>\n\n        WARNING: This is for internal use only, or if you really know what you're doing.\n        \"\"\"\n```\n\nSo I would consider this invalid or wontfix. Any comments?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-23T23:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

As is the code posted doesn't work:

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.8.1, Release Date: 2007-10-21                     |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: sage: a = Matrix_integer_dense.new(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/tmp/Work-mabshoff/sage-2.8.8/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: type object 'sage.matrix.matrix_integer_dense.Matrix_integer_de' has no attribute 'new'
```

If I call

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.8.1, Release Date: 2007-10-21                     |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
sage: sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
```

it works, but I am not certain I get the whole picture here. In any case the code clearly states that it is for internal use only and the elements are not initialized:

```

    def __new__(self, parent, entries, coerce, copy):
        """
        Create and allocate memory for the matrix.  Does not actually initialize
        any of the memory.

        INPUT:
            parent, entries, coerce, copy -- as for __init__.

        EXAMPLES:
            sage: from sage.matrix.matrix_integer_dense import Matrix_integer_dense
            sage: a = Matrix_integer_dense.__new__(Matrix_integer_dense, Mat(ZZ,3), 0,0,0)
            sage: type(a)
            <type 'sage.matrix.matrix_integer_dense.Matrix_integer_dense'>

        WARNING: This is for internal use only, or if you really know what you're doing.
        """
```

So I would consider this invalid or wontfix. Any comments?

Cheers,

Michael



---

archive/issue_comments_004661.json:
```json
{
    "body": "This ticket is invalid.   In short, you should never ever use Matrix_integer_dense unless you know *precisely* what you are doing.\n\n If you want to make a matrix you either:\n   (1) use the \"matrix\" function,\n   (2) create a MatrixSpace and coerce something in,\n   (3) or do something else, e.g., use a __ private method **ONLY** if you know exactly what you are doing.\n\nThis ticket falls into (3).  You're diving into the internals of a C extension module and using a function that should never be used from the outside unless you really knows what you are doing.\n\nIn particular, almost all Cython extension classes have a __new__ method, and its purpose is to *allocate memory*, but not to initialize it.  Thus calling it directly will result in garbage.",
    "created_at": "2007-10-24T01:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4661",
    "user": "https://github.com/williamstein"
}
```

This ticket is invalid.   In short, you should never ever use Matrix_integer_dense unless you know *precisely* what you are doing.

 If you want to make a matrix you either:
   (1) use the "matrix" function,
   (2) create a MatrixSpace and coerce something in,
   (3) or do something else, e.g., use a __ private method **ONLY** if you know exactly what you are doing.

This ticket falls into (3).  You're diving into the internals of a C extension module and using a function that should never be used from the outside unless you really knows what you are doing.

In particular, almost all Cython extension classes have a __new__ method, and its purpose is to *allocate memory*, but not to initialize it.  Thus calling it directly will result in garbage.



---

archive/issue_events_002152.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-24T01:06:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/781#event-2152"
}
```



---

archive/issue_comments_004662.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-10-24T01:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4662",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_004663.json:
```json
{
    "body": "OK, I'm happy with that explanation.  I tripped over this during SD5, while fiddling with some ideas for Module code.  I probably had imported a bunch of stuff that let me call this by accident :-}.",
    "created_at": "2007-10-24T01:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/781#issuecomment-4663",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

OK, I'm happy with that explanation.  I tripped over this during SD5, while fiddling with some ideas for Module code.  I probably had imported a bunch of stuff that let me call this by accident :-}.



---

archive/issue_events_002153.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T03:57:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/781#event-2153"
}
```



---

archive/issue_events_002154.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T03:57:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/781",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/781#event-2154"
}
```
