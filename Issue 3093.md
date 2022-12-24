# Issue 3093: [with patch; needs review] Debian lcalc package missing -DINCLUDE_PARI flag

archive/issues_003093.json:
```json
{
    "body": "Assignee: tabbott\n\nThe Debian package for lcalc was missing the -DINCLUDE_PARI flag.  Also, it had a useless setting of CFLAGS.  This patch fixes these issues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3093\n\n",
    "created_at": "2008-05-03T08:22:40Z",
    "labels": [
        "debian-package",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; needs review] Debian lcalc package missing -DINCLUDE_PARI flag",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3093",
    "user": "tabbott"
}
```
Assignee: tabbott

The Debian package for lcalc was missing the -DINCLUDE_PARI flag.  Also, it had a useless setting of CFLAGS.  This patch fixes these issues.

Issue created by migration from https://trac.sagemath.org/ticket/3093





---

archive/issue_comments_021353.json:
```json
{
    "body": "Attachment [lcal-pari.patch](tarball://root/attachments/some-uuid/ticket3093/lcal-pari.patch) by mabshoff created at 2008-05-03 14:29:13\n\nPatch is correct, hence positive review. Slipped into lcalc-20080205.p0.spkg without bumping the release number.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T14:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3093#issuecomment-21353",
    "user": "mabshoff"
}
```

Attachment [lcal-pari.patch](tarball://root/attachments/some-uuid/ticket3093/lcal-pari.patch) by mabshoff created at 2008-05-03 14:29:13

Patch is correct, hence positive review. Slipped into lcalc-20080205.p0.spkg without bumping the release number.

Cheers,

Michael



---

archive/issue_comments_021354.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T14:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3093#issuecomment-21354",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_comments_021355.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T14:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3093#issuecomment-21355",
    "user": "mabshoff"
}
```

Resolution: fixed
