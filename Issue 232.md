# Issue 232: assert statement does not work in sage

archive/issues_000232.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: python assert\n\nDifferent behavior in sage shell than in regular python shell:\n\nsage: x = 5\nsage: y = 3\nsage: assert x==y\nsage:\n\nin python:\n>>> x = 5\n>>> y = 3\n>>> assert x==y\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\nAssertionError\n>>>\n\nIssue created by migration from https://trac.sagemath.org/ticket/232\n\n",
    "created_at": "2007-01-29T20:07:29Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "assert statement does not work in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/232",
    "user": "@yqiang"
}
```
Assignee: @williamstein

Keywords: python assert

Different behavior in sage shell than in regular python shell:

sage: x = 5
sage: y = 3
sage: assert x==y
sage:

in python:
>>> x = 5
>>> y = 3
>>> assert x==y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>>

Issue created by migration from https://trac.sagemath.org/ticket/232





---

archive/issue_comments_001028.json:
```json
{
    "body": "This is a SAGE/Ipython interaction problem, since assert works fine in the SAGE Notebook, and with dsage.client...",
    "created_at": "2007-01-29T20:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/232#issuecomment-1028",
    "user": "@williamstein"
}
```

This is a SAGE/Ipython interaction problem, since assert works fine in the SAGE Notebook, and with dsage.client...



---

archive/issue_comments_001029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-29T20:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/232#issuecomment-1029",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001030.json:
```json
{
    "body": "Fixed for sage > 2.0.",
    "created_at": "2007-01-29T20:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/232#issuecomment-1030",
    "user": "@williamstein"
}
```

Fixed for sage > 2.0.
