# Issue 2592: NTL abort in Integers(125)[]

archive/issues_002592.json:
```json
{
    "body": "Assignee: somebody\n\nThis NTL abort should be handled with a python exception:\n\n```\nsage: R.<x> = Integers(125)[]\nsage: (3*x).quo_rem(5*x)\nInvMod: inverse undefined\n/home/joel/sage/local/bin/sage-sage: line 214: 31177 Aborted                 sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2592\n\n",
    "created_at": "2008-03-19T08:55:25Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "NTL abort in Integers(125)[]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2592",
    "user": "jbmohler"
}
```
Assignee: somebody

This NTL abort should be handled with a python exception:

```
sage: R.<x> = Integers(125)[]
sage: (3*x).quo_rem(5*x)
InvMod: inverse undefined
/home/joel/sage/local/bin/sage-sage: line 214: 31177 Aborted                 sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
```



Issue created by migration from https://trac.sagemath.org/ticket/2592





---

archive/issue_comments_017738.json:
```json
{
    "body": "Looks like somebody is not checking the return value of some NTL function:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x> = Integers(125)[]\nsage: (3*x).quo_rem(5*x)\nInvMod: inverse undefined\n| SAGE Version 2.10.4, Release Date: 2008-03-16                      |\n| Type notebook() for the GUI, and license() for information.        |\nProgram received signal SIGABRT, Aborted.\n[Switching to Thread 46994942697312 (LWP 9397)]\n0x00002abddcbcc07b in raise () from /lib/libc.so.6\n(gdb) bt\n#0  0x00002abddcbcc07b in raise () from /lib/libc.so.6\n#1  0x00002abddcbcd84e in abort () from /lib/libc.so.6\n#2  0x00002abddddab097 in NTL::Error (s=<value optimized out>) at tools.c:14\n#3  0x00002abdddcfeee9 in NTL::InvMod (a=<value optimized out>, n=125) at ZZ.c:351\n#4  0x00002abdddd716c6 in NTL::PlainDivRem (q=@0x2abdf2106950, r=@0x2abdf21069c0, a=@0x2abdefb18720, b=@0xffffffffffffffff)\n    at ../include/NTL/lzz_p.h:278\n#5  0x00002abde75b842e in __pyx_pf_4sage_5rings_10polynomial_25polynomial_modn_dense_ntl_28Polynomial_dense_modn_ntl_zz_quo_rem (__pyx_v_self=0x2abdefb186e0, __pyx_v_right=0x2abdf21068a0) at sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:7456\n#6  0x0000000000484a96 in PyEval_EvalFrameEx (f=0x14d00c0, throwflag=<value optimized out>) at Python/ceval.c:3552\n#7  0x00000000004856ab in PyEval_EvalCodeEx (co=0x2abdf05a1468, globals=<value optimized out>,\n    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)\n    at Python/ceval.c:2831\n#8  0x0000000000484435 in PyEval_EvalFrameEx (f=0x149ea60, throwflag=<value optimized out>) at Python/ceval.c:494\n#9  0x00000000004856ab in PyEval_EvalCodeEx (co=0x2abde013e918, globals=<value optimized out>,\n    locals=<value optimized out>, args=0x1b43f00, argcount=2, kws=0x1b43f10, kwcount=0, defs=0x0, defcount=0, closure=0x0)\n    at Python/ceval.c:2831\n#10 0x0000000000483dcd in PyEval_EvalFrameEx (f=0x1b43d60, throwflag=<value optimized out>) at Python/ceval.c:3660\n#11 0x00000000004856ab in PyEval_EvalCodeEx (co=0x2abde013e828, globals=<value optimized out>,\n    locals=<value optimized out>, args=0x1, argcount=3, kws=0x1b47730, kwcount=0, defs=0x2abde01ab5c0, defcount=2,\n    closure=0x0) at Python/ceval.c:2831\n```\n",
    "created_at": "2008-03-19T09:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17738",
    "user": "mabshoff"
}
```

Looks like somebody is not checking the return value of some NTL function:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = Integers(125)[]
sage: (3*x).quo_rem(5*x)
InvMod: inverse undefined
| SAGE Version 2.10.4, Release Date: 2008-03-16                      |
| Type notebook() for the GUI, and license() for information.        |
Program received signal SIGABRT, Aborted.
[Switching to Thread 46994942697312 (LWP 9397)]
0x00002abddcbcc07b in raise () from /lib/libc.so.6
(gdb) bt
#0  0x00002abddcbcc07b in raise () from /lib/libc.so.6
#1  0x00002abddcbcd84e in abort () from /lib/libc.so.6
#2  0x00002abddddab097 in NTL::Error (s=<value optimized out>) at tools.c:14
#3  0x00002abdddcfeee9 in NTL::InvMod (a=<value optimized out>, n=125) at ZZ.c:351
#4  0x00002abdddd716c6 in NTL::PlainDivRem (q=@0x2abdf2106950, r=@0x2abdf21069c0, a=@0x2abdefb18720, b=@0xffffffffffffffff)
    at ../include/NTL/lzz_p.h:278
#5  0x00002abde75b842e in __pyx_pf_4sage_5rings_10polynomial_25polynomial_modn_dense_ntl_28Polynomial_dense_modn_ntl_zz_quo_rem (__pyx_v_self=0x2abdefb186e0, __pyx_v_right=0x2abdf21068a0) at sage/rings/polynomial/polynomial_modn_dense_ntl.cpp:7456
#6  0x0000000000484a96 in PyEval_EvalFrameEx (f=0x14d00c0, throwflag=<value optimized out>) at Python/ceval.c:3552
#7  0x00000000004856ab in PyEval_EvalCodeEx (co=0x2abdf05a1468, globals=<value optimized out>,
    locals=<value optimized out>, args=0x0, argcount=0, kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2831
#8  0x0000000000484435 in PyEval_EvalFrameEx (f=0x149ea60, throwflag=<value optimized out>) at Python/ceval.c:494
#9  0x00000000004856ab in PyEval_EvalCodeEx (co=0x2abde013e918, globals=<value optimized out>,
    locals=<value optimized out>, args=0x1b43f00, argcount=2, kws=0x1b43f10, kwcount=0, defs=0x0, defcount=0, closure=0x0)
    at Python/ceval.c:2831
#10 0x0000000000483dcd in PyEval_EvalFrameEx (f=0x1b43d60, throwflag=<value optimized out>) at Python/ceval.c:3660
#11 0x00000000004856ab in PyEval_EvalCodeEx (co=0x2abde013e828, globals=<value optimized out>,
    locals=<value optimized out>, args=0x1, argcount=3, kws=0x1b47730, kwcount=0, defs=0x2abde01ab5c0, defcount=2,
    closure=0x0) at Python/ceval.c:2831
```




---

archive/issue_comments_017739.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-19T09:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17739",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_017740.json:
```json
{
    "body": "Calls to NTL's div (and div-like) functions were only wrapped in `_sig_on`/`_sig_off` if the polynomials were large enough in some cases. The patch I'm attaching removes the condition in these cases, and adds a doctest for one of them.",
    "created_at": "2008-04-15T14:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17740",
    "user": "wjp"
}
```

Calls to NTL's div (and div-like) functions were only wrapped in `_sig_on`/`_sig_off` if the polynomials were large enough in some cases. The patch I'm attaching removes the condition in these cases, and adds a doctest for one of them.



---

archive/issue_comments_017741.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-15T14:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17741",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_017742.json:
```json
{
    "body": "Attachment\n\nThe patch in `ntl_div_sig_after2903.patch` adapts the doctest to the patch for #2903. (Only apply it if #2903 is also applied.)",
    "created_at": "2008-04-15T15:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17742",
    "user": "wjp"
}
```

Attachment

The patch in `ntl_div_sig_after2903.patch` adapts the doctest to the patch for #2903. (Only apply it if #2903 is also applied.)



---

archive/issue_comments_017743.json:
```json
{
    "body": "Both patches look good to me. Positive review. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-17T19:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17743",
    "user": "mabshoff"
}
```

Both patches look good to me. Positive review. 

Cheers,

Michael



---

archive/issue_comments_017744.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-17T20:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17744",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_017745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-17T20:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2592",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2592#issuecomment-17745",
    "user": "mabshoff"
}
```

Resolution: fixed
