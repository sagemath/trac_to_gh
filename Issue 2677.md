# Issue 2677: sage 2.11.alpha1: doctest failures in real_double_dense.pyx

archive/issues_002677.json:
```json
{
    "body": "Assignee: @dfdeshom\n\n\n```\nRe the doctest failure on Clement's G5:\n\nsage -t  devel/sage-main/sage/matrix/matrix_real_double_dense.pyx\n**********************************************************************\nFile \"matrix_real_double_dense.pyx\", line 331:\n    sage: ~A\nExpected:\n    [ 0.1  0.0]\n    [ 0.0 0.01]\nGot:\n    [ 0.1 -0.0]\n    [-0.0 0.01]\n**********************************************************************\nFile \"matrix_real_double_dense.pyx\", line 349:\n    sage: A.inverse()\nExpected:\n    [nan nan]\n    [nan inf]\nGot:\n    [ nan  nan]\n    [ nan -inf]\n**********************************************************************\n\nIt is a sign issue, but I am not sure what we can do here.\n\nCheers,\n\nMichael \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2677\n\n",
    "created_at": "2008-03-26T18:04:16Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "sage 2.11.alpha1: doctest failures in real_double_dense.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2677",
    "user": "https://github.com/dfdeshom"
}
```
Assignee: @dfdeshom


```
Re the doctest failure on Clement's G5:

sage -t  devel/sage-main/sage/matrix/matrix_real_double_dense.pyx
**********************************************************************
File "matrix_real_double_dense.pyx", line 331:
    sage: ~A
Expected:
    [ 0.1  0.0]
    [ 0.0 0.01]
Got:
    [ 0.1 -0.0]
    [-0.0 0.01]
**********************************************************************
File "matrix_real_double_dense.pyx", line 349:
    sage: A.inverse()
Expected:
    [nan nan]
    [nan inf]
Got:
    [ nan  nan]
    [ nan -inf]
**********************************************************************

It is a sign issue, but I am not sure what we can do here.

Cheers,

Michael 
```


Issue created by migration from https://trac.sagemath.org/ticket/2677





---

archive/issue_comments_018379.json:
```json
{
    "body": "Attachment [2677_trac.patch](tarball://root/attachments/some-uuid/ticket2677/2677_trac.patch) by @dfdeshom created at 2008-03-26 20:34:34",
    "created_at": "2008-03-26T20:34:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2677#issuecomment-18379",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2677_trac.patch](tarball://root/attachments/some-uuid/ticket2677/2677_trac.patch) by @dfdeshom created at 2008-03-26 20:34:34



---

archive/issue_comments_018380.json:
```json
{
    "body": "Patch looks good to me and fixes the issue. Positive review.",
    "created_at": "2008-03-26T22:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2677#issuecomment-18380",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me and fixes the issue. Positive review.



---

archive/issue_comments_018381.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-26T22:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2677#issuecomment-18381",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_events_002869.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-26T22:18:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2677",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2677#event-2869"
}
```



---

archive/issue_comments_018382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-26T22:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2677#issuecomment-18382",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
