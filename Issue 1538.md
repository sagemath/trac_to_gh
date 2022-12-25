# Issue 1538: upgrades of sage_scripts can confuse bash

archive/issues_001538.json:
```json
{
    "body": "Assignee: @williamstein\n\nDoing an upgrade of sage_scripts may modify files in local/bin while bash is executing them.  This means that bash may attempt to execute some mixture of the old and new versions (which will usually lead to an error, because bash will begin executing the new version in the middle of a line).\n\nCurrently Sage includes an effective workaround for this problem... the upgrade is automatically retried if it fails.  However, we should put in a real fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1538\n\n",
    "created_at": "2007-12-16T16:01:56Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "upgrades of sage_scripts can confuse bash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1538",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Doing an upgrade of sage_scripts may modify files in local/bin while bash is executing them.  This means that bash may attempt to execute some mixture of the old and new versions (which will usually lead to an error, because bash will begin executing the new version in the middle of a line).

Currently Sage includes an effective workaround for this problem... the upgrade is automatically retried if it fails.  However, we should put in a real fix.

Issue created by migration from https://trac.sagemath.org/ticket/1538





---

archive/issue_comments_009792.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2007-12-16T16:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9792",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_009793.json:
```json
{
    "body": "Changing component from algebraic geometry to distribution.",
    "created_at": "2007-12-16T16:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9793",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing component from algebraic geometry to distribution.



---

archive/issue_comments_009794.json:
```json
{
    "body": "Attachment [1538_upgrade_root.patch](tarball://root/attachments/some-uuid/ticket1538/1538_upgrade_root.patch) by @jdemeyer created at 2012-10-05 13:09:08",
    "created_at": "2012-10-05T13:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9794",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [1538_upgrade_root.patch](tarball://root/attachments/some-uuid/ticket1538/1538_upgrade_root.patch) by @jdemeyer created at 2012-10-05 13:09:08



---

archive/issue_comments_009795.json:
```json
{
    "body": "Changing component from distribution to build.",
    "created_at": "2012-10-05T13:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9795",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from distribution to build.



---

archive/issue_comments_009796.json:
```json
{
    "body": "Attachment [1538_upgrade_scripts.patch](tarball://root/attachments/some-uuid/ticket1538/1538_upgrade_scripts.patch) by @jdemeyer created at 2013-08-13 15:34:36",
    "created_at": "2013-08-13T15:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9796",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [1538_upgrade_scripts.patch](tarball://root/attachments/some-uuid/ticket1538/1538_upgrade_scripts.patch) by @jdemeyer created at 2013-08-13 15:34:36



---

archive/issue_comments_009797.json:
```json
{
    "body": "This is solved by the git workflow because everything is now updated **before** the build, not **during** the build.",
    "created_at": "2013-12-19T12:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9797",
    "user": "https://github.com/jdemeyer"
}
```

This is solved by the git workflow because everything is now updated **before** the build, not **during** the build.



---

archive/issue_comments_009798.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-19T12:17:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9798",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_009799.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-19T12:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9799",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_009800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-12-20T15:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1538#issuecomment-9800",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
