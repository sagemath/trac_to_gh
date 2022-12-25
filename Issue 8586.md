# Issue 8586: Integer overflow in vector_space_dimension()

archive/issues_008586.json:
```json
{
    "body": "Assignee: @malb\n\n\n```python\nsage: P.<x> = PolynomialRing(GF(32003),1)\nsage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()\n32003\n\nsage: P.<x,y> = PolynomialRing(GF(32003),2)\nsage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()\n1024192009\n\nsage: P.<x,y,z> = PolynomialRing(GF(32003),3)\nsage: sage.rings.ideal.FieldIdeal(P).vector_space_dimension()\n-1973539045 # 2^32 - (32003^3) % 2^32 == 1973539045\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8586\n\n",
    "created_at": "2010-03-23T11:29:29Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Integer overflow in vector_space_dimension()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8586",
    "user": "https://github.com/malb"
}
```
Assignee: @malb


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

archive/issue_comments_077633.json:
```json
{
    "body": "The **Reported upstream** field makes it sound so negative (\"little or no feedback\"), so to clarify: I just now reported this bug upstream at\n\n   http://www.singular.uni-kl.de:8002/trac/ticket/218",
    "created_at": "2010-03-23T11:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77633",
    "user": "https://github.com/malb"
}
```

The **Reported upstream** field makes it sound so negative ("little or no feedback"), so to clarify: I just now reported this bug upstream at

   http://www.singular.uni-kl.de:8002/trac/ticket/218



---

archive/issue_comments_077634.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-05-27T19:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77634",
    "user": "https://github.com/kliem"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077635.json:
```json
{
    "body": "With #29746 I would vote to close this ticket.\n\nThe bug is reported upstream, we have documented it. There is already a ticket for it on the singular trac.",
    "created_at": "2020-05-27T19:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77635",
    "user": "https://github.com/kliem"
}
```

With #29746 I would vote to close this ticket.

The bug is reported upstream, we have documented it. There is already a ticket for it on the singular trac.



---

archive/issue_comments_077636.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd109\".",
    "created_at": "2020-05-27T19:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77636",
    "user": "https://github.com/kliem"
}
```

Changing keywords from "" to "sd109".



---

archive/issue_comments_077637.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-09-18T09:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77637",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008763.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-09-18T17:51:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8586#event-8763"
}
```



---

archive/issue_comments_077638.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-18T17:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8586#issuecomment-77638",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
