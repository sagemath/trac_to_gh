# Issue 3908: [with patch, needs review] fix major memory leak in fast_float

Issue created by migration from https://trac.sagemath.org/ticket/3908

Original creator: cwitty

Original creation time: 2008-08-20 02:57:54

Assignee: jkantor

Currently there is a major memory leak in fast_float because it uses `__del__` instead of `__dealloc__`.  (Python uses `__del__`, Cython uses `__dealloc__`.)

Before:

```
sage: from sage.ext.fast_eval import fast_float_constant
sage: get_memory_usage()
117.859375
sage: print sum([fast_float_constant(3.0)] * 2000)
<sage.ext.fast_eval.FastDoubleFunc object at 0xb7ab4b54>
sage: get_memory_usage()
163.6328125
```


After:

```
sage: from sage.ext.fast_eval import fast_float_constant
sage: get_memory_usage()
117.859375
sage: print sum([fast_float_constant(3.0)] * 2000)
<sage.ext.fast_eval.FastDoubleFunc object at 0xb7b18b54>
sage: get_memory_usage()
117.98828125
```




---

Attachment


---

Comment by mabshoff created at 2008-08-20 18:22:22

This patch actually makes it worse: Before:

```
==12210== LEAK SUMMARY:
==12210==    definitely lost: 152,380 bytes in 5,433 blocks.
==12210==      possibly lost: 338,476 bytes in 965 blocks.
==12210==    still reachable: 34,336,340 bytes in 211,430 blocks.
==12210==         suppressed: 300,797 bytes in 4,764 blocks.
```

After:

```
==25373== LEAK SUMMARY:
==25373==    definitely lost: 311,287 bytes in 5,364 blocks.
==25373==      possibly lost: 338,986 bytes in 969 blocks.
==25373==    still reachable: 34,331,200 bytes in 211,437 blocks.
==25373==         suppressed: 0 bytes in 0 blocks.
==25373== Rerun with --leak-check=full to see details of leaked memory.
```


:(

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-20 18:37:39

Mmmh, it seems that having suppression enabled only works with --leak-check=full, so I need to investigate here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-20 19:22:52

Positive review. It does not fix all the issue, but it reduces the problem significantly:

```
==12941== LEAK SUMMARY:
==12941==    definitely lost: 7,300 bytes in 600 blocks.
==12941==    indirectly lost: 3,483 bytes in 5 blocks.
==12941==      possibly lost: 338,598 bytes in 964 blocks.
==12941==    still reachable: 34,339,261 bytes in 211,436 blocks.
==12941==         suppressed: 300,797 bytes in 4,764 blocks.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-08-21 18:51:02

Resolution: fixed


---

Comment by mabshoff created at 2008-08-21 18:51:02

Merged in Sage 3.1.2.alpha0
