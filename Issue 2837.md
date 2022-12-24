# Issue 2837: [witch patch, needs review] use twisted-8.0.1's blockingCallFromThread

archive/issues_002837.json:
```json
{
    "body": "Assignee: yi\n\nThis patch makes use of the official blockingCallFromThread method in twisted.internet.threads instead of the one supplied by dsage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2837\n\n",
    "created_at": "2008-04-07T00:14:16Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[witch patch, needs review] use twisted-8.0.1's blockingCallFromThread",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2837",
    "user": "yi"
}
```
Assignee: yi

This patch makes use of the official blockingCallFromThread method in twisted.internet.threads instead of the one supplied by dsage.

Issue created by migration from https://trac.sagemath.org/ticket/2837





---

archive/issue_comments_019464.json:
```json
{
    "body": "Attachment [blockingcall_api_change.patch](tarball://root/attachments/some-uuid/ticket2837/blockingcall_api_change.patch) by mhansen created at 2008-04-07 01:05:03\n\nApplies and passes tests on 3.0.alpha1 + new twisted spkg.",
    "created_at": "2008-04-07T01:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2837#issuecomment-19464",
    "user": "mhansen"
}
```

Attachment [blockingcall_api_change.patch](tarball://root/attachments/some-uuid/ticket2837/blockingcall_api_change.patch) by mhansen created at 2008-04-07 01:05:03

Applies and passes tests on 3.0.alpha1 + new twisted spkg.



---

archive/issue_comments_019465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T01:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2837#issuecomment-19465",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019466.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T01:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2837#issuecomment-19466",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2
