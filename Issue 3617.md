# Issue 3617: LarentPolynomial.__call__ is broken for Laurent polynomial's that have negative exponents

archive/issues_003617.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nsage: P.<q> = LaurentPolynomialRing(QQ)\nsage: qi = q^(-1)\nsage: qi in P\nFalse\nsage: q in P\nTrue\nsage: P(qi)\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/mike/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/laurent_polynomial_ring.py in __call__(self, x)\n    679             sage: L(1/2)\n    680             1/2\n    681         \"\"\"\n--> 682         return LaurentPolynomial_mpair(self, x)\n    683     \n\n/home/mike/laurent_polynomial.pyx in sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair.__init__ (sage/rings/polynomial/laurent_polynomial.c:1889)()\n\n/home/mike/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:5984)()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)\n    216             return x\n    217 \n--> 218         return sage.rings.rational.Rational(x, base)\n    219         \n    220     def construction(self):\n\n/home/mike/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3321)()\n\n/home/mike/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4494)()\n\nTypeError: Unable to coerce q^-1 (<type 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'>) to Rational\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3617\n\n",
    "created_at": "2008-07-08T21:35:22Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "LarentPolynomial.__call__ is broken for Laurent polynomial's that have negative exponents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3617",
    "user": "mhansen"
}
```
Assignee: malb


```
sage: P.<q> = LaurentPolynomialRing(QQ)
sage: qi = q^(-1)
sage: qi in P
False
sage: q in P
True
sage: P(qi)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mike/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/laurent_polynomial_ring.py in __call__(self, x)
    679             sage: L(1/2)
    680             1/2
    681         """
--> 682         return LaurentPolynomial_mpair(self, x)
    683     

/home/mike/laurent_polynomial.pyx in sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair.__init__ (sage/rings/polynomial/laurent_polynomial.c:1889)()

/home/mike/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:5984)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    216             return x
    217 
--> 218         return sage.rings.rational.Rational(x, base)
    219         
    220     def construction(self):

/home/mike/rational.pyx in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:3321)()

/home/mike/rational.pyx in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:4494)()

TypeError: Unable to coerce q^-1 (<type 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'>) to Rational
```


Issue created by migration from https://trac.sagemath.org/ticket/3617





---

archive/issue_comments_025526.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T22:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3617#issuecomment-25526",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_025527.json:
```json
{
    "body": "This also fixes #5468.",
    "created_at": "2010-01-19T22:58:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3617#issuecomment-25527",
    "user": "mhansen"
}
```

This also fixes #5468.



---

archive/issue_comments_025528.json:
```json
{
    "body": "Attachment [trac_3617.patch](tarball://root/attachments/some-uuid/ticket3617/trac_3617.patch) by mhansen created at 2010-01-20 05:51:43",
    "created_at": "2010-01-20T05:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3617#issuecomment-25528",
    "user": "mhansen"
}
```

Attachment [trac_3617.patch](tarball://root/attachments/some-uuid/ticket3617/trac_3617.patch) by mhansen created at 2010-01-20 05:51:43



---

archive/issue_comments_025529.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T06:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3617#issuecomment-25529",
    "user": "spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025530.json:
```json
{
    "body": "This seems fine to me, and applies and passes all doctests on 4.3.\n\nSebastian",
    "created_at": "2010-01-20T06:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3617#issuecomment-25530",
    "user": "spancratz"
}
```

This seems fine to me, and applies and passes all doctests on 4.3.

Sebastian



---

archive/issue_comments_025531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T08:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3617#issuecomment-25531",
    "user": "mvngu"
}
```

Resolution: fixed
