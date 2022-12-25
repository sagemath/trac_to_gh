# Issue 3064: empty matrices: density() function throws a ZeroDivisionError

archive/issues_003064.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: a = matrix([])\n\nsage: a.density()\n---------------------------------------------------------------------------\n\n\n<type 'exceptions.ZeroDivisionError'>: Rational division by zero\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3064\n\n",
    "created_at": "2008-04-30T15:12:48Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "empty matrices: density() function throws a ZeroDivisionError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3064",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @williamstein


```
sage: a = matrix([])

sage: a.density()
---------------------------------------------------------------------------


<type 'exceptions.ZeroDivisionError'>: Rational division by zero
```


Issue created by migration from https://trac.sagemath.org/ticket/3064





---

archive/issue_comments_021108.json:
```json
{
    "body": "Attachment [3064.patch](tarball://root/attachments/some-uuid/ticket3064/3064.patch) by @dfdeshom created at 2008-04-30 18:17:09\n\nPatch attached.",
    "created_at": "2008-04-30T18:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3064#issuecomment-21108",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [3064.patch](tarball://root/attachments/some-uuid/ticket3064/3064.patch) by @dfdeshom created at 2008-04-30 18:17:09

Patch attached.



---

archive/issue_comments_021109.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-01T05:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3064#issuecomment-21109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021110.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-05-01T05:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3064#issuecomment-21110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1



---

archive/issue_events_003274.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-01T05:45:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3064",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3064#event-3274"
}
```
