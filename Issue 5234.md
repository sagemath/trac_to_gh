# Issue 5234: doctest failure in devel/sage/sage/rings/real_lazy.pyx

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2009-02-11 20:32:00

Assignee: mabshoff

with 3.3.rc0, on gentoo running on an amd64:


```
./sage -t -verbose  "devel/sage/sage/rings/real_lazy.pyx"
[...]
Trying:
    a = RLF(pi) + RLF(sqrt(Integer(1)/Integer(2)))###line 650:_sage_    >>> a = RLF(pi) + RLF(sqrt(1/2))
Expecting nothing
ok
Trying:
    loads(dumps(a)) == a###line 651:_sage_    >>> loads(dumps(a)) == a
Expecting:
    True
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
[...]
```




---

Comment by wjp created at 2009-02-11 20:41:12

backtrace:


```
Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x2ac187c86060 (LWP 6614)]
0x00002ac19060f35d in __pyx_tp_dealloc_4sage_9structure_7element_Element (
    o=0x3e07e60) at sage/structure/element.c:18962
18962     Py_XDECREF(((PyObject *)p->_parent));
(gdb) bt
#0  0x00002ac19060f35d in __pyx_tp_dealloc_4sage_9structure_7element_Element (
    o=0x3e07e60) at sage/structure/element.c:18962
#1  0x0000000000484dff in PyEval_EvalFrameEx (f=0x38a6530, 
    throwflag=<value optimized out>) at Python/ceval.c:2023
#2  0x00000000004886b2 in PyEval_EvalCodeEx (co=0x3206990, 
    globals=<value optimized out>, locals=<value optimized out>, args=0x0, 
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2836
#3  0x00000000004873f2 in PyEval_EvalFrameEx (f=0x32eac20, 
    throwflag=<value optimized out>) at Python/ceval.c:494
#4  0x00000000004886b2 in PyEval_EvalCodeEx (co=0x3122288, 
    globals=<value optimized out>, locals=<value optimized out>, 
    args=0x3091e48, argcount=5, kws=0x0, kwcount=0, defs=0x0, defcount=0, 
    closure=0x0) at Python/ceval.c:2836
#5  0x00000000004d1e18 in function_call (func=0x312f848, arg=0x3091e30, kw=0x0)
    at Objects/funcobject.c:517
#6  0x0000000000417d13 in PyObject_Call (func=0x3e07e60, arg=0x262ab90, 
    kw=0xd24293065676173) at Objects/abstract.c:1861
#7  0x000000000041e44d in instancemethod_call (func=<value optimized out>, 
    arg=0x3091e30, kw=0x0) at Objects/classobject.c:2519
#8  0x0000000000417d13 in PyObject_Call (func=0x3e07e60, arg=0x262ab90, 
    kw=0xd24293065676173) at Objects/abstract.c:1861
#9  0x00000000004856ba in PyEval_EvalFrameEx (f=0x32ea9c0, 
    throwflag=<value optimized out>) at Python/ceval.c:3784
#10 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x311c828, 
    globals=<value optimized out>, locals=<value optimized out>, 
    args=0x3317b70, argcount=5, kws=0x3317b98, kwcount=0, defs=0x0, 
    defcount=0, closure=0x0) at Python/ceval.c:2836
#11 0x0000000000486877 in PyEval_EvalFrameEx (f=0x3317930, 
    throwflag=<value optimized out>) at Python/ceval.c:3669
#12 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x3122300, 
    globals=<value optimized out>, locals=<value optimized out>, 
    args=0x3123a60, argcount=4, kws=0x0, kwcount=0, defs=0x0, defcount=0, 
    closure=0x0) at Python/ceval.c:2836
#13 0x00000000004d1e18 in function_call (func=0x312f8c0, arg=0x3123a48, kw=0x0)
    at Objects/funcobject.c:517
#14 0x0000000000417d13 in PyObject_Call (func=0x3e07e60, arg=0x262ab90, 
    kw=0xd24293065676173) at Objects/abstract.c:1861
#15 0x000000000041e44d in instancemethod_call (func=<value optimized out>, 
    arg=0x3123a48, kw=0x0) at Objects/classobject.c:2519
#16 0x0000000000417d13 in PyObject_Call (func=0x3e07e60, arg=0x262ab90, 
    kw=0xd24293065676173) at Objects/abstract.c:1861
#17 0x00000000004856ba in PyEval_EvalFrameEx (f=0x330d370, 
    throwflag=<value optimized out>) at Python/ceval.c:3784
#18 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x311c7b0, 
    globals=<value optimized out>, locals=<value optimized out>, 
    args=0x36251a0, argcount=4, kws=0x36251c0, kwcount=0, defs=0x0, 
    defcount=0, closure=0x0) at Python/ceval.c:2836
#19 0x0000000000486877 in PyEval_EvalFrameEx (f=0x3624ff0, 
    throwflag=<value optimized out>) at Python/ceval.c:3669
#20 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x3122468, 
    globals=<value optimized out>, locals=<value optimized out>, args=0x5, 
    argcount=2, kws=0x38797d0, kwcount=3, defs=0x3128478, defcount=3, 
    closure=0x0) at Python/ceval.c:2836
#21 0x00000000004d1db1 in function_call (func=0x312fa28, arg=0x309ef38, 
    kw=0x313bd10) at Objects/funcobject.c:517
#22 0x0000000000417d13 in PyObject_Call (func=0x3e07e60, arg=0x262ab90, 
    kw=0xd24293065676173) at Objects/abstract.c:1861
#23 0x000000000041e44d in instancemethod_call (func=<value optimized out>, 
    arg=0x309ef38, kw=0x313bd10) at Objects/classobject.c:2519
#24 0x0000000000417d13 in PyObject_Call (func=0x3e07e60, arg=0x262ab90, 
    kw=0xd24293065676173) at Objects/abstract.c:1861
#25 0x00000000004856ba in PyEval_EvalFrameEx (f=0x3624dd0, 
    throwflag=<value optimized out>) at Python/ceval.c:3784
#26 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x311c738, 
    globals=<value optimized out>, locals=<value optimized out>, args=0x5, 
    argcount=2, kws=0x1e2df50, kwcount=0, defs=0x3119f18, defcount=3, 
    closure=0x0) at Python/ceval.c:2836
#27 0x0000000000486877 in PyEval_EvalFrameEx (f=0x1e2dd60, 
    throwflag=<value optimized out>) at Python/ceval.c:3669
#28 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x3122dc8, 
    globals=<value optimized out>, locals=<value optimized out>, args=0xa, 
    argcount=0, kws=0x1e2dc90, kwcount=10, defs=0x3099e38, defcount=10, 
    closure=0x0) at Python/ceval.c:2836
#29 0x0000000000486877 in PyEval_EvalFrameEx (f=0x1e2dac0, 
    throwflag=<value optimized out>) at Python/ceval.c:3669
#30 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x311c990, 
    globals=<value optimized out>, locals=<value optimized out>, args=0xa, 
    argcount=1, kws=0x76ff08, kwcount=3, defs=0x3099ca0, defcount=10, 
    closure=0x0) at Python/ceval.c:2836
#31 0x0000000000486877 in PyEval_EvalFrameEx (f=0x76fd80, 
    throwflag=<value optimized out>) at Python/ceval.c:3669
#32 0x00000000004886b2 in PyEval_EvalCodeEx (co=0x2ac187fcddc8, 
    globals=<value optimized out>, locals=<value optimized out>, args=0x0, 
---Type <return> to continue, or q <return> to quit---
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2836
#33 0x0000000000488952 in PyEval_EvalCode (co=0x3e07e60, globals=0x262ab90, 
    locals=0xd24293065676173) at Python/ceval.c:494
#34 0x00000000004a9e1e in PyRun_FileExFlags (fp=0x752010, 
    filename=0x7fff23c23304 "/data2/wpalenst/sage-3.3.rc0/tmp/.doctest_real_lazy.py", start=<value optimized out>, globals=0x775640, locals=0x775640, 
    closeit=1, flags=0x7fff23c22a20) at Python/pythonrun.c:1273
#35 0x00000000004aa0b0 in PyRun_SimpleFileExFlags (fp=0x752010, 
    filename=0x7fff23c23304 "/data2/wpalenst/sage-3.3.rc0/tmp/.doctest_real_lazy.py", closeit=1, flags=0x7fff23c22a20) at Python/pythonrun.c:879
#36 0x0000000000414650 in Py_Main (argc=<value optimized out>, 
    argv=0x7fff23c22b48) at Modules/main.c:523
#37 0x00002ac187963b74 in __libc_start_main () from /lib/libc.so.6
#38 0x0000000000413b89 in _start ()
```



---

Comment by jsp created at 2009-02-11 20:46:13

On Ubuntu 8.10, 32 bits:


```
(gdb) backtrace
#0  0x00000000 in ?? ()
#1  0xb72952d4 in __pyx_tp_dealloc_4sage_9structure_7element_Element
(o=0xad9bfec) at sage/structure/element.c:18963
#2  0xb53dc9d4 in __pyx_tp_dealloc_4sage_5rings_9real_lazy_LazyWrapper
(o=0xad9bfec) at sage/rings/real_lazy.c:11677
#3  0x080c95a3 in PyEval_EvalFrameEx (f=0xa914d1c, throwflag=0) at
Python/ceval.c:2023
#4  0x080cf755 in PyEval_EvalCodeEx (co=0xad3ad58, globals=0xaa79714,
locals=0xaa79714, args=0x0, argcount=0, kws=0x0,
   kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#5  0x080cd5a6 in PyEval_EvalFrameEx (f=0xa765164, throwflag=0) at
Python/ceval.c:494
#6  0x080cf755 in PyEval_EvalCodeEx (co=0xa651da0, globals=0xa64dcec,
locals=0x0, args=0xa6500c8, argcount=5, kws=0x0,
   kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#7  0x0811671e in function_call (func=0xa65c844, arg=0xa6500bc,
kw=0x0) at Objects/funcobject.c:517
#8  0x0805d7e7 in PyObject_Call (func=0xad625f0, arg=0xa6500bc,
kw=0x0) at Objects/abstract.c:1861
#9  0x080639fa in instancemethod_call (func=0xa65c844, arg=0xa6500bc,
kw=0x0) at Objects/classobject.c:2519
#10 0x0805d7e7 in PyObject_Call (func=0xad625f0, arg=0xa6500bc,
kw=0x0) at Objects/abstract.c:1861
---Type <return> to continue, or q <return> to quit---c
#11 0x080cb836 in PyEval_EvalFrameEx (f=0xa666e9c, throwflag=0) at
Python/ceval.c:3784
#12 0x080cf755 in PyEval_EvalCodeEx (co=0xa620c80, globals=0xa64d9bc,
locals=0x0, args=0xa8a9eb0, argcount=5,
   kws=0xa8a9ec4, kwcount=0, defs=0x0, defcount=0, closure=0x0) at
Python/ceval.c:2836
#13 0x080ce0c7 in PyEval_EvalFrameEx (f=0xa8a9d14, throwflag=0) at
Python/ceval.c:3669
#14 0x080cf755 in PyEval_EvalCodeEx (co=0xa651de8, globals=0xa64dcec,
locals=0x0, args=0xa653c68, argcount=4, kws=0x0,
   kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#15 0x0811671e in function_call (func=0xa65c87c, arg=0xa653c5c,
kw=0x0) at Objects/funcobject.c:517
#16 0x0805d7e7 in PyObject_Call (func=0xad625f0, arg=0xa653c5c,
kw=0x0) at Objects/abstract.c:1861
#17 0x080639fa in instancemethod_call (func=0xa65c87c, arg=0xa653c5c,
kw=0x0) at Objects/classobject.c:2519
#18 0x0805d7e7 in PyObject_Call (func=0xad625f0, arg=0xa653c5c,
kw=0x0) at Objects/abstract.c:1861
#19 0x080cb836 in PyEval_EvalFrameEx (f=0xa8a91dc, throwflag=0) at
Python/ceval.c:3784
#20 0x080cf755 in PyEval_EvalCodeEx (co=0xa620380, globals=0xa64d9bc,
locals=0x0, args=0xaa3f5b0, argcount=4,
   kws=0xaa3f5c0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at
Python/ceval.c:2836
---Type <return> to continue, or q <return> to quit---c
#21 0x080ce0c7 in PyEval_EvalFrameEx (f=0xaa3f45c, throwflag=0) at
Python/ceval.c:3669
#22 0x080cf755 in PyEval_EvalCodeEx (co=0xa651f08, globals=0xa64dcec,
locals=0x0, args=0xa63a0f8, argcount=2,
   kws=0xab62338, kwcount=3, defs=0xa653dd0, defcount=3, closure=0x0)
at Python/ceval.c:2836
#23 0x081166a6 in function_call (func=0xa65c924, arg=0xa63a0ec,
kw=0xa6b58ac) at Objects/funcobject.c:517
#24 0x0805d7e7 in PyObject_Call (func=0xad625f0, arg=0xa63a0ec,
kw=0xa6b58ac) at Objects/abstract.c:1861
#25 0x080639fa in instancemethod_call (func=0xa65c924, arg=0xa63a0ec,
kw=0xa6b58ac) at Objects/classobject.c:2519
#26 0x0805d7e7 in PyObject_Call (func=0xad625f0, arg=0xa63a0ec,
kw=0xa6b58ac) at Objects/abstract.c:1861
#27 0x080cb836 in PyEval_EvalFrameEx (f=0xaa3f2d4, throwflag=0) at
Python/ceval.c:3784
#28 0x080cf755 in PyEval_EvalCodeEx (co=0xa620608, globals=0xa64d9bc,
locals=0x0, args=0xa6712a0, argcount=2,
   kws=0xa6712a8, kwcount=0, defs=0xa653510, defcount=3, closure=0x0)
at Python/ceval.c:2836
#29 0x080ce0c7 in PyEval_EvalFrameEx (f=0xa671134, throwflag=0) at
Python/ceval.c:3669
#30 0x080cf755 in PyEval_EvalCodeEx (co=0xa655608, globals=0xa64dcec,
locals=0x0, args=0xa6f4a58, argcount=0,
   kws=0xa6f4a58, kwcount=10, defs=0xa6571f8, defcount=10,
closure=0x0) at Python/ceval.c:2836
---Type <return> to continue, or q <return> to quit---
#31 0x080ce0c7 in PyEval_EvalFrameEx (f=0xa6f48f4, throwflag=0) at
Python/ceval.c:3669
#32 0x080cf755 in PyEval_EvalCodeEx (co=0xa620de8, globals=0xa64d9bc,
locals=0x0, args=0x8aa0130, argcount=1,
   kws=0x8aa0134, kwcount=3, defs=0xa657038, defcount=10,
closure=0x0) at Python/ceval.c:2836
#33 0x080ce0c7 in PyEval_EvalFrameEx (f=0x8a9fff4, throwflag=0) at
Python/ceval.c:3669
#34 0x080cf755 in PyEval_EvalCodeEx (co=0xb7e734e8,
globals=0xb7ea2acc, locals=0xb7ea2acc, args=0x0, argcount=0, kws=0x0,
   kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2836
#35 0x080cf967 in PyEval_EvalCode (co=0xb7e734e8, globals=0xb7ea2acc,
locals=0xb7ea2acc) at Python/ceval.c:494
#36 0x080ed13f in PyRun_FileExFlags (fp=0x8a94008,
   filename=0xbfba0123
"/home/jaap/downloads/sage-3.3.alpha3/tmp/.doctest_real_lazy.py",
start=257, globals=0xb7ea2acc,
   locals=0xb7ea2acc, closeit=1, flags=0xbfb9e1c8) at Python/pythonrun.c:1273
#37 0x080ed40a in PyRun_SimpleFileExFlags (fp=0x8a94008,
   filename=0xbfba0123
"/home/jaap/downloads/sage-3.3.alpha3/tmp/.doctest_real_lazy.py",
closeit=1, flags=0xbfb9e1c8)
   at Python/pythonrun.c:879
---Type <return> to continue, or q <return> to quit---
#38 0x0805960b in Py_Main (argc=1, argv=0xbfb9e294) at Modules/main.c:523
#39 0x08058992 in main (argc=0, argv=0x0) at ./Modules/python.c:23
(gdb)
```



---

Comment by wjp created at 2009-02-14 22:39:48

I did a binary search through the hg commits between alpha6 and rc0. This segfault first shows up after the commit titled "Second pass at sage_input -- support more types" (rev11589 in the rc0 hg repo).

Specifically, it is triggered after starting at rev11588 and moving only sage/misc/sage_input.py and any of sage/rings/infinity.py, sage/rings/rational.pyx, sage/rings/rational_field.py, sage/rings/real_double.pyx, sage/rings/real_mpfr.pyx to rev11589.

This seems to be 100% reproducable on my system, but I don't see the logic behind it, or how sage_input would effect this crash.


---

Comment by mabshoff created at 2009-03-01 02:21:36

Resolution: invalid


---

Comment by mabshoff created at 2009-03-01 02:21:36

Ok, neither Jaap nor wjp reported this in subsequent builds, so invalid. If it happens again please open another ticket. The problem is likely deep inside Sage when garbage collection is doing odd things with some weekly referenced structures, but without a testcase this is invalid. 

Cheers,

Michael
