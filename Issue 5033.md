# Issue 5033: matrix lift function bad in two ways

archive/issues_005033.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere are two problem here:\n\n```\nsage: B = matrix(QQ, 2, [1..4])\nsage: B.lift()\n...\nAttributeError: 'RationalField' object has no attribute 'cover_ring'\nsage: B.lift?\n            EXAMPLES:\n...\n```\n          \n\n1. lift should first check if there is a cover_ring attribute.  If not, I think lift should just return self.\n\n2. The lift function is undocumented.  It just has examples but no description of what it is supposed to do.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5033\n\n",
    "created_at": "2009-01-20T06:03:40Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "matrix lift function bad in two ways",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5033",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

There are two problem here:

```
sage: B = matrix(QQ, 2, [1..4])
sage: B.lift()
...
AttributeError: 'RationalField' object has no attribute 'cover_ring'
sage: B.lift?
            EXAMPLES:
...
```
          

1. lift should first check if there is a cover_ring attribute.  If not, I think lift should just return self.

2. The lift function is undocumented.  It just has examples but no description of what it is supposed to do.

Issue created by migration from https://trac.sagemath.org/ticket/5033





---

archive/issue_comments_038257.json:
```json
{
    "body": "Attachment [trac_5033.patch](tarball://root/attachments/some-uuid/ticket5033/trac_5033.patch) by @williamstein created at 2009-01-20 06:35:11\n\nthis is against sage-3.3.alpha0",
    "created_at": "2009-01-20T06:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38257",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5033.patch](tarball://root/attachments/some-uuid/ticket5033/trac_5033.patch) by @williamstein created at 2009-01-20 06:35:11

this is against sage-3.3.alpha0



---

archive/issue_comments_038258.json:
```json
{
    "body": "The patch fixes both issues mentioned in the ticket and the code is nice. Positive review.",
    "created_at": "2009-01-20T06:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38258",
    "user": "https://github.com/dandrake"
}
```

The patch fixes both issues mentioned in the ticket and the code is nice. Positive review.



---

archive/issue_events_005277.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T09:07:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5033#event-5277"
}
```



---

archive/issue_comments_038259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038260.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38260",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1
