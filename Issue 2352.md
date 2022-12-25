# Issue 2352: univariate homogenize is not the same as multivariate homogenize

archive/issues_002352.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @ncalexan\n\nKeywords: univariate polynomial homogenize\n\nTicket #2349 fixes the multivariate case.  This ticket is for the univariate case.  Some examples (these work after like this AFTER #2349 has been applied):\n\n\n```\nsage: x = Zmod(3)['x'].0; (x^2 + x).homogenize()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'\nsage: x = PolynomialRing(Zmod(3), 1, 'x').0; (x^2 + x).homogenize()\nx^2 + x*h\nsage: x = GF(3)['x'].0; (x^2 + x).homogenize()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'\nsage: x = PolynomialRing(GF(3), 1, 'x').0; (x^2 + x).homogenize()\nx^2 + x*h\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2352\n\n",
    "created_at": "2008-02-29T08:24:09Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "univariate homogenize is not the same as multivariate homogenize",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2352",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

CC:  @ncalexan

Keywords: univariate polynomial homogenize

Ticket #2349 fixes the multivariate case.  This ticket is for the univariate case.  Some examples (these work after like this AFTER #2349 has been applied):


```
sage: x = Zmod(3)['x'].0; (x^2 + x).homogenize()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'
sage: x = PolynomialRing(Zmod(3), 1, 'x').0; (x^2 + x).homogenize()
x^2 + x*h
sage: x = GF(3)['x'].0; (x^2 + x).homogenize()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute 'homogenize'
sage: x = PolynomialRing(GF(3), 1, 'x').0; (x^2 + x).homogenize()
x^2 + x*h
```


Issue created by migration from https://trac.sagemath.org/ticket/2352





---

archive/issue_comments_015773.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15773",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015774.json:
```json
{
    "body": "One step more to unify some methods of univariate and multivariate polynomials.\n----\nNew commits:",
    "created_at": "2014-07-24T14:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15774",
    "user": "https://github.com/lftabera"
}
```

One step more to unify some methods of univariate and multivariate polynomials.
----
New commits:



---

archive/issue_comments_015775.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-24T14:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15775",
    "user": "https://github.com/lftabera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_015776.json:
```json
{
    "body": "Should `(1+t).homogenize('t')` really be zero? The docstring says that setting this variable to one yields the original polynomial which does not seem to be the case. So should we clarify (also in the multivariate case) that strange things may happen if `var` is a variable which appears in the polynomial?",
    "created_at": "2014-07-28T22:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15776",
    "user": "https://github.com/saraedum"
}
```

Should `(1+t).homogenize('t')` really be zero? The docstring says that setting this variable to one yields the original polynomial which does not seem to be the case. So should we clarify (also in the multivariate case) that strange things may happen if `var` is a variable which appears in the polynomial?



---

archive/issue_comments_015777.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-07-28T22:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15777",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_015778.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-07-28T23:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15778",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_015779.json:
```json
{
    "body": "I tried to clarify the behaviour in the docstrings. I hope you do not mind my changes.\n----\nNew commits:",
    "created_at": "2014-07-28T23:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15779",
    "user": "https://github.com/saraedum"
}
```

I tried to clarify the behaviour in the docstrings. I hope you do not mind my changes.
----
New commits:



---

archive/issue_comments_015780.json:
```json
{
    "body": "Thanks, the documentation has improved, much clearer now.",
    "created_at": "2014-07-29T09:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15780",
    "user": "https://github.com/lftabera"
}
```

Thanks, the documentation has improved, much clearer now.



---

archive/issue_comments_015781.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-29T09:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15781",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_002529.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-07-29T21:39:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2352#event-2529"
}
```



---

archive/issue_comments_015782.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-07-29T21:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2352#issuecomment-15782",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
