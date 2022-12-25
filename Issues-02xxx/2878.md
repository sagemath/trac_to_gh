# Issue 2878: [with patch; positive review] notebook -- cython .c and .html links should open in new links (use target="_new"

archive/issues_002878.json:
```json
{
    "body": "Assignee: boothby\n\nDo this, because otherwise user (1) clicks html or c link, then (2) sees the html or c, then (3) presses browser back button, then (4) PANICS! since all their work is gone (actually they can get it back by pressing refresh).  This is VERY confusing, and I've had users ask about it multiple times recently. \n\nAlternatively, is there a way so that when a user navigates to a worksheet page via the back button, the page is automatically refreshed?\n\nIssue created by migration from https://trac.sagemath.org/ticket/2878\n\n",
    "closed_at": "2008-04-12T10:49:19Z",
    "created_at": "2008-04-11T16:01:48Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; positive review] notebook -- cython .c and .html links should open in new links (use target=\"_new\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2878",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

Do this, because otherwise user (1) clicks html or c link, then (2) sees the html or c, then (3) presses browser back button, then (4) PANICS! since all their work is gone (actually they can get it back by pressing refresh).  This is VERY confusing, and I've had users ask about it multiple times recently. 

Alternatively, is there a way so that when a user navigates to a worksheet page via the back button, the page is automatically refreshed?

Issue created by migration from https://trac.sagemath.org/ticket/2878





---

archive/issue_comments_019760.json:
```json
{
    "body": "Attachment [sage-2878.patch](tarball://root/attachments/some-uuid/ticket2878/sage-2878.patch) by @williamstein created at 2008-04-12 04:17:09",
    "created_at": "2008-04-12T04:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2878#issuecomment-19760",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2878.patch](tarball://root/attachments/some-uuid/ticket2878/sage-2878.patch) by @williamstein created at 2008-04-12 04:17:09



---

archive/issue_comments_019761.json:
```json
{
    "body": "\"Alternatively, is there a way so that when a user navigates to a worksheet page via the back button, the page is automatically refreshed?\"\n\nThis is a hard problem.  Let's think about making a new ticket out of that issue (because the problem is ultimately larger than these links), and take this patch for now.",
    "created_at": "2008-04-12T06:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2878#issuecomment-19761",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

"Alternatively, is there a way so that when a user navigates to a worksheet page via the back button, the page is automatically refreshed?"

This is a hard problem.  Let's think about making a new ticket out of that issue (because the problem is ultimately larger than these links), and take this patch for now.



---

archive/issue_comments_019762.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T10:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2878#issuecomment-19762",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019763.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T10:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2878#issuecomment-19763",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006598.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-12T10:49:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2878",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2878#event-6598"
}
```
