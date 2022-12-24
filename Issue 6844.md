# Issue 6844: Clean up spkg-install for readline

archive/issues_006844.json:
```json
{
    "body": "Assignee: tbd\n\nThe spkg-install for readline does a lot of silly things. \n\n* It does a grep on /etc/SuSE-release even if the file does not exist. \n* It adds  -m64 only on OS X if SAGE64 is set to 'yes'\n* It adds -m64 as a linker flag, even though no such linker flags exists on any linker I can find. \n\nIt needs a cleanup. I'll do this. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/6844\n\n",
    "created_at": "2009-08-30T07:15:51Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Clean up spkg-install for readline",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6844",
    "user": "drkirkby"
}
```
Assignee: tbd

The spkg-install for readline does a lot of silly things. 

* It does a grep on /etc/SuSE-release even if the file does not exist. 
* It adds  -m64 only on OS X if SAGE64 is set to 'yes'
* It adds -m64 as a linker flag, even though no such linker flags exists on any linker I can find. 

It needs a cleanup. I'll do this. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/6844





---

archive/issue_comments_056455.json:
```json
{
    "body": "Fixed by #6945.",
    "created_at": "2009-09-17T22:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6844#issuecomment-56455",
    "user": "mvngu"
}
```

Fixed by #6945.



---

archive/issue_comments_056456.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-17T22:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6844#issuecomment-56456",
    "user": "mvngu"
}
```

Resolution: duplicate
