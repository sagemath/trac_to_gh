# Issue 290: Converting Pari multivariate polynomials  to MPolynomials doesn't work

archive/issues_000290.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nQQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))\n<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational\n```\n\n\n(Reported by cwitty)\n\nIssue created by migration from https://trac.sagemath.org/ticket/290\n\n",
    "created_at": "2007-02-24T05:04:12Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Converting Pari multivariate polynomials  to MPolynomials doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/290",
    "user": "malb"
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

archive/issue_comments_001365.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-02-24T05:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1365",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001366.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2007-02-24T05:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1366",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_001367.json:
```json
{
    "body": "This is still an issue with 2.8.2pre:\n\n```\nsage: QQxy.<x, y> = QQ['x', 'y']; QQxy(pari(x+y))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/<ipython console> in <module>()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/multi_polynomial_libsingular.pyx in multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)\n    178         if isinstance(x, sage.rings.rational.Rational):\n    179             return x\n--> 180         return sage.rings.rational.Rational(x, base)\n    181\n    182     def construction(self):\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__init__()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.1/rational.pyx in rational.Rational.__set_value()\n\n<type 'exceptions.TypeError'>: Unable to coerce x + y (<type 'sage.libs.pari.gen.gen'>) to Rational\n```\n\n\nI would like to tag this for 2.9 - malb do you agree or would you like to postpone this?\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T10:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1367",
    "user": "mabshoff"
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

archive/issue_comments_001368.json:
```json
{
    "body": "This works now.",
    "created_at": "2007-08-31T20:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1368",
    "user": "was"
}
```

This works now.



---

archive/issue_comments_001369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-31T20:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/290#issuecomment-1369",
    "user": "was"
}
```

Resolution: fixed
