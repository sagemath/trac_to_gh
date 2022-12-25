# Issue 1356: [with patch] fix bug when taking abs() of exactly known QQbar

archive/issues_001356.json:
```json
{
    "body": "Assignee: somebody\n\nThe following test fails in 2.8.15.alpha1:\n\n```\n            sage: v = QQbar.zeta(3) + 1\n            sage: v.exactify()\n            sage: v.abs().minpoly()\n```\nbut the attached patch fixes it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1356\n\n",
    "created_at": "2007-12-02T01:25:31Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] fix bug when taking abs() of exactly known QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1356",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

The following test fails in 2.8.15.alpha1:

```
            sage: v = QQbar.zeta(3) + 1
            sage: v.exactify()
            sage: v.abs().minpoly()
```
but the attached patch fixes it.

Issue created by migration from https://trac.sagemath.org/ticket/1356





---

archive/issue_comments_008649.json:
```json
{
    "body": "Attachment [1356.patch](tarball://root/attachments/some-uuid/ticket1356/1356.patch) by @rlmill created at 2007-12-02 19:34:21\n\nNow:\n\n```\nsage: v = QQbar.zeta(3) + 1\nsage: v.exactify()\nsage: v.abs().minpoly()\nx - 1\n```",
    "created_at": "2007-12-02T19:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8649",
    "user": "https://github.com/rlmill"
}
```

Attachment [1356.patch](tarball://root/attachments/some-uuid/ticket1356/1356.patch) by @rlmill created at 2007-12-02 19:34:21

Now:

```
sage: v = QQbar.zeta(3) + 1
sage: v.exactify()
sage: v.abs().minpoly()
x - 1
```



---

archive/issue_comments_008650.json:
```json
{
    "body": "looks good to me.",
    "created_at": "2007-12-02T19:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8650",
    "user": "https://github.com/williamstein"
}
```

looks good to me.



---

archive/issue_comments_008651.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T20:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8651",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008652.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T20:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8652",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003503.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-02T20:12:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1356#event-3503"
}
```
