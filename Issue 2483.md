# Issue 2483: [with updated spkg] Currently R help does not work

archive/issues_002483.json:
```json
{
    "body": "Assignee: jkantor\n\nKeywords: R\n\nI was looking into the R pexpect interface and noticed that the R help system is totally broken for us. \n\nHowever, adding \n\nmake vignettes \n\nto the R spkg-install fixed this. According to the R website this is for some reason necessary for \nbuilds based on the subversion source. \n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/r-2.6.1.p15.spkg\n\nWith the old package in R, ?mean returned garbage. Now it returns the documentation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2483\n\n",
    "created_at": "2008-03-12T08:05:26Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with updated spkg] Currently R help does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2483",
    "user": "jkantor"
}
```
Assignee: jkantor

Keywords: R

I was looking into the R pexpect interface and noticed that the R help system is totally broken for us. 

However, adding 

make vignettes 

to the R spkg-install fixed this. According to the R website this is for some reason necessary for 
builds based on the subversion source. 

http://sage.math.washington.edu/home/jkantor/spkgs/r-2.6.1.p15.spkg

With the old package in R, ?mean returned garbage. Now it returns the documentation.


Issue created by migration from https://trac.sagemath.org/ticket/2483





---

archive/issue_comments_016827.json:
```json
{
    "body": "Positive review, i.e. the help system now works. But I had to do a couple things:\n\n* add and SPKG.txt entry for the new version\n* commit outstanding changes in the main hg repo\n\nThe new spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/r-2.6.1.p15.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-14T14:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2483#issuecomment-16827",
    "user": "mabshoff"
}
```

Positive review, i.e. the help system now works. But I had to do a couple things:

* add and SPKG.txt entry for the new version
* commit outstanding changes in the main hg repo

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.4/alpha0/r-2.6.1.p15.spkg

Cheers,

Michael



---

archive/issue_comments_016828.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T14:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2483#issuecomment-16828",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_016829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T14:52:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2483#issuecomment-16829",
    "user": "mabshoff"
}
```

Resolution: fixed
