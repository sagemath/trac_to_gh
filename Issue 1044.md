# Issue 1044: segfault apply morphism to field element

Issue created by migration from https://trac.sagemath.org/ticket/1044

Original creator: was

Original creation time: 2007-10-31 21:22:55

Assignee: was


```
sage: K.<a> = NumberField(x^2 - 5)
sage: sigma = K.real_embeddings()
sage: def sig(z):
...       return (sigma[0](z), sigma[1](z))
...
sage: # Plot a bunch of points in the ring of integers.
sage: B = K.maximal_order().basis(); B
[1/2*a + 1/2, a]
sage: # A bug!!  :-(
sage: z = [sig(i*B[0] + j*B[1]) for i in [-3..3] for j in [-3..3]]
```


Results in a segmentation fault on 2.8.9 os x and 2.8.10 linux 64-bit. 


---

Comment by mabshoff created at 2007-11-01 01:25:21

Here is a backtrace:

```
#0  0x00002ba050f5e13a in __gmp_exception () from /tmp/Work-mabshoff/sage-2.8.10.alpha1/local/lib/libgmp.so.3
#1  0x00002ba050f5e15e in __gmp_divide_by_zero () from /tmp/Work-mabshoff/sage-2.8.10.alpha1/local/lib/libgmp.so.3
#2  0x00002ba050f76d9e in __gmpq_canonicalize () from /tmp/Work-mabshoff/sage-2.8.10.alpha1/local/lib/libgmp.so.3
#3  0x00002ba05aafdabd in __pyx_f_4sage_5rings_12number_field_30number_field_element_quadratic_28NumberFieldElement_quadratic_parts (__pyx_v_self=0x2ba061efca50, unused=0x0) at sage/rings/number_field/number_field_element_quadratic.cpp:1862
#4  0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#5  0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2ba061ef8998, arg=0x2ba04fc0b050, kw=0x0)
    at Python/ceval.c:3433
#6  0x00002ba05aafbec3 in __pyx_f_4sage_5rings_12number_field_30number_field_element_quadratic_28NumberFieldElement_quadratic__coefficients (__pyx_v_self=0x2ba061efca50, unused=0x0)
    at sage/rings/number_field/number_field_element_quadratic.cpp:3887
#7  0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#8  0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2ba061ef8710, arg=0x2ba04fc0b050, kw=0x0)
    at Python/ceval.c:3433
#9  0x00002ba05a9bc38c in __pyx_f_4sage_5rings_12number_field_20number_field_element_18NumberFieldElement_polynomial (
    __pyx_v_self=0x2ba061efca50, __pyx_args=0x2ba04fc0b050, __pyx_kwds=0x0)
    at sage/rings/number_field/number_field_element.cpp:5537
#10 0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#11 0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2ba061ef8560, arg=0x2ba04fc0b050, kw=0x0)
    at Python/ceval.c:3433
#12 0x00002ba05a9c3abd in __pyx_f_4sage_5rings_12number_field_20number_field_element_18NumberFieldElement__im_gens_ (
    __pyx_v_self=0x2ba061efca50, __pyx_args=0x2ba061ef52d8, __pyx_kwds=0x0)
    at sage/rings/number_field/number_field_element.cpp:2634
#13 0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#14 0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2ba06187b1b8, arg=0x2ba061ef52d8, kw=0x0)
    at Python/ceval.c:3433
#15 0x00002ba05f0ee37e in __pyx_f_4sage_5rings_8morphism_24RingHomomorphism_im_gens__call_c_impl (
    __pyx_v_self=0x2ba061eeb360, __pyx_v_x=0x2ba061efca50) at sage/rings/morphism.c:2683
#16 0x00002ba0543a00e6 in __pyx_f_4sage_10categories_8morphism_8Morphism__call_ (__pyx_v_self=0x2ba061eeb360,
    __pyx_v_x=0x2ba061efca50) at sage/categories/morphism.c:1631
#17 0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#18 0x000000000047c851 in PyEval_CallObjectWithKeywords (func=0x2ba061ef8518, arg=0x2ba06186c610, kw=0x0)
    at Python/ceval.c:3433
#19 0x00002ba0543a02f3 in __pyx_f_4sage_10categories_8morphism_8Morphism__call_c (__pyx_v_self=0x2ba061eeb360,
    __pyx_v_x=0x2ba061efca50) at sage/categories/morphism.c:1662
#20 0x00002ba05439fdd9 in __pyx_f_4sage_10categories_8morphism_8Morphism___call__ (__pyx_v_self=0x2ba061eeb360,
    __pyx_args=0x2ba061efa910, __pyx_kwds=0x0) at sage/categories/morphism.c:1598
#21 0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#22 0x0000000000456749 in slot_tp_call (self=<value optimized out>, args=0x2ba061efa910, kwds=0x0)
    at Objects/typeobject.c:4633
#23 0x0000000000415523 in PyObject_Call (func=0x2, arg=0x12eca40, kw=0x0) at Objects/abstract.c:1860
#24 0x0000000000481e92 in PyEval_EvalFrameEx (f=0x17aa980, throwflag=<value optimized out>) at Python/ceval.c:3775
#25 0x000000000048403b in PyEval_EvalFrameEx (f=0x177e400, throwflag=<value optimized out>) at Python/ceval.c:3650
#26 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba05f4e54e0, globals=<value optimized out>,
    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2831
#27 0x0000000000483cc5 in PyEval_EvalFrameEx (f=0x171fc20, throwflag=<value optimized out>) at Python/ceval.c:494
#28 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba053458dc8, globals=<value optimized out>,
    locals=<value optimized out>, args=0x17145f0, argcount=2, kws=0x1714600, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2831
#29 0x000000000048365d in PyEval_EvalFrameEx (f=0x1714450, throwflag=<value optimized out>) at Python/ceval.c:3660
#30 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba053458a08, globals=<value optimized out>,
    locals=<value optimized out>, args=0x1, argcount=3, kws=0x17185f0, kwcount=0, defs=0x2ba0536e4d10, defcount=2,
    closure=0x0) at Python/ceval.c:2831
#31 0x000000000048365d in PyEval_EvalFrameEx (f=0x1718440, throwflag=<value optimized out>) at Python/ceval.c:3660
#32 0x000000000048403b in PyEval_EvalFrameEx (f=0x1712e90, throwflag=<value optimized out>) at Python/ceval.c:3650
#33 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba05344c0a8, globals=<value optimized out>,
    locals=<value optimized out>, args=0x17125e8, argcount=2, kws=0x17125f8, kwcount=0, defs=0x2ba0537ff128, defcount=1,
    closure=0x0) at Python/ceval.c:2831
#34 0x000000000048365d in PyEval_EvalFrameEx (f=0x1712460, throwflag=<value optimized out>) at Python/ceval.c:3660
#35 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba05344c300, globals=<value optimized out>,
    locals=<value optimized out>, args=0x7ce7f0, argcount=2, kws=0x7ce800, kwcount=0, defs=0x2ba0537ff0e8, defcount=1,
    closure=0x0) at Python/ceval.c:2831
#36 0x000000000048365d in PyEval_EvalFrameEx (f=0x7ce660, throwflag=<value optimized out>) at Python/ceval.c:3660
#37 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba053315648, globals=<value optimized out>,
    locals=<value optimized out>, args=0x2, argcount=1, kws=0x6cf880, kwcount=2, defs=0x2ba053326800, defcount=2,
    closure=0x0) at Python/ceval.c:2831
#38 0x000000000048365d in PyEval_EvalFrameEx (f=0x6cf6f0, throwflag=<value optimized out>) at Python/ceval.c:3660
#39 0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2ba04fc2fb70, globals=<value optimized out>,
    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2831
#40 0x00000000004851d2 in PyEval_EvalCode (co=0x2, globals=0x12eca40, locals=0x0) at Python/ceval.c:494
#41 0x00000000004a648e in PyRun_FileExFlags (fp=0x6b74f0,
    filename=0x7fff5aeb7d19 "/tmp/Work-mabshoff/sage-2.8.10.alpha1/local/bin/sage-gdb-pythonstartup",
    start=<value optimized out>, globals=0x672390, locals=0x672390, closeit=0, flags=0x7fff5aeb5f40)
    at Python/pythonrun.c:1271
#42 0x00000000004a6720 in PyRun_SimpleFileExFlags (fp=0x6b74f0,
    filename=0x7fff5aeb7d19 "/tmp/Work-mabshoff/sage-2.8.10.alpha1/local/bin/sage-gdb-pythonstartup", closeit=0,
    flags=0x7fff5aeb5f40) at Python/pythonrun.c:877
#43 0x000000000041231a in Py_Main (argc=<value optimized out>, argv=<value optimized out>) at Modules/main.c:134
#44 0x00002ba0501c34ca in __libc_start_main () from /lib/libc.so.6
#45 0x000000000041163a in _start () at ../sysdeps/x86_64/elf/start.S:113
```



---

Comment by mabshoff created at 2007-11-01 01:35:06

This looks like a revisit of the "2*Singular('2')" coercion issue we had:

```
sage: B
[1/2*a + 1/2, a]
sage: B[0]
1/2*a + 1/2
sage: B[1]
a
sage: 1*B[0]


------------------------------------------------------------
Unhandled SIGFPE: An unhandled floating point exception occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Cheers,

Michael


---

Attachment

I've added an attachment that fixes the crash.  (I think the underlying problem might actually be in the coercion code, though.)


---

Comment by mabshoff created at 2007-11-01 10:07:03

applied to 2.8.11.alpha0 - the patch by Carl is a work around, for more discussion see

http://groups.google.com/group/sage-devel/t/2174d803e19c141e
http://groups.google.com/group/sage-devel/t/d49e60aaf7e91645

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-01 10:07:03

Resolution: fixed


---

Comment by robertwb created at 2007-11-01 21:14:46

The coercion model is working as expected. The error is because the base of order elements is Z (which is correctly enforced) but the _rmul_ is inherited from number_field_element which expects a rational. 


```
sage: sage: K.<a> = NumberField(x^2 - 5)
sage: sage: B = K.maximal_order().basis();
sage: B[1].parent().base_ring() # this is bad
Rational Field
sage: B[1].parent().base()
Integer Ring
```


See also Ticket #1057

- Robert
