# Issue 1112: Integer.__pow__

archive/issues_001112.json:
```json
{
    "body": "Assignee: somebody\n\nthe attached patch makes this work:\n\n\n```\nsage: pow(10,20,17)\n4\nsage: pow?\n    pow(x, y[, z]) -> number\n\n    With two arguments, equivalent to x**y.  With three arguments,\n    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).\n```\n\n\nthis is required such that e.g. the Crypto.RSA module works with SAGE integers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1112\n\n",
    "created_at": "2007-11-06T16:22:17Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "Integer.__pow__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1112",
    "user": "malb"
}
```
Assignee: somebody

the attached patch makes this work:


```
sage: pow(10,20,17)
4
sage: pow?
    pow(x, y[, z]) -> number

    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
```


this is required such that e.g. the Crypto.RSA module works with SAGE integers.

Issue created by migration from https://trac.sagemath.org/ticket/1112





---

archive/issue_comments_006723.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-06T16:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1112#issuecomment-6723",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_006724.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1112#issuecomment-6724",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006725.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1112#issuecomment-6725",
    "user": "mabshoff"
}
```

applied to 2.8.12.rc0
