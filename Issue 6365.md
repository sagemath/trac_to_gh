# Issue 6365: bug in constructing extensions of finite fields

archive/issues_006365.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: F = GF(2)\nsage: P.<x> = F[]\nsage: f = 1+x+x^4\nsage: K.<a> = F.extension(f)\nTraceback (most recent call last):\n...\nValueError: variable names must be alphanumeric, but one is '('a' which is not.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6365\n\n",
    "created_at": "2009-06-20T15:00:13Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in constructing extensions of finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6365",
    "user": "@williamstein"
}
```
Assignee: somebody


```
sage: F = GF(2)
sage: P.<x> = F[]
sage: f = 1+x+x^4
sage: K.<a> = F.extension(f)
Traceback (most recent call last):
...
ValueError: variable names must be alphanumeric, but one is '('a' which is not.
```


Issue created by migration from https://trac.sagemath.org/ticket/6365





---

archive/issue_comments_050922.json:
```json
{
    "body": "This is no longer a problem:\n\n\n```\n\nsage: F = GF(2)\nsage: P.<x> = F[]\nsage: f = 1+x+x^4\nsage: K.<a> = F.extension(f)\nsage: K\nUnivariate Quotient Polynomial Ring in a over Finite Field of size 2 with modulus a^4 + a + 1\n\n```\n",
    "created_at": "2012-03-19T17:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6365#issuecomment-50922",
    "user": "@jbalakrishnan"
}
```

This is no longer a problem:


```

sage: F = GF(2)
sage: P.<x> = F[]
sage: f = 1+x+x^4
sage: K.<a> = F.extension(f)
sage: K
Univariate Quotient Polynomial Ring in a over Finite Field of size 2 with modulus a^4 + a + 1

```




---

archive/issue_comments_050923.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-19T17:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6365#issuecomment-50923",
    "user": "@jbalakrishnan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050924.json:
```json
{
    "body": "Changing keywords from \"\" to \"rd2\".",
    "created_at": "2012-03-19T17:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6365#issuecomment-50924",
    "user": "@jbalakrishnan"
}
```

Changing keywords from "" to "rd2".



---

archive/issue_comments_050925.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-19T17:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6365#issuecomment-50925",
    "user": "@jbalakrishnan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050926.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-03-21T11:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6365",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6365#issuecomment-50926",
    "user": "@jdemeyer"
}
```

Resolution: worksforme
