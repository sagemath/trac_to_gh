# Issue 5026: numerical noise doctest failure in rings/polynomial/complex_roots.py

archive/issues_005026.json:
```json
{
    "body": "Assignee: jkantor\n\nKeywords: complex roots, polynomial\n\nOn sage-3.3.alpha0 I get this doctest failure on an intel mac:\n\n\n```\n**********************************************************************\nFile \".../devel/sage/sage/rings/polynomial/complex_roots.py\", line\n270:\n    sage: complex_roots(x^2 + 27*x + 181)\nExpected:\n    [(-14.61803398874990?..., 1), (-12.38196601125010? + 0.?e-27*I,\n1)]\nGot:\n    [(-14.61803398874990? + 0.?e-27*I, 1), (-12.38196601125011? + 0.?\ne-27*I, 1)]\n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5026\n\n",
    "created_at": "2009-01-19T16:11:44Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "numerical noise doctest failure in rings/polynomial/complex_roots.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5026",
    "user": "mhampton"
}
```
Assignee: jkantor

Keywords: complex roots, polynomial

On sage-3.3.alpha0 I get this doctest failure on an intel mac:


```
**********************************************************************
File ".../devel/sage/sage/rings/polynomial/complex_roots.py", line
270:
    sage: complex_roots(x^2 + 27*x + 181)
Expected:
    [(-14.61803398874990?..., 1), (-12.38196601125010? + 0.?e-27*I,
1)]
Got:
    [(-14.61803398874990? + 0.?e-27*I, 1), (-12.38196601125011? + 0.?
e-27*I, 1)]
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/5026





---

archive/issue_comments_038288.json:
```json
{
    "body": "Attachment [trac-5026.patch](tarball://root/attachments/some-uuid/ticket5026/trac-5026.patch) by @craigcitro created at 2009-01-23 13:19:56\n\nAttached patch fixes the doctest.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5026#issuecomment-38288",
    "user": "@craigcitro"
}
```

Attachment [trac-5026.patch](tarball://root/attachments/some-uuid/ticket5026/trac-5026.patch) by @craigcitro created at 2009-01-23 13:19:56

Attached patch fixes the doctest.



---

archive/issue_comments_038289.json:
```json
{
    "body": "Changing assignee from jkantor to @craigcitro.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5026#issuecomment-38289",
    "user": "@craigcitro"
}
```

Changing assignee from jkantor to @craigcitro.



---

archive/issue_comments_038290.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5026#issuecomment-38290",
    "user": "@craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038291.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T16:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5026#issuecomment-38291",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_038292.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T13:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5026#issuecomment-38292",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_038293.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T13:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5026",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5026#issuecomment-38293",
    "user": "mabshoff"
}
```

Resolution: fixed
