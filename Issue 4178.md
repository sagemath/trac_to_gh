# Issue 4178: dist_functions.py doctest timeout is too small

archive/issues_004178.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOn my PPC Power Book 550 MHz, 768 MB RAM, Mac OS X 10.4.11, Xcode 2.5, the \"long\" doctest fails because the timeout is too small.\n\nAs soon as I have checked how big it should be (on that box) to make it run through, I'll add the info here. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4178\n\n",
    "created_at": "2008-09-23T21:58:17Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "dist_functions.py doctest timeout is too small",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4178",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: GeorgSWeber

On my PPC Power Book 550 MHz, 768 MB RAM, Mac OS X 10.4.11, Xcode 2.5, the "long" doctest fails because the timeout is too small.

As soon as I have checked how big it should be (on that box) to make it run through, I'll add the info here. 

Issue created by migration from https://trac.sagemath.org/ticket/4178





---

archive/issue_comments_030257.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-23T21:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4178#issuecomment-30257",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030258.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-23T22:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4178#issuecomment-30258",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_events_004415.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-23T22:04:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4178#event-4415"
}
```



---

archive/issue_comments_030259.json:
```json
{
    "body": "Nope, this is a won't fix. The long timeout is *huge*, i.e. 30 minutes. The problem is another one, i.e. ecm not returning and hence the doctest never finishes. This issue is already covered by another DSage ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T22:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4178#issuecomment-30259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nope, this is a won't fix. The long timeout is *huge*, i.e. 30 minutes. The problem is another one, i.e. ecm not returning and hence the doctest never finishes. This issue is already covered by another DSage ticket.

Cheers,

Michael
