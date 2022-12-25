# Issue 7347: numerical_integral(SR(0), 0, 1) gives an error

archive/issues_007347.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @jasongrout @kcrisman\n\n\n```\nsage: numerical_integral(SR(0), 0, 1)\nTraceback (most recent call last):\n...\nValueError: Integrand has wrong number of parameters\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7347\n\n",
    "created_at": "2009-10-29T07:12:05Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "numerical_integral(SR(0), 0, 1) gives an error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7347",
    "user": "https://github.com/jasongrout"
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

archive/issue_comments_061455.json:
```json
{
    "body": "See #10088, a duplicate, which has a patch attached.",
    "created_at": "2011-02-19T10:03:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61455",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

See #10088, a duplicate, which has a patch attached.



---

archive/issue_events_017389.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2011-08-19T13:58:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7347#event-17389"
}
```



---

archive/issue_comments_061456.json:
```json
{
    "body": "And #10088 was merged quite some time ago. \n\n```\nsage: numerical_integral(SR(0), 0, 1)\n(0.0, 0.0)\n```\n\nYup, works.",
    "created_at": "2011-08-19T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61456",
    "user": "https://github.com/kcrisman"
}
```

And #10088 was merged quite some time ago. 

```
sage: numerical_integral(SR(0), 0, 1)
(0.0, 0.0)
```

Yup, works.



---

archive/issue_comments_061457.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-19T13:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61457",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061458.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-19T13:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61458",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017390.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-08-22T08:09:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7347#event-17390"
}
```



---

archive/issue_comments_061459.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-22T08:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7347#issuecomment-61459",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
