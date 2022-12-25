# Issue 1940: Segmentation fault when comparing two empty ideals

archive/issues_001940.json:
```json
{
    "body": "Assignee: @malb\n\nThe following three lines produce a segmentation fault.\n\n```\nsage: R=PolynomialRing(QQ,'x,y,z')\nsage: I=R.ideal()\nsage: I==R.ideal()\n```\n\nmabshoff gives the following information:\nlibSingular is not surprisingly  involved: \n\n```\n(gdb) bt \n#0 \n__pyx_pf_4sage_5rings_10polynomial_34multi_polynomial_ideal_libsingular_int\u00aderred_libsingular \n( \n    __pyx_self=<value optimized out>, __pyx_v_I=0x2af2cff2eaf0) \n    at sage/rings/polynomial/multi_polynomial_ideal_libsingular.cpp: \n3059 \n#1  0x0000000000484326 in PyEval_EvalFrameEx (f=0x1a6a310, \nthrowflag=<value optimized out>) at Python/ceval.c:3552 \n#2  0x000000000048403b in PyEval_EvalFrameEx (f=0x1a623a0, \nthrowflag=<value optimized out>) at Python/ceval.c:3650 \n#3  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2af2c2b2db70, \nglobals=<value optimized out>, \n    locals=<value optimized out>, args=0x2af2cff25380, argcount=2, \nkws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) \n    at Python/ceval.c:2831 \n#4  0x00000000004ce528 in function_call (func=0x2af2c2b36cf8, \narg=0x2af2cff25368, kw=0x0) at Objects/funcobject.c:517 \n#5  0x0000000000415523 in PyObject_Call (func=0x1a6b890, arg=0x1, \nkw=0x7fffefddfec0) at Objects/abstract.c:1860 \n#6  0x000000000041bc43 in instancemethod_call (func=<value optimized \nout>, arg=0x2af2cff25368, kw=0x0) \n    at Objects/classobject.c:2497 \n#7  0x0000000000415523 in PyObject_Call (func=0x1a6b890, arg=0x1, \nkw=0x7fffefddfec0) at Objects/abstract.c:1860 \n#8  0x000000000047c851 in PyEval_CallObjectWithKeywords \n(func=0x2af2cf8c4320, arg=0x2af2cf8a5d50, kw=0x0) \n    at Python/ceval.c:3433 \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1940\n\n",
    "created_at": "2008-01-26T15:40:43Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Segmentation fault when comparing two empty ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1940",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @malb

The following three lines produce a segmentation fault.

```
sage: R=PolynomialRing(QQ,'x,y,z')
sage: I=R.ideal()
sage: I==R.ideal()
```

mabshoff gives the following information:
libSingular is not surprisingly  involved: 

```
(gdb) bt 
#0 
__pyx_pf_4sage_5rings_10polynomial_34multi_polynomial_ideal_libsingular_int­erred_libsingular 
( 
    __pyx_self=<value optimized out>, __pyx_v_I=0x2af2cff2eaf0) 
    at sage/rings/polynomial/multi_polynomial_ideal_libsingular.cpp: 
3059 
#1  0x0000000000484326 in PyEval_EvalFrameEx (f=0x1a6a310, 
throwflag=<value optimized out>) at Python/ceval.c:3552 
#2  0x000000000048403b in PyEval_EvalFrameEx (f=0x1a623a0, 
throwflag=<value optimized out>) at Python/ceval.c:3650 
#3  0x0000000000484f3b in PyEval_EvalCodeEx (co=0x2af2c2b2db70, 
globals=<value optimized out>, 
    locals=<value optimized out>, args=0x2af2cff25380, argcount=2, 
kws=0x0, kwcount=0, defs=0x0, defcount=0, closure=0x0) 
    at Python/ceval.c:2831 
#4  0x00000000004ce528 in function_call (func=0x2af2c2b36cf8, 
arg=0x2af2cff25368, kw=0x0) at Objects/funcobject.c:517 
#5  0x0000000000415523 in PyObject_Call (func=0x1a6b890, arg=0x1, 
kw=0x7fffefddfec0) at Objects/abstract.c:1860 
#6  0x000000000041bc43 in instancemethod_call (func=<value optimized 
out>, arg=0x2af2cff25368, kw=0x0) 
    at Objects/classobject.c:2497 
#7  0x0000000000415523 in PyObject_Call (func=0x1a6b890, arg=0x1, 
kw=0x7fffefddfec0) at Objects/abstract.c:1860 
#8  0x000000000047c851 in PyEval_CallObjectWithKeywords 
(func=0x2af2cf8c4320, arg=0x2af2cf8a5d50, kw=0x0) 
    at Python/ceval.c:3433 
```



Issue created by migration from https://trac.sagemath.org/ticket/1940





---

archive/issue_comments_012280.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-27T07:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1940#issuecomment-12280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_012281.json:
```json
{
    "body": "Attachment [trac_1940_interred.patch](tarball://root/attachments/some-uuid/ticket1940/trac_1940_interred.patch) by @malb created at 2008-01-27 19:53:45",
    "created_at": "2008-01-27T19:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1940#issuecomment-12281",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1940_interred.patch](tarball://root/attachments/some-uuid/ticket1940/trac_1940_interred.patch) by @malb created at 2008-01-27 19:53:45



---

archive/issue_comments_012282.json:
```json
{
    "body": "Doctests are added for the segfault case, patch looks good to me.",
    "created_at": "2008-01-27T20:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1940#issuecomment-12282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests are added for the segfault case, patch looks good to me.



---

archive/issue_comments_012283.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-27T20:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1940#issuecomment-12283",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc2



---

archive/issue_comments_012284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T20:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1940#issuecomment-12284",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004662.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-27T20:30:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1940",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1940#event-4662"
}
```
