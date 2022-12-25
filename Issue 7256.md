# Issue 7256: reset() needs to be improved

archive/issues_007256.json:
```json
{
    "body": "Assignee: wstein\n\nKeywords: reset, notebook,sage-4.1.2\n\nIn sage-4.1.2, reset() causes problems by deleting 'sagenb' from the namespace; there may be other important things deleted as well.\n\nA simple fix might be to add 'sagenb' to the sage.misc.reset.EXCLUDE list.  But perhaps a more extensive rewrite of this function would be better.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7256\n\n",
    "created_at": "2009-10-20T19:52:35Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "title": "reset() needs to be improved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: wstein

Keywords: reset, notebook,sage-4.1.2

In sage-4.1.2, reset() causes problems by deleting 'sagenb' from the namespace; there may be other important things deleted as well.

A simple fix might be to add 'sagenb' to the sage.misc.reset.EXCLUDE list.  But perhaps a more extensive rewrite of this function would be better.

Issue created by migration from https://trac.sagemath.org/ticket/7256





---

archive/issue_comments_060168.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-20T19:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7256#issuecomment-60168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Resolution: duplicate



---

archive/issue_comments_060169.json:
```json
{
    "body": "This is a duplicate of #7255, sorry about that.",
    "created_at": "2009-10-20T19:54:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7256#issuecomment-60169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

This is a duplicate of #7255, sorry about that.
