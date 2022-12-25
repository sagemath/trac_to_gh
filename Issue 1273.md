# Issue 1273: [with patch] implement complex root isolation

archive/issues_001273.json:
```json
{
    "body": "Assignee: somebody\n\nI'm attaching a patch that implements complex root isolation for exact polynomials.  It uses a fairly inefficient strategy (find the roots using numpy or Pari, then verify them using interval arithmetic), but it does work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1273\n\n",
    "created_at": "2007-11-25T21:33:03Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] implement complex root isolation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1273",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

I'm attaching a patch that implements complex root isolation for exact polynomials.  It uses a fairly inefficient strategy (find the roots using numpy or Pari, then verify them using interval arithmetic), but it does work.

Issue created by migration from https://trac.sagemath.org/ticket/1273





---

archive/issue_comments_007948.json:
```json
{
    "body": "Attachment [7426.patch](tarball://root/attachments/some-uuid/ticket1273/7426.patch) by cwitty created at 2007-11-25 21:33:38",
    "created_at": "2007-11-25T21:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7948",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [7426.patch](tarball://root/attachments/some-uuid/ticket1273/7426.patch) by cwitty created at 2007-11-25 21:33:38



---

archive/issue_comments_007949.json:
```json
{
    "body": "I forgot to mention... this patch depends on the patch from #1270, which must be applied first.",
    "created_at": "2007-11-25T21:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7949",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I forgot to mention... this patch depends on the patch from #1270, which must be applied first.



---

archive/issue_comments_007950.json:
```json
{
    "body": "Fast!",
    "created_at": "2007-11-30T05:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7950",
    "user": "https://github.com/rlmill"
}
```

Fast!



---

archive/issue_comments_007951.json:
```json
{
    "body": "Merged in 2.8.15.alpha0.",
    "created_at": "2007-12-01T10:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7951",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha0.



---

archive/issue_comments_007952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T10:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1273#issuecomment-7952",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001417.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T10:58:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1273",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1273#event-1417"
}
```
