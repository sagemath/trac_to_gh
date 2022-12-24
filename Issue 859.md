# Issue 859: Cannot coerce numpy integral types to ZZ

archive/issues_000859.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nsage: import numpy\nsage: ZZ(numpy.int64(3))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/cwitty/my-sage/<ipython console> in <module>()\n\n/home/cwitty/my-sage/integer_ring.pyx in integer_ring.IntegerRing_class.__call__()\n\n<type 'exceptions.TypeError'>: unable to coerce element to an integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/859\n\n",
    "created_at": "2007-10-12T05:16:54Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "Cannot coerce numpy integral types to ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/859",
    "user": "cwitty"
}
```
Assignee: cwitty


```
sage: import numpy
sage: ZZ(numpy.int64(3))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/cwitty/my-sage/<ipython console> in <module>()

/home/cwitty/my-sage/integer_ring.pyx in integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: unable to coerce element to an integer
```


Issue created by migration from https://trac.sagemath.org/ticket/859





---

archive/issue_comments_005319.json:
```json
{
    "body": "Attachment [6722.patch](tarball://root/attachments/some-uuid/ticket859/6722.patch) by cwitty created at 2007-10-12 05:33:27",
    "created_at": "2007-10-12T05:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/859#issuecomment-5319",
    "user": "cwitty"
}
```

Attachment [6722.patch](tarball://root/attachments/some-uuid/ticket859/6722.patch) by cwitty created at 2007-10-12 05:33:27



---

archive/issue_comments_005320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T07:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/859",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/859#issuecomment-5320",
    "user": "@williamstein"
}
```

Resolution: fixed
