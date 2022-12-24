# Issue 3650: [with patch, needs review] Infinite recursion in pbuild by recursive pxd imports

archive/issues_003650.json:
```json
{
    "body": "Assignee: gfurnish\n\nIn some cases, having pxds with recursive imports may cause pbuild to use recursion to go to infinity.  This patch fixes this issue.  In many cases this will just cause Cython to throw an error later, but pbuild should still behave better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3650\n\n",
    "created_at": "2008-07-13T11:22:50Z",
    "labels": [
        "pbuild",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Infinite recursion in pbuild by recursive pxd imports",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3650",
    "user": "gfurnish"
}
```
Assignee: gfurnish

In some cases, having pxds with recursive imports may cause pbuild to use recursion to go to infinity.  This patch fixes this issue.  In many cases this will just cause Cython to throw an error later, but pbuild should still behave better.

Issue created by migration from https://trac.sagemath.org/ticket/3650





---

archive/issue_comments_025816.json:
```json
{
    "body": "Attachment [trac_3650.patch](tarball://root/attachments/some-uuid/ticket3650/trac_3650.patch) by gfurnish created at 2008-07-13 11:33:05",
    "created_at": "2008-07-13T11:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25816",
    "user": "gfurnish"
}
```

Attachment [trac_3650.patch](tarball://root/attachments/some-uuid/ticket3650/trac_3650.patch) by gfurnish created at 2008-07-13 11:33:05



---

archive/issue_comments_025817.json:
```json
{
    "body": "Positive review. What could go wrong? ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-07-15T23:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25817",
    "user": "mabshoff"
}
```

Positive review. What could go wrong? ;)

Cheers,

Michael



---

archive/issue_comments_025818.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-15T23:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25818",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025819.json:
```json
{
    "body": "Merged in Sage 3.0.6.alpha0",
    "created_at": "2008-07-15T23:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3650#issuecomment-25819",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.alpha0
