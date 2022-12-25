# Issue 3310: sage -b fails after touching sage/libs/mwrank/{mwrank.pyx,wrap.cc}

archive/issues_003310.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n1. Make a fresh clone of a 3.0.2 build.\n2. touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/mwrank.pyx\n3. sage -b\n4. touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/wrap.cc\n5. sage -b\n\n...produces this:\n\n\n```\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nbuilding 'sage.libs.mwrank.mwrank' extension\nerror: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')\nsage: There was an error installing modified sage library code.\n```\n\nbut then after doing again\n\n```\ntouch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/mwrank.pyx\n```\n\nsage -br works fine.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3310\n\n",
    "created_at": "2008-05-26T19:26:46Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "sage -b fails after touching sage/libs/mwrank/{mwrank.pyx,wrap.cc}",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3310",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: mabshoff


1. Make a fresh clone of a 3.0.2 build.
2. touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/mwrank.pyx
3. sage -b
4. touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/wrap.cc
5. sage -b

...produces this:


```
----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
running install
running build
running build_py
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.
```

but then after doing again

```
touch $SAGE_ROOT/devel/sage-test1/sage/libs/mwrank/mwrank.pyx
```

sage -br works fine.



Issue created by migration from https://trac.sagemath.org/ticket/3310





---

archive/issue_comments_022844.json:
```json
{
    "body": "Changing priority from minor to blocker.",
    "created_at": "2008-05-26T20:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3310#issuecomment-22844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from minor to blocker.



---

archive/issue_comments_022845.json:
```json
{
    "body": "Changing assignee from mabshoff to @williamstein.",
    "created_at": "2008-05-26T20:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3310#issuecomment-22845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @williamstein.



---

archive/issue_comments_022846.json:
```json
{
    "body": "For the record: #3491 is a dupe of this and I closed the other ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T22:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3310#issuecomment-22846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: #3491 is a dupe of this and I closed the other ticket.

Cheers,

Michael



---

archive/issue_comments_022847.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-10T08:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3310#issuecomment-22847",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022848.json:
```json
{
    "body": "This ticket has been fixed via Craig's and Gonzalo's patch at #4480.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-10T08:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3310#issuecomment-22848",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket has been fixed via Craig's and Gonzalo's patch at #4480.

Cheers,

Michael
