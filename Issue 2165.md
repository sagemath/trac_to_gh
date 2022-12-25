# Issue 2165: MPolynomialRing(BooleanPolynomial) not as general as it should be

archive/issues_002165.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: polybori boolean polynomial coercion call\n\nCoercion of BooleanPolynomials in subsets of variables should be allowed.\n\nSee #2055 with reference to the following IRC snippet:\n\n\n```\nncalexan: malb: in 2055, is this right?\n[3:26pm] ncalexan: if PY_TYPE_CHECK(element, BooleanPolynomial) and \\\n[3:26pm] ncalexan:  578              element.parent().ngens() == _ring.N and \\\n[3:26pm] ncalexan:  579              element.parent().variable_names() == self.variable_names():\n[3:26pm] ncalexan: This is in a __call__, right?\n[3:26pm] ncalexan: Shouldn't the variable names just be a subset?\n[3:26pm] ncalexan: And then, even just the names in the polynomial?\n[3:26pm] malb: it could be that general, yes\n[3:26pm] ncalexan: eg, sage: QQ['x'](QQ['x', 'y'].0)\n[3:26pm] ncalexan: x\n[3:26pm] ncalexan: sage: QQ['y', 'x'](QQ['x', 'y'].0)\n[3:26pm] ncalexan: x\n[3:27pm] ncalexan: It's inconsistent if not.  Other than that, I say apply.\n[3:27pm] ncalexan: Hopefully it's easy to tell what vars actually appear in any partic. poly.\n[3:27pm] malb: to be honest, I'd like to have it applied and open another ticket for that\n[3:28pm] malb: because you definitely want to solve equations in MPolys with PolyBoRi\n[3:28pm] malb: and your rings will be identical except for the implementation\n[3:28pm] ncalexan: mabshoff: is that okay with you?  Apply and another ticket for additional generality?\n[3:28pm] mabshoff: Sure\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2165\n\n",
    "created_at": "2008-02-14T23:35:39Z",
    "labels": [
        "component: commutative algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "MPolynomialRing(BooleanPolynomial) not as general as it should be",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2165",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

Keywords: polybori boolean polynomial coercion call

Coercion of BooleanPolynomials in subsets of variables should be allowed.

See #2055 with reference to the following IRC snippet:


```
ncalexan: malb: in 2055, is this right?
[3:26pm] ncalexan: if PY_TYPE_CHECK(element, BooleanPolynomial) and \
[3:26pm] ncalexan:  578              element.parent().ngens() == _ring.N and \
[3:26pm] ncalexan:  579              element.parent().variable_names() == self.variable_names():
[3:26pm] ncalexan: This is in a __call__, right?
[3:26pm] ncalexan: Shouldn't the variable names just be a subset?
[3:26pm] ncalexan: And then, even just the names in the polynomial?
[3:26pm] malb: it could be that general, yes
[3:26pm] ncalexan: eg, sage: QQ['x'](QQ['x', 'y'].0)
[3:26pm] ncalexan: x
[3:26pm] ncalexan: sage: QQ['y', 'x'](QQ['x', 'y'].0)
[3:26pm] ncalexan: x
[3:27pm] ncalexan: It's inconsistent if not.  Other than that, I say apply.
[3:27pm] ncalexan: Hopefully it's easy to tell what vars actually appear in any partic. poly.
[3:27pm] malb: to be honest, I'd like to have it applied and open another ticket for that
[3:28pm] malb: because you definitely want to solve equations in MPolys with PolyBoRi
[3:28pm] malb: and your rings will be identical except for the implementation
[3:28pm] ncalexan: mabshoff: is that okay with you?  Apply and another ticket for additional generality?
[3:28pm] mabshoff: Sure
```


Issue created by migration from https://trac.sagemath.org/ticket/2165





---

archive/issue_comments_014189.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-20T15:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2165#issuecomment-14189",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_events_005177.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5177"
}
```



---

archive/issue_events_005178.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5178"
}
```



---

archive/issue_events_005179.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5179"
}
```



---

archive/issue_events_005180.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5180"
}
```



---

archive/issue_events_005181.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5181"
}
```



---

archive/issue_events_005182.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5182"
}
```



---

archive/issue_events_005183.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2165",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2165#event-5183"
}
```
