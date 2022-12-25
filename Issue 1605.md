# Issue 1605: conversion of sage vectors to magma vectors not implemented.

archive/issues_001605.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: v = vector([1,2,3])\nsage: magma(v)\nboom ...\n\nIN:_sage_[2] := (1, 2, 3);\nOUT:\n>> _sage_[2] := (1, 2, 3);\n                ^\nRuntime error in elt< ... >: No permutation group context in which to create cycle\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1605\n\n",
    "created_at": "2007-12-27T02:45:23Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "conversion of sage vectors to magma vectors not implemented.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1605",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


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

archive/issue_comments_010170.json:
```json
{
    "body": "Attachment [1605-sage_vectors_to_magma.patch](tarball://root/attachments/some-uuid/ticket1605/1605-sage_vectors_to_magma.patch) by @burcin created at 2008-05-12 15:12:00\n\nadd support for converting vectors to magma",
    "created_at": "2008-05-12T15:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10170",
    "user": "https://github.com/burcin"
}
```

Attachment [1605-sage_vectors_to_magma.patch](tarball://root/attachments/some-uuid/ticket1605/1605-sage_vectors_to_magma.patch) by @burcin created at 2008-05-12 15:12:00

add support for converting vectors to magma



---

archive/issue_comments_010171.json:
```json
{
    "body": "Changing assignee from @williamstein to @burcin.",
    "created_at": "2008-05-12T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10171",
    "user": "https://github.com/burcin"
}
```

Changing assignee from @williamstein to @burcin.



---

archive/issue_comments_010172.json:
```json
{
    "body": "attachment:1605-sage_vectors_to_magma.patch adds support for converting vectors to Magma.",
    "created_at": "2008-05-12T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10172",
    "user": "https://github.com/burcin"
}
```

attachment:1605-sage_vectors_to_magma.patch adds support for converting vectors to Magma.



---

archive/issue_comments_010173.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-12T15:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10173",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010174.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-05-24T21:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10174",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_010175.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-25T04:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_010176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-25T04:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1605#issuecomment-10176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001763.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-25T04:11:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1605",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1605#event-1763"
}
```
