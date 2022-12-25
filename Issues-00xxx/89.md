# Issue 89: another p-adic division bug

archive/issues_000089.json:
```json
{
    "body": "Assignee: dmharvey\n\n```\nsage: (1 + O(5^2)) / (1 + O(5))\n 1 + O(5^2)\n```\n\nClearly the answer should be instead\n\n```\n 1 + O(5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/89\n\n",
    "closed_at": "2006-10-10T23:58:17Z",
    "created_at": "2006-09-27T13:34:52Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "title": "another p-adic division bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/89",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: dmharvey

```
sage: (1 + O(5^2)) / (1 + O(5))
 1 + O(5^2)
```

Clearly the answer should be instead

```
 1 + O(5)
```


Issue created by migration from https://trac.sagemath.org/ticket/89





---

archive/issue_comments_000439.json:
```json
{
    "body": "Actually the problem is apparently with `__invert__`:\n\n```\nsage: (1 + O(5)).__invert__()\n 1 + O(5^20)\n```",
    "created_at": "2006-09-27T13:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/89#issuecomment-439",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Actually the problem is apparently with `__invert__`:

```
sage: (1 + O(5)).__invert__()
 1 + O(5^20)
```



---

archive/issue_comments_000440.json:
```json
{
    "body": "fixed in sage 1.4",
    "created_at": "2006-10-10T23:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/89#issuecomment-440",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

fixed in sage 1.4



---

archive/issue_events_000184.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2006-10-10T23:58:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/89#event-184"
}
```



---

archive/issue_comments_000441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-10T23:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/89#issuecomment-441",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: fixed
