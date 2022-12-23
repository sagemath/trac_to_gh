# Issue 8865: FractionFieldElement.__call__ doesn't handle keyword arguments

archive/issues_008865.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: FractionField, subs\n\nPolynomialRing elements allow keyword arguments when substitute values for the variables (via !__call!__), but the corresponding method in FractionFieldElement doesn't handle keyword arguments properly.\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: x = PolynomialRing(RationalField(),'x',3).gens()\nsage: f = x[0] + x[1] - 2*x[1]*x[2]\nsage: h = f /(x[1] + x[2])\nsage: h\n(-2*x1*x2 + x0 + x1)/(x1 + x2)\nsage: h(1,2,5)\n-17/7\nsage: h(x0=1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 4.4, Release Date: 2010-04-24                         |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mguaypaq/sage/<ipython console> in <module>()\n\nTypeError: __call__() got an unexpected keyword argument 'x0'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8865\n\n",
    "created_at": "2010-05-03T22:35:47Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "FractionFieldElement.__call__ doesn't handle keyword arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8865",
    "user": "mguaypaq"
}
```
Assignee: AlexGhitza

Keywords: FractionField, subs

PolynomialRing elements allow keyword arguments when substitute values for the variables (via !__call!__), but the corresponding method in FractionFieldElement doesn't handle keyword arguments properly.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x = PolynomialRing(RationalField(),'x',3).gens()
sage: f = x[0] + x[1] - 2*x[1]*x[2]
sage: h = f /(x[1] + x[2])
sage: h
(-2*x1*x2 + x0 + x1)/(x1 + x2)
sage: h(1,2,5)
-17/7
sage: h(x0=1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
/home/mguaypaq/sage/<ipython console> in <module>()

TypeError: __call__() got an unexpected keyword argument 'x0'
```


Issue created by migration from https://trac.sagemath.org/ticket/8865





---

archive/issue_comments_081468.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-04T12:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8865#issuecomment-81468",
    "user": "mguaypaq"
}
```

Attachment



---

archive/issue_comments_081469.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-04T12:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8865#issuecomment-81469",
    "user": "mguaypaq"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-04T14:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8865#issuecomment-81470",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081471.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-04T14:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8865#issuecomment-81471",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_081472.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8865#issuecomment-81472",
    "user": "mvngu"
}
```

Resolution: fixed
