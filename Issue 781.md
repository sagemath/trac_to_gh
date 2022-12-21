# Issue 781: Matrix from Matrix_integer_dense() blows up (Dup of 799 for formatting)

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-10-02 02:41:13

Assignee: was

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



---

Comment by justin created at 2007-10-02 02:49:18

And, by '799', I mean '779'


---

Comment by mabshoff created at 2007-10-04 19:51:41

I will look into this, valgrind might turn up something interesting.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-04 19:51:41

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-10-18 11:03:34

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-18 11:11:45

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

Comment by mabshoff created at 2007-10-18 11:26:19

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

Comment by mabshoff created at 2007-10-23 23:47:58

As is the code posted doesn't work:

```
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.8.8$ ./sage
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
mabshoff`@`sage:/tmp/Work-mabshoff/sage-2.8.8$ ./sage
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

Comment by was created at 2007-10-24 01:06:37

This ticket is invalid.   In short, you should never ever use Matrix_integer_dense unless you know *precisely* what you are doing.

 If you want to make a matrix you either:
   (1) use the "matrix" function,
   (2) create a MatrixSpace and coerce something in,
   (3) or do something else, e.g., use a __ private method **ONLY** if you know exactly what you are doing.

This ticket falls into (3).  You're diving into the internals of a C extension module and using a function that should never be used from the outside unless you really knows what you are doing.

In particular, almost all Cython extension classes have a __new__ method, and its purpose is to *allocate memory*, but not to initialize it.  Thus calling it directly will result in garbage.


---

Comment by was created at 2007-10-24 01:06:41

Resolution: invalid


---

Comment by justin created at 2007-10-24 01:19:38

OK, I'm happy with that explanation.  I tripped over this during SD5, while fiddling with some ideas for Module code.  I probably had imported a bunch of stuff that let me call this by accident :-}.
