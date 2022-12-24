# Issue 3088: [with patch; needs review] Fixes for Debian gfan build

archive/issues_003088.json:
```json
{
    "body": "Assignee: tabbott\n\nAttached is a patch that makes gfan build correctly for the Debian package.  I'm not sure why it stopped working in the first place, but this version is more Debian policy compliant than the old one anyway.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3088\n\n",
    "created_at": "2008-05-03T05:02:38Z",
    "labels": [
        "debian-package",
        "blocker",
        "bug"
    ],
    "title": "[with patch; needs review] Fixes for Debian gfan build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3088",
    "user": "tabbott"
}
```
Assignee: tabbott

Attached is a patch that makes gfan build correctly for the Debian package.  I'm not sure why it stopped working in the first place, but this version is more Debian policy compliant than the old one anyway.

Issue created by migration from https://trac.sagemath.org/ticket/3088





---

archive/issue_comments_021322.json:
```json
{
    "body": "Attachment [gfan-debian-fix.patch](tarball://root/attachments/some-uuid/ticket3088/gfan-debian-fix.patch) by mabshoff created at 2008-05-03 14:16:23\n\nPatch looks good to me. The solution is correct as discussed on sage-devel. Positive review. Slipped into gfan-0.3.p3.spkg without bumping the release number.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T14:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3088#issuecomment-21322",
    "user": "mabshoff"
}
```

Attachment [gfan-debian-fix.patch](tarball://root/attachments/some-uuid/ticket3088/gfan-debian-fix.patch) by mabshoff created at 2008-05-03 14:16:23

Patch looks good to me. The solution is correct as discussed on sage-devel. Positive review. Slipped into gfan-0.3.p3.spkg without bumping the release number.

Cheers,

Michael



---

archive/issue_comments_021323.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T14:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3088#issuecomment-21323",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_comments_021324.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T14:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3088",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3088#issuecomment-21324",
    "user": "mabshoff"
}
```

Resolution: fixed
