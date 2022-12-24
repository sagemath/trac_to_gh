# Issue 323: make and upgrade fails on Ubuntu Edgy (6.10)

archive/issues_000323.json:
```json
{
    "body": "Assignee: @williamstein\n\nUbuntu Edgy uses dash to provide /bin/sh. However the/some SAGE build scripts seem to assume that /bin/sh is provided by bash which is not necessarily true. Consequently, make and upgrade fail on Ubuntu Edgy (6.10). This bug was reported to me by Ralf Weinmann and I cannot personally confirm this as I don't have access to a Ubuntu Edgy install.\n\nIssue created by migration from https://trac.sagemath.org/ticket/323\n\n",
    "created_at": "2007-03-16T10:01:22Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "make and upgrade fails on Ubuntu Edgy (6.10)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/323",
    "user": "@malb"
}
```
Assignee: @williamstein

Ubuntu Edgy uses dash to provide /bin/sh. However the/some SAGE build scripts seem to assume that /bin/sh is provided by bash which is not necessarily true. Consequently, make and upgrade fail on Ubuntu Edgy (6.10). This bug was reported to me by Ralf Weinmann and I cannot personally confirm this as I don't have access to a Ubuntu Edgy install.

Issue created by migration from https://trac.sagemath.org/ticket/323





---

archive/issue_comments_001534.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-21T22:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/323#issuecomment-1534",
    "user": "@williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_001535.json:
```json
{
    "body": "This bug is too imprecise to be of any use, especially since I build SAGE regularly on Edgy eft and it works fine.   (In fact it's my main devel environment.)",
    "created_at": "2007-03-21T22:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/323#issuecomment-1535",
    "user": "@williamstein"
}
```

This bug is too imprecise to be of any use, especially since I build SAGE regularly on Edgy eft and it works fine.   (In fact it's my main devel environment.)
