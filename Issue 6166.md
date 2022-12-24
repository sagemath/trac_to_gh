# Issue 6166: [with patch, needs review] strip 'nodetex' from the reference manual

archive/issues_006166.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @rbeezer @mwhansen\n\nThe patch is supposed to remove 'nodetex' (and any other directives in the same line) from  the reference manual; these are already stripped from interactive docstrings by #6122.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6166\n\n",
    "created_at": "2009-05-31T04:58:37Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] strip 'nodetex' from the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6166",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @rbeezer @mwhansen

The patch is supposed to remove 'nodetex' (and any other directives in the same line) from  the reference manual; these are already stripped from interactive docstrings by #6122.


Issue created by migration from https://trac.sagemath.org/ticket/6166





---

archive/issue_comments_049195.json:
```json
{
    "body": "Attachment [no-nodetex-ref.patch](tarball://root/attachments/some-uuid/ticket6166/no-nodetex-ref.patch) by @jhpalmieri created at 2009-05-31 04:58:59",
    "created_at": "2009-05-31T04:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49195",
    "user": "@jhpalmieri"
}
```

Attachment [no-nodetex-ref.patch](tarball://root/attachments/some-uuid/ticket6166/no-nodetex-ref.patch) by @jhpalmieri created at 2009-05-31 04:58:59



---

archive/issue_comments_049196.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-01T05:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49196",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049197.json:
```json
{
    "body": "Changing assignee from @jhpalmieri to @mwhansen.",
    "created_at": "2009-06-01T05:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49197",
    "user": "@mwhansen"
}
```

Changing assignee from @jhpalmieri to @mwhansen.



---

archive/issue_comments_049198.json:
```json
{
    "body": "Attachment [trac_6166-2.patch](tarball://root/attachments/some-uuid/ticket6166/trac_6166-2.patch) by @mwhansen created at 2009-06-01 05:10:55\n\nThe original patch looks good except it doesn't handle the case when there is an empty docstring.  I've added a patch on top which fixes this.  John, can you review my small patch?",
    "created_at": "2009-06-01T05:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49198",
    "user": "@mwhansen"
}
```

Attachment [trac_6166-2.patch](tarball://root/attachments/some-uuid/ticket6166/trac_6166-2.patch) by @mwhansen created at 2009-06-01 05:10:55

The original patch looks good except it doesn't handle the case when there is an empty docstring.  I've added a patch on top which fixes this.  John, can you review my small patch?



---

archive/issue_comments_049199.json:
```json
{
    "body": "Looks good to me.  (Although we just shouldn't allow empty docstrings in the first place :)",
    "created_at": "2009-06-01T05:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49199",
    "user": "@jhpalmieri"
}
```

Looks good to me.  (Although we just shouldn't allow empty docstrings in the first place :)



---

archive/issue_comments_049200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T05:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49200",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049201.json:
```json
{
    "body": "I think docstringlines is an empty list if there is no docstring as well.\n\nMerged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T05:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6166",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6166#issuecomment-49201",
    "user": "@mwhansen"
}
```

I think docstringlines is an empty list if there is no docstring as well.

Merged in 4.0.1.alpha0.
