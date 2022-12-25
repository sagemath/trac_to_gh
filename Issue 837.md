# Issue 837: RealNumber should have abs method

archive/issues_000837.json:
```json
{
    "body": "Assignee: somebody\n\nThis violates the principle of least surprise, at least for me:\n\n\n```\nsage: x = -2.0\nsage: x.abs()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/david/sage-2.8.5/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'abs'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/837\n\n",
    "created_at": "2007-10-07T15:22:26Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "RealNumber should have abs method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/837",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

This violates the principle of least surprise, at least for me:


```
sage: x = -2.0
sage: x.abs()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'abs'
```



Issue created by migration from https://trac.sagemath.org/ticket/837





---

archive/issue_comments_005156.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-10-19T19:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_005157.json:
```json
{
    "body": "Attachment [7003.patch](tarball://root/attachments/some-uuid/ticket837/7003.patch) by cwitty created at 2007-10-20 20:03:28",
    "created_at": "2007-10-20T20:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5157",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [7003.patch](tarball://root/attachments/some-uuid/ticket837/7003.patch) by cwitty created at 2007-10-20 20:03:28



---

archive/issue_comments_005158.json:
```json
{
    "body": "The attached patch actually adds an abs() method to every RingElement (that just forwards to the `__abs__` method).",
    "created_at": "2007-10-20T20:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5158",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The attached patch actually adds an abs() method to every RingElement (that just forwards to the `__abs__` method).



---

archive/issue_comments_005159.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T21:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5159",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_events_000950.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T21:00:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/837#event-950"
}
```



---

archive/issue_comments_005160.json:
```json
{
    "body": "applied to 2.8.9.alpha0",
    "created_at": "2007-10-23T21:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5160",
    "user": "https://github.com/malb"
}
```

applied to 2.8.9.alpha0
