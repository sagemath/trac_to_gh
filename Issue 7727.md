# Issue 7727: optimized_representation fails,

archive/issues_007727.json:
```json
{
    "body": "Assignee: davidloeffler\n\nThe following code fails with cryptid PariError:\n\n```\nsage: L.<a>=NumberField(x^3+2/3*x+3)\nsage: L.optimized_representation()\n```\n\n\nThe exact failure happens on the command f.polred(2), but I'm not sure what's wrong with it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7727\n\n",
    "created_at": "2009-12-17T20:50:02Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "title": "optimized_representation fails,",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7727",
    "user": "syazdani"
}
```
Assignee: davidloeffler

The following code fails with cryptid PariError:

```
sage: L.<a>=NumberField(x^3+2/3*x+3)
sage: L.optimized_representation()
```


The exact failure happens on the command f.polred(2), but I'm not sure what's wrong with it.

Issue created by migration from https://trac.sagemath.org/ticket/7727





---

archive/issue_comments_066389.json:
```json
{
    "body": "This is related to #252",
    "created_at": "2013-08-20T13:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7727#issuecomment-66389",
    "user": "chapoton"
}
```

This is related to #252



---

archive/issue_comments_066390.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-03-23T08:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7727#issuecomment-66390",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066391.json:
```json
{
    "body": "Fixed in #252, which also adds a similar test.",
    "created_at": "2018-03-23T08:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7727#issuecomment-66391",
    "user": "mmezzarobba"
}
```

Fixed in #252, which also adds a similar test.



---

archive/issue_comments_066392.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-03-23T08:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7727#issuecomment-66392",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066393.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7727#issuecomment-66393",
    "user": "vdelecroix"
}
```

closing positively reviewed duplicates



---

archive/issue_comments_066394.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7727",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7727#issuecomment-66394",
    "user": "vdelecroix"
}
```

Resolution: wontfix
