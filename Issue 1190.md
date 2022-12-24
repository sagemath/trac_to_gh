# Issue 1190: [with patch] fix spkg-check invocation when SAGE_CHECK is non-empty

archive/issues_001190.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe call spkg-check when the env variable SAGE_CHECK is non-empty. This didn't work, but the attached patch fixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1190\n\n",
    "created_at": "2007-11-17T06:46:57Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "[with patch] fix spkg-check invocation when SAGE_CHECK is non-empty",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1190",
    "user": "mabshoff"
}
```
Assignee: mabshoff

We call spkg-check when the env variable SAGE_CHECK is non-empty. This didn't work, but the attached patch fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1190





---

archive/issue_comments_007385.json:
```json
{
    "body": "Attachment [Sage-2.8.12-fix-spkg-check-invocation.patch](tarball://root/attachments/some-uuid/ticket1190/Sage-2.8.12-fix-spkg-check-invocation.patch) by mabshoff created at 2007-11-17 06:47:27",
    "created_at": "2007-11-17T06:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1190#issuecomment-7385",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.12-fix-spkg-check-invocation.patch](tarball://root/attachments/some-uuid/ticket1190/Sage-2.8.12-fix-spkg-check-invocation.patch) by mabshoff created at 2007-11-17 06:47:27



---

archive/issue_comments_007386.json:
```json
{
    "body": "updated rev 2 - incorporates suggestions by malb",
    "created_at": "2007-11-21T07:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1190#issuecomment-7386",
    "user": "mabshoff"
}
```

updated rev 2 - incorporates suggestions by malb



---

archive/issue_comments_007387.json:
```json
{
    "body": "Attachment [Sage-2.8.12-fix-spkg-check-invocation.2.patch](tarball://root/attachments/some-uuid/ticket1190/Sage-2.8.12-fix-spkg-check-invocation.2.patch) by mabshoff created at 2007-11-21 07:27:45\n\nPlease apply only Sage-2.8.12-fix-spkg-check-invocation.2.patch \n\nCheers,\n\nMichael",
    "created_at": "2007-11-21T07:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1190#issuecomment-7387",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.12-fix-spkg-check-invocation.2.patch](tarball://root/attachments/some-uuid/ticket1190/Sage-2.8.12-fix-spkg-check-invocation.2.patch) by mabshoff created at 2007-11-21 07:27:45

Please apply only Sage-2.8.12-fix-spkg-check-invocation.2.patch 

Cheers,

Michael



---

archive/issue_comments_007388.json:
```json
{
    "body": "The code changes look good to me (although I didn't actually test it).",
    "created_at": "2007-11-21T07:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1190#issuecomment-7388",
    "user": "cwitty"
}
```

The code changes look good to me (although I didn't actually test it).



---

archive/issue_comments_007389.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-21T07:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1190#issuecomment-7389",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007390.json:
```json
{
    "body": "Merged in 2.8.13.rc2.",
    "created_at": "2007-11-21T07:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1190",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1190#issuecomment-7390",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc2.
