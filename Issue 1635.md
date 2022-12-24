# Issue 1635: Singular.spkg relatated: lib->LIB link issue on OSX

archive/issues_001635.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe problem has come up a couple times on sage-devel: The OSX binary Sage tar-ball contains a link case sensitive link lib->LIB that is caused by the singular.spkg. I believe it is to accomodate some issue with Singular's high level libraries. We should just skip creating that link on OSX and all should be fine.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1635\n\n",
    "created_at": "2007-12-29T06:19:21Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.2",
    "title": "Singular.spkg relatated: lib->LIB link issue on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1635",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The problem has come up a couple times on sage-devel: The OSX binary Sage tar-ball contains a link case sensitive link lib->LIB that is caused by the singular.spkg. I believe it is to accomodate some issue with Singular's high level libraries. We should just skip creating that link on OSX and all should be fine.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1635





---

archive/issue_comments_010403.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-31T10:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1635#issuecomment-10403",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010404.json:
```json
{
    "body": "The following spkg fixes the issue by avoiding creating a `lib->LIB` link:\n\n* http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p0.spkg\n\nI tested the resulting bdist and it no longer shows the issue on an OSX 10.4 box with default file system options.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-02T21:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1635#issuecomment-10404",
    "user": "mabshoff"
}
```

The following spkg fixes the issue by avoiding creating a `lib->LIB` link:

* http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p0.spkg

I tested the resulting bdist and it no longer shows the issue on an OSX 10.4 box with default file system options.

Cheers,

Michael



---

archive/issue_comments_010405.json:
```json
{
    "body": "Oops, I mean \n\n* http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p1.spkg\n\nSorry for the confusion.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-02T21:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1635#issuecomment-10405",
    "user": "mabshoff"
}
```

Oops, I mean 

* http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p1.spkg

Sorry for the confusion.

Cheers,

Michael



---

archive/issue_comments_010406.json:
```json
{
    "body": "This builds fine for me.",
    "created_at": "2008-01-03T07:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1635#issuecomment-10406",
    "user": "@mwhansen"
}
```

This builds fine for me.



---

archive/issue_comments_010407.json:
```json
{
    "body": "Merged in 2.9.2.alpha0",
    "created_at": "2008-01-03T13:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1635#issuecomment-10407",
    "user": "mabshoff"
}
```

Merged in 2.9.2.alpha0



---

archive/issue_comments_010408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-03T13:51:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1635#issuecomment-10408",
    "user": "mabshoff"
}
```

Resolution: fixed
