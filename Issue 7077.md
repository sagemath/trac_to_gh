# Issue 7077: variables() inconsistently returns a list or tuple

archive/issues_007077.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mhansen\n\nwith 4.1.1:\n\n\n```\nsage: x,y,z=polygens(QQ,'x,y,z')\nsage: (x^2).variables()\n[x]\nsage: x=polygen(QQ)\nsage: (x^2).variables()\n(x,)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7077\n\n",
    "created_at": "2009-09-29T19:51:09Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "variables() inconsistently returns a list or tuple",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7077",
    "user": "jason"
}
```
Assignee: tbd

CC:  mhansen

with 4.1.1:


```
sage: x,y,z=polygens(QQ,'x,y,z')
sage: (x^2).variables()
[x]
sage: x=polygen(QQ)
sage: (x^2).variables()
(x,)
```


Issue created by migration from https://trac.sagemath.org/ticket/7077





---

archive/issue_comments_058521.json:
```json
{
    "body": "Attachment [trac_7077.patch](tarball://root/attachments/some-uuid/ticket7077/trac_7077.patch) by AlexGhitza created at 2009-10-19 23:38:29\n\nThere are a number of methods called `variables()` in the Sage library.  The attached patch makes sure that all of them return tuples.  (This is what univariate polynomials, and symbolics return.)",
    "created_at": "2009-10-19T23:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7077#issuecomment-58521",
    "user": "AlexGhitza"
}
```

Attachment [trac_7077.patch](tarball://root/attachments/some-uuid/ticket7077/trac_7077.patch) by AlexGhitza created at 2009-10-19 23:38:29

There are a number of methods called `variables()` in the Sage library.  The attached patch makes sure that all of them return tuples.  (This is what univariate polynomials, and symbolics return.)



---

archive/issue_comments_058522.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T23:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7077#issuecomment-58522",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058523.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-20T06:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7077#issuecomment-58523",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058524.json:
```json
{
    "body": "Seems to perform as advertised, passes relevant tests, as far as I can tell catches all the cases.  Positive review.",
    "created_at": "2009-10-20T06:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7077#issuecomment-58524",
    "user": "kcrisman"
}
```

Seems to perform as advertised, passes relevant tests, as far as I can tell catches all the cases.  Positive review.



---

archive/issue_comments_058525.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T04:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7077",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7077#issuecomment-58525",
    "user": "mhansen"
}
```

Resolution: fixed
