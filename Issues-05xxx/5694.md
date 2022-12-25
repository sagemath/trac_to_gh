# Issue 5694: [with patch; positive review] _ for previous output is completely broken in the notebook due to the preparser

archive/issues_005694.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook we have the following confusing bug, which caused a lot of trouble during my last Sage tutorial:\n\n```\nsage: 2 + 3\n5\nsage: _\n5\nsage: f(x,y) = x+y\nsage: 2 + 10\n12\nsage: _\n(x, y)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5694\n\n",
    "closed_at": "2009-04-06T23:10:31Z",
    "created_at": "2009-04-06T18:05:33Z",
    "labels": [
        "component: notebook",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch; positive review] _ for previous output is completely broken in the notebook due to the preparser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5694",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

In the notebook we have the following confusing bug, which caused a lot of trouble during my last Sage tutorial:

```
sage: 2 + 3
5
sage: _
5
sage: f(x,y) = x+y
sage: 2 + 10
12
sage: _
(x, y)
```

Issue created by migration from https://trac.sagemath.org/ticket/5694





---

archive/issue_comments_044430.json:
```json
{
    "body": "Attachment [trac_5694.patch](tarball://root/attachments/some-uuid/ticket5694/trac_5694.patch) by @williamstein created at 2009-04-06 18:11:38",
    "created_at": "2009-04-06T18:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5694#issuecomment-44430",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5694.patch](tarball://root/attachments/some-uuid/ticket5694/trac_5694.patch) by @williamstein created at 2009-04-06 18:11:38



---

archive/issue_comments_044431.json:
```json
{
    "body": "I think this is critical enough to make it into 3.4.1. Reassigning.\n\nCheers,\n\nMihcael",
    "created_at": "2009-04-06T22:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5694#issuecomment-44431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think this is critical enough to make it into 3.4.1. Reassigning.

Cheers,

Mihcael



---

archive/issue_events_013385.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-06T22:21:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5694",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5694#event-13385"
}
```



---

archive/issue_events_013386.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-06T23:10:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5694",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5694#event-13386"
}
```



---

archive/issue_comments_044432.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T23:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5694#issuecomment-44432",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T23:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5694#issuecomment-44433",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
