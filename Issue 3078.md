# Issue 3078: [with patch; positive review] sage's spkg-install doesn't return failure if build failed

archive/issues_003078.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf `sage -ba-force` failed, `spkg-install` accidentally returns the return value of an `echo` command.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3078\n\n",
    "closed_at": "2008-05-02T11:55:02Z",
    "created_at": "2008-05-02T10:44:38Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; positive review] sage's spkg-install doesn't return failure if build failed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3078",
    "user": "https://github.com/wjp"
}
```
Assignee: mabshoff

If `sage -ba-force` failed, `spkg-install` accidentally returns the return value of an `echo` command.

Issue created by migration from https://trac.sagemath.org/ticket/3078





---

archive/issue_comments_021190.json:
```json
{
    "body": "Attachment [3078_sage_spkg-install.patch](tarball://root/attachments/some-uuid/ticket3078/3078_sage_spkg-install.patch) by @garyfurnish created at 2008-05-02 11:49:15",
    "created_at": "2008-05-02T11:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3078#issuecomment-21190",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [3078_sage_spkg-install.patch](tarball://root/attachments/some-uuid/ticket3078/3078_sage_spkg-install.patch) by @garyfurnish created at 2008-05-02 11:49:15



---

archive/issue_events_006954.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-02T11:55:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3078#event-6954"
}
```



---

archive/issue_comments_021191.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T11:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3078#issuecomment-21191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_comments_021192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T11:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3078#issuecomment-21192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
