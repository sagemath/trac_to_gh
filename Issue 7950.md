# Issue 7950: factoring broken in 0 variable polynomial ring

archive/issues_007950.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nsage: P = PolynomialRing(QQ,0,'')\nsage: P\nMultivariate Polynomial Ring in no variables over Rational Field\nsage: t = P.random_element()\nsage: t.factor()\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n\n/home/burcin/.sage/temp/karr/24426/_home_burcin__sage_init_sage_0.py in <module>()\n\n/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)\n   1422         # try to use univariate factoring first\n\n   1423         try:\n-> 1424             F = self.univariate_polynomial().factor()\n   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())\n   1426         except TypeError:\n\n/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in univariate_polynomial(self, R)\n   1055         #construct ring if None\n\n   1056         if R is None:\n-> 1057             R = self.base_ring()[str(self.variables()[0])]\n   1058 \n   1059         monomial_coefficients = self._MPolynomial_element__element.dict()\n\nIndexError: tuple index out of range\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7950\n\n",
    "created_at": "2010-01-16T17:52:56Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "factoring broken in 0 variable polynomial ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7950",
    "user": "burcin"
}
```
Assignee: malb


```
sage: P = PolynomialRing(QQ,0,'')
sage: P
Multivariate Polynomial Ring in no variables over Rational Field
sage: t = P.random_element()
sage: t.factor()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/burcin/.sage/temp/karr/24426/_home_burcin__sage_init_sage_0.py in <module>()

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in factor(self, proof)
   1422         # try to use univariate factoring first

   1423         try:
-> 1424             F = self.univariate_polynomial().factor()
   1425             return Factorization([(R(f),m) for f,m in F], unit=F.unit())
   1426         except TypeError:

/home/burcin/sage/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_element.pyc in univariate_polynomial(self, R)
   1055         #construct ring if None

   1056         if R is None:
-> 1057             R = self.base_ring()[str(self.variables()[0])]
   1058 
   1059         monomial_coefficients = self._MPolynomial_element__element.dict()

IndexError: tuple index out of range
```


Issue created by migration from https://trac.sagemath.org/ticket/7950





---

archive/issue_comments_069365.json:
```json
{
    "body": "factor zero variable polynomials",
    "created_at": "2010-01-17T23:26:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69365",
    "user": "burcin"
}
```

factor zero variable polynomials



---

archive/issue_comments_069366.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T23:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69366",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069367.json:
```json
{
    "body": "Attachment\n\ntrivial review please?",
    "created_at": "2010-01-17T23:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69367",
    "user": "burcin"
}
```

Attachment

trivial review please?



---

archive/issue_comments_069368.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-18T09:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69368",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069369.json:
```json
{
    "body": "1. Factoring of 0 should raise an error like it does over ZZ, but doesn't right now:\n\n```\nsage: P = PolynomialRing(ZZ,0,'')\nsage: P(10).factor()\n10\nsage: P(0).factor()\n0\nsage: factor(0)\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n```\n\n\n2. The element 10 in the polynomial ring \"ZZ[]\" in 0-variables is actually *not* a unit.  So it is wrong that it is put in the \"unit\" slot of the factorization.   Notice how factoring 10 works:\n\n```\nsage: R.<x> = ZZ[]\nsage: (10*x).factor()\n2 * 5 * x\nsage: list((10*x).factor())\n[(2, 1), (5, 1), (x, 1)]\n```\n\nIn particular, the 10 is *not* treated incorrectly as a unit.\n\nSo I think this patch needs work.",
    "created_at": "2010-01-18T09:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69369",
    "user": "was"
}
```

1. Factoring of 0 should raise an error like it does over ZZ, but doesn't right now:

```
sage: P = PolynomialRing(ZZ,0,'')
sage: P(10).factor()
10
sage: P(0).factor()
0
sage: factor(0)
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
```


2. The element 10 in the polynomial ring "ZZ[]" in 0-variables is actually *not* a unit.  So it is wrong that it is put in the "unit" slot of the factorization.   Notice how factoring 10 works:

```
sage: R.<x> = ZZ[]
sage: (10*x).factor()
2 * 5 * x
sage: list((10*x).factor())
[(2, 1), (5, 1), (x, 1)]
```

In particular, the 10 is *not* treated incorrectly as a unit.

So I think this patch needs work.



---

archive/issue_comments_069370.json:
```json
{
    "body": "Attachment\n\nonly apply this patch",
    "created_at": "2010-01-18T17:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69370",
    "user": "burcin"
}
```

Attachment

only apply this patch



---

archive/issue_comments_069371.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-18T17:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69371",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069372.json:
```json
{
    "body": "Thanks for the review!\n\nNew patch addressing both points is available at attachment:trac_7950-zero_variable_factor.take2.patch. I hope it doesn't contain more stupid mistakes. :)",
    "created_at": "2010-01-18T17:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69372",
    "user": "burcin"
}
```

Thanks for the review!

New patch addressing both points is available at attachment:trac_7950-zero_variable_factor.take2.patch. I hope it doesn't contain more stupid mistakes. :)



---

archive/issue_comments_069373.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-23T01:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69373",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069374.json:
```json
{
    "body": "Replying to [comment:3 burcin]:\n> New patch addressing both points is available at attachment:trac_7950-zero_variable_factor.take2.patch. I hope it doesn't contain more stupid mistakes. :)\n\nNot that I could find :)\n\nLooks good to me.",
    "created_at": "2010-01-23T01:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69374",
    "user": "AlexGhitza"
}
```

Replying to [comment:3 burcin]:
> New patch addressing both points is available at attachment:trac_7950-zero_variable_factor.take2.patch. I hope it doesn't contain more stupid mistakes. :)

Not that I could find :)

Looks good to me.



---

archive/issue_comments_069375.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T09:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69375",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_069376.json:
```json
{
    "body": "Merged [trac_7950-zero_variable_factor.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7950/trac_7950-zero_variable_factor.take2.patch).",
    "created_at": "2010-01-23T09:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7950#issuecomment-69376",
    "user": "mvngu"
}
```

Merged [trac_7950-zero_variable_factor.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7950/trac_7950-zero_variable_factor.take2.patch).
