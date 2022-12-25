# Issue 4170: symbolic ring does not accept python longs

archive/issues_004170.json:
```json
{
    "body": "Assignee: @burcin\n\nThe easy fix is to add it to the big list in `_coerce_impl` at sage.calculus.calculus.py:481. Because\n\n\n```\nsage: ZZ.has_coerce_map_from(long)\nTrue\nsage: SR.has_coerce_map_from(ZZ)\nTrue\n```\n\n\nThis should be handled in the new model, but symbolics are being changed anyways. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4170\n\n",
    "created_at": "2008-09-23T01:10:30Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "symbolic ring does not accept python longs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4170",
    "user": "https://github.com/robertwb"
}
```
Assignee: @burcin

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

archive/issue_comments_030208.json:
```json
{
    "body": "Attachment [4170-SR-long.patch](tarball://root/attachments/some-uuid/ticket4170/4170-SR-long.patch) by @robertwb created at 2008-09-23 01:15:49",
    "created_at": "2008-09-23T01:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30208",
    "user": "https://github.com/robertwb"
}
```

Attachment [4170-SR-long.patch](tarball://root/attachments/some-uuid/ticket4170/4170-SR-long.patch) by @robertwb created at 2008-09-23 01:15:49



---

archive/issue_comments_030209.json:
```json
{
    "body": "Looks good to me. Assuming this passes doctests positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T01:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30209",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. Assuming this passes doctests positive review.

Cheers,

Michael



---

archive/issue_events_004407.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-23T01:51:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4170#event-4407"
}
```



---

archive/issue_comments_030210.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1",
    "created_at": "2008-09-23T01:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30210",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha1



---

archive/issue_comments_030211.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T01:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4170",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4170#issuecomment-30211",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
