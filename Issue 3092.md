# Issue 3092: [with patch; needs review] Debian Singular permissions fixes

archive/issues_003092.json:
```json
{
    "body": "Assignee: tabbott\n\nI've attached a patch that fixes the permissions issues with libsingular.so (and the oddly executable stuff in /usr/lib/singular).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3092\n\n",
    "created_at": "2008-05-03T08:21:36Z",
    "labels": [
        "debian-package",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; needs review] Debian Singular permissions fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3092",
    "user": "tabbott"
}
```
Assignee: tabbott

I've attached a patch that fixes the permissions issues with libsingular.so (and the oddly executable stuff in /usr/lib/singular).

Issue created by migration from https://trac.sagemath.org/ticket/3092





---

archive/issue_comments_021343.json:
```json
{
    "body": "Attachment [singular-permissions.patch](tarball://root/attachments/some-uuid/ticket3092/singular-permissions.patch) by tabbott created at 2008-05-03 08:21:42",
    "created_at": "2008-05-03T08:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21343",
    "user": "tabbott"
}
```

Attachment [singular-permissions.patch](tarball://root/attachments/some-uuid/ticket3092/singular-permissions.patch) by tabbott created at 2008-05-03 08:21:42



---

archive/issue_comments_021344.json:
```json
{
    "body": "Patch looks good to me. Positive review. Slipped into singular-3-0-4-2-20080405.p1.spkg without increasing the release version.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T14:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21344",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review. Slipped into singular-3-0-4-2-20080405.p1.spkg without increasing the release version.

Cheers,

Michael



---

archive/issue_comments_021345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T14:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21345",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021346.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T14:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21346",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_comments_021347.json:
```json
{
    "body": "That patch didn't actually work.  I've attached a patch on top of that one that fixes the real problem: dh_fixperms removing the executable bit.",
    "created_at": "2008-05-03T18:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21347",
    "user": "tabbott"
}
```

That patch didn't actually work.  I've attached a patch on top of that one that fixes the real problem: dh_fixperms removing the executable bit.



---

archive/issue_comments_021348.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-03T18:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21348",
    "user": "tabbott"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_021349.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-03T18:40:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21349",
    "user": "tabbott"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_021350.json:
```json
{
    "body": "Attachment [singular-permissions.2.patch](tarball://root/attachments/some-uuid/ticket3092/singular-permissions.2.patch) by tabbott created at 2008-05-03 18:41:29",
    "created_at": "2008-05-03T18:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21350",
    "user": "tabbott"
}
```

Attachment [singular-permissions.2.patch](tarball://root/attachments/some-uuid/ticket3092/singular-permissions.2.patch) by tabbott created at 2008-05-03 18:41:29



---

archive/issue_comments_021351.json:
```json
{
    "body": "Ops, merged singular-permissions.2.patch in Sage 3.0.1.final.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T19:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21351",
    "user": "mabshoff"
}
```

Ops, merged singular-permissions.2.patch in Sage 3.0.1.final.

Cheers,

Michael



---

archive/issue_comments_021352.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T19:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3092",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3092#issuecomment-21352",
    "user": "mabshoff"
}
```

Resolution: fixed
