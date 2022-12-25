# Issue 4429: notebook -- wrong display of message " Please enable cookies and try again."

archive/issues_004429.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @mwhansen\n\nIt was reported in sage-support, and I just experienced it myself, that sometimes the sage notebook will give an error on login:\n\n```\nPlease enable cookies and try again.\n```\n\neven though cookies are enabled.   When this just happened to me, I tried\nseveral times to login and it would not work -- always giving that error.\nThen I tried deleting all cookies in the cookie cache, and login worked fine.\nThus somehow we're getting the above error when there is a stale cookie.\nThis is somewhat difficult to replicate, but there is definitely a major\nbug here.  Possibly reading the code in the notebook that produces\nthat message, would produce by pure thought what the problem is.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4429\n\n",
    "created_at": "2008-11-03T01:17:40Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook -- wrong display of message \" Please enable cookies and try again.\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4429",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @mwhansen

It was reported in sage-support, and I just experienced it myself, that sometimes the sage notebook will give an error on login:

```
Please enable cookies and try again.
```

even though cookies are enabled.   When this just happened to me, I tried
several times to login and it would not work -- always giving that error.
Then I tried deleting all cookies in the cookie cache, and login worked fine.
Thus somehow we're getting the above error when there is a stale cookie.
This is somewhat difficult to replicate, but there is definitely a major
bug here.  Possibly reading the code in the notebook that produces
that message, would produce by pure thought what the problem is.

Issue created by migration from https://trac.sagemath.org/ticket/4429





---

archive/issue_comments_032486.json:
```json
{
    "body": "The message now reads: \"Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again,\" which I think is clear enough. This should probably be closed.",
    "created_at": "2009-12-06T13:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4429#issuecomment-32486",
    "user": "https://github.com/TimDumol"
}
```

The message now reads: "Please enable cookies or delete all Sage cookies and localhost cookies in your browser and try again," which I think is clear enough. This should probably be closed.



---

archive/issue_comments_032487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T16:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4429#issuecomment-32487",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_032488.json:
```json
{
    "body": "OK.  I would really like to fix the problem though, since this should never happen when cookies are enabled.  It happens a lot for me when I try safari on os x.",
    "created_at": "2009-12-09T16:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4429",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4429#issuecomment-32488",
    "user": "https://github.com/williamstein"
}
```

OK.  I would really like to fix the problem though, since this should never happen when cookies are enabled.  It happens a lot for me when I try safari on os x.



---

archive/issue_events_004673.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-09T16:26:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4429",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4429#event-4673"
}
```
