# Issue 290: Converting Pari multivariate polynomials  to MPolynomials doesn't work

archive/issues_000290.json:
```json
{
    "body": "Assignee: somebody\n\n```\nQQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))\n<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational\n```\n\n(Reported by cwitty)\n\nIssue created by migration from https://trac.sagemath.org/ticket/290\n\n",
    "created_at": "2007-02-24T05:04:12Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Converting Pari multivariate polynomials  to MPolynomials doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/290",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

```
QQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))
<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational
```

(Reported by cwitty)

Issue created by migration from https://trac.sagemath.org/ticket/290





---

archive/issue_comments_001361.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-02-24T05:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1361",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001362.json:
```json
{
    "body": "Changing assignee from somebody to @malb.",
    "created_at": "2007-02-24T05:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1362",
    "user": "https://github.com/malb"
}
```

Changing assignee from somebody to @malb.



---

archive/issue_events_000656.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-21T10:06:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-656"
}
```



---

archive/issue_comments_001363.json:
```json
{
    "body": "This is still an issue with 2.8.2pre:\n\n```\nsage: QQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/<ipython console> in <module>()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)\n    178         if isinstance(x, sage.rings.rational.Rational):\n    179             return x\n--> 180         return sage.rings.rational.Rational(x, base)\n    181\n    182     def construction(self):\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__init__()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__set_value()\n\n<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational\n```\n\nI would like to tag this for 2.9 - malb do you agree or would you like to postpone this?\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T10:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1363",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still an issue with 2.8.2pre:

```
sage: QQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.1/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()

/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    178         if isinstance(x, sage.rings.rational.Rational):
    179             return x
--> 180         return sage.rings.rational.Rational(x, base)
    181
    182     def construction(self):

/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__init__()

/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__set_value()

<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational
```

I would like to tag this for 2.9 - malb do you agree or would you like to postpone this?

Cheers,

Michael



---

archive/issue_events_000657.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-31T20:43:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-657"
}
```



---

archive/issue_events_000658.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-31T20:43:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-658"
}
```



---

archive/issue_comments_001364.json:
```json
{
    "body": "This works now.",
    "created_at": "2007-08-31T20:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1364",
    "user": "https://github.com/williamstein"
}
```

This works now.



---

archive/issue_events_000659.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-31T20:43:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-659"
}
```



---

archive/issue_comments_001365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-31T20:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1365",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000660.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-31T20:44:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-660"
}
```



---

archive/issue_events_000661.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-31T20:44:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-661"
}
```



---

archive/issue_events_000662.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-03T21:20:44Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-662"
}
```



---

archive/issue_events_000663.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-03T21:20:44Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "milestone": "sage-2.8.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/290#event-663"
}
```
