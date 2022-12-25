# Issue 5835: deleting a file from the DATA directory gives an error page

archive/issues_005835.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein\n\nSteps to reproduce:\n\n* Upload a file to a worksheet using the Data... menu\n* Click on the filename in the Data... menu\n* Click the link to delete the file.\n\nMy guess is that it deletes the file, but then tries to display it.  Instead, it should either go back to the worksheet view or to some list of all files in the DATA directory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5835\n\n",
    "created_at": "2009-04-20T17:09:44Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "deleting a file from the DATA directory gives an error page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5835",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

CC:  @williamstein

Steps to reproduce:

* Upload a file to a worksheet using the Data... menu
* Click on the filename in the Data... menu
* Click the link to delete the file.

My guess is that it deletes the file, but then tries to display it.  Instead, it should either go back to the worksheet view or to some list of all files in the DATA directory.

Issue created by migration from https://trac.sagemath.org/ticket/5835





---

archive/issue_comments_045770.json:
```json
{
    "body": "This has been fixed. Confirm and chekc please?",
    "created_at": "2010-01-18T04:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45770",
    "user": "https://github.com/TimDumol"
}
```

This has been fixed. Confirm and chekc please?



---

archive/issue_events_006085.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:11:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5835#event-6085"
}
```



---

archive/issue_comments_045771.json:
```json
{
    "body": "Works with sagenb-0.6",
    "created_at": "2010-01-19T03:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45771",
    "user": "https://github.com/TimDumol"
}
```

Works with sagenb-0.6



---

archive/issue_comments_045772.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45772",
    "user": "https://github.com/TimDumol"
}
```

Resolution: duplicate



---

archive/issue_comments_045773.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-01-19T03:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5835#issuecomment-45773",
    "user": "https://github.com/TimDumol"
}
```

Resolution changed from duplicate to fixed
