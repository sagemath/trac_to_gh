# Issue 8673: No KeyErrror raised when it should for FiniteWord_callable

archive/issues_008673.json:
```json
{
    "body": "Assignee: slabbe\n\nCC:  abmasse\n\n\n```\nLe 10-02-23, Paul Zimmermann a \u00e9crit :\n\nsage: def f(n):\n   return n^2\n\nsage: w = Word(f,length=23)\n\nsage: w[24]\n576\n\nPaul\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8673\n\n",
    "created_at": "2010-04-11T14:00:57Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "No KeyErrror raised when it should for FiniteWord_callable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8673",
    "user": "slabbe"
}
```
Assignee: slabbe

CC:  abmasse


```
Le 10-02-23, Paul Zimmermann a écrit :

sage: def f(n):
   return n^2

sage: w = Word(f,length=23)

sage: w[24]
576

Paul
```


Issue created by migration from https://trac.sagemath.org/ticket/8673





---

archive/issue_comments_078928.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-02-18T19:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78928",
    "user": "slabbe"
}
```

Attachment



---

archive/issue_comments_078929.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-18T19:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78929",
    "user": "slabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078930.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-18T20:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78930",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078931.json:
```json
{
    "body": "Pretty straight-forward. All tests pass! Positive review.",
    "created_at": "2011-02-18T20:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78931",
    "user": "abmasse"
}
```

Pretty straight-forward. All tests pass! Positive review.



---

archive/issue_comments_078932.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-25T12:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8673",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8673#issuecomment-78932",
    "user": "jdemeyer"
}
```

Resolution: fixed
