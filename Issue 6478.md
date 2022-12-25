# Issue 6478: [with patch, positive review] Make sage -combinat work without touching .hgrc

archive/issues_006478.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: sage -combinat\n\nWith the attached patch, sage -combinat uses the --config switch of hg to request it to load the mq extension. This relieves the user from creating a .hgrc for basic usage of sage -combinat.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6478\n\n",
    "closed_at": "2009-07-08T20:22:50Z",
    "created_at": "2009-07-08T06:26:33Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, positive review] Make sage -combinat work without touching .hgrc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6478",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: sage -combinat

With the attached patch, sage -combinat uses the --config switch of hg to request it to load the mq extension. This relieves the user from creating a .hgrc for basic usage of sage -combinat.

Issue created by migration from https://trac.sagemath.org/ticket/6478





---

archive/issue_comments_052265.json:
```json
{
    "body": "Attachment [trac_6478_sage-combinat-hgext-mq.patch](tarball://root/attachments/some-uuid/ticket6478/trac_6478_sage-combinat-hgext-mq.patch) by @nthiery created at 2009-07-08 06:53:32",
    "created_at": "2009-07-08T06:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52265",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6478_sage-combinat-hgext-mq.patch](tarball://root/attachments/some-uuid/ticket6478/trac_6478_sage-combinat-hgext-mq.patch) by @nthiery created at 2009-07-08 06:53:32



---

archive/issue_comments_052266.json:
```json
{
    "body": "Looks good. Positive review.",
    "created_at": "2009-07-08T08:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52266",
    "user": "https://github.com/dandrake"
}
```

Looks good. Positive review.



---

archive/issue_events_015296.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-08T20:22:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6478#event-15296"
}
```



---

archive/issue_comments_052267.json:
```json
{
    "body": "Merged in sage-4.1 final.",
    "created_at": "2009-07-08T20:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52267",
    "user": "https://github.com/rlmill"
}
```

Merged in sage-4.1 final.



---

archive/issue_comments_052268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-08T20:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52268",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
