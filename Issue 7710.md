# Issue 7710: documentation of rational_reconstruction incoherent with code

archive/issues_007710.json:
```json
{
    "body": "Assignee: @aghitza\n\nThe documentation of rational_reconstruction says that an error\n*ZeroDivisionError* is raised when no solution exists with the given\nbounds, but the code returns an error *ValueError*.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7710\n\n",
    "created_at": "2009-12-16T11:59:05Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "documentation of rational_reconstruction incoherent with code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7710",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

The documentation of rational_reconstruction says that an error
*ZeroDivisionError* is raised when no solution exists with the given
bounds, but the code returns an error *ValueError*.

Issue created by migration from https://trac.sagemath.org/ticket/7710





---

archive/issue_comments_066066.json:
```json
{
    "body": "Still there in 4.3.1:\n\n```\nsage: rational_reconstruction?\n...\n\n        exists, that pair is unique and this function returns it. If no\n        such pair exists, this function raises ZeroDivisionError.\n```\n\nand:\n\n```\nsage: rational_reconstruction(29,105)\n...\nValueError: Rational reconstruction of 29 (mod 105) does not exist.\n```\n\n\nNote also that in 4.3.1 a.rational_reconstruction? gives a different documentation, which does\nnot mention what happens in case of error. Why are the documentations different?",
    "created_at": "2010-02-05T20:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7710#issuecomment-66066",
    "user": "https://github.com/zimmermann6"
}
```

Still there in 4.3.1:

```
sage: rational_reconstruction?
...

        exists, that pair is unique and this function returns it. If no
        such pair exists, this function raises ZeroDivisionError.
```

and:

```
sage: rational_reconstruction(29,105)
...
ValueError: Rational reconstruction of 29 (mod 105) does not exist.
```


Note also that in 4.3.1 a.rational_reconstruction? gives a different documentation, which does
not mention what happens in case of error. Why are the documentations different?



---

archive/issue_comments_066067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-10-20T19:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7710#issuecomment-66067",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066068.json:
```json
{
    "body": "Fixed by #17180.",
    "created_at": "2014-10-20T19:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7710#issuecomment-66068",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by #17180.



---

archive/issue_comments_066069.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-10-20T19:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7710#issuecomment-66069",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066070.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-10-27T16:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7710",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7710#issuecomment-66070",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
