# Issue 841: hash() on algebraic reals is not stable

archive/issues_000841.json:
```json
{
    "body": "Assignee: cwitty\n\nThe hash() function applied to a single algebraic real may give different results at different times:\n\n```\nsage: foo = sqrt(AA(4))\nsage: hash(foo)\n-1289340516\nsage: foo == 2\nTrue\nsage: hash(foo)\n2105051955\n```\n\n\n(I plan to fix this problem very soon.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/841\n\n",
    "created_at": "2007-10-09T00:42:55Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "hash() on algebraic reals is not stable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/841",
    "user": "cwitty"
}
```
Assignee: cwitty

The hash() function applied to a single algebraic real may give different results at different times:

```
sage: foo = sqrt(AA(4))
sage: hash(foo)
-1289340516
sage: foo == 2
True
sage: hash(foo)
2105051955
```


(I plan to fix this problem very soon.)


Issue created by migration from https://trac.sagemath.org/ticket/841





---

archive/issue_comments_005206.json:
```json
{
    "body": "Attachment\n\nOK, here's a patch that makes hash() on algebraic reals stable.  New results after the patch:\n\n\n```\nsage: foo = sqrt(AA(4))\nsage: hash(foo)\n-1968313278\nsage: foo == 2\nTrue\nsage: hash(foo)\n-1968313278\n```\n",
    "created_at": "2007-10-09T01:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/841#issuecomment-5206",
    "user": "cwitty"
}
```

Attachment

OK, here's a patch that makes hash() on algebraic reals stable.  New results after the patch:


```
sage: foo = sqrt(AA(4))
sage: hash(foo)
-1968313278
sage: foo == 2
True
sage: hash(foo)
-1968313278
```




---

archive/issue_comments_005207.json:
```json
{
    "body": "Changing assignee from cwitty to tbd.",
    "created_at": "2007-10-09T01:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/841#issuecomment-5207",
    "user": "cwitty"
}
```

Changing assignee from cwitty to tbd.



---

archive/issue_comments_005208.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/841#issuecomment-5208",
    "user": "was"
}
```

Resolution: fixed
