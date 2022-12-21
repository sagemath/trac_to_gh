# Issue 562: memleak in Matrix_integer_dense__zero_out_matrix exposed by ModularSymbols(n,sign=1).decomposition()

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 00:19:15

Assignee: mabshoff

Hello folks,

```
for n in range(10,100): a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

causes (among other things) the following:

```
==5107== 133,912 bytes in 16,739 blocks are definitely lost in loss record 2,832 of 2,944
==5107==    at 0x4A05809: malloc (vg_replace_malloc.c:149)
==5107==    by 0x94A2697: __gmpz_init (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libgmp.so.3.4.1)
==5107==    by 0x203F822F: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__zero_out_matrix (matrix_integer_dense.c:46
35)
==5107==    by 0x20426114: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense___init__ (matrix_integer_dense.c:3755)
==5107==    by 0x45A321: type_call (typeobject.c:436)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==5107==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==5107==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==5107==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==5107==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==5107==    by 0x4CFED0: function_call (funcobject.c:517)
==5107==    by 0x4156A2: PyObject_Call (abstract.c:1860)
```

Cheers,

Tagged for 2.8.4

Michael


---

Comment by mabshoff created at 2007-09-02 00:30:09

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-03 12:49:00

Mmmh, it looks like a matrix over ZZ isn't properly deallocated in Sage's python code. I looked at all the path and the deallocation seems to work correctly. William did mention something about this in IRC a couple days ago.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-03 12:57:38

I have to correct myself. Doing a 

```
sage: for I in range(1000):
....:     a = Matrix(ZZ,2,[1,2,3,4])
....:     del a
```

vs. 

```
sage: for I in range(1000):
....:     a = Matrix(ZZ,2,[1,2,3,4])
```

leads to identical numbers when valgrinding. My guess is that the leak must be somewhere in the Cython code when initializing a matrix filled with zeros without deallocating it.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-07 17:07:39

Resolution: duplicate


---

Comment by mabshoff created at 2007-09-07 17:07:39

Am am an idiot, because I just opened a duplicate of the same problem at #619. Since the descrition is better over there I am closing this one as duplicate.

Cheers,

Michael
