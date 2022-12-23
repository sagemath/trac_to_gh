# Issue 1605: conversion of sage vectors to magma vectors not implemented.

archive/issues_001605.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: v = vector([1,2,3])\nsage: magma(v)\nboom ...\n\nIN:_sage_[2] := (1, 2, 3);\nOUT:\n>> _sage_[2] := (1, 2, 3);\n                ^\nRuntime error in elt< ... >: No permutation group context in which to create cycle\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1605\n\n",
    "created_at": "2007-12-27T02:45:23Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "conversion of sage vectors to magma vectors not implemented.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1605",
    "user": "was"
}
```
Assignee: was


```
sage: v = vector([1,2,3])
sage: magma(v)
boom ...

IN:_sage_[2] := (1, 2, 3);
OUT:
>> _sage_[2] := (1, 2, 3);
                ^
Runtime error in elt< ... >: No permutation group context in which to create cycle

```


Issue created by migration from https://trac.sagemath.org/ticket/1605





---

archive/issue_comments_010197.json:
```json
{
    "body": "Attachment\n\nadd support for converting vectors to magma",
    "created_at": "2008-05-12T15:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10197",
    "user": "burcin"
}
```

Attachment

add support for converting vectors to magma



---

archive/issue_comments_010198.json:
```json
{
    "body": "Changing assignee from was to burcin.",
    "created_at": "2008-05-12T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10198",
    "user": "burcin"
}
```

Changing assignee from was to burcin.



---

archive/issue_comments_010199.json:
```json
{
    "body": "attachment:1605-sage_vectors_to_magma.patch adds support for converting vectors to Magma.",
    "created_at": "2008-05-12T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10199",
    "user": "burcin"
}
```

attachment:1605-sage_vectors_to_magma.patch adds support for converting vectors to Magma.



---

archive/issue_comments_010200.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-12T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10200",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010201.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-05-24T21:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10201",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_010202.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-25T04:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10202",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_010203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-25T04:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10203",
    "user": "mabshoff"
}
```

Resolution: fixed
