# Issue 9498: The function _factor_over_nonprime_finite_field is wrong in Sage, so remove it

archive/issues_009498.json:
```json
{
    "body": "Assignee: malb\n\nI wrote the function _factor_over_nonprime_finite_field in multi_polynomial.pyx in hopes that Singular's multivariate poly factorization worked over GF(p).  But it doesn't, so that function is pointless.  Moreover, as John Cremona pointed out in email on the sagedays23 list recently, the algorithm there is wrong!:\n\n```\nIf f is irreducible over R but not over S then your\ngcd will be f again which does not help you factor over S.\n\nBasically what one needs is that the conjugates of f (whose product is\nthe norm) are coprime.\n\n?\n```\n\n\nHere's an example to illustrate that it is wrong:\n\n```\nflat:polynomial wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x> = GF(3)[]\nsage: x^2+1\nx^2 + 1\nsage: (x^2+1).factor()\nx^2 + 1\nsage: f = x^2+1\nsage: f\nx^2 + 1\nsage: g = f.change_ring(GF(9,'a'))\nsage: g\nx^2 + 1\nsage: g.factor()\n(x + a + 1) * (x + 2*a + 2)\nsage: type(g)\n<type 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>\nsage: R.<x,y> = GF(3)[]\nsage: f = x^2+1\nsage: g = f.change_ring(GF(9,'a'))\nsage: g\nx^2 + 1\nsage: g.factor()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n| Sage Version 4.4.4, Release Date: 2010-06-23                       |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/wstein/sage/build/sage-4.4.4/devel/sage-main/sage/rings/polynomial/<ipython console> in <module>()\n\n/Users/wstein/sage/build/sage-4.4.4/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor (sage/rings/polynomial/multi_polynomial_libsingular.cpp:22745)()\n   3586                 raise NotImplementedError, \"Factorization of multivariate polynomials over prime fields with characteristic > 2^29 is not implemented.\"\n   3587             if proof:\n-> 3588                 raise NotImplementedError, \"proof = True factorization not implemented.  Call factor with proof=False.\"\n   3589             if not self._parent._base.is_prime_field():\n   3590                 return self._factor_over_nonprime_finite_field()\n\nNotImplementedError: proof = True factorization not implemented.  Call factor with proof=False.\nsage: g._factor_over_nonprime_finite_field()\nx^2 + 1\nsage: g.factor(proof=False)\nx^2 + 1\n```\n\n\nThe point is that g should factor as a product of two linear factors. \n\nSo, let's just delete this function, and anything that calls it, and use Singular's builtin factorization code in the non-prime case. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9498\n\n",
    "created_at": "2010-07-14T14:18:10Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "The function _factor_over_nonprime_finite_field is wrong in Sage, so remove it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9498",
    "user": "was"
}
```
Assignee: malb

I wrote the function _factor_over_nonprime_finite_field in multi_polynomial.pyx in hopes that Singular's multivariate poly factorization worked over GF(p).  But it doesn't, so that function is pointless.  Moreover, as John Cremona pointed out in email on the sagedays23 list recently, the algorithm there is wrong!:

```
If f is irreducible over R but not over S then your
gcd will be f again which does not help you factor over S.

Basically what one needs is that the conjugates of f (whose product is
the norm) are coprime.

?
```


Here's an example to illustrate that it is wrong:

```
flat:polynomial wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x> = GF(3)[]
sage: x^2+1
x^2 + 1
sage: (x^2+1).factor()
x^2 + 1
sage: f = x^2+1
sage: f
x^2 + 1
sage: g = f.change_ring(GF(9,'a'))
sage: g
x^2 + 1
sage: g.factor()
(x + a + 1) * (x + 2*a + 2)
sage: type(g)
<type 'sage.rings.polynomial.polynomial_zz_pex.Polynomial_ZZ_pEX'>
sage: R.<x,y> = GF(3)[]
sage: f = x^2+1
sage: g = f.change_ring(GF(9,'a'))
sage: g
x^2 + 1
sage: g.factor()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/wstein/sage/build/sage-4.4.4/devel/sage-main/sage/rings/polynomial/<ipython console> in <module>()

/Users/wstein/sage/build/sage-4.4.4/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular.factor (sage/rings/polynomial/multi_polynomial_libsingular.cpp:22745)()
   3586                 raise NotImplementedError, "Factorization of multivariate polynomials over prime fields with characteristic > 2^29 is not implemented."
   3587             if proof:
-> 3588                 raise NotImplementedError, "proof = True factorization not implemented.  Call factor with proof=False."
   3589             if not self._parent._base.is_prime_field():
   3590                 return self._factor_over_nonprime_finite_field()

NotImplementedError: proof = True factorization not implemented.  Call factor with proof=False.
sage: g._factor_over_nonprime_finite_field()
x^2 + 1
sage: g.factor(proof=False)
x^2 + 1
```


The point is that g should factor as a product of two linear factors. 

So, let's just delete this function, and anything that calls it, and use Singular's builtin factorization code in the non-prime case. 

Issue created by migration from https://trac.sagemath.org/ticket/9498





---

archive/issue_comments_091211.json:
```json
{
    "body": "Look into whether the comment malb posted on #5074 is really just an indication of a bug in this code, and not in Singular.",
    "created_at": "2010-07-14T15:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91211",
    "user": "was"
}
```

Look into whether the comment malb posted on #5074 is really just an indication of a bug in this code, and not in Singular.



---

archive/issue_comments_091212.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-14T22:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91212",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_091213.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-14T22:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91213",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_091214.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-14T22:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91214",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091215.json:
```json
{
    "body": "Looks good to me. Since there seems to be no movement on #5074 -- I guess we're waiting for the Singular performance bug to be resolved -- let's at least deal with this ticket. \n\nI tested `sage/rings` with `trac_9498.patch` applied and everything passed. Strictly speaking we should perhaps have a doctest, but since the patch adds no new code -- it just removes bad old code -- I don't think there's any need to insist on that.",
    "created_at": "2010-12-16T11:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91215",
    "user": "davidloeffler"
}
```

Looks good to me. Since there seems to be no movement on #5074 -- I guess we're waiting for the Singular performance bug to be resolved -- let's at least deal with this ticket. 

I tested `sage/rings` with `trac_9498.patch` applied and everything passed. Strictly speaking we should perhaps have a doctest, but since the patch adds no new code -- it just removes bad old code -- I don't think there's any need to insist on that.



---

archive/issue_comments_091216.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-16T11:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91216",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091217.json:
```json
{
    "body": "Attachment\n\nSame patch, fixed commit message",
    "created_at": "2011-01-19T02:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91217",
    "user": "jdemeyer"
}
```

Attachment

Same patch, fixed commit message



---

archive/issue_comments_091218.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9498#issuecomment-91218",
    "user": "jdemeyer"
}
```

Resolution: fixed
