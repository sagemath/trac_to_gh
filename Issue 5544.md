# Issue 5544: multipolynomial __call__ not consistant

archive/issues_005544.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage: parent(RR['x,y'].gen(1)(0,CC.0))\nComplex Field with 53 bits of precision\nsage: parent(RR['x,y'](0)(0,0))\nInteger Ring\nsage: parent(RR['x,y'](0)(0,CC.0))\nInteger Ring\nsage: parent(RR['x,y'](1)(0,CC.0))\nReal Field with 53 bits of precision\n\nsage: parent(QQ['x,y'](1)(0,CC.0))\nRational Field\nsage: parent(QQ['x,y'](0)(0,0))\nRational Field\nsage: parent(QQ['x,y'](0)(0,CC.0))\nRational Field\nsage: parent(QQ['x,y'].gen(1)(0,CC.0))\nComplex Field with 53 bits of precision\n```\n\n\nThe result should not depend on the specific polynomial, only on its parent and the parent of the inputs. \n\nUnivariate ones get it right:\n\n\n```\nsage: sage: parent(RR['x'](0)(0))\nReal Field with 53 bits of precision\nsage: sage: parent(RR['x'](0)(CC.0))\nComplex Field with 53 bits of precision\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5544\n\n",
    "created_at": "2009-03-17T06:21:40Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "multipolynomial __call__ not consistant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5544",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd


```
sage: parent(RR['x,y'].gen(1)(0,CC.0))
Complex Field with 53 bits of precision
sage: parent(RR['x,y'](0)(0,0))
Integer Ring
sage: parent(RR['x,y'](0)(0,CC.0))
Integer Ring
sage: parent(RR['x,y'](1)(0,CC.0))
Real Field with 53 bits of precision

sage: parent(QQ['x,y'](1)(0,CC.0))
Rational Field
sage: parent(QQ['x,y'](0)(0,0))
Rational Field
sage: parent(QQ['x,y'](0)(0,CC.0))
Rational Field
sage: parent(QQ['x,y'].gen(1)(0,CC.0))
Complex Field with 53 bits of precision
```


The result should not depend on the specific polynomial, only on its parent and the parent of the inputs. 

Univariate ones get it right:


```
sage: sage: parent(RR['x'](0)(0))
Real Field with 53 bits of precision
sage: sage: parent(RR['x'](0)(CC.0))
Complex Field with 53 bits of precision
```


Issue created by migration from https://trac.sagemath.org/ticket/5544





---

archive/issue_comments_043050.json:
```json
{
    "body": "According to this definition, there are bugs in univariate polynomials as well:\n\n```\nsage: parent(QQ['x'](0)(1))\nInteger Ring\nsage: parent(QQ['x'].gen(0)(1))\nRational Field\n```\n",
    "created_at": "2009-03-17T06:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5544#issuecomment-43050",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

According to this definition, there are bugs in univariate polynomials as well:

```
sage: parent(QQ['x'](0)(1))
Integer Ring
sage: parent(QQ['x'].gen(0)(1))
Rational Field
```




---

archive/issue_events_013009.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13009"
}
```



---

archive/issue_events_013010.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13010"
}
```



---

archive/issue_events_013011.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13011"
}
```



---

archive/issue_events_013012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13012"
}
```



---

archive/issue_events_013013.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13013"
}
```



---

archive/issue_events_013014.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13014"
}
```



---

archive/issue_events_013015.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5544",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5544#event-13015"
}
```
