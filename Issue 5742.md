# Issue 5742: ATLAS.spkg: parallel make breaks on system with "real" sh

archive/issues_005742.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe spkg-install-$FOO script that actually builds atlas uses `/bin/sh` as shebang and does not export MAKE properly. So if one builds Sage on Solaris or FreeBSD with parallel make where sh is the real shell things blow up since ATLAS does not handle parallel make too well :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5742\n\n",
    "created_at": "2009-04-11T01:23:52Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "ATLAS.spkg: parallel make breaks on system with \"real\" sh",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5742",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The spkg-install-$FOO script that actually builds atlas uses `/bin/sh` as shebang and does not export MAKE properly. So if one builds Sage on Solaris or FreeBSD with parallel make where sh is the real shell things blow up since ATLAS does not handle parallel make too well :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5742





---

archive/issue_comments_044814.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-18T06:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5742#issuecomment-44814",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044815.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T23:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5742#issuecomment-44815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044816.json:
```json
{
    "body": "Fixed in Sage 3.4.1.rc4 via #5219.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T23:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5742#issuecomment-44816",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.4.1.rc4 via #5219.

Cheers,

Michael
