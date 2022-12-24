# Issue 7347: numerical_integral(SR(0), 0, 1) gives an error

archive/issues_007347.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @jasongrout @kcrisman\n\n\n```\nsage: numerical_integral(SR(0), 0, 1)\nTraceback (most recent call last):\n...\nValueError: Integrand has wrong number of parameters\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7347\n\n",
    "created_at": "2009-10-29T07:12:05Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "numerical_integral(SR(0), 0, 1) gives an error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7347",
    "user": "@jasongrout"
}
```
Assignee: jkantor

CC:  @jasongrout @kcrisman


```
sage: numerical_integral(SR(0), 0, 1)
Traceback (most recent call last):
...
ValueError: Integrand has wrong number of parameters
```


Issue created by migration from https://trac.sagemath.org/ticket/7347





---

archive/issue_comments_061568.json:
```json
{
    "body": "See #10088, a duplicate, which has a patch attached.",
    "created_at": "2011-02-19T10:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61568",
    "user": "dsm"
}
```

See #10088, a duplicate, which has a patch attached.



---

archive/issue_comments_061569.json:
```json
{
    "body": "And #10088 was merged quite some time ago. \n\n```\nsage: numerical_integral(SR(0), 0, 1)\n(0.0, 0.0)\n```\n\nYup, works.",
    "created_at": "2011-08-19T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61569",
    "user": "@kcrisman"
}
```

And #10088 was merged quite some time ago. 

```
sage: numerical_integral(SR(0), 0, 1)
(0.0, 0.0)
```

Yup, works.



---

archive/issue_comments_061570.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-19T13:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61570",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061571.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-19T13:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61571",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061572.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-22T08:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61572",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
