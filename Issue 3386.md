# Issue 3386: zn_poly test code is still being run

archive/issues_003386.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe build process is still running the full `zn_poly` test suite. This is probably no longer necessary, and makes the build time somewhat longer than it needs to be.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3386\n\n",
    "created_at": "2008-06-09T14:17:58Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "zn_poly test code is still being run",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3386",
    "user": "dmharvey"
}
```
Assignee: mabshoff

The build process is still running the full `zn_poly` test suite. This is probably no longer necessary, and makes the build time somewhat longer than it needs to be.


Issue created by migration from https://trac.sagemath.org/ticket/3386





---

archive/issue_comments_023705.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-09T21:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3386#issuecomment-23705",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023706.json:
```json
{
    "body": "I know about the test suite still running, but I thought you wouldn't mind the extra coverage. But I agree that we should now disable the testing. The updated spkg that moves the test suite to spkg-check can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha2/zn_poly-0.8.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T21:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3386#issuecomment-23706",
    "user": "mabshoff"
}
```

I know about the test suite still running, but I thought you wouldn't mind the extra coverage. But I agree that we should now disable the testing. The updated spkg that moves the test suite to spkg-check can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha2/zn_poly-0.8.p1.spkg

Cheers,

Michael



---

archive/issue_comments_023707.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha2",
    "created_at": "2008-06-09T21:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3386#issuecomment-23707",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha2



---

archive/issue_comments_023708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-09T21:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3386#issuecomment-23708",
    "user": "mabshoff"
}
```

Resolution: fixed
