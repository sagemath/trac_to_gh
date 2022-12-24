# Issue 2542: [with patch, needs review] implement right_kernel() and right_nullity() for matrices

archive/issues_002542.json:
```json
{
    "body": "Assignee: was\n\nI implemented right_kernel() and right_nullity() for matrices in the simplest possible way (calling the left_ functions on the transpose of self).  This is a tiny little step in the direction of #1607.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2542\n\n",
    "created_at": "2008-03-16T03:49:14Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] implement right_kernel() and right_nullity() for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2542",
    "user": "AlexGhitza"
}
```
Assignee: was

I implemented right_kernel() and right_nullity() for matrices in the simplest possible way (calling the left_ functions on the transpose of self).  This is a tiny little step in the direction of #1607.


Issue created by migration from https://trac.sagemath.org/ticket/2542





---

archive/issue_comments_017332.json:
```json
{
    "body": "Attachment [2542-2.patch](tarball://root/attachments/some-uuid/ticket2542/2542-2.patch) by mhansen created at 2008-03-16 04:12:31",
    "created_at": "2008-03-16T04:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17332",
    "user": "mhansen"
}
```

Attachment [2542-2.patch](tarball://root/attachments/some-uuid/ticket2542/2542-2.patch) by mhansen created at 2008-03-16 04:12:31



---

archive/issue_comments_017333.json:
```json
{
    "body": "Looks good to me.  Apply 2542-2.patch which is rebased against 2.10.4.alpha0.",
    "created_at": "2008-03-16T04:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17333",
    "user": "mhansen"
}
```

Looks good to me.  Apply 2542-2.patch which is rebased against 2.10.4.alpha0.



---

archive/issue_comments_017334.json:
```json
{
    "body": "This patch causes a doctest failure for me:\n\n```\nsage -t -long devel/sage/sage/matrix/matrix2.pyx\n**********************************************************************\nFile \"matrix2.pyx\", line 1170:\n    sage: A.right_nullity()\nExpected:\n    1\nGot:\n    0\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_26\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_matrix2.pyx\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T05:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17334",
    "user": "mabshoff"
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

archive/issue_comments_017335.json:
```json
{
    "body": "\n```\n[06:34] <mhansen> mabshoff: For 2542, the doctest is wrong and the answer returned is correct.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T06:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17335",
    "user": "mabshoff"
}
```


```
[06:34] <mhansen> mabshoff: For 2542, the doctest is wrong and the answer returned is correct.
```


Cheers,

Michael



---

archive/issue_comments_017336.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T07:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17336",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017337.json:
```json
{
    "body": "Merged 2542-2.patch with corrected doctest in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T07:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2542#issuecomment-17337",
    "user": "mabshoff"
}
```

Merged 2542-2.patch with corrected doctest in Sage 2.10.4.rc0
