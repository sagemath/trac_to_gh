# Issue 478: completely eliminate the dependence of sage on openssl

archive/issues_000478.json:
```json
{
    "body": "Assignee: was\n\nSAGE should not depend on openssl, since openssl is gpl-incompatible.\n\nUnfortunately, gnutls's presence isn't enough for Python to build the \"md5\" module, and\nSAGE needs that module.\n\nIssue created by migration from https://trac.sagemath.org/ticket/478\n\n",
    "created_at": "2007-08-22T07:01:43Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "completely eliminate the dependence of sage on openssl",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/478",
    "user": "was"
}
```
Assignee: was

SAGE should not depend on openssl, since openssl is gpl-incompatible.

Unfortunately, gnutls's presence isn't enough for Python to build the "md5" module, and
SAGE needs that module.

Issue created by migration from https://trac.sagemath.org/ticket/478





---

archive/issue_comments_002382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T17:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/478#issuecomment-2382",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002383.json:
```json
{
    "body": "We did this in May, 2007.",
    "created_at": "2008-01-27T17:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/478#issuecomment-2383",
    "user": "was"
}
```

We did this in May, 2007.
