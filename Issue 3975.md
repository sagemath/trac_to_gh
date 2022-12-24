# Issue 3975: Small mistake in the new plot() code.

archive/issues_003975.json:
```json
{
    "body": "Assignee: was\n\ndelta is computed with xmin and xmax in the wrong order resulting in a negative delta.\n\nThis makes the rest of the code go very slowly.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3975\n\n",
    "created_at": "2008-08-28T14:42:56Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Small mistake in the new plot() code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3975",
    "user": "anakha"
}
```
Assignee: was

delta is computed with xmin and xmax in the wrong order resulting in a negative delta.

This makes the rest of the code go very slowly.



Issue created by migration from https://trac.sagemath.org/ticket/3975





---

archive/issue_comments_028561.json:
```json
{
    "body": "Attachment [trac_3975.patch](tarball://root/attachments/some-uuid/ticket3975/trac_3975.patch) by anakha created at 2008-08-28 14:49:41",
    "created_at": "2008-08-28T14:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3975#issuecomment-28561",
    "user": "anakha"
}
```

Attachment [trac_3975.patch](tarball://root/attachments/some-uuid/ticket3975/trac_3975.patch) by anakha created at 2008-08-28 14:49:41



---

archive/issue_comments_028562.json:
```json
{
    "body": "Attachment [trac_3975.2.patch](tarball://root/attachments/some-uuid/ticket3975/trac_3975.2.patch) by mhansen created at 2008-08-28 19:31:34\n\nI posted a rebased patch which should apply with all of the new plotting patches applied.\n\nPositive review.",
    "created_at": "2008-08-28T19:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3975#issuecomment-28562",
    "user": "mhansen"
}
```

Attachment [trac_3975.2.patch](tarball://root/attachments/some-uuid/ticket3975/trac_3975.2.patch) by mhansen created at 2008-08-28 19:31:34

I posted a rebased patch which should apply with all of the new plotting patches applied.

Positive review.



---

archive/issue_comments_028563.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T20:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3975#issuecomment-28563",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028564.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T20:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3975",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3975#issuecomment-28564",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha2
