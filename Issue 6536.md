# Issue 6536: [with patch, positive review] Constructor in sage.rings.number_field.order.Order calls a method of the wrong class

archive/issues_006536.json:
```json
{
    "body": "Assignee: @loefflerd\n\nAt the moment the `__init__` method of class `sage.rings.number_field.order.Order` calls `DedekindDomain.__init__`, despite the fact that `Order` doesn't inherit from `DedekindDomain`. This hasn't caused any problems yet, since `DedekindDomain` inherits its `__init__` function from `IntegralDomain` (which /is/ the correct base class for `Order`). But nonetheless it is sloppy coding, and if the Dedekind domain class is either deleted or added to it will cause weird behaviour.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6536\n\n",
    "closed_at": "2009-07-23T08:30:00Z",
    "created_at": "2009-07-15T07:37:59Z",
    "labels": [
        "component: number fields",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] Constructor in sage.rings.number_field.order.Order calls a method of the wrong class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6536",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @loefflerd

At the moment the `__init__` method of class `sage.rings.number_field.order.Order` calls `DedekindDomain.__init__`, despite the fact that `Order` doesn't inherit from `DedekindDomain`. This hasn't caused any problems yet, since `DedekindDomain` inherits its `__init__` function from `IntegralDomain` (which /is/ the correct base class for `Order`). But nonetheless it is sloppy coding, and if the Dedekind domain class is either deleted or added to it will cause weird behaviour.

Issue created by migration from https://trac.sagemath.org/ticket/6536





---

archive/issue_comments_053181.json:
```json
{
    "body": "Attachment [trac_6536-order_wrong_init.patch](tarball://root/attachments/some-uuid/ticket6536/trac_6536-order_wrong_init.patch) by @loefflerd created at 2009-07-15 07:40:25\n\nHere's a two-line fix.",
    "created_at": "2009-07-15T07:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53181",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6536-order_wrong_init.patch](tarball://root/attachments/some-uuid/ticket6536/trac_6536-order_wrong_init.patch) by @loefflerd created at 2009-07-15 07:40:25

Here's a two-line fix.



---

archive/issue_comments_053182.json:
```json
{
    "body": "Nicely spotted.",
    "created_at": "2009-07-21T04:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53182",
    "user": "https://github.com/williamstein"
}
```

Nicely spotted.



---

archive/issue_comments_053183.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53183",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_053184.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53184",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_events_015415.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T08:30:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6536#event-15415"
}
```



---

archive/issue_comments_053185.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T08:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
