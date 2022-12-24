# Issue 9927: vectors from numpy arrays don't always work

archive/issues_009927.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  rbeezer\n\nFrom Victor Miller:\n\n\n```\n\nsage: import numpy\nsage: a = numpy.array([1,2,3])\nsage: v = vector(a)\n\nTraceback (click to the left of this block for traceback)\n...\nTypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and\n'int'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9928\n\n",
    "created_at": "2010-09-17T02:00:19Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "vectors from numpy arrays don't always work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9927",
    "user": "jason"
}
```
Assignee: jason, was

CC:  rbeezer

From Victor Miller:


```

sage: import numpy
sage: a = numpy.array([1,2,3])
sage: v = vector(a)

Traceback (click to the left of this block for traceback)
...
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and
'int'
```



Issue created by migration from https://trac.sagemath.org/ticket/9928





---

archive/issue_comments_098864.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-17T02:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9927#issuecomment-98864",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098865.json:
```json
{
    "body": "Attachment [9928-vector-numpy.patch](tarball://root/attachments/some-uuid/ticket9928/9928-vector-numpy.patch) by jason created at 2010-09-17 02:07:23",
    "created_at": "2010-09-17T02:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9927#issuecomment-98865",
    "user": "jason"
}
```

Attachment [9928-vector-numpy.patch](tarball://root/attachments/some-uuid/ticket9928/9928-vector-numpy.patch) by jason created at 2010-09-17 02:07:23



---

archive/issue_comments_098866.json:
```json
{
    "body": "The problem was that we were falling through to the last case (R**len(v)), but R was never prepared (i.e., was None) because the else statement was tied to the numpy check, not the dict check.",
    "created_at": "2010-09-17T02:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9927#issuecomment-98866",
    "user": "jason"
}
```

The problem was that we were falling through to the last case (R**len(v)), but R was never prepared (i.e., was None) because the else statement was tied to the numpy check, not the dict check.



---

archive/issue_comments_098867.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-17T04:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9927#issuecomment-98867",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098868.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-09-17T04:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9927#issuecomment-98868",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_098869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-28T10:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9927#issuecomment-98869",
    "user": "mpatel"
}
```

Resolution: fixed
