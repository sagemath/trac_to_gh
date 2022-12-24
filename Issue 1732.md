# Issue 1732: block matrix construction

archive/issues_001732.json:
```json
{
    "body": "Assignee: was\n\nCC:  dfdeshom@gmail.com\n\n\n```\nIs there a way to construct block matrices in SAGE?\nNot just the \"block_sum\", \"augment\" and \"stack\" functions.\n\nAs an example, let A, B, C, D be matrices and i want to construct a\nmatrix like E=[[A,B],[C,D]]\n\nSuch a feature would be very nice.\n\n-vgermrk-\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1732\n\n",
    "created_at": "2008-01-09T08:24:23Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "block matrix construction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1732",
    "user": "robertwb"
}
```
Assignee: was

CC:  dfdeshom@gmail.com


```
Is there a way to construct block matrices in SAGE?
Not just the "block_sum", "augment" and "stack" functions.

As an example, let A, B, C, D be matrices and i want to construct a
matrix like E=[[A,B],[C,D]]

Such a feature would be very nice.

-vgermrk-

```


Issue created by migration from https://trac.sagemath.org/ticket/1732





---

archive/issue_comments_010963.json:
```json
{
    "body": "Attachment [block_sum.diff](tarball://root/attachments/some-uuid/ticket1732/block_sum.diff) by robertwb created at 2008-01-09 08:26:09",
    "created_at": "2008-01-09T08:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10963",
    "user": "robertwb"
}
```

Attachment [block_sum.diff](tarball://root/attachments/some-uuid/ticket1732/block_sum.diff) by robertwb created at 2008-01-09 08:26:09



---

archive/issue_comments_010964.json:
```json
{
    "body": "Attachment [1732-block-matrix.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix.diff) by robertwb created at 2008-01-11 03:14:39\n\nMuch expanded functionality due to discussion at http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg08958.html\n\nSee the docstrings in the patch for many examples.",
    "created_at": "2008-01-11T03:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10964",
    "user": "robertwb"
}
```

Attachment [1732-block-matrix.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix.diff) by robertwb created at 2008-01-11 03:14:39

Much expanded functionality due to discussion at http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg08958.html

See the docstrings in the patch for many examples.



---

archive/issue_comments_010965.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-01-11T03:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10965",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_010966.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-11T03:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10966",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010967.json:
```json
{
    "body": "more memory friendly for constant entries",
    "created_at": "2008-01-11T03:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10967",
    "user": "robertwb"
}
```

more memory friendly for constant entries



---

archive/issue_comments_010968.json:
```json
{
    "body": "Attachment [1732-block-matrix-mem.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix-mem.diff) by dfdeshom created at 2008-01-15 01:40:14\n\nJust wanted to point out that this patch works great for me, both for block diagonal matrices and for creating block matrices from lists.",
    "created_at": "2008-01-15T01:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10968",
    "user": "dfdeshom"
}
```

Attachment [1732-block-matrix-mem.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix-mem.diff) by dfdeshom created at 2008-01-15 01:40:14

Just wanted to point out that this patch works great for me, both for block diagonal matrices and for creating block matrices from lists.



---

archive/issue_comments_010969.json:
```json
{
    "body": "I merged all three patches into Sage 2.10.alpha3",
    "created_at": "2008-01-15T03:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10969",
    "user": "mabshoff"
}
```

I merged all three patches into Sage 2.10.alpha3



---

archive/issue_comments_010970.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T03:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10970",
    "user": "mabshoff"
}
```

Resolution: fixed
