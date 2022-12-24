# Issue 2649: [with patch, needs review] matrix() constructor fails to find ring for empty dict

archive/issues_002649.json:
```json
{
    "body": "Assignee: was\n\nTry the following:\n\n```\nsage: D = {}\nsage: matrix(D)\n```\n\nCurrently this throws an exception.  With this patch, it returns [0] when it should return [].  I don't know how to fix this, so I will open a separate ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2649\n\n",
    "created_at": "2008-03-22T19:26:58Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] matrix() constructor fails to find ring for empty dict",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2649",
    "user": "rhinton"
}
```
Assignee: was

Try the following:

```
sage: D = {}
sage: matrix(D)
```

Currently this throws an exception.  With this patch, it returns [0] when it should return [].  I don't know how to fix this, so I will open a separate ticket.

Issue created by migration from https://trac.sagemath.org/ticket/2649





---

archive/issue_comments_018210.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-23T02:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2649#issuecomment-18210",
    "user": "rhinton"
}
```

Resolution: duplicate



---

archive/issue_comments_018211.json:
```json
{
    "body": "Attachment [matrix-empty-dict.patch](tarball://root/attachments/some-uuid/ticket2649/matrix-empty-dict.patch) by rhinton created at 2008-03-23 02:17:49\n\nsubsumed by #2651",
    "created_at": "2008-03-23T02:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2649",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2649#issuecomment-18211",
    "user": "rhinton"
}
```

Attachment [matrix-empty-dict.patch](tarball://root/attachments/some-uuid/ticket2649/matrix-empty-dict.patch) by rhinton created at 2008-03-23 02:17:49

subsumed by #2651
