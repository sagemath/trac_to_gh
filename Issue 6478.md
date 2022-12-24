# Issue 6478: [with patch, needs review] Make sage -combinat work without touching .hgrc

archive/issues_006478.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: sage -combinat\n\nWith the attached patch, sage -combinat uses the --config switch of hg to request it to load the mq extension. This relieves the user from creating a .hgrc for basic usage of sage -combinat.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6478\n\n",
    "created_at": "2009-07-08T06:26:33Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Make sage -combinat work without touching .hgrc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6478",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: sage -combinat

With the attached patch, sage -combinat uses the --config switch of hg to request it to load the mq extension. This relieves the user from creating a .hgrc for basic usage of sage -combinat.

Issue created by migration from https://trac.sagemath.org/ticket/6478





---

archive/issue_comments_052363.json:
```json
{
    "body": "Attachment [trac_6478_sage-combinat-hgext-mq.patch](tarball://root/attachments/some-uuid/ticket6478/trac_6478_sage-combinat-hgext-mq.patch) by nthiery created at 2009-07-08 06:53:32",
    "created_at": "2009-07-08T06:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52363",
    "user": "nthiery"
}
```

Attachment [trac_6478_sage-combinat-hgext-mq.patch](tarball://root/attachments/some-uuid/ticket6478/trac_6478_sage-combinat-hgext-mq.patch) by nthiery created at 2009-07-08 06:53:32



---

archive/issue_comments_052364.json:
```json
{
    "body": "Looks good. Positive review.",
    "created_at": "2009-07-08T08:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52364",
    "user": "ddrake"
}
```

Looks good. Positive review.



---

archive/issue_comments_052365.json:
```json
{
    "body": "Merged in sage-4.1 final.",
    "created_at": "2009-07-08T20:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52365",
    "user": "rlm"
}
```

Merged in sage-4.1 final.



---

archive/issue_comments_052366.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-08T20:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6478#issuecomment-52366",
    "user": "rlm"
}
```

Resolution: fixed
