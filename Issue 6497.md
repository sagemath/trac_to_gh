# Issue 6497: [with patch, needs review] symbolic functions should understand numpy arrays

archive/issues_006497.json:
```json
{
    "body": "Assignee: @burcin\n\nWe want\n\n\n```\nsage: import numpy\nsage: sin(numpy.arange(5))\narray([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6497\n\n",
    "created_at": "2009-07-09T10:14:40Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] symbolic functions should understand numpy arrays",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6497",
    "user": "@robertwb"
}
```
Assignee: @burcin

We want


```
sage: import numpy
sage: sin(numpy.arange(5))
array([ 0.        ,  0.84147098,  0.90929743,  0.14112001, -0.7568025 ])
```


Issue created by migration from https://trac.sagemath.org/ticket/6497





---

archive/issue_comments_052854.json:
```json
{
    "body": "Attachment [6497-numpy-sin.patch](tarball://root/attachments/some-uuid/ticket6497/6497-numpy-sin.patch) by @burcin created at 2009-07-12 10:33:03\n\nThis depends on #5081.",
    "created_at": "2009-07-12T10:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6497#issuecomment-52854",
    "user": "@burcin"
}
```

Attachment [6497-numpy-sin.patch](tarball://root/attachments/some-uuid/ticket6497/6497-numpy-sin.patch) by @burcin created at 2009-07-12 10:33:03

This depends on #5081.



---

archive/issue_comments_052855.json:
```json
{
    "body": "With the patches at #5081 and #6506, and `6497-numpy-sin.patch` on this ticket, I got one doctest failure:\n\n```\nsage -t -long devel/sage-main/sage/modules/vector_double_dense.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/modules/vector_double_dense.pyx\", line 663:\n    sage: v.stats_kurtosis()\nExpected:\n    -1.23\nGot:\n    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?\n    -1.23\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_29\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_vector_double_dense.py\n\t [2.5 s]\n```\n",
    "created_at": "2009-07-30T01:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6497#issuecomment-52855",
    "user": "mvngu"
}
```

With the patches at #5081 and #6506, and `6497-numpy-sin.patch` on this ticket, I got one doctest failure:

```
sage -t -long devel/sage-main/sage/modules/vector_double_dense.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha1/devel/sage-main/sage/modules/vector_double_dense.pyx", line 663:
    sage: v.stats_kurtosis()
Expected:
    -1.23
Got:
    doctest:106: SyntaxWarning: assertion is always true, perhaps remove parentheses?
    -1.23
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_29
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha1/tmp/.doctest_vector_double_dense.py
	 [2.5 s]
```




---

archive/issue_comments_052856.json:
```json
{
    "body": "I am unable to reproduce the error above on 4.1.1, so I am re-instating the positive review. (Also, the error itself seems totally unrelated to this patch.)",
    "created_at": "2009-09-10T09:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6497#issuecomment-52856",
    "user": "@robertwb"
}
```

I am unable to reproduce the error above on 4.1.1, so I am re-instating the positive review. (Also, the error itself seems totally unrelated to this patch.)



---

archive/issue_comments_052857.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> I am unable to reproduce the error above on 4.1.1, so I am re-instating the positive review. (Also, the error itself seems totally unrelated to this patch.)\nThe above error is not due to the patch. Ticket #6825 contains steps to reproduce the errors.",
    "created_at": "2009-09-10T09:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6497#issuecomment-52857",
    "user": "mvngu"
}
```

Replying to [comment:3 robertwb]:
> I am unable to reproduce the error above on 4.1.1, so I am re-instating the positive review. (Also, the error itself seems totally unrelated to this patch.)
The above error is not due to the patch. Ticket #6825 contains steps to reproduce the errors.



---

archive/issue_comments_052858.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-10T09:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6497#issuecomment-52858",
    "user": "mvngu"
}
```

Resolution: fixed
