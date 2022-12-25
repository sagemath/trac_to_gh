# Issue 2837: [witch patch, needs review] use twisted-8.0.1's blockingCallFromThread

archive/issues_002837.json:
```json
{
    "body": "Assignee: @yqiang\n\nThis patch makes use of the official blockingCallFromThread method in twisted.internet.threads instead of the one supplied by dsage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2837\n\n",
    "created_at": "2008-04-07T00:14:16Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[witch patch, needs review] use twisted-8.0.1's blockingCallFromThread",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2837",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

This patch makes use of the official blockingCallFromThread method in twisted.internet.threads instead of the one supplied by dsage.

Issue created by migration from https://trac.sagemath.org/ticket/2837





---

archive/issue_comments_019423.json:
```json
{
    "body": "Attachment [blockingcall_api_change.patch](tarball://root/attachments/some-uuid/ticket2837/blockingcall_api_change.patch) by @mwhansen created at 2008-04-07 01:05:03\n\nApplies and passes tests on 3.0.alpha1 + new twisted spkg.",
    "created_at": "2008-04-07T01:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2837#issuecomment-19423",
    "user": "https://github.com/mwhansen"
}
```

Attachment [blockingcall_api_change.patch](tarball://root/attachments/some-uuid/ticket2837/blockingcall_api_change.patch) by @mwhansen created at 2008-04-07 01:05:03

Applies and passes tests on 3.0.alpha1 + new twisted spkg.



---

archive/issue_comments_019424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2837#issuecomment-19424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003027.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T01:23:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2837#event-3027"
}
```



---

archive/issue_comments_019425.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2837#issuecomment-19425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2
