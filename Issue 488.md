# Issue 488: python on itanium -- fix readline

archive/issues_000488.json:
```json
{
    "body": "Assignee: was\n\nPython2.5.1 is broken on itanium.  The fix in SAGE is also broken in sage-2.8.2.  Fix this for sage-2.8.3. \n \n1. look at old hack from sage-1.5.*\n2. get rid of #else and #ifdef stuff from around line 33\n3. keep the casting stuff around line 670??\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/488\n\n",
    "created_at": "2007-08-24T07:46:07Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "python on itanium -- fix readline",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/488",
    "user": "was"
}
```
Assignee: was

Python2.5.1 is broken on itanium.  The fix in SAGE is also broken in sage-2.8.2.  Fix this for sage-2.8.3. 
 
1. look at old hack from sage-1.5.*
2. get rid of #else and #ifdef stuff from around line 33
3. keep the casting stuff around line 670??


Issue created by migration from https://trac.sagemath.org/ticket/488





---

archive/issue_comments_002433.json:
```json
{
    "body": "Changing component from algebraic geometry to packages.",
    "created_at": "2007-08-24T13:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/488#issuecomment-2433",
    "user": "mabshoff"
}
```

Changing component from algebraic geometry to packages.



---

archive/issue_comments_002434.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T03:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/488#issuecomment-2434",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002435.json:
```json
{
    "body": "fixed in python-2.5.1.p6",
    "created_at": "2007-08-29T03:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/488#issuecomment-2435",
    "user": "was"
}
```

fixed in python-2.5.1.p6
