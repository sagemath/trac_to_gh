# Issue 7328: latex doesn't handle python floats correctly

archive/issues_007328.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  kcrisman\n\nCompare:\n\n\n```\nsage: latex(float(3e-10))\n3e-10\nsage: latex(RR(3e-10))\n3.00000000000000 \\times 10^{-10}\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7328\n\n",
    "created_at": "2009-10-28T00:35:44Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "latex doesn't handle python floats correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7328",
    "user": "jason"
}
```
Assignee: cwitty

CC:  kcrisman

Compare:


```
sage: latex(float(3e-10))
3e-10
sage: latex(RR(3e-10))
3.00000000000000 \times 10^{-10}
```



Issue created by migration from https://trac.sagemath.org/ticket/7328





---

archive/issue_comments_061288.json:
```json
{
    "body": "Attachment [trac-7328-latex-float.patch](tarball://root/attachments/some-uuid/ticket7328/trac-7328-latex-float.patch) by jason created at 2009-10-28 00:53:54",
    "created_at": "2009-10-28T00:53:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7328#issuecomment-61288",
    "user": "jason"
}
```

Attachment [trac-7328-latex-float.patch](tarball://root/attachments/some-uuid/ticket7328/trac-7328-latex-float.patch) by jason created at 2009-10-28 00:53:54



---

archive/issue_comments_061289.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T03:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7328#issuecomment-61289",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061290.json:
```json
{
    "body": "This seems good and consistent with the rest of the latex_table, and certainly makes sense for the notebook!  Unless there are other obvious places to put doctests for this (notebook?), positive review.",
    "created_at": "2009-10-29T18:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7328#issuecomment-61290",
    "user": "kcrisman"
}
```

This seems good and consistent with the rest of the latex_table, and certainly makes sense for the notebook!  Unless there are other obvious places to put doctests for this (notebook?), positive review.



---

archive/issue_comments_061291.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T18:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7328#issuecomment-61291",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061292.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7328#issuecomment-61292",
    "user": "mhansen"
}
```

Resolution: fixed
