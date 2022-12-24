# Issue 176: sagex -- add support for the "//" --> floordiv operator

archive/issues_000176.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/176\n\n",
    "created_at": "2006-12-02T23:36:36Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "sagex -- add support for the \"//\" --> floordiv operator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/176",
    "user": "was"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/176





---

archive/issue_comments_000815.json:
```json
{
    "body": "Hello,\n\nI have the impression this works unless I misunderstood the definition of the floordiv operator. From Sage 2.8.2\n\n```\nsage: 12//6\n2\nsage: 13//6\n2\nsage: 18//6\n3\n```\n\n\nCan anyone confirm this?\n\nCheers,\n\nMichael",
    "created_at": "2007-08-22T19:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/176#issuecomment-815",
    "user": "mabshoff"
}
```

Hello,

I have the impression this works unless I misunderstood the definition of the floordiv operator. From Sage 2.8.2

```
sage: 12//6
2
sage: 13//6
2
sage: 18//6
3
```


Can anyone confirm this?

Cheers,

Michael



---

archive/issue_comments_000816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-23T05:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/176#issuecomment-816",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000817.json:
```json
{
    "body": "This works in cython.",
    "created_at": "2007-08-23T05:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/176",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/176#issuecomment-817",
    "user": "was"
}
```

This works in cython.
