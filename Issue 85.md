# Issue 85: p-adic coercion incorrect for negative numbers

archive/issues_000085.json:
```json
{
    "body": "Assignee: dmharvey\n\n\n```\nsage: pAdicField(5, 3)(-1)\n 4 + 4*5 + 4*5^2 + O(5^Infinity)\n```\n\n\nI know where the bug is.... it's all my fault....\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/85\n\n",
    "created_at": "2006-09-26T19:23:17Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "p-adic coercion incorrect for negative numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/85",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: dmharvey


```
sage: pAdicField(5, 3)(-1)
 4 + 4*5 + 4*5^2 + O(5^Infinity)
```


I know where the bug is.... it's all my fault....


Issue created by migration from https://trac.sagemath.org/ticket/85





---

archive/issue_comments_000424.json:
```json
{
    "body": "I've fixed this (patch to be submitted soon), but the problem is deeper, it's not just to do with coercion, e.g.\n\n```\nsage: K = pAdicField(5, 3)\nsage: K(2) - K(3)\n 4 + 4*5 + 4*5^2 + O(5^Infinity)\n```\n",
    "created_at": "2006-09-26T19:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/85",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/85#issuecomment-424",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I've fixed this (patch to be submitted soon), but the problem is deeper, it's not just to do with coercion, e.g.

```
sage: K = pAdicField(5, 3)
sage: K(2) - K(3)
 4 + 4*5 + 4*5^2 + O(5^Infinity)
```




---

archive/issue_events_000180.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2006-10-10T23:57:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/85",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/85#event-180"
}
```



---

archive/issue_comments_000425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-10T23:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/85",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/85#issuecomment-425",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: fixed



---

archive/issue_comments_000426.json:
```json
{
    "body": "fixed in sage 1.4",
    "created_at": "2006-10-10T23:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/85",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/85#issuecomment-426",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

fixed in sage 1.4
