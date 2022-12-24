# Issue 837: RealNumber should have abs method

archive/issues_000837.json:
```json
{
    "body": "Assignee: somebody\n\nThis violates the principle of least surprise, at least for me:\n\n\n```\nsage: x = -2.0\nsage: x.abs()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/david/sage-2.8.5/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.real_mpfr.RealNumber' object has no attribute 'abs'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/837\n\n",
    "created_at": "2007-10-07T15:22:26Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "RealNumber should have abs method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/837",
    "user": "dmharvey"
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

archive/issue_comments_005172.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2007-10-19T19:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5172",
    "user": "mabshoff"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_005173.json:
```json
{
    "body": "Attachment [7003.patch](tarball://root/attachments/some-uuid/ticket837/7003.patch) by cwitty created at 2007-10-20 20:03:28",
    "created_at": "2007-10-20T20:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5173",
    "user": "cwitty"
}
```

Attachment [7003.patch](tarball://root/attachments/some-uuid/ticket837/7003.patch) by cwitty created at 2007-10-20 20:03:28



---

archive/issue_comments_005174.json:
```json
{
    "body": "The attached patch actually adds an abs() method to every RingElement (that just forwards to the `__abs__` method).",
    "created_at": "2007-10-20T20:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5174",
    "user": "cwitty"
}
```

The attached patch actually adds an abs() method to every RingElement (that just forwards to the `__abs__` method).



---

archive/issue_comments_005175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T21:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5175",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_005176.json:
```json
{
    "body": "applied to 2.8.9.alpha0",
    "created_at": "2007-10-23T21:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/837#issuecomment-5176",
    "user": "malb"
}
```

applied to 2.8.9.alpha0
