# Issue 2221: Silent failure of sage-env

archive/issues_002221.json:
```json
{
    "body": "Assignee: mabshoff\n\nsource sage-env currently fails silently to change $SAGE_ROOT if it is already set to a different directory.  This patch prints a warning message if sage-env should have changed $SAGE_ROOT but did not.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/2221\n\n",
    "created_at": "2008-02-20T06:29:55Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Silent failure of sage-env",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2221",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: mabshoff

source sage-env currently fails silently to change $SAGE_ROOT if it is already set to a different directory.  This patch prints a warning message if sage-env should have changed $SAGE_ROOT but did not.  

Issue created by migration from https://trac.sagemath.org/ticket/2221





---

archive/issue_comments_014688.json:
```json
{
    "body": "Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket2221/sage-env.patch) by mabshoff created at 2008-02-20 09:48:08",
    "created_at": "2008-02-20T09:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2221#issuecomment-14688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket2221/sage-env.patch) by mabshoff created at 2008-02-20 09:48:08



---

archive/issue_comments_014689.json:
```json
{
    "body": "Patch looks good and solves a long standing annoyance. We might even go so far to not only print a warning, but to also exit since the warning might just fly by.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-20T10:22:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2221#issuecomment-14689",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good and solves a long standing annoyance. We might even go so far to not only print a warning, but to also exit since the warning might just fly by.

Cheers,

Michael



---

archive/issue_comments_014690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T10:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2221#issuecomment-14690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014691.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T10:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2221",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2221#issuecomment-14691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha2
