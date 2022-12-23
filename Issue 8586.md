# Issue 8586: Integer overflow in vector_space_dimension()

archive/issues_008586.json:
```json
{
    "body": "Assignee: malb\n\n\n```python\nsage: P.<x> = PolynomialRing(GF(32003),1)\nsage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()\n32003\n\nsage: P.<x,y> = PolynomialRing(GF(32003),2)\nsage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()\n1024192009\n\nsage: P.<x,y,z> = PolynomialRing(GF(32003),3)\nsage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()\n-1973539045 # 2^32 - (32003^3) % 2^32 == 1973539045\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8586\n\n",
    "created_at": "2010-03-23T11:29:29Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "Integer overflow in vector_space_dimension()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8586",
    "user": "malb"
}
```
Assignee: malb


```python
sage: P.<x> = PolynomialRing(GF(32003),1)
sage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()
32003

sage: P.<x,y> = PolynomialRing(GF(32003),2)
sage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()
1024192009

sage: P.<x,y,z> = PolynomialRing(GF(32003),3)
sage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()
-1973539045 # 2^32 - (32003^3) % 2^32 == 1973539045
```


Issue created by migration from https://trac.sagemath.org/ticket/8586





---

archive/issue_comments_077761.json:
```json
{
    "body": "The **Reported upstream** field makes it sound so negative (\"little or no feedback\"), so to clarify: I just now reported this bug upstream at\n\n   http://www.singular.uni-kl.de:8002/trac/ticket/218",
    "created_at": "2010-03-23T11:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77761",
    "user": "malb"
}
```

The **Reported upstream** field makes it sound so negative ("little or no feedback"), so to clarify: I just now reported this bug upstream at

   http://www.singular.uni-kl.de:8002/trac/ticket/218



---

archive/issue_comments_077762.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-27T19:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77762",
    "user": "@kliem"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077763.json:
```json
{
    "body": "With #29746 I would vote to close this ticket.\n\nThe bug is reported upstream, we have documented it. There is already a ticket for it on the singular trac.",
    "created_at": "2020-05-27T19:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77763",
    "user": "@kliem"
}
```

With #29746 I would vote to close this ticket.

The bug is reported upstream, we have documented it. There is already a ticket for it on the singular trac.



---

archive/issue_comments_077764.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd109\".",
    "created_at": "2020-05-27T19:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77764",
    "user": "@kliem"
}
```

Changing keywords from "" to "sd109".



---

archive/issue_comments_077765.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-09-18T09:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77765",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077766.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-18T17:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77766",
    "user": "mkoeppe"
}
```

Resolution: invalid
