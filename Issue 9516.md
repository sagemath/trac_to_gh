# Issue 9516: numerical noise in sage-4.5.rc1 on PowerPC OS X

archive/issues_009516.json:
```json
{
    "body": "Assignee: mvngu\n\n\n```\nsage -t  -long \"devel/sage/sage/plot/plot3d/parametric_surface.pyx\"\n**********************************************************************\nFile \"/Users/wstein/build/sage-4.5.rc1/devel/sage/sage/plot/plot3d/parametric_surface.pyx\", line 311:\n    sage: M.bounding_box()\nExpected:\n    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))\nGot:\n    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_11\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9516\n\n",
    "created_at": "2010-07-16T09:38:53Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "numerical noise in sage-4.5.rc1 on PowerPC OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9516",
    "user": "https://github.com/williamstein"
}
```
Assignee: mvngu


```
sage -t  -long "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
**********************************************************************
File "/Users/wstein/build/sage-4.5.rc1/devel/sage/sage/plot/plot3d/parametric_surface.pyx", line 311:
    sage: M.bounding_box()
Expected:
    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
Got:
    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest
```


Issue created by migration from https://trac.sagemath.org/ticket/9516





---

archive/issue_comments_091339.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-16T09:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9516#issuecomment-91339",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091340.json:
```json
{
    "body": "Attachment [trac_9516.patch](tarball://root/attachments/some-uuid/ticket9516/trac_9516.patch) by @williamstein created at 2010-07-16 09:44:46",
    "created_at": "2010-07-16T09:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9516#issuecomment-91340",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9516.patch](tarball://root/attachments/some-uuid/ticket9516/trac_9516.patch) by @williamstein created at 2010-07-16 09:44:46



---

archive/issue_comments_091341.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T09:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9516#issuecomment-91341",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091342.json:
```json
{
    "body": "This ticket seems the same as #9002...",
    "created_at": "2010-07-22T02:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9516#issuecomment-91342",
    "user": "https://github.com/dandrake"
}
```

This ticket seems the same as #9002...



---

archive/issue_comments_091343.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-07-22T02:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9516#issuecomment-91343",
    "user": "https://github.com/dandrake"
}
```

Resolution: duplicate



---

archive/issue_comments_091344.json:
```json
{
    "body": "The patches here and at #9002 are identical, but Karl-Dieter beat out William by two months, so I'm closing this ticket and will merge #9002.",
    "created_at": "2010-07-22T02:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9516#issuecomment-91344",
    "user": "https://github.com/dandrake"
}
```

The patches here and at #9002 are identical, but Karl-Dieter beat out William by two months, so I'm closing this ticket and will merge #9002.
