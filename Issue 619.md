# Issue 619: memleak in Matrix_integer_dense__zero_out_matrix

Issue created by migration from https://trac.sagemath.org/ticket/619

Original creator: mabshoff

Original creation time: 2007-09-07 16:56:00

Assignee: mabshoff

This is caused when running Sage 2.8.3.6+malb's fix for #566:

```
for i in range(3):
    get_memory_usage()
    m = ModularSymbols(501,2).decomposition(3); 
    del m; ModularSymbols_clear_cache(); 
    get_memory_usage()
```

and results in 

```
==8920== LEAK SUMMARY:
==8920==    definitely lost: 1,518,830 bytes in 183,739 blocks.
==8920==    indirectly lost: 288,408 bytes in 610 blocks.
==8920==      possibly lost: 489,439 bytes in 1,002 blocks.
==8920==    still reachable: 160,311,066 bytes in 872,845 blocks.
==8920==         suppressed: 0 bytes in 0 blocks.
```

The exact problem:

```
==8920== 1,435,632 bytes in 179,454 blocks are definitely lost in loss record 2,365 of 2,372
==8920==    at 0x4A05A66: malloc (vg_replace_malloc.c:207)
==8920==    by 0x95A4697: __gmpz_init (in /tmp/Work2/sage-2.8.3.6-clean/local/lib/libgmp.so.3.4.1)
==8920==    by 0x205E040F: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense__zero_out_matrix (matrix_integer_dense.c:46
49)
==8920==    by 0x2060E1E4: __pyx_f_20matrix_integer_dense_20Matrix_integer_dense___init__ (matrix_integer_dense.c:3769)
==8920==    by 0x45A321: type_call (typeobject.c:436)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==8920==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==8920==    by 0x4845B3: PyEval_EvalFrameEx (ceval.c:3660)
==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==8920==    by 0x4CFED0: function_call (funcobject.c:517)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-09-07 16:59:39

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-09 02:52:09

Well, _zero_out_matrix is not the cause, but the leaks happen down the road so to speak. For some info see 

http://groups.google.com/group/sage-devel/t/b946f7a49eb0dd23

Cheers,

Michael


---

Comment by burcin created at 2007-09-21 00:30:32

With the current release, 2.8.4.2.1, the output of valgrind for the given code doesn't contain the string "zero_out". I suppose this was fixed along the way.


---

Comment by burcin created at 2007-09-21 00:30:32

Resolution: worksforme


---

Attachment


---

Comment by mabshoff created at 2007-10-16 03:00:53

Code run:

```
for i in range(3):
    get_memory_usage()
    m = ModularSymbols(501,2).decomposition(3); 
    del m; ModularSymbols_clear_cache(); 
    get_memory_usage()
```

Before:

```
==29325== LEAK SUMMARY:
==29325==    definitely lost: 1,450,402 bytes in 182,205 blocks.
==29325==    indirectly lost: 389,280 bytes in 386 blocks.
==29325==      possibly lost: 357,750 bytes in 874 blocks.
==29325==    still reachable: 70,513,431 bytes in 1,284,573 blocks.
==29325==         suppressed: 0 bytes in 0 blocks.
```

After applying this patch and the one from #561:

```
==15358== LEAK SUMMARY:
==15358==    definitely lost: 11,519 bytes in 2,386 blocks.
==15358==    indirectly lost: 384,464 bytes in 385 blocks.
==15358==      possibly lost: 360,446 bytes in 872 blocks.
==15358==    still reachable: 70,528,918 bytes in 1,284,388 blocks.
==15358==         suppressed: 0 bytes in 0 blocks.
```


"definitely & indirectly lost" memory can nearly all be attributed to LinBox in this case!


---

Comment by mabshoff created at 2007-10-16 03:03:17

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-16 03:03:17

Resolution changed from worksforme to 


---

Comment by mabshoff created at 2007-10-16 03:03:24

Changing status from reopened to new.


---

Comment by mabshoff created at 2007-10-16 03:04:11

Changing status from new to assigned.


---

Comment by was created at 2007-10-20 19:16:01

Resolution: fixed
