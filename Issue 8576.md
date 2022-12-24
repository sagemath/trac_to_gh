# Issue 8576: Categories for QQ, CC, RR and friends

archive/issues_008576.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  sage-combinat\n\nKeywords: categories, real fields\n\nAfter this patch, QQ,ZZ,... inherit properly from categories: \n\n\n```\nsage: QQ.category()\nCategory of fields\nsage: TestSuite(QQ).run()\n```\n\n\nThis patch also documents the following effect discovered by TestSuite:\n\n```\n    sage: CDF = ComplexDoubleField()\n    sage: x = CDF.an_element()\n    sage: x\n    1.0*I\n    sage: x*x, x**2, x*x == x**2\n    (-1.0, -1.0 + 1.22460635382e-16*I, False)\n```\n\nThis effect won't be touched by this patch. Should anyone consider this as a bug, please open a new ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8576\n\n",
    "created_at": "2010-03-22T10:16:15Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Categories for QQ, CC, RR and friends",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8576",
    "user": "nthiery"
}
```
Assignee: AlexGhitza

CC:  sage-combinat

Keywords: categories, real fields

After this patch, QQ,ZZ,... inherit properly from categories: 


```
sage: QQ.category()
Category of fields
sage: TestSuite(QQ).run()
```


This patch also documents the following effect discovered by TestSuite:

```
    sage: CDF = ComplexDoubleField()
    sage: x = CDF.an_element()
    sage: x
    1.0*I
    sage: x*x, x**2, x*x == x**2
    (-1.0, -1.0 + 1.22460635382e-16*I, False)
```

This effect won't be touched by this patch. Should anyone consider this as a bug, please open a new ticket.

Issue created by migration from https://trac.sagemath.org/ticket/8576





---

archive/issue_comments_077680.json:
```json
{
    "body": "Attachment [trac_8576-category-QQ-RR-CC-nt.patch](tarball://root/attachments/some-uuid/ticket8576/trac_8576-category-QQ-RR-CC-nt.patch) by nthiery created at 2010-03-22 22:25:55\n\nAll test passed for me.",
    "created_at": "2010-03-22T22:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77680",
    "user": "nthiery"
}
```

Attachment [trac_8576-category-QQ-RR-CC-nt.patch](tarball://root/attachments/some-uuid/ticket8576/trac_8576-category-QQ-RR-CC-nt.patch) by nthiery created at 2010-03-22 22:25:55

All test passed for me.



---

archive/issue_comments_077681.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-22T22:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77681",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077682.json:
```json
{
    "body": "Applies fine to 4.3.5 and all tests pass.",
    "created_at": "2010-04-05T14:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77682",
    "user": "cremona"
}
```

Applies fine to 4.3.5 and all tests pass.



---

archive/issue_comments_077683.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T14:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77683",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077684.json:
```json
{
    "body": "Thanks for the review!",
    "created_at": "2010-04-06T05:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77684",
    "user": "nthiery"
}
```

Thanks for the review!



---

archive/issue_comments_077685.json:
```json
{
    "body": "Merged \"trac_8576-category-QQ-RR-CC-nt.patch\" in 4.4.alpha0",
    "created_at": "2010-04-16T18:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77685",
    "user": "jhpalmieri"
}
```

Merged "trac_8576-category-QQ-RR-CC-nt.patch" in 4.4.alpha0



---

archive/issue_comments_077686.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8576#issuecomment-77686",
    "user": "jhpalmieri"
}
```

Resolution: fixed
