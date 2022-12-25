# Issue 1732: block matrix construction

archive/issues_001732.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  dfdeshom@gmail.com\n\n\n```\nIs there a way to construct block matrices in SAGE?\nNot just the \"block_sum\", \"augment\" and \"stack\" functions.\n\nAs an example, let A, B, C, D be matrices and i want to construct a\nmatrix like E=[[A,B],[C,D]]\n\nSuch a feature would be very nice.\n\n-vgermrk-\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1732\n\n",
    "created_at": "2008-01-09T08:24:23Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "block matrix construction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1732",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

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

archive/issue_comments_010936.json:
```json
{
    "body": "Attachment [block_sum.diff](tarball://root/attachments/some-uuid/ticket1732/block_sum.diff) by @robertwb created at 2008-01-09 08:26:09",
    "created_at": "2008-01-09T08:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10936",
    "user": "https://github.com/robertwb"
}
```

Attachment [block_sum.diff](tarball://root/attachments/some-uuid/ticket1732/block_sum.diff) by @robertwb created at 2008-01-09 08:26:09



---

archive/issue_comments_010937.json:
```json
{
    "body": "Attachment [1732-block-matrix.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix.diff) by @robertwb created at 2008-01-11 03:14:39\n\nMuch expanded functionality due to discussion at http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg08958.html\n\nSee the docstrings in the patch for many examples.",
    "created_at": "2008-01-11T03:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10937",
    "user": "https://github.com/robertwb"
}
```

Attachment [1732-block-matrix.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix.diff) by @robertwb created at 2008-01-11 03:14:39

Much expanded functionality due to discussion at http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg08958.html

See the docstrings in the patch for many examples.



---

archive/issue_comments_010938.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2008-01-11T03:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10938",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_010939.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-11T03:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10939",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010940.json:
```json
{
    "body": "more memory friendly for constant entries",
    "created_at": "2008-01-11T03:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10940",
    "user": "https://github.com/robertwb"
}
```

more memory friendly for constant entries



---

archive/issue_comments_010941.json:
```json
{
    "body": "Attachment [1732-block-matrix-mem.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix-mem.diff) by @dfdeshom created at 2008-01-15 01:40:14\n\nJust wanted to point out that this patch works great for me, both for block diagonal matrices and for creating block matrices from lists.",
    "created_at": "2008-01-15T01:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10941",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [1732-block-matrix-mem.diff](tarball://root/attachments/some-uuid/ticket1732/1732-block-matrix-mem.diff) by @dfdeshom created at 2008-01-15 01:40:14

Just wanted to point out that this patch works great for me, both for block diagonal matrices and for creating block matrices from lists.



---

archive/issue_comments_010942.json:
```json
{
    "body": "I merged all three patches into Sage 2.10.alpha3",
    "created_at": "2008-01-15T03:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10942",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I merged all three patches into Sage 2.10.alpha3



---

archive/issue_comments_010943.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T03:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1732#issuecomment-10943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001890.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-15T03:10:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1732",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1732#event-1890"
}
```
