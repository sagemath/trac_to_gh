# Issue 7150: Wrong substitution implementation for fraction fields

archive/issues_007150.json:
```json
{
    "body": "CC:  @williamstein\n\nI am getting this in 4.1.1 and find it really frustrating (especially since it took me several hours to catch):\n\n\n\n```\nsage: QQ[\"x\", \"y\"].inject_variables()\nDefining x, y\nsage: e1 = x^2*y^3 - x^2*y - x*y\nsage: e2 = e1.parent().fraction_field()(e1)\nsage: print e2\nx^2*y^3 - x^2*y - x*y\nsage: print e2.subs(y=SR(\"s\"))\nx^2*s^3 - (x^2 - x)*s\n```\n\nThe last line is wrong!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7150\n\n",
    "created_at": "2009-10-08T04:40:11Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Wrong substitution implementation for fraction fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7150",
    "user": "https://github.com/novoselt"
}
```
CC:  @williamstein

I am getting this in 4.1.1 and find it really frustrating (especially since it took me several hours to catch):



```
sage: QQ["x", "y"].inject_variables()
Defining x, y
sage: e1 = x^2*y^3 - x^2*y - x*y
sage: e2 = e1.parent().fraction_field()(e1)
sage: print e2
x^2*y^3 - x^2*y - x*y
sage: print e2.subs(y=SR("s"))
x^2*s^3 - (x^2 - x)*s
```

The last line is wrong!

Issue created by migration from https://trac.sagemath.org/ticket/7150





---

archive/issue_comments_059129.json:
```json
{
    "body": "But in 4.1.2.rc0:\n\n```\nsage: QQ[\"x\", \"y\"].inject_variables()\nDefining x, y\nsage: e1 = x^2*y^3 - x^2*y - x*y\nsage: e2 = e1.parent().fraction_field()(e1)\nsage: print e2\nx^2*y^3 - x^2*y - x*y\nsage: print e2.subs(y=SR(\"s\"))\ns^3*x^2 - s*x^2 - s*x\n```\n\nSo the problem may already have been solved.",
    "created_at": "2009-10-08T07:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7150#issuecomment-59129",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

But in 4.1.2.rc0:

```
sage: QQ["x", "y"].inject_variables()
Defining x, y
sage: e1 = x^2*y^3 - x^2*y - x*y
sage: e2 = e1.parent().fraction_field()(e1)
sage: print e2
x^2*y^3 - x^2*y - x*y
sage: print e2.subs(y=SR("s"))
s^3*x^2 - s*x^2 - s*x
```

So the problem may already have been solved.



---

archive/issue_comments_059130.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-08T07:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7150#issuecomment-59130",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Changing status from new to needs_review.



---

archive/issue_events_016903.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/fwclarke",
    "created_at": "2009-10-08T07:43:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7150#event-16903"
}
```



---

archive/issue_events_016904.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-10T19:03:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7150#event-16904"
}
```



---

archive/issue_comments_059131.json:
```json
{
    "body": "This may need to be closed with 4.1.2.",
    "created_at": "2009-10-14T21:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7150#issuecomment-59131",
    "user": "https://github.com/jasongrout"
}
```

This may need to be closed with 4.1.2.



---

archive/issue_comments_059132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-16T05:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7150#issuecomment-59132",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_059133.json:
```json
{
    "body": "Yep, I think we can close this.",
    "created_at": "2009-10-16T05:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7150#issuecomment-59133",
    "user": "https://github.com/mwhansen"
}
```

Yep, I think we can close this.



---

archive/issue_events_016905.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-16T05:00:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7150#event-16905"
}
```



---

archive/issue_events_016906.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-16T05:00:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7150",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7150#event-16906"
}
```
