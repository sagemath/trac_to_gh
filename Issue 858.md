# Issue 858: add support for numpy arrays with integer entries

archive/issues_000858.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: numpy\n\n\n```\nsage: import numpy\nsage: a = numpy.array([[1,2],[3,4]],'int32')\nsage: matrix(a)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/mhansen/sage/devel/sage-856/<ipython console> in <module>()\n\n/home/mhansen/sage/local/lib/python2.5/site-packages/sage/matrix/constructor.py in matrix(arg0, arg1, arg2, arg3, sparse)\n    399                     raise TypeError(\"cannot convert numpy matrix to SAGE matrix\")\n    400             else:\n--> 401                 raise TypeError(\"cannot convert numpy matrix to SAGE matrix\")\n    402 \n    403         else:\n\n<type 'exceptions.TypeError'>: cannot convert numpy matrix to SAGE matrix\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/858\n\n",
    "created_at": "2007-10-12T04:51:54Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "add support for numpy arrays with integer entries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/858",
    "user": "@mwhansen"
}
```
Assignee: @williamstein

Keywords: numpy


```
sage: import numpy
sage: a = numpy.array([[1,2],[3,4]],'int32')
sage: matrix(a)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mhansen/sage/devel/sage-856/<ipython console> in <module>()

/home/mhansen/sage/local/lib/python2.5/site-packages/sage/matrix/constructor.py in matrix(arg0, arg1, arg2, arg3, sparse)
    399                     raise TypeError("cannot convert numpy matrix to SAGE matrix")
    400             else:
--> 401                 raise TypeError("cannot convert numpy matrix to SAGE matrix")
    402 
    403         else:

<type 'exceptions.TypeError'>: cannot convert numpy matrix to SAGE matrix
```


Issue created by migration from https://trac.sagemath.org/ticket/858





---

archive/issue_comments_005313.json:
```json
{
    "body": "Attachment [858.patch](tarball://root/attachments/some-uuid/ticket858/858.patch) by @mwhansen created at 2007-10-12 05:44:40\n\npatch #1",
    "created_at": "2007-10-12T05:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/858#issuecomment-5313",
    "user": "@mwhansen"
}
```

Attachment [858.patch](tarball://root/attachments/some-uuid/ticket858/858.patch) by @mwhansen created at 2007-10-12 05:44:40

patch #1



---

archive/issue_comments_005314.json:
```json
{
    "body": "Attachment [858.2.patch](tarball://root/attachments/some-uuid/ticket858/858.2.patch) by @mwhansen created at 2007-10-12 05:46:21\n\nadded doctest",
    "created_at": "2007-10-12T05:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/858#issuecomment-5314",
    "user": "@mwhansen"
}
```

Attachment [858.2.patch](tarball://root/attachments/some-uuid/ticket858/858.2.patch) by @mwhansen created at 2007-10-12 05:46:21

added doctest



---

archive/issue_comments_005315.json:
```json
{
    "body": "#859 should be applied before these two patches",
    "created_at": "2007-10-12T05:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/858#issuecomment-5315",
    "user": "@mwhansen"
}
```

#859 should be applied before these two patches



---

archive/issue_comments_005316.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-10-12T05:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/858#issuecomment-5316",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_005317.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-12T05:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/858#issuecomment-5317",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T08:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/858#issuecomment-5318",
    "user": "@williamstein"
}
```

Resolution: fixed
