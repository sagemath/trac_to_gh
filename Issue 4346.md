# Issue 4346: segmentation fault with set_block

archive/issues_004346.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.4, Release Date: 2008-10-16                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: M=Matrix([1])\nsage: M.set_block(0,1,matrix([1]))\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4346\n\n",
    "created_at": "2008-10-23T09:07:15Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "segmentation fault with set_block",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4346",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: M=Matrix([1])
sage: M.set_block(0,1,matrix([1]))


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/4346





---

archive/issue_comments_031864.json:
```json
{
    "body": "Attachment [sage-4346.patch](tarball://root/attachments/some-uuid/ticket4346/sage-4346.patch) by @williamstein created at 2008-10-23 19:35:07\n\nThe attached patch fixes the problem.  However, there are two additional issues, which should be addressed as new tickets.   \n\n1. After applying this patch and doctesting all sage, there are a bunch of failures in the modular abelian varieties code:\n\n```\n\tsage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 3 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/homspace.py # 34 doctests failed\n\tsage -t  devel/sage-main/sage/modular/abvar/abvar.py # 11 doctests failed\n```\n\n\nThese are because of bugs in that code exposed by doing proper bounds checking.\nThis is now trac #4351, and must also be fixed before #4346 can go into Sage.  \n\n2. In this patch, matrix_window does *not* do bounds checking by default.  This is because there is a bunch of internal usage of matrix_window for strassen algorithms, which actually relies on matrix_window not being bounds checked (it's ok as used by those algorithms).  However, a bunch of code would have to be changed to make bounds checking of matrix_window the default.  That said it is currently easy (even with this patch) to segfault sage interactively:\n\n```\nsage: a = matrix([1]).matrix_window(1,1,1,1)\nsage: a\n\nMatrix window of size 1 x 1 at (1,1):\n[1]\nsage: a[0,0] = 1\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nThis is now trac #4350.",
    "created_at": "2008-10-23T19:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4346#issuecomment-31864",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4346.patch](tarball://root/attachments/some-uuid/ticket4346/sage-4346.patch) by @williamstein created at 2008-10-23 19:35:07

The attached patch fixes the problem.  However, there are two additional issues, which should be addressed as new tickets.   

1. After applying this patch and doctesting all sage, there are a bunch of failures in the modular abelian varieties code:

```
	sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 34 doctests failed
	sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 11 doctests failed
```


These are because of bugs in that code exposed by doing proper bounds checking.
This is now trac #4351, and must also be fixed before #4346 can go into Sage.  

2. In this patch, matrix_window does *not* do bounds checking by default.  This is because there is a bunch of internal usage of matrix_window for strassen algorithms, which actually relies on matrix_window not being bounds checked (it's ok as used by those algorithms).  However, a bunch of code would have to be changed to make bounds checking of matrix_window the default.  That said it is currently easy (even with this patch) to segfault sage interactively:

```
sage: a = matrix([1]).matrix_window(1,1,1,1)
sage: a

Matrix window of size 1 x 1 at (1,1):
[1]
sage: a[0,0] = 1


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


This is now trac #4350.



---

archive/issue_comments_031865.json:
```json
{
    "body": "NOTE: There is an off-by-one mistake in this patch, which is addressed by the second patch to #4350.  Thus #4346 and #4350 should be refereed together.",
    "created_at": "2008-10-23T20:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4346#issuecomment-31865",
    "user": "https://github.com/williamstein"
}
```

NOTE: There is an off-by-one mistake in this patch, which is addressed by the second patch to #4350.  Thus #4346 and #4350 should be refereed together.



---

archive/issue_comments_031866.json:
```json
{
    "body": "Also, the fixes in #4350 fix the non-issue that caused me to open #4351.",
    "created_at": "2008-10-23T20:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4346#issuecomment-31866",
    "user": "https://github.com/williamstein"
}
```

Also, the fixes in #4350 fix the non-issue that caused me to open #4351.



---

archive/issue_comments_031867.json:
```json
{
    "body": "Looks good, as long as you also apply the patches at #4350.",
    "created_at": "2008-10-23T22:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4346#issuecomment-31867",
    "user": "https://github.com/craigcitro"
}
```

Looks good, as long as you also apply the patches at #4350.



---

archive/issue_comments_031868.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T02:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4346#issuecomment-31868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004592.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-26T02:26:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4346#event-4592"
}
```



---

archive/issue_comments_031869.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T02:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4346#issuecomment-31869",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1
