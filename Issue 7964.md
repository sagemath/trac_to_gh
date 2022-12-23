# Issue 7964: axis labels in weird scientific notation

archive/issues_007964.json:
```json
{
    "body": "Assignee: was\n\nThe vertical axis labels look weird here.  What is \"1e\"?\n\n\n```\nsage: plot(abs(exp(i*x)), (x,1,2))\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7964\n\n",
    "created_at": "2010-01-17T10:31:15Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "axis labels in weird scientific notation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7964",
    "user": "jason"
}
```
Assignee: was

The vertical axis labels look weird here.  What is "1e"?


```
sage: plot(abs(exp(i*x)), (x,1,2))
```



Issue created by migration from https://trac.sagemath.org/ticket/7964





---

archive/issue_comments_069490.json:
```json
{
    "body": "Confirmed with sage-6.2.beta3.",
    "created_at": "2014-03-04T15:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7964#issuecomment-69490",
    "user": "mmezzarobba"
}
```

Confirmed with sage-6.2.beta3.



---

archive/issue_comments_069491.json:
```json
{
    "body": "[Sage 9.6](https://sagecell.sagemath.org/?z=eJwryMkv0UhMKtZIrSjQyNSq0NTUUdCo0DHUMdLUBACHAwgR&lang=sage&interacts=eJyLjgUAARUAuQ==) does not seem to have this problem, but still has a different related error with\n\n```\nplot(x^2,(x,0,5000))\n```\n\nSee [this sage-devel discussion](https://groups.google.com/g/sage-devel/c/s39WysaG0fI).",
    "created_at": "2022-07-27T13:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7964",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7964#issuecomment-69491",
    "user": "kcrisman"
}
```

[Sage 9.6](https://sagecell.sagemath.org/?z=eJwryMkv0UhMKtZIrSjQyNSq0NTUUdCo0DHUMdLUBACHAwgR&lang=sage&interacts=eJyLjgUAARUAuQ==) does not seem to have this problem, but still has a different related error with

```
plot(x^2,(x,0,5000))
```

See [this sage-devel discussion](https://groups.google.com/g/sage-devel/c/s39WysaG0fI).
