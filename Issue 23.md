# Issue 23: (Z/nZ)^k problem

archive/issues_000023.json:
```json
{
    "body": "Assignee: somebody\n\nmaybe adding elements of (Z/nZ)^k is broken if one isn't in there.\n   See line 66 of free_module_element.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/23\n\n",
    "created_at": "2006-09-12T23:22:28Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "(Z/nZ)^k problem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/23",
    "user": "@williamstein"
}
```
Assignee: somebody

maybe adding elements of (Z/nZ)^k is broken if one isn't in there.
   See line 66 of free_module_element.py

Issue created by migration from https://trac.sagemath.org/ticket/23





---

archive/issue_comments_000182.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T02:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/23",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/23#issuecomment-182",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000183.json:
```json
{
    "body": "This works fine now (I'm not really sure what the error is from the error report).\n\n\n```\nsage: V = Integers(18)^3\nsage: a = V([1,2,3])\nsage: a+a\n(2, 4, 6)\n```\n",
    "created_at": "2007-01-13T02:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/23",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/23#issuecomment-183",
    "user": "@williamstein"
}
```

This works fine now (I'm not really sure what the error is from the error report).


```
sage: V = Integers(18)^3
sage: a = V([1,2,3])
sage: a+a
(2, 4, 6)
```

