# Issue 8265: LaTeX-friendly Unicode characters in underscored methods' docstrings

archive/issues_008265.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri\n\nIt seems the only problem is in\n\n   `sagenb.notebook.worksheet.Worksheet.__init__`\n\nSee #7549.  This is a follow-up to #8167.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8265\n\n",
    "created_at": "2010-02-14T18:54:03Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "LaTeX-friendly Unicode characters in underscored methods' docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8265",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @jhpalmieri

It seems the only problem is in

   `sagenb.notebook.worksheet.Worksheet.__init__`

See #7549.  This is a follow-up to #8167.

Issue created by migration from https://trac.sagemath.org/ticket/8265





---

archive/issue_comments_073039.json:
```json
{
    "body": "Applies #8167's treatment to `Worksheet.__init__`.  sagenb repo.",
    "created_at": "2010-02-14T18:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73039",
    "user": "https://github.com/qed777"
}
```

Applies #8167's treatment to `Worksheet.__init__`.  sagenb repo.



---

archive/issue_comments_073040.json:
```json
{
    "body": "Attachment [trac_8265-unicode_underscore.patch](tarball://root/attachments/some-uuid/ticket8265/trac_8265-unicode_underscore.patch) by @qed777 created at 2010-02-14 19:05:38",
    "created_at": "2010-02-14T19:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73040",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8265-unicode_underscore.patch](tarball://root/attachments/some-uuid/ticket8265/trac_8265-unicode_underscore.patch) by @qed777 created at 2010-02-14 19:05:38



---

archive/issue_comments_073041.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T19:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73041",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073042.json:
```json
{
    "body": "As far as I understand it, this patch is supposed to make the documentation build in pdf format with underscore methods included.  It does this successfully.",
    "created_at": "2010-02-17T20:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73042",
    "user": "https://github.com/jhpalmieri"
}
```

As far as I understand it, this patch is supposed to make the documentation build in pdf format with underscore methods included.  It does this successfully.



---

archive/issue_comments_073043.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2010-02-17T20:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73043",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_073044.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T20:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73044",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073045.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-04T22:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8265#issuecomment-73045",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019783.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-03-04T22:51:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8265",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8265#event-19783"
}
```
