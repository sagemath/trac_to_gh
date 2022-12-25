# Issue 5195: Multivariate factorization raises NotImplementedError in sage-3.3.alpha3

archive/issues_005195.json:
```json
{
    "body": "Assignee: @malb\n\nThe following happened to me on `sage.math`\n\n```\nsage: R=PolynomialRing(GF(2),5,'x')\nsage: p=R.random_element()\nsage: p.factor()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/SimonKing/.sage/temp/sage.math.washington.edu/11643/_home_SimonKing__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor (sage/rings/polynomial/multi_polynomial_libsingular.cpp:23156)()\n\nNotImplementedError: proof = True factorization not implemented.  Call factor with proof=False.\nsage: ver\nverbose      version      vert_to_ieq\nsage: version()\n'Sage Version 3.3.alpha3, Release Date: 2009-01-28'\nsage: p.factor(proof=False)\nx4\n```\n\n\nApparently the optional parameter 'proof' is 'True' by default, but the default case is not implemented.\n\nSince I believe factorization is frequently used, I think this bug is critical.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5195\n\n",
    "created_at": "2009-02-06T10:06:18Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Multivariate factorization raises NotImplementedError in sage-3.3.alpha3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5195",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @malb

The following happened to me on `sage.math`

```
sage: R=PolynomialRing(GF(2),5,'x')
sage: p=R.random_element()
sage: p.factor()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/11643/_home_SimonKing__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor (sage/rings/polynomial/multi_polynomial_libsingular.cpp:23156)()

NotImplementedError: proof = True factorization not implemented.  Call factor with proof=False.
sage: ver
verbose      version      vert_to_ieq
sage: version()
'Sage Version 3.3.alpha3, Release Date: 2009-01-28'
sage: p.factor(proof=False)
x4
```


Apparently the optional parameter 'proof' is 'True' by default, but the default case is not implemented.

Since I believe factorization is frequently used, I think this bug is critical.

Issue created by migration from https://trac.sagemath.org/ticket/5195





---

archive/issue_comments_039750.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-02-06T11:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5195#issuecomment-39750",
    "user": "https://github.com/malb"
}
```

Resolution: wontfix



---

archive/issue_events_005451.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2009-02-06T11:28:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5195",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5195#event-5451"
}
```



---

archive/issue_comments_039751.json:
```json
{
    "body": "This is 'wontfix'\n* by default Sage will always attempt to give an answer which is provably correct\n* we can't give that answer for multivariate factoring because of a bug in Singular\n* thus we need to raise an error.",
    "created_at": "2009-02-06T11:28:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5195#issuecomment-39751",
    "user": "https://github.com/malb"
}
```

This is 'wontfix'
* by default Sage will always attempt to give an answer which is provably correct
* we can't give that answer for multivariate factoring because of a bug in Singular
* thus we need to raise an error.
