# Issue 4170: symbolic ring does not accept python longs

archive/issues_004170.json:
```json
{
    "body": "Assignee: burcin\n\nThe easy fix is to add it to the big list in `_coerce_impl` at sage.calculus.calculus.py:481. Because\n\n\n```\nsage: ZZ.has_coerce_map_from(long)\nTrue\nsage: SR.has_coerce_map_from(ZZ)\nTrue\n```\n\n\nThis should be handled in the new model, but symbolics are being changed anyways. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4170\n\n",
    "created_at": "2008-09-23T01:10:30Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "symbolic ring does not accept python longs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4170",
    "user": "robertwb"
}
```
Assignee: burcin

The easy fix is to add it to the big list in `_coerce_impl` at sage.calculus.calculus.py:481. Because


```
sage: ZZ.has_coerce_map_from(long)
True
sage: SR.has_coerce_map_from(ZZ)
True
```


This should be handled in the new model, but symbolics are being changed anyways. 

Issue created by migration from https://trac.sagemath.org/ticket/4170





---

archive/issue_comments_030269.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-23T01:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30269",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_030270.json:
```json
{
    "body": "Looks good to me. Assuming this passes doctests positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T01:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30270",
    "user": "mabshoff"
}
```

Looks good to me. Assuming this passes doctests positive review.

Cheers,

Michael



---

archive/issue_comments_030271.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T01:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30271",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_030272.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T01:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30272",
    "user": "mabshoff"
}
```

Resolution: fixed
