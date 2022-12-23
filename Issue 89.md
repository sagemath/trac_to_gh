# Issue 89: another p-adic division bug

archive/issues_000089.json:
```json
{
    "body": "Assignee: dmharvey\n\n\n```\nsage: (1 + O(5^2)) / (1 + O(5))\n 1 + O(5^2)\n```\n\n\nClearly the answer should be instead\n\n```\n 1 + O(5)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/89\n\n",
    "created_at": "2006-09-27T13:34:52Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "another p-adic division bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/89",
    "user": "dmharvey"
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

archive/issue_comments_000441.json:
```json
{
    "body": "Actually the problem is apparently with `__invert__`:\n\n```\nsage: (1 + O(5)).__invert__()\n 1 + O(5^20)\n```\n",
    "created_at": "2006-09-27T13:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/89#issuecomment-441",
    "user": "dmharvey"
}
```

Actually the problem is apparently with `__invert__`:

```
sage: (1 + O(5)).__invert__()
 1 + O(5^20)
```




---

archive/issue_comments_000442.json:
```json
{
    "body": "fixed in sage 1.4",
    "created_at": "2006-10-10T23:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/89#issuecomment-442",
    "user": "dmharvey"
}
```

fixed in sage 1.4



---

archive/issue_comments_000443.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-10T23:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/89",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/89#issuecomment-443",
    "user": "dmharvey"
}
```

Resolution: fixed
