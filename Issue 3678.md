# Issue 3678: Fractional powers for polynomial variables bug

archive/issues_003678.json:
```json
{
    "body": "Assignee: tbd\n\nThis was reported by Andrey Novoseltsev:\n\n\n```\nsage: pr = PolynomialRing(QQ, \"u,v\")\nsage: pr.injvar()\nDefining u, v\nsage: u^(1/2)\n1\nsage: pr = PolynomialRing(QQ, \"w\")\nsage: pr.injvar()\nDefining w\nsage: w^(1/2)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call\nlast)\n\n/home/novoselt/<ipython console> in <module>()\n\n/home/novoselt/polynomial_element.pyx in\nsage.rings.polynomial.polynomial_element.Polynomial.__pow__ (sage/\nrings/polynomial/polynomial_element.c:8179)()\n\n/home/novoselt/element.pyx in\nsage.structure.element.RingElement.__mul__ (sage/structure/element.c:\n8814)()\n\n/home/novoselt/coerce.pyx in\nsage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/\nstructure/coerce.c:5582)()\n\nTypeError: unsupported operand parent(s) for '*': '<type 'list'>' and\n'Rational Field'\nsage: sqrt(w)\nsqrt(w)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3678\n\n",
    "created_at": "2008-07-19T06:00:37Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "Fractional powers for polynomial variables bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3678",
    "user": "wdj"
}
```
Assignee: tbd

This was reported by Andrey Novoseltsev:


```
sage: pr = PolynomialRing(QQ, "u,v")
sage: pr.injvar()
Defining u, v
sage: u^(1/2)
1
sage: pr = PolynomialRing(QQ, "w")
sage: pr.injvar()
Defining w
sage: w^(1/2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call
last)

/home/novoselt/<ipython console> in <module>()

/home/novoselt/polynomial_element.pyx in
sage.rings.polynomial.polynomial_element.Polynomial.__pow__ (sage/
rings/polynomial/polynomial_element.c:8179)()

/home/novoselt/element.pyx in
sage.structure.element.RingElement.__mul__ (sage/structure/element.c:
8814)()

/home/novoselt/coerce.pyx in
sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/
structure/coerce.c:5582)()

TypeError: unsupported operand parent(s) for '*': '<type 'list'>' and
'Rational Field'
sage: sqrt(w)
sqrt(w)
```


Issue created by migration from https://trac.sagemath.org/ticket/3678





---

archive/issue_comments_026045.json:
```json
{
    "body": "The attached patch fixes this by introducing the same type-check as in the univariate polynomial case.",
    "created_at": "2008-12-21T05:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-26045",
    "user": "AlexGhitza"
}
```

The attached patch fixes this by introducing the same type-check as in the univariate polynomial case.



---

archive/issue_comments_026046.json:
```json
{
    "body": "Attachment [trac_3678.patch](tarball://root/attachments/some-uuid/ticket3678/trac_3678.patch) by AlexGhitza created at 2008-12-21 05:29:15",
    "created_at": "2008-12-21T05:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-26046",
    "user": "AlexGhitza"
}
```

Attachment [trac_3678.patch](tarball://root/attachments/some-uuid/ticket3678/trac_3678.patch) by AlexGhitza created at 2008-12-21 05:29:15



---

archive/issue_comments_026047.json:
```json
{
    "body": "Positive review.  Patch applies cleanly to 3.2.2 and tests in sage/rings/polynomial pass.",
    "created_at": "2008-12-21T17:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-26047",
    "user": "cremona"
}
```

Positive review.  Patch applies cleanly to 3.2.2 and tests in sage/rings/polynomial pass.



---

archive/issue_comments_026048.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T22:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-26048",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026049.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T22:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3678#issuecomment-26049",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0
