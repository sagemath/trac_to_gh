# Issue 4727: list method on relative number field elements is broken -- it doesn't satisfy the most basic consistency check

archive/issues_004727.json:
```json
{
    "body": "Assignee: was\n\nWhat the heck is this?\n\n```\nsage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]\nsage: j\nI\nsage: K(j.list())\nI - sqrt2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4727\n\n",
    "created_at": "2008-12-06T18:45:19Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "list method on relative number field elements is broken -- it doesn't satisfy the most basic consistency check",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4727",
    "user": "was"
}
```
Assignee: was

What the heck is this?

```
sage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]
sage: j
I
sage: K(j.list())
I - sqrt2
```


Issue created by migration from https://trac.sagemath.org/ticket/4727





---

archive/issue_comments_035689.json:
```json
{
    "body": "The patches for #1367 fix and doctest this.  It should be closed as fixed after #1367 is merged.",
    "created_at": "2009-01-24T09:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4727#issuecomment-35689",
    "user": "ncalexan"
}
```

The patches for #1367 fix and doctest this.  It should be closed as fixed after #1367 is merged.



---

archive/issue_comments_035690.json:
```json
{
    "body": "Fixed via #1367 in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T05:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4727#issuecomment-35690",
    "user": "mabshoff"
}
```

Fixed via #1367 in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_035691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T05:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4727#issuecomment-35691",
    "user": "mabshoff"
}
```

Resolution: fixed
