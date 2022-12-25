# Issue 307: vector/vector multiplication should return a scalar

archive/issues_000307.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently vector/vector multiplication returns a vector, when it should just return a scalar:\n\n```\nsage: b = vector([0,1,2]); u= vector([1,3,5]);\nsage: u*b\n(0, 3, 10)\n```\n\n\nIn this particular case, the answer should just be 13\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/307\n\n",
    "created_at": "2007-03-04T06:20:56Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "title": "vector/vector multiplication should return a scalar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/307",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein

Currently vector/vector multiplication returns a vector, when it should just return a scalar:

```
sage: b = vector([0,1,2]); u= vector([1,3,5]);
sage: u*b
(0, 3, 10)
```


In this particular case, the answer should just be 13
 

Issue created by migration from https://trac.sagemath.org/ticket/307





---

archive/issue_comments_001457.json:
```json
{
    "body": "No it shouldn't.  If you want the dot product, you should do this:\n\n```\nsage:  b = vector([0,1,2]); u= vector([1,3,5]);\nsage: b.dot_product(u)\n13\n```\n",
    "created_at": "2007-03-04T21:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/307#issuecomment-1457",
    "user": "https://github.com/williamstein"
}
```

No it shouldn't.  If you want the dot product, you should do this:

```
sage:  b = vector([0,1,2]); u= vector([1,3,5]);
sage: b.dot_product(u)
13
```




---

archive/issue_events_000326.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-03-04T21:22:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/307",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/307#event-326"
}
```



---

archive/issue_comments_001458.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-03-04T21:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/307#issuecomment-1458",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid
