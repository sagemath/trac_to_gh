# Issue 3936: Throw exceptions on nonsensical comparisons?

archive/issues_003936.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jakobkroeker\n\nIt is impossible to have Python's universal comparison and have mathematically sound meaning to comparison. Transitivity and/or other properties have to cave at some point.\n\nOne example:\n\n```\nsage: L=[int(0),None,1,int(2),3]\nsage: L.sort()\nsage: L\n[1, None, 0, 2, 3]\nsage: L[0]<L[2]\nFalse\n```\n\nWould it be at all feasible to throw exceptions on non-sensical comparisons, such as 1 > None ?\n`**` instead of `^` seems pretty mild compared to this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3936\n\n",
    "created_at": "2008-08-23T20:08:58Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Throw exceptions on nonsensical comparisons?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3936",
    "user": "@nbruin"
}
```
Assignee: tbd

CC:  jakobkroeker

It is impossible to have Python's universal comparison and have mathematically sound meaning to comparison. Transitivity and/or other properties have to cave at some point.

One example:

```
sage: L=[int(0),None,1,int(2),3]
sage: L.sort()
sage: L
[1, None, 0, 2, 3]
sage: L[0]<L[2]
False
```

Would it be at all feasible to throw exceptions on non-sensical comparisons, such as 1 > None ?
`**` instead of `^` seems pretty mild compared to this.

Issue created by migration from https://trac.sagemath.org/ticket/3936





---

archive/issue_comments_028206.json:
```json
{
    "body": "What about `1 == None` or `1 != None`, should those throw errors as well? (They use the same code).",
    "created_at": "2008-09-11T06:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3936#issuecomment-28206",
    "user": "@robertwb"
}
```

What about `1 == None` or `1 != None`, should those throw errors as well? (They use the same code).



---

archive/issue_comments_028207.json:
```json
{
    "body": "As Rob points out, there's really no way to do this cleanly. In particular, though, how often do you end up accidentally comparing an integer to something like `None`? It seems much better to have an occasional result that seems strange at first than to break Python conventions, and run into more serious problems because of it.\n\nI'm closing this as invalid.",
    "created_at": "2009-01-23T07:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3936#issuecomment-28207",
    "user": "@craigcitro"
}
```

As Rob points out, there's really no way to do this cleanly. In particular, though, how often do you end up accidentally comparing an integer to something like `None`? It seems much better to have an occasional result that seems strange at first than to break Python conventions, and run into more serious problems because of it.

I'm closing this as invalid.



---

archive/issue_comments_028208.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-23T07:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3936#issuecomment-28208",
    "user": "@craigcitro"
}
```

Resolution: invalid
