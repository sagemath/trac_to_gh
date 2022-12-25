# Issue 2649: [with patch, needs review] matrix() constructor fails to find ring for empty dict

archive/issues_002649.json:
```json
{
    "body": "Assignee: @williamstein\n\nTry the following:\n\n```\nsage: D = {}\nsage: matrix(D)\n```\n\nCurrently this throws an exception.  With this patch, it returns [0] when it should return [].  I don't know how to fix this, so I will open a separate ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2649\n\n",
    "created_at": "2008-03-22T19:26:58Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] matrix() constructor fails to find ring for empty dict",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2649",
    "user": "https://github.com/rhinton"
}
```
Assignee: @williamstein

Try the following:

```
sage: D = {}
sage: matrix(D)
```

Currently this throws an exception.  With this patch, it returns [0] when it should return [].  I don't know how to fix this, so I will open a separate ticket.

Issue created by migration from https://trac.sagemath.org/ticket/2649





---

archive/issue_comments_018171.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-23T02:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2649#issuecomment-18171",
    "user": "https://github.com/rhinton"
}
```

Resolution: duplicate



---

archive/issue_comments_018172.json:
```json
{
    "body": "Attachment [matrix-empty-dict.patch](tarball://root/attachments/some-uuid/ticket2649/matrix-empty-dict.patch) by @rhinton created at 2008-03-23 02:17:49\n\nsubsumed by #2651",
    "created_at": "2008-03-23T02:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2649#issuecomment-18172",
    "user": "https://github.com/rhinton"
}
```

Attachment [matrix-empty-dict.patch](tarball://root/attachments/some-uuid/ticket2649/matrix-empty-dict.patch) by @rhinton created at 2008-03-23 02:17:49

subsumed by #2651



---

archive/issue_events_002840.json:
```json
{
    "actor": "https://github.com/rhinton",
    "created_at": "2008-03-23T02:17:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2649",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2649#event-2840"
}
```
