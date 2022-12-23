# Issue 3611: sympow: make it use $CC instead of cc

archive/issues_003611.json:
```json
{
    "body": "Assignee: mabshoff\n\nMake sympow default to $CC[=gcc] instead of cc since that can cause trouble by picking up another compiler\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3611\n\n",
    "created_at": "2008-07-08T17:42:57Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "sympow: make it use $CC instead of cc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3611",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Make sympow default to $CC[=gcc] instead of cc since that can cause trouble by picking up another compiler

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/3611





---

archive/issue_comments_025501.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-08T17:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3611#issuecomment-25501",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025502.json:
```json
{
    "body": "An spkg which picks the default gcc from $PATH is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/sympow-1.018.1.p5.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-07-29T15:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3611#issuecomment-25502",
    "user": "mabshoff"
}
```

An spkg which picks the default gcc from $PATH is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/sympow-1.018.1.p5.spkg

Cheers,

Michael



---

archive/issue_comments_025503.json:
```json
{
    "body": "Looks safe enough.",
    "created_at": "2008-07-29T15:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3611#issuecomment-25503",
    "user": "was"
}
```

Looks safe enough.



---

archive/issue_comments_025504.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T15:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3611#issuecomment-25504",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025505.json:
```json
{
    "body": "Merged in Sage 3.0.6.final",
    "created_at": "2008-07-29T15:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3611#issuecomment-25505",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.final
