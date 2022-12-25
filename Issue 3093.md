# Issue 3093: [with patch; needs review] Debian lcalc package missing -DINCLUDE_PARI flag

archive/issues_003093.json:
```json
{
    "body": "Assignee: @timabbott\n\nThe Debian package for lcalc was missing the -DINCLUDE_PARI flag.  Also, it had a useless setting of CFLAGS.  This patch fixes these issues.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3093\n\n",
    "created_at": "2008-05-03T08:22:40Z",
    "labels": [
        "component: debian-package",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "[with patch; needs review] Debian lcalc package missing -DINCLUDE_PARI flag",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3093",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

The Debian package for lcalc was missing the -DINCLUDE_PARI flag.  Also, it had a useless setting of CFLAGS.  This patch fixes these issues.

Issue created by migration from https://trac.sagemath.org/ticket/3093





---

archive/issue_comments_021309.json:
```json
{
    "body": "Attachment [lcal-pari.patch](tarball://root/attachments/some-uuid/ticket3093/lcal-pari.patch) by mabshoff created at 2008-05-03 14:29:13\n\nPatch is correct, hence positive review. Slipped into lcalc-20080205.p0.spkg without bumping the release number.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T14:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3093#issuecomment-21309",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [lcal-pari.patch](tarball://root/attachments/some-uuid/ticket3093/lcal-pari.patch) by mabshoff created at 2008-05-03 14:29:13

Patch is correct, hence positive review. Slipped into lcalc-20080205.p0.spkg without bumping the release number.

Cheers,

Michael



---

archive/issue_comments_021310.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T14:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3093#issuecomment-21310",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_events_003309.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-03T14:29:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3093#event-3309"
}
```



---

archive/issue_comments_021311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T14:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3093",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3093#issuecomment-21311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
