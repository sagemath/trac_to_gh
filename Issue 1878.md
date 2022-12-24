# Issue 1878: [with patch] add new function from mpfr-2.3.0

archive/issues_001878.json:
```json
{
    "body": "Assignee: somebody\n\nThis patch completes #1716. Some new functions are added, also some functions already available\nin SAGE are replaced by their exact mpfr flavour. For example sec(x) was defined as 1/cos(x),\nit now calls directly mpfr_sec.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1878\n\n",
    "created_at": "2008-01-21T07:12:06Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch] add new function from mpfr-2.3.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1878",
    "user": "zimmerma"
}
```
Assignee: somebody

This patch completes #1716. Some new functions are added, also some functions already available
in SAGE are replaced by their exact mpfr flavour. For example sec(x) was defined as 1/cos(x),
it now calls directly mpfr_sec.

Issue created by migration from https://trac.sagemath.org/ticket/1878





---

archive/issue_comments_011888.json:
```json
{
    "body": "Attachment [8087.patch](tarball://root/attachments/some-uuid/ticket1878/8087.patch) by zimmerma created at 2008-01-21 07:12:35",
    "created_at": "2008-01-21T07:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1878#issuecomment-11888",
    "user": "zimmerma"
}
```

Attachment [8087.patch](tarball://root/attachments/some-uuid/ticket1878/8087.patch) by zimmerma created at 2008-01-21 07:12:35



---

archive/issue_comments_011889.json:
```json
{
    "body": "Excellent docs and tests.  Apply.",
    "created_at": "2008-01-21T20:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1878#issuecomment-11889",
    "user": "ncalexan"
}
```

Excellent docs and tests.  Apply.



---

archive/issue_comments_011890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T23:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1878#issuecomment-11890",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011891.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T23:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1878#issuecomment-11891",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
