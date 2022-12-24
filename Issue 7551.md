# Issue 7551: Remove all Fortran binary compilers except OS X.

archive/issues_007551.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein\n\nThe package fortran-20071120.p9 has Fortran compilers for various systems. William Stein said:\n\nhttp://groups.google.com/group/sage-devel/msg/b4cf0f10ed040d5d?hl=en\n\n*\"I think in sage-4.3 on, we should *only* include fortran compilers for OS X, and *nothing* else.\"*\n\nI've looked at the fortran package, with a view to removing these, but it looks an quite a complex spkg-install, and since William is listed as the maintainer, I've assigned this to him. Feel free to unassign yourself William, but I think you are probably the best person for this. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/7551\n\n",
    "created_at": "2009-11-28T22:22:58Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Remove all Fortran binary compilers except OS X.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7551",
    "user": "drkirkby"
}
```
Assignee: @williamstein

CC:  @williamstein

The package fortran-20071120.p9 has Fortran compilers for various systems. William Stein said:

http://groups.google.com/group/sage-devel/msg/b4cf0f10ed040d5d?hl=en

*"I think in sage-4.3 on, we should *only* include fortran compilers for OS X, and *nothing* else."*

I've looked at the fortran package, with a view to removing these, but it looks an quite a complex spkg-install, and since William is listed as the maintainer, I've assigned this to him. Feel free to unassign yourself William, but I think you are probably the best person for this. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/7551





---

archive/issue_comments_064170.json:
```json
{
    "body": "This ticket looks like a doublette to\n\n#7485:\nmake fortran a prerequisite on all platforms except OS X. Remove g95 binaries from Sage",
    "created_at": "2009-12-01T21:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7551#issuecomment-64170",
    "user": "GeorgSWeber"
}
```

This ticket looks like a doublette to

#7485:
make fortran a prerequisite on all platforms except OS X. Remove g95 binaries from Sage



---

archive/issue_comments_064171.json:
```json
{
    "body": "Hi George, \n\nyou are correct, this ticket is identical to William's \"make fortran a prerequisite on all platforms except OS X. Remove g95 binaries from Sage\" #7485 which he has in fact marked as \"critical\". It's best if William resolves this, as he has a better understanding of this Fortran issue. I've cc'ed William, and closed this as a duplicate of #7485.",
    "created_at": "2009-12-06T10:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7551#issuecomment-64171",
    "user": "drkirkby"
}
```

Hi George, 

you are correct, this ticket is identical to William's "make fortran a prerequisite on all platforms except OS X. Remove g95 binaries from Sage" #7485 which he has in fact marked as "critical". It's best if William resolves this, as he has a better understanding of this Fortran issue. I've cc'ed William, and closed this as a duplicate of #7485.



---

archive/issue_comments_064172.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-12-06T10:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7551#issuecomment-64172",
    "user": "drkirkby"
}
```

Resolution: duplicate



---

archive/issue_comments_064173.json:
```json
{
    "body": "> It's best if William resolves this, as he has a better understanding \n> of this Fortran issue. \n\nIt's best if anybody does this.  Don't assign it to me, since I might never find time to actually do it.    In fact, it's best if somebody else does this, since then the number of people that have an understanding of the Fortran issue increases. :-)\n\nWilliam",
    "created_at": "2009-12-06T15:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7551#issuecomment-64173",
    "user": "@williamstein"
}
```

> It's best if William resolves this, as he has a better understanding 
> of this Fortran issue. 

It's best if anybody does this.  Don't assign it to me, since I might never find time to actually do it.    In fact, it's best if somebody else does this, since then the number of people that have an understanding of the Fortran issue increases. :-)

William
