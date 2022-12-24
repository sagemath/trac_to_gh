# Issue 4009: [with spkg, needs review] OSX 10.4/5: build R without the aqua support

archive/issues_004009.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a followup to #4407: When we build R on OSX we per default build extensions that depend on OSX specific frameworks, namely aqua dependent code. That FrameWork ends up pulling in Apple's libpng.dylib which is incompatible with the one we build. Consequently the build of R fails. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/r-2.6.1.p18.spkg\n\ndisables aqua support for R just like the 64 bit OSX build. The spkg builds fine on OSX 10.4 and 10.5 and passes doctests. \n\nCheers,\n\nMichael\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4009\n\n",
    "created_at": "2008-08-30T23:46:01Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] OSX 10.4/5: build R without the aqua support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4009",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This is a followup to #4407: When we build R on OSX we per default build extensions that depend on OSX specific frameworks, namely aqua dependent code. That FrameWork ends up pulling in Apple's libpng.dylib which is incompatible with the one we build. Consequently the build of R fails. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/r-2.6.1.p18.spkg

disables aqua support for R just like the 64 bit OSX build. The spkg builds fine on OSX 10.4 and 10.5 and passes doctests. 

Cheers,

Michael

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4009





---

archive/issue_comments_028935.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-30T23:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4009#issuecomment-28935",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028936.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T23:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4009#issuecomment-28936",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha3



---

archive/issue_comments_028937.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T23:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4009",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4009#issuecomment-28937",
    "user": "mabshoff"
}
```

Resolution: fixed
