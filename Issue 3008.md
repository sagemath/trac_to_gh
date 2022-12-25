# Issue 3008: first cell in notebook is undeletable

archive/issues_003008.json:
```json
{
    "body": "Assignee: somebody\n\nThe top cell in a notebook worksheet cannot be deleted by backspace.  A workaround is ctrl-backspace from the next cell, but that is annoyingly indirect.  I have tried this on both Safari and Firefox on OS X, but not other platforms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3008\n\n",
    "created_at": "2008-04-23T18:44:30Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "first cell in notebook is undeletable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: somebody

The top cell in a notebook worksheet cannot be deleted by backspace.  A workaround is ctrl-backspace from the next cell, but that is annoyingly indirect.  I have tried this on both Safari and Firefox on OS X, but not other platforms.

Issue created by migration from https://trac.sagemath.org/ticket/3008





---

archive/issue_comments_020641.json:
```json
{
    "body": "Attachment [sage-3008.patch](tarball://root/attachments/some-uuid/ticket3008/sage-3008.patch) by @williamstein created at 2008-05-10 23:13:03\n\nThis patch:\n\n```\nFix trac #3008 -- Fix delete first cell bug. Also:\n  2. Make deleting/merging cells via control-backspace feel slightly snappier\n  3. Improve the documentation in js.py for the join_cell function.\n```",
    "created_at": "2008-05-10T23:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20641",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3008.patch](tarball://root/attachments/some-uuid/ticket3008/sage-3008.patch) by @williamstein created at 2008-05-10 23:13:03

This patch:

```
Fix trac #3008 -- Fix delete first cell bug. Also:
  2. Make deleting/merging cells via control-backspace feel slightly snappier
  3. Improve the documentation in js.py for the join_cell function.
```



---

archive/issue_comments_020642.json:
```json
{
    "body": "The attached patch works for me, looks good.  Positive review.",
    "created_at": "2008-05-11T12:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20642",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

The attached patch works for me, looks good.  Positive review.



---

archive/issue_comments_020643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T12:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20643",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020644.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T12:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3008#issuecomment-20644",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_events_006837.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-11T12:21:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3008",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3008#event-6837"
}
```
