# Issue 7554: bug in multivariate polynomial factorization

archive/issues_007554.json:
```json
{
    "body": "Assignee: malb\n\nThis is suspicious:\n\n\n```\nsage: # define the coefficient field K and R=K[x,y]\nsage: K.<a>=PolynomialRing(QQ,1)\nsage: K=FractionField(K)\nsage: R.<x,y>=PolynomialRing(K,2)\nsage: factor(x^2-y^2)\n(x - y) * (x + y)\nsage: factor(x)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/Users/wstein/<ipython console> in <module>()\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/arith.pyc in factor(n, proof, int_, algorithm, verbose, **kwds)\n   2100         # this happens for example if n = x**2 + y**2 + 2*x*y\n   2101         try:\n-> 2102             return n.factor(proof=proof, **kwds)\n   2103         except AttributeError:\n   2104             raise TypeError, \"unable to factor n\"\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)\n   1422         # try to use univariate factoring first\n   1423         try:\n-> 1424             F = self.univariate_polynomial().factor()\n   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())\n   1426         except TypeError:\n\n/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.factor (sage/rings/polynomial/polynomial_element.c:22319)()\n\nNotImplementedError: \n```\n\n\nSee emails from Stefan Boettner in sage-support on Nov 28, 2009\n\nIssue created by migration from https://trac.sagemath.org/ticket/7554\n\n",
    "created_at": "2009-11-29T08:49:16Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "bug in multivariate polynomial factorization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7554",
    "user": "was"
}
```
Assignee: malb

This is suspicious:


```
sage: # define the coefficient field K and R=K[x,y]
sage: K.<a>=PolynomialRing(QQ,1)
sage: K=FractionField(K)
sage: R.<x,y>=PolynomialRing(K,2)
sage: factor(x^2-y^2)
(x - y) * (x + y)
sage: factor(x)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/Users/wstein/<ipython console> in <module>()

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/arith.pyc in factor(n, proof, int_, algorithm, verbose, **kwds)
   2100         # this happens for example if n = x**2 + y**2 + 2*x*y
   2101         try:
-> 2102             return n.factor(proof=proof, **kwds)
   2103         except AttributeError:
   2104             raise TypeError, "unable to factor n"

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)
   1422         # try to use univariate factoring first
   1423         try:
-> 1424             F = self.univariate_polynomial().factor()
   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())
   1426         except TypeError:

/Users/wstein/s/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.factor (sage/rings/polynomial/polynomial_element.c:22319)()

NotImplementedError: 
```


See emails from Stefan Boettner in sage-support on Nov 28, 2009

Issue created by migration from https://trac.sagemath.org/ticket/7554





---

archive/issue_comments_064207.json:
```json
{
    "body": "Would it make sense to except not only `TypeError`, but also `AttributeError` (for the case when `univariate_polynomial` is not a method of `self`) and `NotImplementedError` (for exactly the reason that's happening here)?",
    "created_at": "2013-06-22T12:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64207",
    "user": "darij"
}
```

Would it make sense to except not only `TypeError`, but also `AttributeError` (for the case when `univariate_polynomial` is not a method of `self`) and `NotImplementedError` (for exactly the reason that's happening here)?



---

archive/issue_comments_064208.json:
```json
{
    "body": "I've implemented a fallback using singular for generic univariate polynomials (which is what the multivariate case did). I'm not 100% sure it is the best solution (in fact the factorization can be somewhat strange IMO), but it works:\n\n```\nsage: L.<q> = LaurentPolynomialRing(QQ)\nsage: F = L.fraction_field()\nsage: R.<x> = PolynomialRing(F)\nsage: factor(x)\nx\nsage: factor(x^2 - q^2)\n(-1) * (-x + q) * (x + q)\nsage: factor(x^2 - q^-2)\n(1/q^2) * (q*x - 1) * (q*x + 1)\n\nsage: P.<a,b,c> = PolynomialRing(ZZ)\nsage: R.<x> = PolynomialRing(FractionField(P))\nsage: p = (x - a)*(b*x + c)*(a*b*x + a*c) / (a + 2)\nsage: factor(p)\n(a/(a + 2)) * (x - a) * (b*x + c)^2\n```\n\n----\nNew commits:",
    "created_at": "2014-06-23T01:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64208",
    "user": "tscrim"
}
```

I've implemented a fallback using singular for generic univariate polynomials (which is what the multivariate case did). I'm not 100% sure it is the best solution (in fact the factorization can be somewhat strange IMO), but it works:

```
sage: L.<q> = LaurentPolynomialRing(QQ)
sage: F = L.fraction_field()
sage: R.<x> = PolynomialRing(F)
sage: factor(x)
x
sage: factor(x^2 - q^2)
(-1) * (-x + q) * (x + q)
sage: factor(x^2 - q^-2)
(1/q^2) * (q*x - 1) * (q*x + 1)

sage: P.<a,b,c> = PolynomialRing(ZZ)
sage: R.<x> = PolynomialRing(FractionField(P))
sage: p = (x - a)*(b*x + c)*(a*b*x + a*c) / (a + 2)
sage: factor(p)
(a/(a + 2)) * (x - a) * (b*x + c)^2
```

----
New commits:



---

archive/issue_comments_064209.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-06-23T01:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64209",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064210.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd59\".",
    "created_at": "2014-06-23T01:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64210",
    "user": "tscrim"
}
```

Changing keywords from "" to "sd59".



---

archive/issue_comments_064211.json:
```json
{
    "body": "Looks okay.",
    "created_at": "2014-06-26T17:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64211",
    "user": "malb"
}
```

Looks okay.



---

archive/issue_comments_064212.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-26T17:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64212",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-27T01:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7554",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7554#issuecomment-64213",
    "user": "vbraun"
}
```

Resolution: fixed
