# Issue 973: Unhandled SIGSEGV: A segmentation fault occured in SAGE matrix.matrix2.pyx

archive/issues_000973.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n> sage: time dance(10)\n> \n> \n> ------------------------------------------------------------\n> Unhandled SIGSEGV: A segmentation fault occured in SAGE.\n> This probably occured because a *compiled* component\n> of SAGE has a bug in it (typically accessing invalid memory)\n> or is not properly wrapped with _sig_on, _sig_off.\n> You might want to run SAGE under gdb with 'sage -gdb' to debug this.\n> SAGE will now terminate (sorry).\n> ------------------------------------------------------------\n```\n\nWith sage -gdb:\n\n```\n> sage: time dance(9)\n> h^9 - 27*h^8 + 414*h^7 - 4158*h^6 + 29421*h^5 - 148743*h^4 + 530796*h^3 - 1276992*h^2 + 1866384*h - 1255608\n> CPU times: user 1786.82 s, sys: 23.05 s, total: 1809.87 s\n> Wall time: 1831.52\n> \n> sage: time dance(10)\n> \n> Program received signal SIGSEGV, Segmentation fault.\n> [Switching to Thread -1208523072 (LWP 30162)]\n> 0x0064d473 in strlen () from /lib/libc.so.6\n> (gdb)\n\n```\nThe program (see below) uses methods from sage.matrix.matrix2.pyx:\n\n\n```\n##########################################################################\n#  Copyright (C) 2006 Jaap Spies, jaapspies@gmail.com\n#\n#  Distributed under the terms of the GNU General Public License (GPL):\n#\n#                  http://www.gnu.org/licenses/\n##########################################################################\n\n\"\"\"\n        Usage from sage\n\n        sage: attach 'dancing.sage'\n\n        sage: dance(4)\n        h^4 - 2*h^3 + 9*h^2 - 8*h + 6\n        \n\"\"\"\n\n# use variable 'h' in the polynomial ring over the rationals\n\nh = QQ['h'].gen()\n\ndef dance(m):\n    \"\"\"\n        Generates the polynomial solutions of the Dancing School Problem\n        Based on a modification of theorem 7.2.1 from Brualdi and Ryser,\n        Combinatorial Matrix Theory.\n\n        See NAW 5/7 nr. 4 december 2006 p. 285\n\n        INPUT: integer m \n\n        OUTPUT: polynomial in 'h'\n\n        EXAMPLE:\n            sage: dance(4)\n            h^4 - 2*h^3 + 9*h^2 - 8*h + 6\n\n        AUTHOR: Jaap Spies (2006)\n    \"\"\"    \n    n = 2*m-2\n    M = MatrixSpace(ZZ, m, n)\n    A = M([0 for i in range(m*n)])\n    for i in range(m):\n        for j in range(n):\n            if i > j or j > i + n - m:\n                A[i,j] = 1\n    rv = A.rook_vector()\n#   print rv\n    s = sum([(-1)^k*rv[k]*falling_factorial(m+h-k, m-k) for k in range(m+1)])\n    print s\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/973\n\n",
    "created_at": "2007-10-23T11:20:50Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "Unhandled SIGSEGV: A segmentation fault occured in SAGE matrix.matrix2.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/973",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @williamstein


```
> sage: time dance(10)
> 
> 
> ------------------------------------------------------------
> Unhandled SIGSEGV: A segmentation fault occured in SAGE.
> This probably occured because a *compiled* component
> of SAGE has a bug in it (typically accessing invalid memory)
> or is not properly wrapped with _sig_on, _sig_off.
> You might want to run SAGE under gdb with 'sage -gdb' to debug this.
> SAGE will now terminate (sorry).
> ------------------------------------------------------------
```

With sage -gdb:

```
> sage: time dance(9)
> h^9 - 27*h^8 + 414*h^7 - 4158*h^6 + 29421*h^5 - 148743*h^4 + 530796*h^3 - 1276992*h^2 + 1866384*h - 1255608
> CPU times: user 1786.82 s, sys: 23.05 s, total: 1809.87 s
> Wall time: 1831.52
> 
> sage: time dance(10)
> 
> Program received signal SIGSEGV, Segmentation fault.
> [Switching to Thread -1208523072 (LWP 30162)]
> 0x0064d473 in strlen () from /lib/libc.so.6
> (gdb)

```
The program (see below) uses methods from sage.matrix.matrix2.pyx:


```
##########################################################################
#  Copyright (C) 2006 Jaap Spies, jaapspies@gmail.com
#
#  Distributed under the terms of the GNU General Public License (GPL):
#
#                  http://www.gnu.org/licenses/
##########################################################################

"""
        Usage from sage

        sage: attach 'dancing.sage'

        sage: dance(4)
        h^4 - 2*h^3 + 9*h^2 - 8*h + 6
        
"""

# use variable 'h' in the polynomial ring over the rationals

h = QQ['h'].gen()

def dance(m):
    """
        Generates the polynomial solutions of the Dancing School Problem
        Based on a modification of theorem 7.2.1 from Brualdi and Ryser,
        Combinatorial Matrix Theory.

        See NAW 5/7 nr. 4 december 2006 p. 285

        INPUT: integer m 

        OUTPUT: polynomial in 'h'

        EXAMPLE:
            sage: dance(4)
            h^4 - 2*h^3 + 9*h^2 - 8*h + 6

        AUTHOR: Jaap Spies (2006)
    """    
    n = 2*m-2
    M = MatrixSpace(ZZ, m, n)
    A = M([0 for i in range(m*n)])
    for i in range(m):
        for j in range(n):
            if i > j or j > i + n - m:
                A[i,j] = 1
    rv = A.rook_vector()
#   print rv
    s = sum([(-1)^k*rv[k]*falling_factorial(m+h-k, m-k) for k in range(m+1)])
    print s


```


Issue created by migration from https://trac.sagemath.org/ticket/973





---

archive/issue_comments_005913.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-10-23T16:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_005914.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-23T16:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005915.json:
```json
{
    "body": "Well, it works for me on sage.math:\n\n```\nsage: dance(10)\nh^10 - 35*h^9 + 675*h^8 - 8610*h^7 + 78435*h^6 - 523467*h^5 + 2562525*h^4 - 9008160*h^3 + 21623220*h^2 - 31840760*h + 21750840\nsage:\nExiting SAGE (CPU time 393m46.71s, Wall time 398m11.21s).\n```\nCould this potentially go wrong on a 32 bit box?\n\nCheers,\n\nMichael",
    "created_at": "2007-10-23T22:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, it works for me on sage.math:

```
sage: dance(10)
h^10 - 35*h^9 + 675*h^8 - 8610*h^7 + 78435*h^6 - 523467*h^5 + 2562525*h^4 - 9008160*h^3 + 21623220*h^2 - 31840760*h + 21750840
sage:
Exiting SAGE (CPU time 393m46.71s, Wall time 398m11.21s).
```
Could this potentially go wrong on a 32 bit box?

Cheers,

Michael



---

archive/issue_comments_005916.json:
```json
{
    "body": "On my 32 bit box:\n\n\n```\nsage: time dance(10)\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread -1208297792 (LWP 3914)]\n0x0a6c2a64 in ?? ()\n(gdb) bt\n#0  0x0a6c2a64 in ?? ()\n#1  0x08087aa2 in PyObject_RichCompare (v=0x8f94f44, w=0x8f94f44, op=2) at Objects/object.c:914\n#2  0x080c3862 in PyEval_EvalFrameEx (f=0xa7bb864, throwflag=0) at Python/ceval.c:3980\n#3  0x0810b4ed in gen_send_ex (gen=0xa70a3ec, arg=0x16, exc=0) at Objects/genobject.c:82\n#4  0x080c00cd in PyEval_EvalFrameEx (f=0xa7bd5e4, throwflag=0) at Python/ceval.c:2164\n#5  0x0810b4ed in gen_send_ex (gen=0xa70a32c, arg=0x16, exc=0) at Objects/genobject.c:82\n#6  0x080c00cd in PyEval_EvalFrameEx (f=0xa7bd15c, throwflag=0) at Python/ceval.c:2164\n#7  0x0810b4ed in gen_send_ex (gen=0xa70a72c, arg=0x16, exc=0) at Objects/genobject.c:82\n#8  0x080c00cd in PyEval_EvalFrameEx (f=0xa7bc4fc, throwflag=0) at Python/ceval.c:2164\n#9  0x0810b4ed in gen_send_ex (gen=0xa70a70c, arg=0x16, exc=0) at Objects/genobject.c:82\n#10 0x080c00cd in PyEval_EvalFrameEx (f=0xa7bea2c, throwflag=0) at Python/ceval.c:2164\n#11 0x0810b4ed in gen_send_ex (gen=0xa70a6ec, arg=0x16, exc=0) at Objects/genobject.c:82\n#12 0x080c00cd in PyEval_EvalFrameEx (f=0xa7be134, throwflag=0) at Python/ceval.c:2164\n#13 0x0810b4ed in gen_send_ex (gen=0xa70a68c, arg=0x16, exc=0) at Objects/genobject.c:82\n#14 0x080c00cd in PyEval_EvalFrameEx (f=0xa7bf77c, throwflag=0) at Python/ceval.c:2164\n#15 0x0810b4ed in gen_send_ex (gen=0xa70a6cc, arg=0x16, exc=0) at Objects/genobject.c:82\n#16 0x080c00cd in PyEval_EvalFrameEx (f=0xa7be434, throwflag=0) at Python/ceval.c:2164\n#17 0x0810b4ed in gen_send_ex (gen=0xa70aa2c, arg=0x16, exc=0) at Objects/genobject.c:82\n#18 0x080c00cd in PyEval_EvalFrameEx (f=0xa7bb9dc, throwflag=0) at Python/ceval.c:2164\n#19 0x0810b4ed in gen_send_ex (gen=0xa70a66c, arg=0x16, exc=0) at Objects/genobject.c:82\n#20 0x0805a213 in PyIter_Next (iter=0xa70a66c) at Objects/abstract.c:2375\n#21 0x0121c5bd in __pyx_f_py_7matrix2_6Matrix_permanent (__pyx_v_self=0x9c37194, unused=0x0) at sage/matrix/matrix2.c:1633\n#22 0x0805a277 in PyObject_Call (func=0x92c1a54, arg=0xb7f6d02c, kw=0x0) at Objects/abstract.c:1860\n---Type <return> to continue, or q <return> to quit---\n#23 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xa71282c, arg=0xb7f6d02c, kw=0x0) at Python/ceval.c:3433\n#24 0x0805a490 in PyObject_CallObject (o=0xa71282c, a=0x0) at Objects/abstract.c:1851\n#25 0x0121b491 in __pyx_f_py_7matrix2_6Matrix_permanental_minor (__pyx_v_self=0x9c37fa4, __pyx_arg_k=0x8f94ee4)\n    at sage/matrix/matrix2.c:2074\n#26 0x0805a277 in PyObject_Call (func=0x92c1a54, arg=0x9186b4c, kw=0x0) at Objects/abstract.c:1860\n#27 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xa70ab2c, arg=0x9186b4c, kw=0x0) at Python/ceval.c:3433\n#28 0x0805a490 in PyObject_CallObject (o=0xa70ab2c, a=0x9186b4c) at Objects/abstract.c:1851\n#29 0x01212462 in __pyx_f_py_7matrix2_6Matrix_rook_vector (__pyx_v_self=0x9c37fa4, __pyx_args=0xb7f6d02c, __pyx_kwds=0x0)\n    at sage/matrix/matrix2.c:2399\n#30 0x080c539c in PyEval_EvalFrameEx (f=0x9c58bf4, throwflag=0) at Python/ceval.c:3564\n#31 0x080c57c5 in PyEval_EvalFrameEx (f=0x9c662b4, throwflag=0) at Python/ceval.c:3650\n#32 0x080c65d5 in PyEval_EvalCodeEx (co=0x9c37068, globals=0xa7048ac, locals=0xa7048ac, args=0x0, argcount=0, kws=0x0, \n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#33 0x080c6647 in PyEval_EvalCode (co=0x9c37068, globals=0xa7048ac, locals=0xa7048ac) at Python/ceval.c:494\n#34 0x080bdc01 in builtin_eval (self=0x0, args=0xa70886c) at Python/bltinmodule.c:571\n#35 0x080c539c in PyEval_EvalFrameEx (f=0x9ba3cbc, throwflag=0) at Python/ceval.c:3564\n#36 0x080c65d5 in PyEval_EvalCodeEx (co=0x91c8338, globals=0x91bd1c4, locals=0x0, args=0x9c5af7c, argcount=2, kws=0x9c5af84, \n    kwcount=0, defs=0x91dc6d8, defcount=1, closure=0x0) at Python/ceval.c:2831\n#37 0x080c4a89 in PyEval_EvalFrameEx (f=0x9c5ae2c, throwflag=0) at Python/ceval.c:3660\n#38 0x080c57c5 in PyEval_EvalFrameEx (f=0x9b8a354, throwflag=0) at Python/ceval.c:3650\n#39 0x080c65d5 in PyEval_EvalCodeEx (co=0x9ae78d8, globals=0xa7048ac, locals=0xa7048ac, args=0x0, argcount=0, kws=0x0, \n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#40 0x080c5852 in PyEval_EvalFrameEx (f=0x9c5a61c, throwflag=0) at Python/ceval.c:494\n---Type <return> to continue, or q <return> to quit---\n#41 0x080c65d5 in PyEval_EvalCodeEx (co=0x91871d0, globals=0x91768ac, locals=0x0, args=0x9ba09c8, argcount=2, kws=0x9ba09d0, \n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#42 0x080c4a89 in PyEval_EvalFrameEx (f=0x9ba087c, throwflag=0) at Python/ceval.c:3660\n#43 0x080c65d5 in PyEval_EvalCodeEx (co=0x9187140, globals=0x91768ac, locals=0x0, args=0x9b925e4, argcount=3, kws=0x9b925f0, \n    kwcount=0, defs=0x91eb178, defcount=2, closure=0x0) at Python/ceval.c:2831\n#44 0x080c4a89 in PyEval_EvalFrameEx (f=0x9b9249c, throwflag=0) at Python/ceval.c:3660\n#45 0x080c57c5 in PyEval_EvalFrameEx (f=0xa743c0c, throwflag=0) at Python/ceval.c:3650\n#46 0x080c65d5 in PyEval_EvalCodeEx (co=0x9177e78, globals=0x91768ac, locals=0x0, args=0xa7441c4, argcount=2, kws=0xa7441cc, \n    kwcount=0, defs=0x91eb4d8, defcount=1, closure=0x0) at Python/ceval.c:2831\n#47 0x080c4a89 in PyEval_EvalFrameEx (f=0xa744084, throwflag=0) at Python/ceval.c:3660\n#48 0x080c65d5 in PyEval_EvalCodeEx (co=0x9177da0, globals=0x91768ac, locals=0x0, args=0x906c7d0, argcount=2, kws=0x906c7d8, \n    kwcount=0, defs=0x91eb4b8, defcount=1, closure=0x0) at Python/ceval.c:2831\n#49 0x080c4a89 in PyEval_EvalFrameEx (f=0x906c68c, throwflag=0) at Python/ceval.c:3660\n#50 0x080c65d5 in PyEval_EvalCodeEx (co=0x9122d58, globals=0x912968c, locals=0x0, args=0x8f9fe4c, argcount=1, kws=0x8f9fe50, \n    kwcount=2, defs=0x915cb18, defcount=2, closure=0x0) at Python/ceval.c:2831\n#51 0x080c4a89 in PyEval_EvalFrameEx (f=0x8f9fd14, throwflag=0) at Python/ceval.c:3660\n#52 0x080c65d5 in PyEval_EvalCodeEx (co=0xb7f32530, globals=0xb7f85acc, locals=0xb7f85acc, args=0x0, argcount=0, kws=0x0, \n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#53 0x080c6647 in PyEval_EvalCode (co=0xb7f32530, globals=0xb7f85acc, locals=0xb7f85acc) at Python/ceval.c:494\n#54 0x080e52c8 in PyRun_FileExFlags (fp=0x8f93068, filename=0xbfe5fc5a \"/usr/local/sage/local/bin/sage-gdb-pythonstartup\", \n    start=257, globals=0xb7f85acc, locals=0xb7f85acc, closeit=0, flags=0xbfe5d618) at Python/pythonrun.c:1271\n#55 0x080e5557 in PyRun_SimpleFileExFlags (fp=0x8f93068, \n    filename=0xbfe5fc5a \"/usr/local/sage/local/bin/sage-gdb-pythonstartup\", closeit=0, flags=0xbfe5d618)\n---Type <return> to continue, or q <return> to quit---\n    at Python/pythonrun.c:877\n#56 0x080571a6 in Py_Main (argc=0, argv=0xbfe5d6e4) at Modules/main.c:134\n#57 0x08056432 in main (argc=1, argv=0x8144c20) at ./Modules/python.c:23\n(gdb) \n\n\n```",
    "created_at": "2007-10-24T10:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5916",
    "user": "https://github.com/jaapspies"
}
```

On my 32 bit box:


```
sage: time dance(10)

Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1208297792 (LWP 3914)]
0x0a6c2a64 in ?? ()
(gdb) bt
#0  0x0a6c2a64 in ?? ()
#1  0x08087aa2 in PyObject_RichCompare (v=0x8f94f44, w=0x8f94f44, op=2) at Objects/object.c:914
#2  0x080c3862 in PyEval_EvalFrameEx (f=0xa7bb864, throwflag=0) at Python/ceval.c:3980
#3  0x0810b4ed in gen_send_ex (gen=0xa70a3ec, arg=0x16, exc=0) at Objects/genobject.c:82
#4  0x080c00cd in PyEval_EvalFrameEx (f=0xa7bd5e4, throwflag=0) at Python/ceval.c:2164
#5  0x0810b4ed in gen_send_ex (gen=0xa70a32c, arg=0x16, exc=0) at Objects/genobject.c:82
#6  0x080c00cd in PyEval_EvalFrameEx (f=0xa7bd15c, throwflag=0) at Python/ceval.c:2164
#7  0x0810b4ed in gen_send_ex (gen=0xa70a72c, arg=0x16, exc=0) at Objects/genobject.c:82
#8  0x080c00cd in PyEval_EvalFrameEx (f=0xa7bc4fc, throwflag=0) at Python/ceval.c:2164
#9  0x0810b4ed in gen_send_ex (gen=0xa70a70c, arg=0x16, exc=0) at Objects/genobject.c:82
#10 0x080c00cd in PyEval_EvalFrameEx (f=0xa7bea2c, throwflag=0) at Python/ceval.c:2164
#11 0x0810b4ed in gen_send_ex (gen=0xa70a6ec, arg=0x16, exc=0) at Objects/genobject.c:82
#12 0x080c00cd in PyEval_EvalFrameEx (f=0xa7be134, throwflag=0) at Python/ceval.c:2164
#13 0x0810b4ed in gen_send_ex (gen=0xa70a68c, arg=0x16, exc=0) at Objects/genobject.c:82
#14 0x080c00cd in PyEval_EvalFrameEx (f=0xa7bf77c, throwflag=0) at Python/ceval.c:2164
#15 0x0810b4ed in gen_send_ex (gen=0xa70a6cc, arg=0x16, exc=0) at Objects/genobject.c:82
#16 0x080c00cd in PyEval_EvalFrameEx (f=0xa7be434, throwflag=0) at Python/ceval.c:2164
#17 0x0810b4ed in gen_send_ex (gen=0xa70aa2c, arg=0x16, exc=0) at Objects/genobject.c:82
#18 0x080c00cd in PyEval_EvalFrameEx (f=0xa7bb9dc, throwflag=0) at Python/ceval.c:2164
#19 0x0810b4ed in gen_send_ex (gen=0xa70a66c, arg=0x16, exc=0) at Objects/genobject.c:82
#20 0x0805a213 in PyIter_Next (iter=0xa70a66c) at Objects/abstract.c:2375
#21 0x0121c5bd in __pyx_f_py_7matrix2_6Matrix_permanent (__pyx_v_self=0x9c37194, unused=0x0) at sage/matrix/matrix2.c:1633
#22 0x0805a277 in PyObject_Call (func=0x92c1a54, arg=0xb7f6d02c, kw=0x0) at Objects/abstract.c:1860
---Type <return> to continue, or q <return> to quit---
#23 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xa71282c, arg=0xb7f6d02c, kw=0x0) at Python/ceval.c:3433
#24 0x0805a490 in PyObject_CallObject (o=0xa71282c, a=0x0) at Objects/abstract.c:1851
#25 0x0121b491 in __pyx_f_py_7matrix2_6Matrix_permanental_minor (__pyx_v_self=0x9c37fa4, __pyx_arg_k=0x8f94ee4)
    at sage/matrix/matrix2.c:2074
#26 0x0805a277 in PyObject_Call (func=0x92c1a54, arg=0x9186b4c, kw=0x0) at Objects/abstract.c:1860
#27 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xa70ab2c, arg=0x9186b4c, kw=0x0) at Python/ceval.c:3433
#28 0x0805a490 in PyObject_CallObject (o=0xa70ab2c, a=0x9186b4c) at Objects/abstract.c:1851
#29 0x01212462 in __pyx_f_py_7matrix2_6Matrix_rook_vector (__pyx_v_self=0x9c37fa4, __pyx_args=0xb7f6d02c, __pyx_kwds=0x0)
    at sage/matrix/matrix2.c:2399
#30 0x080c539c in PyEval_EvalFrameEx (f=0x9c58bf4, throwflag=0) at Python/ceval.c:3564
#31 0x080c57c5 in PyEval_EvalFrameEx (f=0x9c662b4, throwflag=0) at Python/ceval.c:3650
#32 0x080c65d5 in PyEval_EvalCodeEx (co=0x9c37068, globals=0xa7048ac, locals=0xa7048ac, args=0x0, argcount=0, kws=0x0, 
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#33 0x080c6647 in PyEval_EvalCode (co=0x9c37068, globals=0xa7048ac, locals=0xa7048ac) at Python/ceval.c:494
#34 0x080bdc01 in builtin_eval (self=0x0, args=0xa70886c) at Python/bltinmodule.c:571
#35 0x080c539c in PyEval_EvalFrameEx (f=0x9ba3cbc, throwflag=0) at Python/ceval.c:3564
#36 0x080c65d5 in PyEval_EvalCodeEx (co=0x91c8338, globals=0x91bd1c4, locals=0x0, args=0x9c5af7c, argcount=2, kws=0x9c5af84, 
    kwcount=0, defs=0x91dc6d8, defcount=1, closure=0x0) at Python/ceval.c:2831
#37 0x080c4a89 in PyEval_EvalFrameEx (f=0x9c5ae2c, throwflag=0) at Python/ceval.c:3660
#38 0x080c57c5 in PyEval_EvalFrameEx (f=0x9b8a354, throwflag=0) at Python/ceval.c:3650
#39 0x080c65d5 in PyEval_EvalCodeEx (co=0x9ae78d8, globals=0xa7048ac, locals=0xa7048ac, args=0x0, argcount=0, kws=0x0, 
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#40 0x080c5852 in PyEval_EvalFrameEx (f=0x9c5a61c, throwflag=0) at Python/ceval.c:494
---Type <return> to continue, or q <return> to quit---
#41 0x080c65d5 in PyEval_EvalCodeEx (co=0x91871d0, globals=0x91768ac, locals=0x0, args=0x9ba09c8, argcount=2, kws=0x9ba09d0, 
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#42 0x080c4a89 in PyEval_EvalFrameEx (f=0x9ba087c, throwflag=0) at Python/ceval.c:3660
#43 0x080c65d5 in PyEval_EvalCodeEx (co=0x9187140, globals=0x91768ac, locals=0x0, args=0x9b925e4, argcount=3, kws=0x9b925f0, 
    kwcount=0, defs=0x91eb178, defcount=2, closure=0x0) at Python/ceval.c:2831
#44 0x080c4a89 in PyEval_EvalFrameEx (f=0x9b9249c, throwflag=0) at Python/ceval.c:3660
#45 0x080c57c5 in PyEval_EvalFrameEx (f=0xa743c0c, throwflag=0) at Python/ceval.c:3650
#46 0x080c65d5 in PyEval_EvalCodeEx (co=0x9177e78, globals=0x91768ac, locals=0x0, args=0xa7441c4, argcount=2, kws=0xa7441cc, 
    kwcount=0, defs=0x91eb4d8, defcount=1, closure=0x0) at Python/ceval.c:2831
#47 0x080c4a89 in PyEval_EvalFrameEx (f=0xa744084, throwflag=0) at Python/ceval.c:3660
#48 0x080c65d5 in PyEval_EvalCodeEx (co=0x9177da0, globals=0x91768ac, locals=0x0, args=0x906c7d0, argcount=2, kws=0x906c7d8, 
    kwcount=0, defs=0x91eb4b8, defcount=1, closure=0x0) at Python/ceval.c:2831
#49 0x080c4a89 in PyEval_EvalFrameEx (f=0x906c68c, throwflag=0) at Python/ceval.c:3660
#50 0x080c65d5 in PyEval_EvalCodeEx (co=0x9122d58, globals=0x912968c, locals=0x0, args=0x8f9fe4c, argcount=1, kws=0x8f9fe50, 
    kwcount=2, defs=0x915cb18, defcount=2, closure=0x0) at Python/ceval.c:2831
#51 0x080c4a89 in PyEval_EvalFrameEx (f=0x8f9fd14, throwflag=0) at Python/ceval.c:3660
#52 0x080c65d5 in PyEval_EvalCodeEx (co=0xb7f32530, globals=0xb7f85acc, locals=0xb7f85acc, args=0x0, argcount=0, kws=0x0, 
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#53 0x080c6647 in PyEval_EvalCode (co=0xb7f32530, globals=0xb7f85acc, locals=0xb7f85acc) at Python/ceval.c:494
#54 0x080e52c8 in PyRun_FileExFlags (fp=0x8f93068, filename=0xbfe5fc5a "/usr/local/sage/local/bin/sage-gdb-pythonstartup", 
    start=257, globals=0xb7f85acc, locals=0xb7f85acc, closeit=0, flags=0xbfe5d618) at Python/pythonrun.c:1271
#55 0x080e5557 in PyRun_SimpleFileExFlags (fp=0x8f93068, 
    filename=0xbfe5fc5a "/usr/local/sage/local/bin/sage-gdb-pythonstartup", closeit=0, flags=0xbfe5d618)
---Type <return> to continue, or q <return> to quit---
    at Python/pythonrun.c:877
#56 0x080571a6 in Py_Main (argc=0, argv=0xbfe5d6e4) at Modules/main.c:134
#57 0x08056432 in main (argc=1, argv=0x8144c20) at ./Modules/python.c:23
(gdb) 


```



---

archive/issue_comments_005917.json:
```json
{
    "body": "The backtrace indicates that python itself fails to allocate more memory. For a detailed discussion see \n\nhttp://groups.google.com/group/sage-devel/t/7fd9dacc353fef7c\n\nI am leaning toward invalid, but I would like to wait for the valgrind session of \"dance(10)\" on sage.math to finish. This might actually take a whole months, assuming the code does not segfault and valgrind doesn't slow down too much. But since dance(k) for k in 1..6 valgrind clean we might close this anyway before any potential finish.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-24T11:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The backtrace indicates that python itself fails to allocate more memory. For a detailed discussion see 

http://groups.google.com/group/sage-devel/t/7fd9dacc353fef7c

I am leaning toward invalid, but I would like to wait for the valgrind session of "dance(10)" on sage.math to finish. This might actually take a whole months, assuming the code does not segfault and valgrind doesn't slow down too much. But since dance(k) for k in 1..6 valgrind clean we might close this anyway before any potential finish.

Cheers,

Michael



---

archive/issue_comments_005918.json:
```json
{
    "body": "Upon further investigation it seems that the crash does happen at least on 32 bit x86 Fedora Core 7.\n\nStill investigating.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-24T19:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Upon further investigation it seems that the crash does happen at least on 32 bit x86 Fedora Core 7.

Still investigating.

Cheers,

Michael



---

archive/issue_events_002692.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-25T01:10:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "milestone": "sage-2.8.10",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/973#event-2692"
}
```



---

archive/issue_comments_005919.json:
```json
{
    "body": "Hello,\n\nlooks like a got a much better bt:\n\n```\nsage: time dance(10)\n\n\nProgram received signal SIGSEGV, Segmentation fault.\n[Switching to Thread -1208650048 (LWP 3143)]\n0x00786473 in strlen () from /lib/libc.so.6\n(gdb)\n(gdb) bt\n#0  0x00786473 in strlen () from /lib/libc.so.6\n#1  0x0809354f in PyString_FromFormatV (format=0x811ef6c \"'%.200s' object cannot be interpreted as an index\",\n    vargs=<value optimized out>) at Objects/stringobject.c:202\n#2  0x080d4ee0 in PyErr_Format (exception=0x813b560, format=0x811ef6c \"'%.200s' object cannot be interpreted as an index\")\n    at Python/errors.c:522\n#3  0x0805d578 in PyNumber_Index (item=0x0) at Objects/abstract.c:965\n#4  0x011ac5ee in __pyx_f_py_20matrix_integer_dense_20Matrix_integer_dense_prod_of_row_sums (__pyx_v_self=0xa4a8104,\n    __pyx_v_cols=0xaf96ecc) at sage/matrix/matrix_integer_dense.c:13576\n#5  0x0805a277 in PyObject_Call (func=0x0, arg=0xa4a048c, kw=0x0) at Objects/abstract.c:1860\n#6  0x080be7cc in PyEval_CallObjectWithKeywords (func=0xaf9b62c, arg=0xa4a048c, kw=0x0) at Python/ceval.c:3433\n#7  0x0805a490 in PyObject_CallObject (o=0xaf9b62c, a=0xa4a048c) at Objects/abstract.c:1851\n#8  0x07db98c6 in __pyx_f_py_7matrix2_6Matrix_permanent (__pyx_v_self=0xa4a8104, unused=0x0) at sage/matrix/matrix2.c:1657\n#9  0x0805a277 in PyObject_Call (func=0x0, arg=0xb7f1702c, kw=0x0) at Objects/abstract.c:1860\n#10 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xaf9694c, arg=0xb7f1702c, kw=0x0) at Python/ceval.c:3433\n#11 0x0805a490 in PyObject_CallObject (o=0xaf9694c, a=0x0) at Objects/abstract.c:1851\n#12 0x07db8711 in __pyx_f_py_7matrix2_6Matrix_permanental_minor (__pyx_v_self=0xa4a8a94, __pyx_arg_k=0x97f8ee4)\n    at sage/matrix/matrix2.c:2077\n#13 0x0805a277 in PyObject_Call (func=0x0, arg=0xa41c44c, kw=0x0) at Objects/abstract.c:1860\n#14 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xaf87cec, arg=0xa41c44c, kw=0x0) at Python/ceval.c:3433\n#15 0x0805a490 in PyObject_CallObject (o=0xaf87cec, a=0xa41c44c) at Objects/abstract.c:1851\n#16 0x07daf6e2 in __pyx_f_py_7matrix2_6Matrix_rook_vector (__pyx_v_self=0xa4a8a94, __pyx_args=0xb7f1702c, __pyx_kwds=0x0)\n    at sage/matrix/matrix2.c:2402\n#17 0x080c539c in PyEval_EvalFrameEx (f=0xb00497c, throwflag=0) at Python/ceval.c:3564\n#18 0x080c57c5 in PyEval_EvalFrameEx (f=0xb004814, throwflag=0) at Python/ceval.c:3650\n#19 0x080c65d5 in PyEval_EvalCodeEx (co=0xa4a8338, globals=0xaf1035c, locals=0xaf1035c, args=0x0, argcount=0, kws=0x0,\n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#20 0x080c6647 in PyEval_EvalCode (co=0xa4a8338, globals=0xaf1035c, locals=0xaf1035c) at Python/ceval.c:494\n#21 0x080bdc01 in builtin_eval (self=0x0, args=0xaf96c8c) at Python/bltinmodule.c:571\n#22 0x080c539c in PyEval_EvalFrameEx (f=0xb00466c, throwflag=0) at Python/ceval.c:3564\n#23 0x080c65d5 in PyEval_EvalCodeEx (co=0x9a345c0, globals=0x9a2c3e4, locals=0x0, args=0xb00463c, argcount=2,\n    kws=0xb004644, kwcount=0, defs=0x9a4a8d8, defcount=1, closure=0x0) at Python/ceval.c:2831\n#24 0x080c4a89 in PyEval_EvalFrameEx (f=0xb0044ec, throwflag=0) at Python/ceval.c:3660\n#25 0x080c57c5 in PyEval_EvalFrameEx (f=0xb004394, throwflag=0) at Python/ceval.c:3650\n#26 0x080c65d5 in PyEval_EvalCodeEx (co=0xa4a8218, globals=0xaf1035c, locals=0xaf1035c, args=0x0, argcount=0, kws=0x0,\n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#27 0x080c5852 in PyEval_EvalFrameEx (f=0xaff7aec, throwflag=0) at Python/ceval.c:494\n---Type <return> to continue, or q <return> to quit---\n#28 0x080c65d5 in PyEval_EvalCodeEx (co=0x99ebad0, globals=0x99ddacc, locals=0x0, args=0xaff7ab8, argcount=2,\n    kws=0xaff7ac0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#29 0x080c4a89 in PyEval_EvalFrameEx (f=0xaff796c, throwflag=0) at Python/ceval.c:3660\n#30 0x080c65d5 in PyEval_EvalCodeEx (co=0x99eba40, globals=0x99ddacc, locals=0x0, args=0xaff7944, argcount=3,\n    kws=0xaff7950, kwcount=0, defs=0x9a5a338, defcount=2, closure=0x0) at Python/ceval.c:2831\n#31 0x080c4a89 in PyEval_EvalFrameEx (f=0xaff77fc, throwflag=0) at Python/ceval.c:3660\n#32 0x080c57c5 in PyEval_EvalFrameEx (f=0xafc9604, throwflag=0) at Python/ceval.c:3650\n#33 0x080c65d5 in PyEval_EvalCodeEx (co=0x99eb7b8, globals=0x99ddacc, locals=0x0, args=0xaf85b7c, argcount=2,\n    kws=0xaf85b84, kwcount=0, defs=0x9a5a698, defcount=1, closure=0x0) at Python/ceval.c:2831\n#34 0x080c4a89 in PyEval_EvalFrameEx (f=0xaf85a3c, throwflag=0) at Python/ceval.c:3660\n#35 0x080c65d5 in PyEval_EvalCodeEx (co=0x99eb6e0, globals=0x99ddacc, locals=0x0, args=0x98c98f0, argcount=2,\n    kws=0x98c98f8, kwcount=0, defs=0x9a5a678, defcount=1, closure=0x0) at Python/ceval.c:2831\n#36 0x080c4a89 in PyEval_EvalFrameEx (f=0x98c97ac, throwflag=0) at Python/ceval.c:3660\n#37 0x080c65d5 in PyEval_EvalCodeEx (co=0x999a410, globals=0x99988ac, locals=0x0, args=0x980366c, argcount=1,\n    kws=0x9803670, kwcount=2, defs=0x99c1c38, defcount=2, closure=0x0) at Python/ceval.c:2831\n#38 0x080c4a89 in PyEval_EvalFrameEx (f=0x9803534, throwflag=0) at Python/ceval.c:3660\n#39 0x080c65d5 in PyEval_EvalCodeEx (co=0xb7edd5c0, globals=0xb7f2facc, locals=0xb7f2facc, args=0x0, argcount=0, kws=0x0,\n    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831\n#40 0x080c6647 in PyEval_EvalCode (co=0xb7edd5c0, globals=0xb7f2facc, locals=0xb7f2facc) at Python/ceval.c:494\n#41 0x080e52c8 in PyRun_FileExFlags (fp=0x982c788,\n    filename=0xbff57c9e \"/tmp/Work/sage-2.8.9.alpha0/local/bin/sage-gdb-pythonstartup\", start=257, globals=0xb7f2facc,\n    locals=0xb7f2facc, closeit=0, flags=0xbff55698) at Python/pythonrun.c:1271\n#42 0x080e5557 in PyRun_SimpleFileExFlags (fp=0x982c788,\n    filename=0xbff57c9e \"/tmp/Work/sage-2.8.9.alpha0/local/bin/sage-gdb-pythonstartup\", closeit=0, flags=0xbff55698)\n    at Python/pythonrun.c:877\n#43 0x080571a6 in Py_Main (argc=0, argv=0xbff55764) at Modules/main.c:134\n#44 0x08056432 in main (argc=Cannot access memory at address 0x0\n) at ./Modules/python.c:23\n(gdb)\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-10-25T09:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5919",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello,

looks like a got a much better bt:

```
sage: time dance(10)


Program received signal SIGSEGV, Segmentation fault.
[Switching to Thread -1208650048 (LWP 3143)]
0x00786473 in strlen () from /lib/libc.so.6
(gdb)
(gdb) bt
#0  0x00786473 in strlen () from /lib/libc.so.6
#1  0x0809354f in PyString_FromFormatV (format=0x811ef6c "'%.200s' object cannot be interpreted as an index",
    vargs=<value optimized out>) at Objects/stringobject.c:202
#2  0x080d4ee0 in PyErr_Format (exception=0x813b560, format=0x811ef6c "'%.200s' object cannot be interpreted as an index")
    at Python/errors.c:522
#3  0x0805d578 in PyNumber_Index (item=0x0) at Objects/abstract.c:965
#4  0x011ac5ee in __pyx_f_py_20matrix_integer_dense_20Matrix_integer_dense_prod_of_row_sums (__pyx_v_self=0xa4a8104,
    __pyx_v_cols=0xaf96ecc) at sage/matrix/matrix_integer_dense.c:13576
#5  0x0805a277 in PyObject_Call (func=0x0, arg=0xa4a048c, kw=0x0) at Objects/abstract.c:1860
#6  0x080be7cc in PyEval_CallObjectWithKeywords (func=0xaf9b62c, arg=0xa4a048c, kw=0x0) at Python/ceval.c:3433
#7  0x0805a490 in PyObject_CallObject (o=0xaf9b62c, a=0xa4a048c) at Objects/abstract.c:1851
#8  0x07db98c6 in __pyx_f_py_7matrix2_6Matrix_permanent (__pyx_v_self=0xa4a8104, unused=0x0) at sage/matrix/matrix2.c:1657
#9  0x0805a277 in PyObject_Call (func=0x0, arg=0xb7f1702c, kw=0x0) at Objects/abstract.c:1860
#10 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xaf9694c, arg=0xb7f1702c, kw=0x0) at Python/ceval.c:3433
#11 0x0805a490 in PyObject_CallObject (o=0xaf9694c, a=0x0) at Objects/abstract.c:1851
#12 0x07db8711 in __pyx_f_py_7matrix2_6Matrix_permanental_minor (__pyx_v_self=0xa4a8a94, __pyx_arg_k=0x97f8ee4)
    at sage/matrix/matrix2.c:2077
#13 0x0805a277 in PyObject_Call (func=0x0, arg=0xa41c44c, kw=0x0) at Objects/abstract.c:1860
#14 0x080be7cc in PyEval_CallObjectWithKeywords (func=0xaf87cec, arg=0xa41c44c, kw=0x0) at Python/ceval.c:3433
#15 0x0805a490 in PyObject_CallObject (o=0xaf87cec, a=0xa41c44c) at Objects/abstract.c:1851
#16 0x07daf6e2 in __pyx_f_py_7matrix2_6Matrix_rook_vector (__pyx_v_self=0xa4a8a94, __pyx_args=0xb7f1702c, __pyx_kwds=0x0)
    at sage/matrix/matrix2.c:2402
#17 0x080c539c in PyEval_EvalFrameEx (f=0xb00497c, throwflag=0) at Python/ceval.c:3564
#18 0x080c57c5 in PyEval_EvalFrameEx (f=0xb004814, throwflag=0) at Python/ceval.c:3650
#19 0x080c65d5 in PyEval_EvalCodeEx (co=0xa4a8338, globals=0xaf1035c, locals=0xaf1035c, args=0x0, argcount=0, kws=0x0,
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#20 0x080c6647 in PyEval_EvalCode (co=0xa4a8338, globals=0xaf1035c, locals=0xaf1035c) at Python/ceval.c:494
#21 0x080bdc01 in builtin_eval (self=0x0, args=0xaf96c8c) at Python/bltinmodule.c:571
#22 0x080c539c in PyEval_EvalFrameEx (f=0xb00466c, throwflag=0) at Python/ceval.c:3564
#23 0x080c65d5 in PyEval_EvalCodeEx (co=0x9a345c0, globals=0x9a2c3e4, locals=0x0, args=0xb00463c, argcount=2,
    kws=0xb004644, kwcount=0, defs=0x9a4a8d8, defcount=1, closure=0x0) at Python/ceval.c:2831
#24 0x080c4a89 in PyEval_EvalFrameEx (f=0xb0044ec, throwflag=0) at Python/ceval.c:3660
#25 0x080c57c5 in PyEval_EvalFrameEx (f=0xb004394, throwflag=0) at Python/ceval.c:3650
#26 0x080c65d5 in PyEval_EvalCodeEx (co=0xa4a8218, globals=0xaf1035c, locals=0xaf1035c, args=0x0, argcount=0, kws=0x0,
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#27 0x080c5852 in PyEval_EvalFrameEx (f=0xaff7aec, throwflag=0) at Python/ceval.c:494
---Type <return> to continue, or q <return> to quit---
#28 0x080c65d5 in PyEval_EvalCodeEx (co=0x99ebad0, globals=0x99ddacc, locals=0x0, args=0xaff7ab8, argcount=2,
    kws=0xaff7ac0, kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#29 0x080c4a89 in PyEval_EvalFrameEx (f=0xaff796c, throwflag=0) at Python/ceval.c:3660
#30 0x080c65d5 in PyEval_EvalCodeEx (co=0x99eba40, globals=0x99ddacc, locals=0x0, args=0xaff7944, argcount=3,
    kws=0xaff7950, kwcount=0, defs=0x9a5a338, defcount=2, closure=0x0) at Python/ceval.c:2831
#31 0x080c4a89 in PyEval_EvalFrameEx (f=0xaff77fc, throwflag=0) at Python/ceval.c:3660
#32 0x080c57c5 in PyEval_EvalFrameEx (f=0xafc9604, throwflag=0) at Python/ceval.c:3650
#33 0x080c65d5 in PyEval_EvalCodeEx (co=0x99eb7b8, globals=0x99ddacc, locals=0x0, args=0xaf85b7c, argcount=2,
    kws=0xaf85b84, kwcount=0, defs=0x9a5a698, defcount=1, closure=0x0) at Python/ceval.c:2831
#34 0x080c4a89 in PyEval_EvalFrameEx (f=0xaf85a3c, throwflag=0) at Python/ceval.c:3660
#35 0x080c65d5 in PyEval_EvalCodeEx (co=0x99eb6e0, globals=0x99ddacc, locals=0x0, args=0x98c98f0, argcount=2,
    kws=0x98c98f8, kwcount=0, defs=0x9a5a678, defcount=1, closure=0x0) at Python/ceval.c:2831
#36 0x080c4a89 in PyEval_EvalFrameEx (f=0x98c97ac, throwflag=0) at Python/ceval.c:3660
#37 0x080c65d5 in PyEval_EvalCodeEx (co=0x999a410, globals=0x99988ac, locals=0x0, args=0x980366c, argcount=1,
    kws=0x9803670, kwcount=2, defs=0x99c1c38, defcount=2, closure=0x0) at Python/ceval.c:2831
#38 0x080c4a89 in PyEval_EvalFrameEx (f=0x9803534, throwflag=0) at Python/ceval.c:3660
#39 0x080c65d5 in PyEval_EvalCodeEx (co=0xb7edd5c0, globals=0xb7f2facc, locals=0xb7f2facc, args=0x0, argcount=0, kws=0x0,
    kwcount=0, defs=0x0, defcount=0, closure=0x0) at Python/ceval.c:2831
#40 0x080c6647 in PyEval_EvalCode (co=0xb7edd5c0, globals=0xb7f2facc, locals=0xb7f2facc) at Python/ceval.c:494
#41 0x080e52c8 in PyRun_FileExFlags (fp=0x982c788,
    filename=0xbff57c9e "/tmp/Work/sage-2.8.9.alpha0/local/bin/sage-gdb-pythonstartup", start=257, globals=0xb7f2facc,
    locals=0xb7f2facc, closeit=0, flags=0xbff55698) at Python/pythonrun.c:1271
#42 0x080e5557 in PyRun_SimpleFileExFlags (fp=0x982c788,
    filename=0xbff57c9e "/tmp/Work/sage-2.8.9.alpha0/local/bin/sage-gdb-pythonstartup", closeit=0, flags=0xbff55698)
    at Python/pythonrun.c:877
#43 0x080571a6 in Py_Main (argc=0, argv=0xbff55764) at Modules/main.c:134
#44 0x08056432 in main (argc=Cannot access memory at address 0x0
) at ./Modules/python.c:23
(gdb)
```

Cheers,

Michael



---

archive/issue_comments_005920.json:
```json
{
    "body": "Hmm, googling reveals:\n\n```\n-/* Return a Py_ssize_t integer from the object item */\n-Py_ssize_t\n+/* Return a Python Int or Long from the object item\n+   Raise TypeError if the result is not an int-or-long\n+   or if the object cannot be interpreted as an index.\n```\nSee http://mail.python.org/pipermail/python-dev/2006-August/068204.html\n\nMaybe dense_prod_of_row_sums fails.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-25T10:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, googling reveals:

```
-/* Return a Py_ssize_t integer from the object item */
-Py_ssize_t
+/* Return a Python Int or Long from the object item
+   Raise TypeError if the result is not an int-or-long
+   or if the object cannot be interpreted as an index.
```
See http://mail.python.org/pipermail/python-dev/2006-August/068204.html

Maybe dense_prod_of_row_sums fails.

Cheers,

Michael



---

archive/issue_comments_005921.json:
```json
{
    "body": "I think we nailed it:\n\n```\n[02:30] <mabshoff> Ok, every time c=0 the refcount for int(0) goes up by one.\n[02:42] <cwitty> It's a Cython bug.\n[02:42] <mabshoff> Yep, for c in cols:\n[02:42] <mabshoff> increments the refcount on int(?)\n[02:42] <cwitty> I've been having a hard time debugging it because the bug doesn't occur any more in the current Cython (so it's gone in 2.8.10).\n[02:43] <mabshoff> Ok, let me upgrade and see if the problem goes away.\n[02:44] <mabshoff> Got any more technical details?\n[02:45] <cwitty> In 2.8.9's version of Cython, converting a Python object (like the int objects we're dealing with) to a Py_Ssize_t goes via this line of code:\n[02:45] <cwitty> #define __pyx_PyIndex_AsSsize_t(b) PyInt_AsSsize_t(PyNumber_Index(b))\n[02:46] <cwitty> PyNumber_Index(b) returns a new object (although in this case it's actually the exact same int object), with its refcount incremented.\n[02:46] <mabshoff> Ok, that makes sense.\n[02:46] <cwitty> So the caller of PyNumber_Index() is supposed to decref the return value at some point.\n```\nI am verifying that the problem is gone. So stay tuned.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-31T02:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think we nailed it:

```
[02:30] <mabshoff> Ok, every time c=0 the refcount for int(0) goes up by one.
[02:42] <cwitty> It's a Cython bug.
[02:42] <mabshoff> Yep, for c in cols:
[02:42] <mabshoff> increments the refcount on int(?)
[02:42] <cwitty> I've been having a hard time debugging it because the bug doesn't occur any more in the current Cython (so it's gone in 2.8.10).
[02:43] <mabshoff> Ok, let me upgrade and see if the problem goes away.
[02:44] <mabshoff> Got any more technical details?
[02:45] <cwitty> In 2.8.9's version of Cython, converting a Python object (like the int objects we're dealing with) to a Py_Ssize_t goes via this line of code:
[02:45] <cwitty> #define __pyx_PyIndex_AsSsize_t(b) PyInt_AsSsize_t(PyNumber_Index(b))
[02:46] <cwitty> PyNumber_Index(b) returns a new object (although in this case it's actually the exact same int object), with its refcount incremented.
[02:46] <mabshoff> Ok, that makes sense.
[02:46] <cwitty> So the caller of PyNumber_Index() is supposed to decref the return value at some point.
```
I am verifying that the problem is gone. So stay tuned.

Cheers,

Michael



---

archive/issue_comments_005922.json:
```json
{
    "body": "Fixed by the Cython update that was merged in 2.8.10.\n\nThe test passes on my 32 bit box:\n\n```\nsage: time dance(10)\nh^10 - 35*h^9 + 675*h^8 - 8610*h^7 + 78435*h^6 - 523467*h^5 + 2562525*h^4 - 9008160*h^3 + 21623220*h^2 - 31840760*h + 21750840\nCPU times: user 11462.61 s, sys: 58.83 s, total: 11521.44 s\nWall time: 12070.05\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-10-31T05:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by the Cython update that was merged in 2.8.10.

The test passes on my 32 bit box:

```
sage: time dance(10)
h^10 - 35*h^9 + 675*h^8 - 8610*h^7 + 78435*h^6 - 523467*h^5 + 2562525*h^4 - 9008160*h^3 + 21623220*h^2 - 31840760*h + 21750840
CPU times: user 11462.61 s, sys: 58.83 s, total: 11521.44 s
Wall time: 12070.05
```

Cheers,

Michael



---

archive/issue_comments_005923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-31T05:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/973#issuecomment-5923",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002693.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-31T05:54:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/973",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/973#event-2693"
}
```
