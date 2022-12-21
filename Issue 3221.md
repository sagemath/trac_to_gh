# Issue 3221: libSingular segfaults Sage on startup on OSX 64

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-16 16:20:23

Assignee: malb

With a custom 3.0.2.alpha0 build [not all fixes are in Sage yet to actually build Sage out of the box] I get the following backtrace when I run `P.<x,y>=QQ[]` [I disabled some default imports so Sage doesn't segfault on startup]:

```

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<x,y>=QQ[]
| SAGE Version 3.0.2.alpha0, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_INVALID_ADDRESS at address: 0x0000000000000018
0x0000000107baa12b in omInsertBinPage [inlined] () at om_Alloc.c:109
109           after->next->prev = page;
(gdb) bt
Function omInsertBinPage was inlined into function omAllocBinFromFullPage at line 145.
#1  0x0000000107baa12b in omAllocBinFromFullPage (bin=0x107517050) at om_Alloc.c:145
#2  0x0000000107ba86fe in __omDebugAlloc (size_bin=0x107517050, flags=<value temporarily unavailable, due to optimizations>, track=<value temporarily unavailable, due to optimizations>, f=<value temporarily unavailable, due to optimizations>, l=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#3  0x0000000107b943d3 in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_27MPolynomialRing_libsingular___init__ (__pyx_v_self=0x10990ec30, __pyx_args=<value temporarily unavailable, due to optimizations>, __pyx_kwds=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#4  0x000000010005dfbc in type_call (type=0x107517050, args=0x10011b500, kwds=0x2) at om_Alloc.c:145
#5  0x000000010000710b in PyObject_Call (func=<value temporarily unavailable, due to optimizations>, arg=<value temporarily unavailable, due to optimizations>, kw=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#6  0x000000010009ae39 in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#7  0x000000010009e049 in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#8  0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=2, kws=0x0, kwcount=0, defs=0x105168af8, defcount=6, closure=0x0) at om_Alloc.c:145
#9  0x000000010002b469 in function_call (func=0x10528bc80, arg=0x10982a320, kw=0x10011b500) at om_Alloc.c:145
#10 0x000000010000710b in PyObject_Call (func=<value temporarily unavailable, due to optimizations>, arg=<value temporarily unavailable, due to optimizations>, kw=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#11 0x0000000101e6e447 in __pyx_pf_4sage_5rings_4ring_4Ring___getitem__ (__pyx_v_self=0x101ba8200, __pyx_v_x=0x10011b500) at om_Alloc.c:145
#12 0x000000010000710b in PyObject_Call (func=<value temporarily unavailable, due to optimizations>, arg=<value temporarily unavailable, due to optimizations>, kw=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#13 0x0000000100066fff in call_method (o=0x101ba8200, name=<value temporarily unavailable, due to optimizations>, nameobj=0x100153400, format=0x1000edc2b "(O)") at om_Alloc.c:145
#14 0x00000001000997d2 in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#15 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at om_Alloc.c:145
#16 0x000000010009d915 in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#17 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=2, kws=0x1086fb7d0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at om_Alloc.c:145
#18 0x000000010009c78c in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#19 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=3, kws=0x10990b110, kwcount=0, defs=0x101968d58, defcount=2, closure=0x0) at om_Alloc.c:145
#20 0x000000010009c78c in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#21 0x000000010009e049 in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#22 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=2, kws=0x100272228, kwcount=0, defs=0x1019712a8, defcount=1, closure=0x0) at om_Alloc.c:145
#23 0x000000010009c78c in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#24 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=2, kws=0x1002c46d0, kwcount=0, defs=0x101971268, defcount=1, closure=0x0) at om_Alloc.c:145
#25 0x000000010009c78c in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#26 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=1, kws=0x100217500, kwcount=2, defs=0x101823ec0, defcount=2, closure=0x0) at om_Alloc.c:145
#27 0x000000010009c78c in PyEval_EvalFrameEx (f=0x2, throwflag=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#28 0x000000010009e776 in PyEval_EvalCodeEx (co=0x2, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>, args=0x10011b500, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at om_Alloc.c:145
#29 0x000000010009e9d6 in PyEval_EvalCode (co=<value temporarily unavailable, due to optimizations>, globals=<value temporarily unavailable, due to optimizations>, locals=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#30 0x00000001000c3641 in PyRun_FileExFlags (fp=0x7fff70600b20, filename=0x10990ec30 "\001", start=<value temporarily unavailable, due to optimizations>, globals=0x100206790, locals=0x100206790, closeit=0, flags=0x10011b500) at om_Alloc.c:145
#31 0x00000001000c3991 in PyRun_SimpleFileExFlags (fp=<value temporarily unavailable, due to optimizations>, filename=0x107bc9ee0 "", closeit=1160448, flags=0x7fff5fbfdf70) at om_Alloc.c:145
#32 0x00000001000ce5db in Py_Main (argc=<value temporarily unavailable, due to optimizations>, argv=<value temporarily unavailable, due to optimizations>) at om_Alloc.c:145
#33 0x0000000100001248 in _start ()
#34 0x0000000100001161 in start ()
(gdb)                                                                                                   }}}



---

Comment by mabshoff created at 2008-05-19 13:29:08

The solution here is to compile [lib]Singular with "--with-malloc=system" in 64 bit mode on OSX.

Cheers,

Michale


---

Comment by mabshoff created at 2008-05-19 13:29:08

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-19 13:29:08

Changing assignee from malb to mabshoff.


---

Comment by mabshoff created at 2008-08-19 22:47:42

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 22:47:42

This is fixed by the spkg at #3194.

Cheers,

Michael
