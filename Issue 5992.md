# Issue 5992: [with spkg, needs review] Set stack size in Maxima.spkg to 32kb for clisp

archive/issues_005992.json:
```json
{
    "body": "Assignee: mabshoff\n\nclisp needs a stack larger than many systems provide, i.e. 8kb. If the stacksize isn't raised Maxima can randomly fail to build.\n\nThe spkg at \n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/post-final/maxima-5.16.3.p2.spkg\n\nfixes that issue.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5992\n\n",
    "created_at": "2009-05-06T05:26:28Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with spkg, needs review] Set stack size in Maxima.spkg to 32kb for clisp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5992",
    "user": "mabshoff"
}
```
Assignee: mabshoff

clisp needs a stack larger than many systems provide, i.e. 8kb. If the stacksize isn't raised Maxima can randomly fail to build.

The spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/post-final/maxima-5.16.3.p2.spkg

fixes that issue.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5992





---

archive/issue_comments_047625.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-06T05:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5992#issuecomment-47625",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-06T06:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5992#issuecomment-47626",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047627.json:
```json
{
    "body": "Merged in Sage 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-06T06:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5992",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5992#issuecomment-47627",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.

Cheers,

Michael
