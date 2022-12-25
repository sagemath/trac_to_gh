# Issue 2542: [with patch, needs review] implement right_kernel() and right_nullity() for matrices

archive/issues_002542.json:
```json
{
    "body": "Assignee: @williamstein\n\nI implemented right_kernel() and right_nullity() for matrices in the simplest possible way (calling the left_ functions on the transpose of self).  This is a tiny little step in the direction of #1607.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2542\n\n",
    "created_at": "2008-03-16T03:49:14Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] implement right_kernel() and right_nullity() for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2542",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

I implemented right_kernel() and right_nullity() for matrices in the simplest possible way (calling the left_ functions on the transpose of self).  This is a tiny little step in the direction of #1607.


Issue created by migration from https://trac.sagemath.org/ticket/2542





---

archive/issue_comments_017295.json:
```json
{
    "body": "Attachment [2542-2.patch](tarball://root/attachments/some-uuid/ticket2542/2542-2.patch) by @mwhansen created at 2008-03-16 04:12:31",
    "created_at": "2008-03-16T04:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17295",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2542-2.patch](tarball://root/attachments/some-uuid/ticket2542/2542-2.patch) by @mwhansen created at 2008-03-16 04:12:31



---

archive/issue_comments_017296.json:
```json
{
    "body": "Looks good to me.  Apply 2542-2.patch which is rebased against 2.10.4.alpha0.",
    "created_at": "2008-03-16T04:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17296",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Apply 2542-2.patch which is rebased against 2.10.4.alpha0.



---

archive/issue_comments_017297.json:
```json
{
    "body": "This patch causes a doctest failure for me:\n\n```\nsage -t -long devel/sage/sage/matrix/matrix2.pyx\n**********************************************************************\nFile \"matrix2.pyx\", line 1170:\n    sage: A.right_nullity()\nExpected:\n    1\nGot:\n    0\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_26\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_matrix2.pyx\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T05:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes a doctest failure for me:

```
sage -t -long devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "matrix2.pyx", line 1170:
    sage: A.right_nullity()
Expected:
    1
Got:
    0
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_26
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_matrix2.pyx
```


Cheers,

Michael



---

archive/issue_comments_017298.json:
```json
{
    "body": "\n```\n[06:34] <mhansen> mabshoff: For 2542, the doctest is wrong and the answer returned is correct.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T06:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17298",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[06:34] <mhansen> mabshoff: For 2542, the doctest is wrong and the answer returned is correct.
```


Cheers,

Michael



---

archive/issue_comments_017299.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T07:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17299",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017300.json:
```json
{
    "body": "Merged 2542-2.patch with corrected doctest in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T07:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2542-2.patch with corrected doctest in Sage 2.10.4.rc0
