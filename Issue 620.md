# Issue 620: memory still reachable in vector_rational_dense_21Vector_rational_dense__init

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-07 16:59:17

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

==8920== 1,612,736 bytes in 446 blocks are still reachable in loss record 2,367 of 2,372
==8920==    at 0x4A05A66: malloc (vg_replace_malloc.c:207)
==8920==    by 0x210A2D65: __pyx_f_21vector_rational_dense_21Vector_rational_dense__init (vector_rational_dense.c:770)
==8920==    by 0x210A0DE7: __pyx_tp_new_21vector_rational_dense_Vector_rational_dense (vector_rational_dense.c:865)
==8920==    by 0x45A272: type_call (typeobject.c:422)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==8920==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
==8920==    by 0x4865EF: PyEval_EvalCodeEx (ceval.c:2831)
==8920==    by 0x4CFED0: function_call (funcobject.c:517)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==8920==    by 0x41BE0C: instancemethod_call (classobject.c:2497)
==8920==    by 0x4156A2: PyObject_Call (abstract.c:1860)
==8920==    by 0x480783: PyEval_EvalFrameEx (ceval.c:3775)
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-09-07 16:59:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-03 14:06:02

It looks like the ModularSymbols_clear_cache() does nothing:

```
mabshoff`@`sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.11, Release Date: 2007-11-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: for i in range(3):
....:         print "start: ", get_memory_usage()
....:     m = ModularSymbols(501,2).decomposition(3);
....:     del m;
....:     print "deleted m: ", get_memory_usage()
....:     ModularSymbols_clear_cache();
....:     print "cache cleaned: ", get_memory_usage()
....:
start:  329.03515625
deleted m:  379.66015625
cache cleaned:  379.66015625
start:  379.66015625
deleted m:  391.63671875
cache cleaned:  391.63671875
start:  391.63671875
deleted m:  401.21484375
cache cleaned:  401.21484375
```

I had a quick look at the code and we play with weak references there, so that might be the cause. Same applies to #621.

Cheers,

Michael


---

Comment by kcrisman created at 2009-12-30 04:55:35

This is still a problem in Sage 4.3:

```
start:  162.12109375
deleted m:  185.9375
cache cleaned:  185.9375
start:  185.9375
deleted m:  194.11328125
cache cleaned:  194.11328125
start:  194.11328125
deleted m:  199.1328125
cache cleaned:  199.1328125
```



---

Comment by kcrisman created at 2013-06-12 21:18:53

It's not really clear to me how #621 is different, other than the valgrind output.  I recommend closing that ticket.


---

Comment by mmezzarobba created at 2014-02-15 15:35:11

Still present in sage-6.2.beta1.

It looks like tons of rings of integer modulo p and matrix spaces over these rings are kept alive, along with their whole coercion infrastructure. The fixes at #14711 (more precisely, 0af59ea93689cb6abb9d3fae0f1cf11f2aee5cca) are not enough to prevent this from happening.


---

Comment by mmezzarobba created at 2014-02-16 13:56:19

After a merging #14711 (actually `21aa9bc`) into `6.2.beta1` and applying the mercurial patch from #14072 on top, the memory leak gets under control. But it doesn't entirely disappear, as illustrated below. What happens is apparently that the entries of `sage.modular.hecke.algebra._cache` stay alive; I don't understand if it is intentional or not.


```
sage: import objgraph, inspect, random, gc
sage: objgraph.show_growth(limit=20)
...
sage: objgraph.show_most_common_types()
function                   26766
tuple                      10264
dict                       8604
method_descriptor          6292
weakref                    4856
list                       4330
wrapper_descriptor         3952
getset_descriptor          2638
builtin_function_or_method 2423
type                       2046
sage: for i in range(30):                   
         print get_memory_usage()
         m = ModularSymbols(501,2).decomposition(3)
         del m; ModularSymbols_clear_cache()
....:     
971.3828125
1052.734375
...
1087.4140625
...
1087.4140625
1087.671875
...
1087.1484375
sage: gc.collect()
11973
sage: gc.collect()
317
sage: gc.collect()
0
sage: objgraph.show_growth(limit=20)
tuple                         12128     +1897
function                      28505     +1739
dict                          10148     +1553
list                           5303      +983
Rational                        823      +794
ManinSymbol                     785      +785   <-----
weakref                        5481      +629
wrapper_descriptor             4367      +427
Vector_rational_dense           336      +336
KeyedRef                        939      +280
method_descriptor              6516      +225
cell                           1556      +209
getset_descriptor              2836      +202
builtin_function_or_method     2610      +188
MonoDictEraser                  446      +183
MonoDict                        446      +183
staticmethod                    739      +134
FormalSum                       113      +113
ModularSymbolsElement           113      +113   <-----
instance                        215      +106
```

