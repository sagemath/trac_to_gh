# Issue 478: completely eliminate the dependence of sage on openssl

archive/issues_000478.json:
```json
{
    "body": "Assignee: @williamstein\n\nSAGE should not depend on openssl, since openssl is gpl-incompatible.\n\nUnfortunately, gnutls's presence isn't enough for Python to build the \"md5\" module, and\nSAGE needs that module.\n\nIssue created by migration from https://trac.sagemath.org/ticket/478\n\n",
    "closed_at": "2008-01-27T17:31:17Z",
    "created_at": "2007-08-22T07:01:43Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "completely eliminate the dependence of sage on openssl",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/478",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

SAGE should not depend on openssl, since openssl is gpl-incompatible.

Unfortunately, gnutls's presence isn't enough for Python to build the "md5" module, and
SAGE needs that module.

Issue created by migration from https://trac.sagemath.org/ticket/478





---

archive/issue_comments_002372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T17:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/478#issuecomment-2372",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001210.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-01-27T17:31:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/478",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/478#event-1210"
}
```



---

archive/issue_comments_002373.json:
```json
{
    "body": "We did this in May, 2007.",
    "created_at": "2008-01-27T17:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/478#issuecomment-2373",
    "user": "https://github.com/williamstein"
}
```

We did this in May, 2007.



---

archive/issue_events_001211.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-01-27T17:31:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/478",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/478#event-1211"
}
```
