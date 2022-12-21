# Issue 454: VERY SEVERE memory leaks, probably in linear algebra -- exposed by modular symbols functionality

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-19 08:42:08

Assignee: was

To see some VERY SEVERE memory leaks, probably in linear algebra -- exposed by modular symbols functionality do the following. 

  1. comment out the line "_cache[key] = weakref.ref(M)" in sage/modular/modsym/modsym.py
  2. build and observe:
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()
174.125
191.1796875
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()
191.1796875
197.6875
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(2); del m; get_memory_usage()
197.6875
203.5546875
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; get_memory_usage()
203.546875
208.12890625
sage: get_memory_usage(); m = ModularSymbols(501,2).decomposition(3); del m; get_memory_usage()
208.12890625
210.41796875

}}}


---

Comment by was created at 2007-08-19 08:46:47

Changing priority from major to critical.


---

Comment by was created at 2007-08-19 08:46:47

Changing component from algebraic geometry to linear algebra.


---

Comment by mabshoff created at 2007-08-19 23:53:35

Hello William,

I did valgrind that exact example three times in a row in the same sage session and I got:

==14358== LEAK SUMMARY:
==14358==    definitely lost: 3,297,622 bytes in 194,267 blocks.
==14358==    indirectly lost: 703,345 bytes in 4,603 blocks.
==14358==      possibly lost: 387,022 bytes in 984 blocks.
==14358==    still reachable: 153,105,982 bytes in 1,028,503 blocks.
==14358==         suppressed: 0 bytes in 0 blocks.

The complete log is at http://sage.math.washington.edu/home/mabshoff/sage-2.8.1-ticket-454.valgrind

Just search for "indirectly" and "definitely" to see the most interesting bits. Problems are all over the map: sparse & dense matricies, gmp allocations, LinBox Wrapper and so.

Let me know if you need any help.

I changed the Milestone to 2.8.2 - feel free to assign it to 3.0 if you feel that the 2.8.2 release cuts it too close.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-29 22:56:09

Ok,

various bits and pieces have been broken out into different tickets and fixed. We should revisit this ticket during Bug Day 2 and see what is left.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-29 22:56:09

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-08-29 22:56:09

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-08-30 00:41:31

Changing priority from critical to major.


---

Comment by mabshoff created at 2007-10-16 03:09:46

A status update for Sage 2.8.7.rc1:

code run:

```
for n in range(10,100):
  a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

Before:

```
==29058== LEAK SUMMARY:
==29058==    definitely lost: 1,210,265 bytes in 113,436 blocks.
==29058==    indirectly lost: 420,632 bytes in 7,210 blocks.
==29058==      possibly lost: 375,630 bytes in 1,188 blocks.
==29058==    still reachable: 92,961,383 bytes in 1,342,309 blocks.
```

After Patch 1 (fix for #619):

```
==13453== LEAK SUMMARY:
==13453==    definitely lost: 1,075,235 bytes in 96,549 blocks.
==13453==    indirectly lost: 419,640 bytes in 7,212 blocks.
==13453==      possibly lost: 376,270 bytes in 1,195 blocks.
==13453==    still reachable: 92,923,804 bytes in 1,342,166 blocks.
==13453==         suppressed: 0 bytes in 0 blocks.
```

After Patch 2 (burcin's fix for #561):

```
==15147== LEAK SUMMARY:
==15147==    definitely lost: 1,072,216 bytes in 96,412 blocks.
==15147==    indirectly lost: 419,120 bytes in 7,205 blocks.
==15147==      possibly lost: 376,558 bytes in 1,194 blocks.
==15147==    still reachable: 92,977,412 bytes in 1,342,343 blocks.
==15147==         suppressed: 0 bytes in 0 blocks.
```

Remaining leak: mix of LinBox and

```
==15147== 94,288 bytes in 11,786 blocks are definitely lost in loss record 2,401 of 2,546
==15147==    at 0x4A1BB35: malloc (vg_replace_malloc.c:207)
==15147==    by 0x610A9A6: __gmpq_init (in /tmp/Work-mabshoff/sage-2.8.7.rc1/local/lib/libgmp.so.3.4.1)
==15147==    by 0x12EC8E22: __pyx_f_22matrix_rational_sparse_allocate_mpq_vector (matrix_rational_sparse.c:5519)
==15147==    by 0x12ECC464: __pyx_f_22matrix_rational_sparse_mpq_vector_set_entry (matrix_rational_sparse.c:6560)
==15147==    by 0x12ECC5F5: __pyx_f_22matrix_rational_sparse_22Matrix_rational_sparse_set_unsafe (matrix_rational_sparse.c:8
668)
==15147==    by 0x114ED321: __pyx_mp_ass_subscript_7matrix0_Matrix (matrix0.c:2339)
==15147==    by 0x47F046: PyEval_EvalFrameEx (ceval.c:1497)
==15147==    by 0x484F3A: PyEval_EvalCodeEx (ceval.c:2831)
==15147==    by 0x48365C: PyEval_EvalFrameEx (ceval.c:3660)
==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
==15147==    by 0x48403A: PyEval_EvalFrameEx (ceval.c:3650)
```



---

Comment by mabshoff created at 2007-10-28 22:13:01

With 2.8.10.rc1 (which applied #1024) we get:

```
==15811== LEAK SUMMARY:
==15811==    definitely lost: 406,088 bytes in 5,792 blocks.
==15811==    indirectly lost: 415,504 bytes in 7,199 blocks.
==15811==      possibly lost: 382,110 bytes in 1,198 blocks.
==15811==    still reachable: 93,391,247 bytes in 1,343,745 blocks.
==15811==         suppressed: 0 bytes in 0 blocks.
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-29 04:38:55

Once #1026 is merged we will have:

```
==19741== LEAK SUMMARY:
==19741==    definitely lost: 11,608 bytes in 352 blocks.
==19741==    indirectly lost: 286,560 bytes in 390 blocks.
==19741==      possibly lost: 463,342 bytes in 879 blocks.
==19741==    still reachable: 71,109,048 bytes in 1,285,713 blocks.
==19741==         suppressed: 0 bytes in 0 blocks.
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-26 15:56:38

With Sage 2.9.1.1 we get:

```
==29169==    definitely lost: 1,237 bytes in 54 blocks.
==29169==    indirectly lost: 7,704 bytes in 345 blocks.
==29169==      possibly lost: 407,801 bytes in 991 blocks.
==29169==    still reachable: 74,012,699 bytes in 1,287,766 blocks.
==29169==         suppressed: 0 bytes in 0 blocks.
```

The remaining definitely & indirectly lost are all due to known problems in LinBox when using Givaro.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 05:06:22

With the updated givaro.spkg from #2525 the leak in LinBox that was caused by Givaro is gone. Hence once that ticket is merged we cam close this old, long overdue ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-15 06:44:33

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 06:44:33

Closed in Sage 2.10.4.alpha0

Since #2524 has been merged this is in effect fixed. #2525 does fix some other issues, but not the memory leak that is the last one left.

Many people have contributed to fixing this ticket over a seven month period:

 * Michael Abshoff
 * Martin Albrecht
 * Burcin Erocal
 * Willem Jan Palenstijn
 * Clement Pernet
 * William Stein 

It is good to have reached the end of this journey.

Cheers,

Michael
