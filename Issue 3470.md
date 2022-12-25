# Issue 3470: [with spkg; needs review] add pyprocessing (=multiproccessing) to sage

archive/issues_003470.json:
```json
{
    "body": "Assignee: @yqiang\n\nThis has been officially excepted for Python 2.7, but we need it now.  It is Python/c and takes literally 1 second to install, and supports OSX, Linux, Windows, etc.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3470\n\n",
    "created_at": "2008-06-19T16:32:23Z",
    "labels": [
        "component: dsage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg; needs review] add pyprocessing (=multiproccessing) to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3470",
    "user": "https://github.com/williamstein"
}
```
Assignee: @yqiang

This has been officially excepted for Python 2.7, but we need it now.  It is Python/c and takes literally 1 second to install, and supports OSX, Linux, Windows, etc.

Issue created by migration from https://trac.sagemath.org/ticket/3470





---

archive/issue_comments_024416.json:
```json
{
    "body": "Attachment [processing-0.52.spkg](tarball://root/attachments/some-uuid/ticket3470/processing-0.52.spkg) by boothby created at 2008-06-19 18:01:51\n\nspkg contains spkg-check, SPKG.txt, hg repo.  Works on debian/xeon.  Needs testing on other platforms.",
    "created_at": "2008-06-19T18:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24416",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [processing-0.52.spkg](tarball://root/attachments/some-uuid/ticket3470/processing-0.52.spkg) by boothby created at 2008-06-19 18:01:51

spkg contains spkg-check, SPKG.txt, hg repo.  Works on debian/xeon.  Needs testing on other platforms.



---

archive/issue_comments_024417.json:
```json
{
    "body": "Having looked at the source, I'm very worried about the lack of comments, but the design is solid.  The socket io code is poor - its not very robust or fast compared to twisted.  However, it \"just works\" as of now, and as long as it is hidden entirely behind the parallel api (so that we don't have any pyprocessing specific functions), I approve of this spkg from a code review perspective.",
    "created_at": "2008-06-19T18:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24417",
    "user": "https://github.com/garyfurnish"
}
```

Having looked at the source, I'm very worried about the lack of comments, but the design is solid.  The socket io code is poor - its not very robust or fast compared to twisted.  However, it "just works" as of now, and as long as it is hidden entirely behind the parallel api (so that we don't have any pyprocessing specific functions), I approve of this spkg from a code review perspective.



---

archive/issue_comments_024418.json:
```json
{
    "body": "Looks good to me, pretty straightforward spkg. Also I'm not worried too much about the code since it will be included upstream in python 2.7 and it will have to adhere to Python's coding standards.",
    "created_at": "2008-06-19T20:56:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24418",
    "user": "https://github.com/yqiang"
}
```

Looks good to me, pretty straightforward spkg. Also I'm not worried too much about the code since it will be included upstream in python 2.7 and it will have to adhere to Python's coding standards.



---

archive/issue_comments_024419.json:
```json
{
    "body": "\n```\nAnyway, since every single person voted +1 and nobody voted -1 or\nhad issues, I declare this package officially accepted.\n\n -- William\n```\n",
    "created_at": "2008-06-24T17:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24419",
    "user": "https://github.com/williamstein"
}
```


```
Anyway, since every single person voted +1 and nobody voted -1 or
had issues, I declare this package officially accepted.

 -- William
```




---

archive/issue_comments_024420.json:
```json
{
    "body": "Nick wants the vote reopened for two more days, so I reopened it until Thursday.",
    "created_at": "2008-06-24T17:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24420",
    "user": "https://github.com/williamstein"
}
```

Nick wants the vote reopened for two more days, so I reopened it until Thursday.



---

archive/issue_comments_024421.json:
```json
{
    "body": "In the end the vote was positive and no one voted against it. It is nearly Thursday, so I am merging this. I did end up adding a `.hgignore` and check some more files into the repo. I also renamed the spkg `pyprocessing-0.52.spkg`. Additional positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T04:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

In the end the vote was positive and no one voted against it. It is nearly Thursday, so I am merging this. I did end up adding a `.hgignore` and check some more files into the repo. I also renamed the spkg `pyprocessing-0.52.spkg`. Additional positive review.

Cheers,

Michael



---

archive/issue_comments_024422.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T04:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024423.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T04:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3470",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3470#issuecomment-24423",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
