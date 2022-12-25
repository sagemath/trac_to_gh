# Issue 52: O(5) prints as "0"

archive/issues_000052.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: O(5)\n 0\n```\n\n\nPerhaps it would be better if it printed as `0 + O(5)`. Especially because otherwise there's no way to tell the difference between O(5) and O(25).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/52\n\n",
    "created_at": "2006-09-13T19:04:57Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "O(5) prints as \"0\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/52",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody


```
sage: O(5)
 0
```


Perhaps it would be better if it printed as `0 + O(5)`. Especially because otherwise there's no way to tell the difference between O(5) and O(25).


Issue created by migration from https://trac.sagemath.org/ticket/52





---

archive/issue_comments_000287.json:
```json
{
    "body": "Fixed.\n\n```\nsage: O(5)\nO(5^1)\n```\n",
    "created_at": "2007-01-13T02:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/52",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/52#issuecomment-287",
    "user": "https://github.com/williamstein"
}
```

Fixed.

```
sage: O(5)
O(5^1)
```




---

archive/issue_comments_000288.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T02:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/52",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/52#issuecomment-288",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
