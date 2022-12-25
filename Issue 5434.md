# Issue 5434: [with patch, needs review] .shift() of a zero polynomial is broken

archive/issues_005434.json:
```json
{
    "body": "Assignee: cwitty\n\n```\nsage: K.<x> = RDF[]\nsage: K(0).shift(3).is_zero()\nFalse\nsage: K.<x> = RR[]\nsage: K(0).shift(3).is_zero()\nFalse\nsage: K.<x> = AA[]\nsage: K(0).shift(3).is_zero()\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5434\n\n",
    "created_at": "2009-03-04T04:02:25Z",
    "labels": [
        "component: basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] .shift() of a zero polynomial is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5434",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

```
sage: K.<x> = RDF[]
sage: K(0).shift(3).is_zero()
False
sage: K.<x> = RR[]
sage: K(0).shift(3).is_zero()
False
sage: K.<x> = AA[]
sage: K(0).shift(3).is_zero()
False
```


Issue created by migration from https://trac.sagemath.org/ticket/5434





---

archive/issue_comments_041960.json:
```json
{
    "body": "Attachment [poly-shift-of-zero.patch](tarball://root/attachments/some-uuid/ticket5434/poly-shift-of-zero.patch) by @williamstein created at 2009-03-04 07:04:38\n\nExcellent.  Thanks!",
    "created_at": "2009-03-04T07:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5434#issuecomment-41960",
    "user": "https://github.com/williamstein"
}
```

Attachment [poly-shift-of-zero.patch](tarball://root/attachments/some-uuid/ticket5434/poly-shift-of-zero.patch) by @williamstein created at 2009-03-04 07:04:38

Excellent.  Thanks!



---

archive/issue_comments_041961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-05T00:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5434#issuecomment-41961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041962.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-05T00:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5434#issuecomment-41962",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_events_012680.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-05T00:07:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5434",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5434#event-12680"
}
```
