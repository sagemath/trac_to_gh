# Issue 8554: Failed RealNumber conversion from str in base 16.

archive/issues_008554.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  jason\n\nKeywords: hexadecimal, string conversion\n\n\n```\nsage: RealNumber(\"1ffef\", base=16)  \n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/opt/sage-4.3.3/<ipython console> in <module>()\n\n/opt/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:25128)()\n\nValueError: invalid literal for int() with base 10: 'f'\n```\n\n\nThe problem arises because 'e' is incorrectly parsed as the mantissa/exponent delimiter. If Sage wants to follow MPFR in this regard, '`@`' should be used as a delimiter for base > 10.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8554\n\n",
    "created_at": "2010-03-17T20:04:11Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Failed RealNumber conversion from str in base 16.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8554",
    "user": "lfousse"
}
```
Assignee: jkantor

CC:  jason

Keywords: hexadecimal, string conversion


```
sage: RealNumber("1ffef", base=16)  
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/opt/sage-4.3.3/<ipython console> in <module>()

/opt/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.create_RealNumber (sage/rings/real_mpfr.c:25128)()

ValueError: invalid literal for int() with base 10: 'f'
```


The problem arises because 'e' is incorrectly parsed as the mantissa/exponent delimiter. If Sage wants to follow MPFR in this regard, '`@`' should be used as a delimiter for base > 10.

Issue created by migration from https://trac.sagemath.org/ticket/8554





---

archive/issue_comments_077397.json:
```json
{
    "body": "See #14702.",
    "created_at": "2014-02-02T11:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8554#issuecomment-77397",
    "user": "mmezzarobba"
}
```

See #14702.



---

archive/issue_comments_077398.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-02T11:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8554#issuecomment-77398",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077399.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-09T20:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8554#issuecomment-77399",
    "user": "aapitzsch"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077400.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-11T21:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8554#issuecomment-77400",
    "user": "vbraun"
}
```

Resolution: fixed
