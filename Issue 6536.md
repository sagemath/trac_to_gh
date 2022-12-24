# Issue 6536: Constructor in sage.rings.number_field.order.Order calls a method of the wrong class

archive/issues_006536.json:
```json
{
    "body": "Assignee: was\n\nAt the moment the `__init__` method of class `sage.rings.number_field.order.Order` calls `DedekindDomain.__init__`, despite the fact that `Order` doesn't inherit from `DedekindDomain`. This hasn't caused any problems yet, since `DedekindDomain` inherits its `__init__` function from `IntegralDomain` (which *is* the correct base class for `Order`). But nonetheless it is sloppy coding, and if the Dedekind domain class is either deleted or added to it will cause weird behaviour.\n\n\ninherits from `sage.rings.ring.IntegralDomain`, but its `__init__` method , despite the fact that\n\nIssue created by migration from https://trac.sagemath.org/ticket/6536\n\n",
    "created_at": "2009-07-15T07:37:59Z",
    "labels": [
        "number theory",
        "trivial",
        "bug"
    ],
    "title": "Constructor in sage.rings.number_field.order.Order calls a method of the wrong class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6536",
    "user": "davidloeffler"
}
```
Assignee: was

At the moment the `__init__` method of class `sage.rings.number_field.order.Order` calls `DedekindDomain.__init__`, despite the fact that `Order` doesn't inherit from `DedekindDomain`. This hasn't caused any problems yet, since `DedekindDomain` inherits its `__init__` function from `IntegralDomain` (which *is* the correct base class for `Order`). But nonetheless it is sloppy coding, and if the Dedekind domain class is either deleted or added to it will cause weird behaviour.


inherits from `sage.rings.ring.IntegralDomain`, but its `__init__` method , despite the fact that

Issue created by migration from https://trac.sagemath.org/ticket/6536





---

archive/issue_comments_053281.json:
```json
{
    "body": "Attachment [trac_6536-order_wrong_init.patch](tarball://root/attachments/some-uuid/ticket6536/trac_6536-order_wrong_init.patch) by davidloeffler created at 2009-07-15 07:40:25\n\nHere's a two-line fix.",
    "created_at": "2009-07-15T07:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53281",
    "user": "davidloeffler"
}
```

Attachment [trac_6536-order_wrong_init.patch](tarball://root/attachments/some-uuid/ticket6536/trac_6536-order_wrong_init.patch) by davidloeffler created at 2009-07-15 07:40:25

Here's a two-line fix.



---

archive/issue_comments_053282.json:
```json
{
    "body": "Nicely spotted.",
    "created_at": "2009-07-21T04:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53282",
    "user": "was"
}
```

Nicely spotted.



---

archive/issue_comments_053283.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53283",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_053284.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53284",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_053285.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T08:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6536#issuecomment-53285",
    "user": "mvngu"
}
```

Resolution: fixed
