# Issue 835: cannot coerce real numbers to Integer

archive/issues_000835.json:
```json
{
    "body": "Assignee: somebody\n\nIf a real number is exactly an integer, it should be possible to coerce to an Integer, but this is what happens:\n\n\n```\nsage: Integer(RR(2.0))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/david/sage-2.8.5/<ipython console> in <module>()\n\n/Users/david/sage-2.8.5/integer.pyx in integer.Integer.__init__()\n\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/835\n\n",
    "created_at": "2007-10-06T15:33:28Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "cannot coerce real numbers to Integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/835",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

If a real number is exactly an integer, it should be possible to coerce to an Integer, but this is what happens:


```
sage: Integer(RR(2.0))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/david/sage-2.8.5/<ipython console> in <module>()

/Users/david/sage-2.8.5/integer.pyx in integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
```



Issue created by migration from https://trac.sagemath.org/ticket/835





---

archive/issue_comments_005149.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-10-07T14:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/835#issuecomment-5149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_005150.json:
```json
{
    "body": "Attachment [6721.patch](tarball://root/attachments/some-uuid/ticket835/6721.patch) by cwitty created at 2007-10-11 04:57:10",
    "created_at": "2007-10-11T04:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/835#issuecomment-5150",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [6721.patch](tarball://root/attachments/some-uuid/ticket835/6721.patch) by cwitty created at 2007-10-11 04:57:10



---

archive/issue_events_000948.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-13T05:46:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/835",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/835#event-948"
}
```



---

archive/issue_comments_005151.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T05:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/835#issuecomment-5151",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
