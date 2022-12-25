# Issue 7951: coercion problem with 0 variable polynomials

archive/issues_007951.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @malb\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: P = PolynomialRing(QQ,0,'')\nsage: P\nMultivariate Polynomial Ring in no variables over Rational Field\nsage: t = P.random_element()\nsage: t\n-1\nsage: t*x\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/burcin/.sage/temp/karr/24426/_home_burcin__sage_init_sage_0.py in <module>()\n\n/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10153)()\n\n/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6988)()\n\nTypeError: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in no variables over Rational Field' and 'Multivariate Polynomial Ring in x, y over Rational Field'\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7951\n\n",
    "created_at": "2010-01-16T17:56:27Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "coercion problem with 0 variable polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7951",
    "user": "https://github.com/burcin"
}
```
Assignee: @aghitza

CC:  @malb


```
sage: R.<x,y> = QQ[]
sage: P = PolynomialRing(QQ,0,'')
sage: P
Multivariate Polynomial Ring in no variables over Rational Field
sage: t = P.random_element()
sage: t
-1
sage: t*x
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/burcin/.sage/temp/karr/24426/_home_burcin__sage_init_sage_0.py in <module>()

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10153)()

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6988)()

TypeError: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in no variables over Rational Field' and 'Multivariate Polynomial Ring in x, y over Rational Field'


Issue created by migration from https://trac.sagemath.org/ticket/7951





---

archive/issue_comments_069258.json:
```json
{
    "body": "Attachment [trac_7951-zero_variable_poly_coercion.patch](tarball://root/attachments/some-uuid/ticket7951/trac_7951-zero_variable_poly_coercion.patch) by @burcin created at 2010-01-17 22:50:27",
    "created_at": "2010-01-17T22:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69258",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7951-zero_variable_poly_coercion.patch](tarball://root/attachments/some-uuid/ticket7951/trac_7951-zero_variable_poly_coercion.patch) by @burcin created at 2010-01-17 22:50:27



---

archive/issue_comments_069259.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T22:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69259",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069260.json:
```json
{
    "body": "Here is the cause:\n\n\n```\nsage: P = PolynomialRing(QQ,0,'')\nsage: P('pi')\npi\nsage: type(P('pi'))\n<type 'sage.symbolic.expression.Expression'>\n```\n\n\nattachment:trac_7951-zero_variable_poly_coercion.patch has the fix.",
    "created_at": "2010-01-17T22:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69260",
    "user": "https://github.com/burcin"
}
```

Here is the cause:


```
sage: P = PolynomialRing(QQ,0,'')
sage: P('pi')
pi
sage: type(P('pi'))
<type 'sage.symbolic.expression.Expression'>
```


attachment:trac_7951-zero_variable_poly_coercion.patch has the fix.



---

archive/issue_comments_069261.json:
```json
{
    "body": "Doesn't apply cleanly to 4.3.1, maybe I don't have a new enough alpha?",
    "created_at": "2010-01-20T09:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69261",
    "user": "https://github.com/robertwb"
}
```

Doesn't apply cleanly to 4.3.1, maybe I don't have a new enough alpha?



---

archive/issue_comments_069262.json:
```json
{
    "body": "But the code looks good.",
    "created_at": "2010-01-20T09:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69262",
    "user": "https://github.com/robertwb"
}
```

But the code looks good.



---

archive/issue_comments_069263.json:
```json
{
    "body": "It applies without problems to 4.3.1.rc1 for me.",
    "created_at": "2010-01-20T20:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69263",
    "user": "https://github.com/burcin"
}
```

It applies without problems to 4.3.1.rc1 for me.



---

archive/issue_comments_069264.json:
```json
{
    "body": "Applies cleanly for me on 4.3.1, passes tests, looks good.",
    "created_at": "2010-01-23T00:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69264",
    "user": "https://github.com/aghitza"
}
```

Applies cleanly for me on 4.3.1, passes tests, looks good.



---

archive/issue_comments_069265.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T00:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69265",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069266.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T06:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7951#issuecomment-69266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008167.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-01-23T06:37:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7951",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7951#event-8167"
}
```
