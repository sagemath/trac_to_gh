# Issue 5189: [with patch, positive review] notebook -- now possible to delete all computation cells

archive/issues_005189.json:
```json
{
    "body": "Assignee: @jasongrout\n\nThis is a bug in counting the number of cells to make sure the number is >= 2. The counter should only count computation cells.\n\nDeleting all computation cells makes it impossible to create new ones.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5189\n\n",
    "closed_at": "2009-02-06T21:53:40Z",
    "created_at": "2009-02-05T22:42:23Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] notebook -- now possible to delete all computation cells",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5189",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: @jasongrout

This is a bug in counting the number of cells to make sure the number is >= 2. The counter should only count computation cells.

Deleting all computation cells makes it impossible to create new ones.

Issue created by migration from https://trac.sagemath.org/ticket/5189





---

archive/issue_comments_039714.json:
```json
{
    "body": "This is definitely a blocker.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T22:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39714",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is definitely a blocker.

Cheers,

Michael



---

archive/issue_comments_039715.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-05T22:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_039716.json:
```json
{
    "body": "Attachment [delete-all-cells.patch](tarball://root/attachments/some-uuid/ticket5189/delete-all-cells.patch) by @jasongrout created at 2009-02-06 08:18:30",
    "created_at": "2009-02-06T08:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39716",
    "user": "https://github.com/jasongrout"
}
```

Attachment [delete-all-cells.patch](tarball://root/attachments/some-uuid/ticket5189/delete-all-cells.patch) by @jasongrout created at 2009-02-06 08:18:30



---

archive/issue_comments_039717.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-06T08:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39717",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039718.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-02-06T08:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39718",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_039719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T21:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039720.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T21:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5189#issuecomment-39720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_events_012010.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T21:53:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5189",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5189#event-12010"
}
```
