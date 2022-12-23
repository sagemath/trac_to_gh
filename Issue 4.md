# Issue 4: should exist a conversion from Integers(p**N) to pAdicField(p)

archive/issues_000004.json:
```json
{
    "body": "Assignee: somebody\n\nCurrently this:\n\npAdicField(5)(Integers(125)(13))\n\nproduces this:\n\nTraceback (most recent call last):\n...\nTypeError: unable to compute ordp\n\nI think SAGE should be able to perform such a conversion.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4\n\n",
    "created_at": "2006-09-12T00:41:16Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "should exist a conversion from Integers(p**N) to pAdicField(p)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4",
    "user": "dmharvey"
}
```
Assignee: somebody

Currently this:

pAdicField(5)(Integers(125)(13))

produces this:

Traceback (most recent call last):
...
TypeError: unable to compute ordp

I think SAGE should be able to perform such a conversion.


Issue created by migration from https://trac.sagemath.org/ticket/4





---

archive/issue_comments_000013.json:
```json
{
    "body": "Changing assignee from somebody to dmharvey.",
    "created_at": "2006-09-26T22:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4#issuecomment-13",
    "user": "dmharvey"
}
```

Changing assignee from somebody to dmharvey.



---

archive/issue_comments_000014.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-04-13T03:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4#issuecomment-14",
    "user": "roed"
}
```

Resolution: fixed



---

archive/issue_comments_000015.json:
```json
{
    "body": "Works in new p-adic architecture",
    "created_at": "2007-04-13T03:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4#issuecomment-15",
    "user": "roed"
}
```

Works in new p-adic architecture
