# Issue 1380: subs in the MPolynomial_libsingular insists on taking things to QQ

Issue created by migration from https://trac.sagemath.org/ticket/1380

Original creator: jbmohler

Original creation time: 2007-12-03 10:01:35

Assignee: was

The following code should not give an error:

```
sage: R.<x,y>=QQ[]
sage: x.subs(x=1/y)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
...
<type 'exceptions.TypeError'>: no implicit coercion of element to the rational numbers
```


As evidence, I give,

```
sage: R.<x,y>=ZZ[]
sage: x.subs(x=1/y)
1/y
```

which makes perfect sense to me.



---

Comment by jbmohler created at 2007-12-03 10:01:52

Changing assignee from was to malb.


---

Comment by jbmohler created at 2007-12-03 10:01:52

Changing component from algebraic geometry to commutative algebra.


---

Comment by mabshoff created at 2007-12-03 10:39:19

Well, I think this exposes a more severe issue. It certainly looks like a familiar pattern and on Solaris I get a segfault:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.14, Release Date: 2007-11-24                      |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<x,y>=QQ[]
sage: x.subs(x=1/y)


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

I tend to believe that this is related to or the same bug as #1325.


---

Comment by mabshoff created at 2007-12-03 10:39:19

Changing priority from major to blocker.


---

Comment by mabshoff created at 2007-12-03 10:41:26

Backtrace from neron:

```
#0  0xfc65f980 in nlPower (x=0xfc396018, exp=5, u=0x0) at longrat.cc:932
#1  0xfc89629c in __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__cmp_c_impl (
    __pyx_v_left=0x23b57e0, __pyx_v_right=0x23b57e0) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:13105
#2  0xfe12d600 in __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (__pyx_v_left=0x23b57e0,
    __pyx_v_right=0x23b57e0, __pyx_v_op=2) at sage/structure/element.c:5394
#3  0xfe158350 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x23b57e0, __pyx_v_right=0x23b57e0,
    __pyx_v_op=2) at sage/structure/element.c:5151
#4  0xfc88c75c in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___richcmp__ (
    __pyx_v_left=0x23b57e0, __pyx_v_right=0x23b57e0, __pyx_v_op=2)
    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:12840
#5  0x00055ee4 in PyObject_RichCompare (v=0x23b57e0, w=0x23b57e0, op=2) at Objects/object.c:905
#6  0xfe1afd38 in __pyx_pf_4sage_9structure_6parent_7EltPair___eq__ (__pyx_self=<value optimized out>,
    __pyx_args=<value optimized out>, __pyx_kwds=<value optimized out>) at sage/structure/parent.c:6541
#7  0x000ee73c in PyCFunction_Call (func=0x5a7df0, arg=0x23affa8, kw=0xfc8f9110) at Objects/methodobject.c:77
#8  0x0002268c in PyObject_Call (func=0x5a7df0, arg=0x23affa8, kw=0x0) at Objects/abstract.c:1860
#9  0x000294c4 in instancemethod_call (func=0x5a7df0, arg=0x23affa8, kw=0x0) at Objects/classobject.c:2497
#10 0x0002268c in PyObject_Call (func=0x1, arg=0x23affa8, kw=0x0) at Objects/abstract.c:1860
#11 0x000952e8 in PyEval_CallObjectWithKeywords (func=0x2442210, arg=0x23b4e10, kw=0x0) at Python/ceval.c:3433
#12 0x0002ad88 in half_richcompare (v=0x23b0f80, w=0x23b0a80, op=<value optimized out>) at Objects/classobject.c:1925
#13 0x0002b0ac in instance_richcompare (v=0x23b0f80, w=0x23b0a80, op=2) at Objects/classobject.c:1938
#14 0x00053fdc in try_rich_compare (v=0x23b0f80, w=0x23b0a80, op=2) at Objects/object.c:577
#15 0x00055e80 in PyObject_RichCompare (v=0x23b0f80, w=0x23b0a80, op=2) at Objects/object.c:874
#16 0x00056248 in PyObject_RichCompareBool (v=0x23b0f80, w=0x23b0a80, op=2) at Objects/object.c:948
#17 0x00044d84 in listremove (self=0x5a7300, v=0x23b0a80) at Objects/listobject.c:2256
#18 0x000ee698 in PyCFunction_Call (func=0x23afa30, arg=0x23a6410, kw=0x0) at Objects/methodobject.c:93
#19 0x0002268c in PyObject_Call (func=0x23afa30, arg=0x23a6410, kw=0x5a7300) at Objects/abstract.c:1860
#20 0x000952e8 in PyEval_CallObjectWithKeywords (func=0x23afa30, arg=0x23a6410, kw=0x0) at Python/ceval.c:3433
#21 0xfe1abdfc in __pyx_f_4sage_9structure_6parent__unregister_pair (__pyx_v_x=0x23b57e0, __pyx_v_y=0x1315c00)
    at sage/structure/parent.c:6955
#22 0xfe1b8718 in __pyx_f_4sage_9structure_6parent_6Parent_get_action_c_impl (__pyx_v_self=0x130f8a0, __pyx_v_S=0x5f65e0,
    __pyx_v_op=0x1ec030, __pyx_v_self_on_left=0) at sage/structure/parent.c:3106
#23 0xfe1ab838 in __pyx_f_4sage_9structure_6parent_6Parent_get_action_c (__pyx_v_self=0x130f8a0, __pyx_v_S=0x5f65e0,
    __pyx_v_op=0x1ec030, __pyx_v_self_on_left=0) at sage/structure/parent.c:2011
#24 0xfe0a95f0 in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_discover_action_c (__pyx_v_self=0x5e3c10,
    __pyx_v_R=0x5f65e0, __pyx_v_S=0x130f8a0, __pyx_v_op=0x1ec080) at sage/structure/coerce.c:8236
#25 0xfe09ce74 in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_get_action_c (__pyx_v_self=0x5e3c10,
    __pyx_v_R=0x5f65e0, __pyx_v_S=0x130f8a0, __pyx_v_op=0x1ec080) at sage/structure/coerce.c:7900
#26 0xfe0c48a0 in __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (__pyx_v_self=0x5e3c10,
    __pyx_v_x=0x1308a20, __pyx_v_y=0x23b5840, __pyx_v_op=0x1ec080) at sage/structure/coerce.c:5813
#27 0xfe154780 in __pyx_pf_4sage_9structure_7element_11RingElement___div__ (__pyx_v_self=0x1308a20,
    __pyx_v_right=0x23b5840) at sage/structure/element.c:10234
#28 0x00022cd4 in binary_op1 (v=0x1308a20, w=0xfc396000, op_slot=12) at Objects/abstract.c:398
#29 0x00024158 in PyNumber_Divide (v=0x1308a20, w=0x23b5840) at Objects/abstract.c:450
#30 0x0009a0c8 in PyEval_EvalFrameEx (f=0x242a608, throwflag=<value optimized out>) at Python/ceval.c:1083
#31 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23b1218, globals=<value optimized out>, locals=<value optimized out>, args=0x0,
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#32 0x0009cd20 in PyEval_EvalFrameEx (f=0x23f3260, throwflag=<value optimized out>) at Python/ceval.c:494
#33 0x0009dcf8 in PyEval_EvalCodeEx (co=0x507de8, globals=<value optimized out>, locals=<value optimized out>,
    args=0x23fbd94, argcount=2, kws=0x23fbd9c, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#34 0x0009b670 in PyEval_EvalFrameEx (f=0x23fbc48, throwflag=<value optimized out>) at Python/ceval.c:3660
#35 0x0009dcf8 in PyEval_EvalCodeEx (co=0x507d58, globals=<value optimized out>, locals=<value optimized out>,
    args=0x23f6738, argcount=3, kws=0x23f6744, kwcount=0, defs=0x57f1f4, defcount=2, closure=0x0) at Python/ceval.c:2831
#36 0x0009b670 in PyEval_EvalFrameEx (f=0x23f65f0, throwflag=<value optimized out>) at Python/ceval.c:3660
#37 0x0009c920 in PyEval_EvalFrameEx (f=0x23f8a58, throwflag=<value optimized out>) at Python/ceval.c:3650
#38 0x0009dcf8 in PyEval_EvalCodeEx (co=0x507a88, globals=<value optimized out>, locals=<value optimized out>,
    args=0x23fb748, argcount=2, kws=0x23fb750, kwcount=0, defs=0x57d47c, defcount=1, closure=0x0) at Python/ceval.c:2831
#39 0x0009b670 in PyEval_EvalFrameEx (f=0x23fb608, throwflag=<value optimized out>) at Python/ceval.c:3660
#40 0x0009dcf8 in PyEval_EvalCodeEx (co=0x507968, globals=<value optimized out>, locals=<value optimized out>,
    args=0x295d8c, argcount=2, kws=0x295d94, kwcount=0, defs=0x57d45c, defcount=1, closure=0x0) at Python/ceval.c:2831
#41 0x0009b670 in PyEval_EvalFrameEx (f=0x295c48, throwflag=<value optimized out>) at Python/ceval.c:3660
#42 0x0009dcf8 in PyEval_EvalCodeEx (co=0x4a8608, globals=<value optimized out>, locals=<value optimized out>,
    args=0x1cfce0, argcount=1, kws=0x15a038, kwcount=2, defs=0x4b8884, defcount=2, closure=0x0) at Python/ceval.c:2831
#43 0x0009b670 in PyEval_EvalFrameEx (f=0x19f898, throwflag=<value optimized out>) at Python/ceval.c:3660
#44 0x0009dcf8 in PyEval_EvalCodeEx (co=0x17b4e8, globals=<value optimized out>, locals=<value optimized out>, args=0x0,
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#45 0x0009e00c in PyEval_EvalCode (co=0x17b4e8, globals=0x16ad20, locals=0x16ad20) at Python/ceval.c:494
#46 0x000c1bd0 in PyRun_FileExFlags (fp=0x14c308,
    filename=0xffbffc2c "/tmp/Work-mabshoff/sage-2.8.14/local/bin/sage-gdb-pythonstartup", start=<value optimized out>,
    globals=0x16ad20, locals=0x16ad20, closeit=<value optimized out>, flags=0xffbff27c) at Python/pythonrun.c:1271
#47 0x000c1e60 in PyRun_SimpleFileExFlags (fp=0x14c308,
    filename=0xffbffc2c "/tmp/Work-mabshoff/sage-2.8.14/local/bin/sage-gdb-pythonstartup", closeit=0, flags=0xffbff27c)
    at Python/pythonrun.c:877
#48 0x0001e81c in Py_Main (argc=2, argv=0xffbff2f4) at Modules/main.c:134
#49 0x0001d9b0 in _start ()
```


Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2007-12-18 21:21:15

Merged in 2.9.1.alpha1


---

Comment by rlm created at 2007-12-18 21:21:15

Resolution: fixed
