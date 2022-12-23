# Issue 8508: max is broken on symbolic input

archive/issues_008508.json:
```json
{
    "body": "Assignee: burcin\n\ncf http://groups.google.com/group/sage-support/msg/55dafb49058a55c6\n\n```\nsage: var('y');\nsage: max(x,y)\nx\nsage: max(y,x)\ny\n```\n\nWe expect both to give `max(x,y)` of course.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8508\n\n",
    "created_at": "2010-03-12T17:19:56Z",
    "labels": [
        "calculus",
        "critical",
        "bug"
    ],
    "title": "max is broken on symbolic input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8508",
    "user": "zimmerma"
}
```
Assignee: burcin

cf http://groups.google.com/group/sage-support/msg/55dafb49058a55c6

```
sage: var('y');
sage: max(x,y)
x
sage: max(y,x)
y
```

We expect both to give `max(x,y)` of course.

Issue created by migration from https://trac.sagemath.org/ticket/8508





---

archive/issue_comments_076827.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-03-12T18:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8508#issuecomment-76827",
    "user": "burcin"
}
```

Resolution: duplicate



---

archive/issue_comments_076828.json:
```json
{
    "body": "This is a duplicate of #6949.",
    "created_at": "2010-03-12T18:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8508#issuecomment-76828",
    "user": "burcin"
}
```

This is a duplicate of #6949.
