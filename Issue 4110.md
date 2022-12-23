# Issue 4110: Memory leak in saving matrices

Issue created by migration from https://trac.sagemath.org/ticket/4110

Original creator: rlm

Original creation time: 2008-09-13 19:00:31

Assignee: tbd

CC:  malb

This is in sage-3.1.2.rc1.

If I do

```
sage: L = [random_matrix(GF(2), 20, 20) for _ in xrange(10^5)]
```

then my process is here:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND          
15889 rlmill    25   0  446m 131m  17m S    0  0.2   0:06.30 sage-ipython
```


Then I do the following:

```
sage: save(L, 'crap')
sage: del L
```


And my process is here:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND          
15889 rlmill    16   0 1471m 1.1g  17m S    0  1.8   1:02.37 sage-ipython
```



---

Comment by rlm created at 2008-09-13 19:01:11

Changing assignee from tbd to mabshoff.


---

Comment by rlm created at 2008-09-13 19:01:11

Changing component from algebra to memleak.


---

Comment by mabshoff created at 2008-09-13 22:02:24

Oops, with `10^4` elements:

```
==27766== LEAK SUMMARY:
==27766==    definitely lost: 73,004,158 bytes in 10,007 blocks.
==27766==    indirectly lost: 5,586,420 bytes in 209,482 blocks.
==27766==      possibly lost: 402,505 bytes in 1,011 blocks.
==27766==    still reachable: 36,106,357 bytes in 217,055 blocks.
==27766==         suppressed: 305,691 bytes in 4,843 blocks.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 00:02:26

Before:

```
==27766== LEAK SUMMARY:
==27766==    definitely lost: 73,004,158 bytes in 10,007 blocks.
==27766==    indirectly lost: 5,586,420 bytes in 209,482 blocks.
==27766==      possibly lost: 402,505 bytes in 1,011 blocks.
==27766==    still reachable: 36,106,357 bytes in 217,055 blocks.
==27766==         suppressed: 305,691 bytes in 4,843 blocks.
```

Specifically:

```
==27766== 78,589,900 (73,003,480 direct, 5,586,420 indirect) bytes in 9,995 blocks are definitely lost in loss record 13,758 of 13,758
==27766==    at 0x4A1BDEB: malloc (vg_replace_malloc.c:207)
==27766==    by 0x16A44C5E: gdMalloc (gdhelpers.c:85)
==27766==    by 0x16A2E130: gdImageCreate (gd.c:83)
==27766==    by 0x166C828B: __pyx_pf_4sage_6matrix_17matrix_mod2_dense_17Matrix_mod2_dense___reduce__ (matrix_mod2_dense.c:6925)
==27766==    by 0x415832: PyObject_Call (abstract.c:1861)
==27766==    by 0x47D750: PyEval_CallObjectWithKeywords (ceval.c:3442)
==27766==    by 0x458C0F: object_reduce_ex (typeobject.c:2867)
==27766==    by 0x415832: PyObject_Call (abstract.c:1861)
==27766==    by 0x7D86723: save (cPickle.c:2498)
==27766==    by 0x7D87ECC: batch_list (cPickle.c:1561)
==27766==    by 0x7D86C5B: save (cPickle.c:1629)
==27766==    by 0x7D88587: cpm_dumps (cPickle.c:2580)
```


After:

```
==29605== LEAK SUMMARY:
==29605==    definitely lost: 678 bytes in 12 blocks.
==29605==      possibly lost: 369,938 bytes in 975 blocks.
==29605==    still reachable: 36,091,754 bytes in 216,569 blocks.
==29605==         suppressed: 305,691 bytes in 4,843 blocks.
```



---

Comment by mabshoff created at 2008-09-14 00:02:26

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-09-14 02:24:28

Resolution: fixed


---

Comment by mabshoff created at 2008-09-14 02:24:28

Merged in Sage 3.1.2.rc3
