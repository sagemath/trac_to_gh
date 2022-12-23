# Issue 3696: [with spkg, needs review] Fix gmp.spkg build issue on Solaris

archive/issues_003696.json:
```json
{
    "body": "Assignee: mabshoff\n\nDue to bashisms on Solaris gmp fails to build. This is fixed by using \"/usr/bin/env bash\" instead of \"/bin/sh\" in spkg/install. That is the only change to \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/gmp-4.2.2.p1.fake.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3696\n\n",
    "created_at": "2008-07-21T19:07:54Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "[with spkg, needs review] Fix gmp.spkg build issue on Solaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3696",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Due to bashisms on Solaris gmp fails to build. This is fixed by using "/usr/bin/env bash" instead of "/bin/sh" in spkg/install. That is the only change to 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/gmp-4.2.2.p1.fake.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3696





---

archive/issue_comments_026228.json:
```json
{
    "body": "Merged in Sage 3.0.6.rc0",
    "created_at": "2008-07-21T19:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3696#issuecomment-26228",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.rc0



---

archive/issue_comments_026229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-21T19:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3696#issuecomment-26229",
    "user": "mabshoff"
}
```

Resolution: fixed
