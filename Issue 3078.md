# Issue 3078: [with patch; needs review] sage's spkg-install doesn't return failure if build failed

archive/issues_003078.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf `sage -ba-force` failed, `spkg-install` accidentally returns the return value of an `echo` command.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3078\n\n",
    "created_at": "2008-05-02T10:44:38Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "title": "[with patch; needs review] sage's spkg-install doesn't return failure if build failed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3078",
    "user": "wjp"
}
```
Assignee: mabshoff

If `sage -ba-force` failed, `spkg-install` accidentally returns the return value of an `echo` command.

Issue created by migration from https://trac.sagemath.org/ticket/3078





---

archive/issue_comments_021234.json:
```json
{
    "body": "Attachment [3078_sage_spkg-install.patch](tarball://root/attachments/some-uuid/ticket3078/3078_sage_spkg-install.patch) by gfurnish created at 2008-05-02 11:49:15",
    "created_at": "2008-05-02T11:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3078#issuecomment-21234",
    "user": "gfurnish"
}
```

Attachment [3078_sage_spkg-install.patch](tarball://root/attachments/some-uuid/ticket3078/3078_sage_spkg-install.patch) by gfurnish created at 2008-05-02 11:49:15



---

archive/issue_comments_021235.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T11:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3078#issuecomment-21235",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_comments_021236.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T11:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3078#issuecomment-21236",
    "user": "mabshoff"
}
```

Resolution: fixed
