# Issue 1325: 2.8.14/Solaris: rings/polynomial/multi_polynomial_libsingular.pyx doctest failure

archive/issues_001325.json:
```json
{
    "body": "Assignee: @malb\n\nSee also http://groups.google.com/group/sage-devel/t/2ebfa37291bcb6e4\n\n```\nmabshoff@neron sage-2.8.14$ ./sage -t -gdb  devel/sage/rings/polynomial/multi_polynomial_libsingular.pyx\nERROR: File ./devel/sage/rings/polynomial/multi_polynomial_libsingular.pyx is missing\nexit code: 1\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        ./devel/sage/rings/polynomial/multi_polynomial_libsingular.pyx\nTotal time for all tests: 0.0 seconds\nmabshoff@neron sage-2.8.14$ ./sage -t -gdb  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx\nsage -t -gdb devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx\n********************************************************************************\nType r at the (gdb) prompt to run the doctests.\nType bt if there is a crash to see a traceback.\n********************************************************************************\nGNU gdb 6.6\nCopyright (C) 2006 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"sparc-sun-solaris2.9\"...\n(gdb) r\nStarting program: /tmp/Work-mabshoff/sage-2.8.14/local/bin/python .doctest_multi_polynomial_libsingular.py\nwarning: Lowest section in /usr/lib/libintl.so.1 is .hash at 00000074\n\nProgram received signal SIGSEGV, Segmentation fault.\n0xfc65f980 in nlPower (x=0xfc396018, exp=5, u=0x0) at longrat.cc:932\n932     longrat.cc: No such file or directory.\n        in longrat.cc\nCurrent language:  auto; currently c++\n(gdb) bt\n#0  0xfc65f980 in nlPower (x=0xfc396018, exp=5, u=0x0) at longrat.cc:932\n#1  0xfc89629c in __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__cmp_c_impl (\n    __pyx_v_left=0x24baea0, __pyx_v_right=0x179aba0) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:13105\n#2  0xfe15d600 in __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (__pyx_v_left=0x24baea0,\n    __pyx_v_right=0x179aba0, __pyx_v_op=2) at sage/structure/element.c:5394\n#3  0xfe188350 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x24baea0, __pyx_v_right=0x179aba0,\n    __pyx_v_op=2) at sage/structure/element.c:5151\n#4  0xfe165b18 in __pyx_pf_4sage_9structure_7element_7Element__richcmp_ (__pyx_v_left=0x24baea0, __pyx_args=0x17a0120,\n    __pyx_kwds=<value optimized out>) at sage/structure/element.c:4593\n#5  0x000ee73c in PyCFunction_Call (func=0x24500a8, arg=0x17a0120, kw=0x2) at Objects/methodobject.c:77\n#6  0x0002268c in PyObject_Call (func=0x24500a8, arg=0x17a0120, kw=0x24baea0) at Objects/abstract.c:1860\n#7  0x000952e8 in PyEval_CallObjectWithKeywords (func=0x24500a8, arg=0x17a0120, kw=0x0) at Python/ceval.c:3433\n#8  0xfe189f7c in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x24baea0, __pyx_v_right=0x24bacc0,\n    __pyx_v_op=2) at sage/structure/element.c:4776\n#9  0xfc88c75c in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___richcmp__ (\n    __pyx_v_left=0x24baea0, __pyx_v_right=0x24bacc0, __pyx_v_op=2)\n    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:12840\n#10 0x00055ee4 in PyObject_RichCompare (v=0x24baea0, w=0x24bacc0, op=2) at Objects/object.c:905\n#11 0x00098b68 in PyEval_EvalFrameEx (f=0x2942448, throwflag=<value optimized out>) at Python/ceval.c:3980\n#12 0x0009dcf8 in PyEval_EvalCodeEx (co=0x24c8380, globals=<value optimized out>, locals=<value optimized out>, args=0x0,\n    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#13 0x0009cd20 in PyEval_EvalFrameEx (f=0x29bfee0, throwflag=<value optimized out>) at Python/ceval.c:494\n#14 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23cf698, globals=<value optimized out>, locals=<value optimized out>,\n    args=0x24819a4, argcount=4, kws=0x24819b4, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#15 0x0009b670 in PyEval_EvalFrameEx (f=0x2481850, throwflag=<value optimized out>) at Python/ceval.c:3660\n#16 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23cf800, globals=<value optimized out>, locals=<value optimized out>,\n    args=0x2408244, argcount=2, kws=0x240824c, kwcount=0, defs=0x2450d84, defcount=3, closure=0x0) at Python/ceval.c:2831\n#17 0x0009b670 in PyEval_EvalFrameEx (f=0x24080d8, throwflag=<value optimized out>) at Python/ceval.c:3660\n#18 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23cfe30, globals=<value optimized out>, locals=<value optimized out>,\n    args=0x1cfc60, argcount=1, kws=0x16ad20, kwcount=3, defs=0x23cce3c, defcount=9, closure=0x0) at Python/ceval.c:2831\n#19 0x0009b670 in PyEval_EvalFrameEx (f=0x24df20, throwflag=<value optimized out>) at Python/ceval.c:3660\n#20 0x0009dcf8 in PyEval_EvalCodeEx (co=0x1e05c0, globals=<value optimized out>, locals=<value optimized out>, args=0x0,\n    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#21 0x0009e00c in PyEval_EvalCode (co=0x1e05c0, globals=0x16ad20, locals=0x16ad20) at Python/ceval.c:494\n#22 0x000c1bd0 in PyRun_FileExFlags (fp=0x14c308, filename=0xffbff4f0 \".doctest_multi_polynomial_libsingular.py\",\n    start=<value optimized out>, globals=0x16ad20, locals=0x16ad20, closeit=<value optimized out>, flags=0xffbff2d4)\n    at Python/pythonrun.c:1271\n#23 0x000c1e60 in PyRun_SimpleFileExFlags (fp=0x14c308, filename=0xffbff4f0 \".doctest_multi_polynomial_libsingular.py\",\n    closeit=1, flags=0xffbff2d4) at Python/pythonrun.c:877\n#24 0x0001e5d8 in Py_Main (argc=2, argv=0xffbff34c) at Modules/main.c:523\n#25 0x0001d9b0 in _start ()\n(gdb)\n(gdb) q\nThe program is running.  Exit anyway? (y or n) y\n\n         [42.7 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 42.7 seconds\n```\n\n\nSome more observations:\n\n```\nmabshoff@neron sage-2.8.14$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.14, Release Date: 2007-11-24                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R.<x,y>=MPolynomialRing(QQ,2)\nsage: A = matrix([[Integer(1),x], [y,Integer(1)]])\nsage: A\n\n[1 x]\n[y 1]\nsage: A*A\n\n[x*y + 1     2*x]\n[    2*y x*y + 1]\nsage: A**2\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\nWhen using ZZ as a coefficient ring the problem goes away:\n\nmabshoff@neron sage-2.8.14$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.14, Release Date: 2007-11-24                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: R.<x,y>=MPolynomialRing(ZZ,2)\nsage: A = matrix([[Integer(1),x], [y,Integer(1)]])\nsage: A\n\n[1 x]\n[y 1]\nsage: A*A\n\n[x*y + 1     2*x]\n[    2*y x*y + 1]\nsage: A**2\n\n[x*y + 1     2*x]\n[    2*y x*y + 1]\nsage: A**10\n\n[x^5*y^5 + 45*x^4*y^4 + 210*x^3*y^3 + 210*x^2*y^2 + 45*x*y + 1\n10*x^5*y^4 + 120*x^4*y^3 + 252*x^3*y^2 + 120*x^2*y + 10*x]\n[    10*x^4*y^5 + 120*x^3*y^4 + 252*x^2*y^3 + 120*x*y^2 + 10*y x^5*y^5\n+ 45*x^4*y^4 + 210*x^3*y^3 + 210*x^2*y^2 + 45*x*y + 1]\nsage:\n\nThese issues seems to rely on matrices, i.e. \"just\" polynomials does\nwork:\n\nmabshoff@neron sage-2.8.14$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.14, Release Date: 2007-11-24                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: R.<x,y>=MPolynomialRing(QQ,2)\nsage:             sage: f = x^3 + y\nsage: f*f\nx^6 + 2*x^3*y + y^2\nsage: f^2\nx^6 + 2*x^3*y + y^2\nsage: f**2\nx^6 + 2*x^3*y + y^2\nsage: f**10\nx^30 + 10*x^27*y + 45*x^24*y^2 + 120*x^21*y^3 + 210*x^18*y^4 +\n252*x^15*y^5 + 210*x^12*y^6 + 120*x^9*y^7 + 45*x^6*y^8 + 10*x^3*y^9 +\ny^10\nsage:\nExiting SAGE (CPU time 0m0.03s, Wall time 0m29.97s).\n```\n\nAnd ideas? I know malb is on his way to Paris shortly, but I have\nwasted a tremendous amount of time playing with 2.8.14 on Solaris\ninstead of doing \"real\" work since I wanted 2.8.15 to come close to\ncompilable out of the box on Solaris. We might get close to\ncompilable, but are certainly way off on the doctests at the moment\n\nCheers,\n\nMichael \n\nIssue created by migration from https://trac.sagemath.org/ticket/1325\n\n",
    "created_at": "2007-11-28T21:54:58Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "2.8.14/Solaris: rings/polynomial/multi_polynomial_libsingular.pyx doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1325",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

See also http://groups.google.com/group/sage-devel/t/2ebfa37291bcb6e4

```
mabshoff@neron sage-2.8.14$ ./sage -t -gdb  devel/sage/rings/polynomial/multi_polynomial_libsingular.pyx
ERROR: File ./devel/sage/rings/polynomial/multi_polynomial_libsingular.pyx is missing
exit code: 1

----------------------------------------------------------------------
The following tests failed:


        ./devel/sage/rings/polynomial/multi_polynomial_libsingular.pyx
Total time for all tests: 0.0 seconds
mabshoff@neron sage-2.8.14$ ./sage -t -gdb  devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx
sage -t -gdb devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx
********************************************************************************
Type r at the (gdb) prompt to run the doctests.
Type bt if there is a crash to see a traceback.
********************************************************************************
GNU gdb 6.6
Copyright (C) 2006 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "sparc-sun-solaris2.9"...
(gdb) r
Starting program: /tmp/Work-mabshoff/sage-2.8.14/local/bin/python .doctest_multi_polynomial_libsingular.py
warning: Lowest section in /usr/lib/libintl.so.1 is .hash at 00000074

Program received signal SIGSEGV, Segmentation fault.
0xfc65f980 in nlPower (x=0xfc396018, exp=5, u=0x0) at longrat.cc:932
932     longrat.cc: No such file or directory.
        in longrat.cc
Current language:  auto; currently c++
(gdb) bt
#0  0xfc65f980 in nlPower (x=0xfc396018, exp=5, u=0x0) at longrat.cc:932
#1  0xfc89629c in __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__cmp_c_impl (
    __pyx_v_left=0x24baea0, __pyx_v_right=0x179aba0) at sage/rings/polynomial/multi_polynomial_libsingular.cpp:13105
#2  0xfe15d600 in __pyx_f_4sage_9structure_7element_7Element__richcmp_c_impl (__pyx_v_left=0x24baea0,
    __pyx_v_right=0x179aba0, __pyx_v_op=2) at sage/structure/element.c:5394
#3  0xfe188350 in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x24baea0, __pyx_v_right=0x179aba0,
    __pyx_v_op=2) at sage/structure/element.c:5151
#4  0xfe165b18 in __pyx_pf_4sage_9structure_7element_7Element__richcmp_ (__pyx_v_left=0x24baea0, __pyx_args=0x17a0120,
    __pyx_kwds=<value optimized out>) at sage/structure/element.c:4593
#5  0x000ee73c in PyCFunction_Call (func=0x24500a8, arg=0x17a0120, kw=0x2) at Objects/methodobject.c:77
#6  0x0002268c in PyObject_Call (func=0x24500a8, arg=0x17a0120, kw=0x24baea0) at Objects/abstract.c:1860
#7  0x000952e8 in PyEval_CallObjectWithKeywords (func=0x24500a8, arg=0x17a0120, kw=0x0) at Python/ceval.c:3433
#8  0xfe189f7c in __pyx_f_4sage_9structure_7element_7Element__richcmp (__pyx_v_left=0x24baea0, __pyx_v_right=0x24bacc0,
    __pyx_v_op=2) at sage/structure/element.c:4776
#9  0xfc88c75c in __pyx_pf_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular___richcmp__ (
    __pyx_v_left=0x24baea0, __pyx_v_right=0x24bacc0, __pyx_v_op=2)
    at sage/rings/polynomial/multi_polynomial_libsingular.cpp:12840
#10 0x00055ee4 in PyObject_RichCompare (v=0x24baea0, w=0x24bacc0, op=2) at Objects/object.c:905
#11 0x00098b68 in PyEval_EvalFrameEx (f=0x2942448, throwflag=<value optimized out>) at Python/ceval.c:3980
#12 0x0009dcf8 in PyEval_EvalCodeEx (co=0x24c8380, globals=<value optimized out>, locals=<value optimized out>, args=0x0,
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#13 0x0009cd20 in PyEval_EvalFrameEx (f=0x29bfee0, throwflag=<value optimized out>) at Python/ceval.c:494
#14 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23cf698, globals=<value optimized out>, locals=<value optimized out>,
    args=0x24819a4, argcount=4, kws=0x24819b4, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#15 0x0009b670 in PyEval_EvalFrameEx (f=0x2481850, throwflag=<value optimized out>) at Python/ceval.c:3660
#16 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23cf800, globals=<value optimized out>, locals=<value optimized out>,
    args=0x2408244, argcount=2, kws=0x240824c, kwcount=0, defs=0x2450d84, defcount=3, closure=0x0) at Python/ceval.c:2831
#17 0x0009b670 in PyEval_EvalFrameEx (f=0x24080d8, throwflag=<value optimized out>) at Python/ceval.c:3660
#18 0x0009dcf8 in PyEval_EvalCodeEx (co=0x23cfe30, globals=<value optimized out>, locals=<value optimized out>,
    args=0x1cfc60, argcount=1, kws=0x16ad20, kwcount=3, defs=0x23cce3c, defcount=9, closure=0x0) at Python/ceval.c:2831
#19 0x0009b670 in PyEval_EvalFrameEx (f=0x24df20, throwflag=<value optimized out>) at Python/ceval.c:3660
#20 0x0009dcf8 in PyEval_EvalCodeEx (co=0x1e05c0, globals=<value optimized out>, locals=<value optimized out>, args=0x0,
    argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#21 0x0009e00c in PyEval_EvalCode (co=0x1e05c0, globals=0x16ad20, locals=0x16ad20) at Python/ceval.c:494
#22 0x000c1bd0 in PyRun_FileExFlags (fp=0x14c308, filename=0xffbff4f0 ".doctest_multi_polynomial_libsingular.py",
    start=<value optimized out>, globals=0x16ad20, locals=0x16ad20, closeit=<value optimized out>, flags=0xffbff2d4)
    at Python/pythonrun.c:1271
#23 0x000c1e60 in PyRun_SimpleFileExFlags (fp=0x14c308, filename=0xffbff4f0 ".doctest_multi_polynomial_libsingular.py",
    closeit=1, flags=0xffbff2d4) at Python/pythonrun.c:877
#24 0x0001e5d8 in Py_Main (argc=2, argv=0xffbff34c) at Modules/main.c:523
#25 0x0001d9b0 in _start ()
(gdb)
(gdb) q
The program is running.  Exit anyway? (y or n) y

         [42.7 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 42.7 seconds
```


Some more observations:

```
mabshoff@neron sage-2.8.14$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.14, Release Date: 2007-11-24                      |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<x,y>=MPolynomialRing(QQ,2)
sage: A = matrix([[Integer(1),x], [y,Integer(1)]])
sage: A

[1 x]
[y 1]
sage: A*A

[x*y + 1     2*x]
[    2*y x*y + 1]
sage: A**2

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

When using ZZ as a coefficient ring the problem goes away:

mabshoff@neron sage-2.8.14$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.14, Release Date: 2007-11-24                      |
| Type notebook() for the GUI, and license() for information.        |
sage: R.<x,y>=MPolynomialRing(ZZ,2)
sage: A = matrix([[Integer(1),x], [y,Integer(1)]])
sage: A

[1 x]
[y 1]
sage: A*A

[x*y + 1     2*x]
[    2*y x*y + 1]
sage: A**2

[x*y + 1     2*x]
[    2*y x*y + 1]
sage: A**10

[x^5*y^5 + 45*x^4*y^4 + 210*x^3*y^3 + 210*x^2*y^2 + 45*x*y + 1
10*x^5*y^4 + 120*x^4*y^3 + 252*x^3*y^2 + 120*x^2*y + 10*x]
[    10*x^4*y^5 + 120*x^3*y^4 + 252*x^2*y^3 + 120*x*y^2 + 10*y x^5*y^5
+ 45*x^4*y^4 + 210*x^3*y^3 + 210*x^2*y^2 + 45*x*y + 1]
sage:

These issues seems to rely on matrices, i.e. "just" polynomials does
work:

mabshoff@neron sage-2.8.14$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.14, Release Date: 2007-11-24                      |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x,y>=MPolynomialRing(QQ,2)
sage:             sage: f = x^3 + y
sage: f*f
x^6 + 2*x^3*y + y^2
sage: f^2
x^6 + 2*x^3*y + y^2
sage: f**2
x^6 + 2*x^3*y + y^2
sage: f**10
x^30 + 10*x^27*y + 45*x^24*y^2 + 120*x^21*y^3 + 210*x^18*y^4 +
252*x^15*y^5 + 210*x^12*y^6 + 120*x^9*y^7 + 45*x^6*y^8 + 10*x^3*y^9 +
y^10
sage:
Exiting SAGE (CPU time 0m0.03s, Wall time 0m29.97s).
```

And ideas? I know malb is on his way to Paris shortly, but I have
wasted a tremendous amount of time playing with 2.8.14 on Solaris
instead of doing "real" work since I wanted 2.8.15 to come close to
compilable out of the box on Solaris. We might get close to
compilable, but are certainly way off on the doctests at the moment

Cheers,

Michael 

Issue created by migration from https://trac.sagemath.org/ticket/1325





---

archive/issue_comments_008465.json:
```json
{
    "body": "One more data point: The coercion.pyx doctest fails with the exact\nsame backtrace (modulo the top of the call chain) when doing:\n\n``` \nTrying:\n    f.parent()###line 207:_sage_    >>> f.parent()\nExpecting:\n    Multivariate Polynomial Ring in t, x over Cyclotomic Field of\norder 13 and degree 12\nok\nTrying:\n    ZZ['x','y'].gen(0) + ~Frac(QQ['y']).gen(0)###line 209:_sage_\n>>> ZZ['x','y'].0 + ~Frac(QQ['y']).0\n\nExpecting:\n    (x*y + 1)/y\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n         [3.8 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n        sage -t -verbose devel/sage-main/sage/structure/coerce.pyx \n```\n",
    "created_at": "2007-12-01T23:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1325#issuecomment-8465",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One more data point: The coercion.pyx doctest fails with the exact
same backtrace (modulo the top of the call chain) when doing:

``` 
Trying:
    f.parent()###line 207:_sage_    >>> f.parent()
Expecting:
    Multivariate Polynomial Ring in t, x over Cyclotomic Field of
order 13 and degree 12
ok
Trying:
    ZZ['x','y'].gen(0) + ~Frac(QQ['y']).gen(0)###line 209:_sage_
>>> ZZ['x','y'].0 + ~Frac(QQ['y']).0

Expecting:
    (x*y + 1)/y

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

         [3.8 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:

        sage -t -verbose devel/sage-main/sage/structure/coerce.pyx 
```




---

archive/issue_comments_008466.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-12-01T23:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1325#issuecomment-8466",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_008467.json:
```json
{
    "body": "I have looked at this and I am almost positive it is a libsingular issue rather than a coercion issue. Specifically, adding the line \n\n\n```\n        print type(left), type(right)\n```\n\n\nto the top of `_cmp_c_impl` in multi_polynomial_libsingular.pyx, we get\n\n\n```\nsage: ZZ['x','y'].0 + ~Frac(QQ['y']).0\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n(x*y + 1)/y\n```\n\n\nMaybe try this on solaris, but if the types are all correct it indicates a bug in comparing libsingular pointers rather than coercion.",
    "created_at": "2007-12-02T02:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1325#issuecomment-8467",
    "user": "https://github.com/robertwb"
}
```

I have looked at this and I am almost positive it is a libsingular issue rather than a coercion issue. Specifically, adding the line 


```
        print type(left), type(right)
```


to the top of `_cmp_c_impl` in multi_polynomial_libsingular.pyx, we get


```
sage: ZZ['x','y'].0 + ~Frac(QQ['y']).0
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'> <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
(x*y + 1)/y
```


Maybe try this on solaris, but if the types are all correct it indicates a bug in comparing libsingular pointers rather than coercion.



---

archive/issue_comments_008468.json:
```json
{
    "body": "This should be fixed once #3405 is in.",
    "created_at": "2008-06-12T23:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1325#issuecomment-8468",
    "user": "https://github.com/malb"
}
```

This should be fixed once #3405 is in.



---

archive/issue_comments_008469.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T06:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1325#issuecomment-8469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008470.json:
```json
{
    "body": "Yes, I agree :)",
    "created_at": "2008-06-26T06:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1325",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1325#issuecomment-8470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, I agree :)
