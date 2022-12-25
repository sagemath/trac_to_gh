# Issue 7711: integral() does not reduce coefficients in finite field

archive/issues_007711.json:
```json
{
    "body": "Assignee: @malb\n\nConsider the following example:\n\n```\nsage: P.<x,z> = PolynomialRing(GF(2147483647))\nsage: Q.<y> = PolynomialRing(P)\nsage: p=x+y+z   \nsage: p.integral()\n1/2*y^2 + (x + z)*y\n```\n\nNote the leading coefficient 1/2 is not reduced mod 2147483647.\n\nFor smaller p this seems to work:\n\n```\nsage: P.<x,z> = PolynomialRing(GF(2147483629))\nsage: Q.<y> = PolynomialRing(P)\nsage: p=x+y+z\nsage: p.integral()\n-1073741814*y^2 + (x + z)*y\n```\n\nIt works also when the smaller ring P has only one variable:\n\n```\nsage: P.<x> = PolynomialRing(GF(2147483647))\nsage: Q.<y> = PolynomialRing(P)\nsage: p=x+y\nsage: p.integral()\n1073741824*y^2 + x*y\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7711\n\n",
    "created_at": "2009-12-16T12:21:31Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "integral() does not reduce coefficients in finite field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7711",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @malb

Consider the following example:

```
sage: P.<x,z> = PolynomialRing(GF(2147483647))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z   
sage: p.integral()
1/2*y^2 + (x + z)*y
```

Note the leading coefficient 1/2 is not reduced mod 2147483647.

For smaller p this seems to work:

```
sage: P.<x,z> = PolynomialRing(GF(2147483629))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z
sage: p.integral()
-1073741814*y^2 + (x + z)*y
```

It works also when the smaller ring P has only one variable:

```
sage: P.<x> = PolynomialRing(GF(2147483647))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y
sage: p.integral()
1073741824*y^2 + x*y
```


Issue created by migration from https://trac.sagemath.org/ticket/7711





---

archive/issue_comments_066071.json:
```json
{
    "body": "I'm declaring a total feature freeze on sage-4.3.",
    "created_at": "2009-12-24T07:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66071",
    "user": "https://github.com/williamstein"
}
```

I'm declaring a total feature freeze on sage-4.3.



---

archive/issue_comments_066072.json:
```json
{
    "body": "Note also that in Paul's first example we have:\n\n\n```\nsage: p.integral().parent()\nUnivariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in x, z over Finite Field of size 2147483647\n```\n\n\nwhereas in the second:\n\n\n```\nsage: p.integral().parent()\nUnivariate Polynomial Ring in y over Multivariate Polynomial Ring in x, z over Finite Field of size 2147483629\n```\n\n\nThis is probably where the issue is.",
    "created_at": "2010-01-02T11:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66072",
    "user": "https://github.com/aghitza"
}
```

Note also that in Paul's first example we have:


```
sage: p.integral().parent()
Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in x, z over Finite Field of size 2147483647
```


whereas in the second:


```
sage: p.integral().parent()
Univariate Polynomial Ring in y over Multivariate Polynomial Ring in x, z over Finite Field of size 2147483629
```


This is probably where the issue is.



---

archive/issue_comments_066073.json:
```json
{
    "body": "The bug is still there in 4.3.1.",
    "created_at": "2010-02-05T20:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66073",
    "user": "https://github.com/zimmermann6"
}
```

The bug is still there in 4.3.1.



---

archive/issue_comments_066074.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-19T18:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66074",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066075.json:
```json
{
    "body": "Changing keywords from \"\" to \"rd2\".",
    "created_at": "2012-03-19T18:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66075",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing keywords from "" to "rd2".



---

archive/issue_comments_066076.json:
```json
{
    "body": "This is no longer an issue:\n\n\n```\nsage: P.<x,z> = PolynomialRing(GF(2147483647))\nsage: Q.<y> = PolynomialRing(P)\nsage: p=x+y+z   \nsage: p.integral()\n-1073741823*y^2 + (x + z)*y\nsage: P(-1073741823*2)\n1\n```\n",
    "created_at": "2012-03-19T18:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66076",
    "user": "https://github.com/jbalakrishnan"
}
```

This is no longer an issue:


```
sage: P.<x,z> = PolynomialRing(GF(2147483647))
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z   
sage: p.integral()
-1073741823*y^2 + (x + z)*y
sage: P(-1073741823*2)
1
```




---

archive/issue_comments_066077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-19T18:28:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66077",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066078.json:
```json
{
    "body": "I don't agree that this has been fixed.  In 5.0.beta8, I only have to go up to the next prime:\n\n\n\n```\n\nsage: def f(N):\n....:     P.<x,z> = PolynomialRing(GF(N))\n....:     Q.<y> = PolynomialRing(P)\n....:     p=x+y+z   \n....:     return p.integral()\n....: \nsage: N = 2147483647\nsage: f(N)\n-1073741823*y^2 + (x + z)*y\nsage: N = next_prime(N)\nsage: N\n2147483659\nsage: f(N)\n1/2*y^2 + (x + z)*y\n\n```\n",
    "created_at": "2012-03-19T18:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66078",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

I don't agree that this has been fixed.  In 5.0.beta8, I only have to go up to the next prime:



```

sage: def f(N):
....:     P.<x,z> = PolynomialRing(GF(N))
....:     Q.<y> = PolynomialRing(P)
....:     p=x+y+z   
....:     return p.integral()
....: 
sage: N = 2147483647
sage: f(N)
-1073741823*y^2 + (x + z)*y
sage: N = next_prime(N)
sage: N
2147483659
sage: f(N)
1/2*y^2 + (x + z)*y

```




---

archive/issue_comments_066079.json:
```json
{
    "body": "Good catch. I'll change it back to \"needs work.\"",
    "created_at": "2012-03-19T18:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66079",
    "user": "https://github.com/jbalakrishnan"
}
```

Good catch. I'll change it back to "needs work."



---

archive/issue_comments_066080.json:
```json
{
    "body": "Changing keywords from \"rd2\" to \"\".",
    "created_at": "2012-03-19T18:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66080",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing keywords from "rd2" to "".



---

archive/issue_comments_066081.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-03-19T18:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66081",
    "user": "https://github.com/jbalakrishnan"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066082.json:
```json
{
    "body": "For large primes, Sage uses polydicts for representing multivariate polynomials, instead of using Singular.  The trouble here is that dividing a polydict by another polydict automatically creates the fraction field, even when the denominator is actually an element of the coefficient ring.\n\nThe attached patch tries to detect this (relatively common) special case and perform the division in the coefficient ring instead of going to the fraction field of the ring of polynomials.  This fixes the problems with `integral()` reported here.",
    "created_at": "2012-03-24T05:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66082",
    "user": "https://github.com/aghitza"
}
```

For large primes, Sage uses polydicts for representing multivariate polynomials, instead of using Singular.  The trouble here is that dividing a polydict by another polydict automatically creates the fraction field, even when the denominator is actually an element of the coefficient ring.

The attached patch tries to detect this (relatively common) special case and perform the division in the coefficient ring instead of going to the fraction field of the ring of polynomials.  This fixes the problems with `integral()` reported here.



---

archive/issue_comments_066083.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-03-24T05:25:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66083",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066084.json:
```json
{
    "body": "Alex,\n\nthere is something I don't understand with your patch. You check that `right` is in the base\nring, but not `1/right`, thus what happens the base ring is not a field? Compare for example:\n\n```\nsage: P.<x,z> = PolynomialRing(ZZ)\nsage: Q.<y> = PolynomialRing(P)\nsage: p=x+y+z\nsage: t=p/2\nsage: t.parent()\nUnivariate Polynomial Ring in y over Multivariate Polynomial Ring in x, z over Rational Field\nsage: u=p.integral()\nsage: u.parent()\nUnivariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in x, z over Integer Ring\n```\n\nWhy do t and u have different parents?\n\nPaul",
    "created_at": "2012-03-24T08:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66084",
    "user": "https://github.com/zimmermann6"
}
```

Alex,

there is something I don't understand with your patch. You check that `right` is in the base
ring, but not `1/right`, thus what happens the base ring is not a field? Compare for example:

```
sage: P.<x,z> = PolynomialRing(ZZ)
sage: Q.<y> = PolynomialRing(P)
sage: p=x+y+z
sage: t=p/2
sage: t.parent()
Univariate Polynomial Ring in y over Multivariate Polynomial Ring in x, z over Rational Field
sage: u=p.integral()
sage: u.parent()
Univariate Polynomial Ring in y over Fraction Field of Multivariate Polynomial Ring in x, z over Integer Ring
```

Why do t and u have different parents?

Paul



---

archive/issue_comments_066085.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-03-24T09:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66085",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_066086.json:
```json
{
    "body": "I guess I always found the following strange:\n\n\n```\nsage: type(3)\n<type 'sage.rings.integer.Integer'>\nsage: type(3/1)\n<type 'sage.rings.rational.Rational'>\n```\n\n\nand that influenced me in writing this patch.  I don't however have a strong opinion about this, and I'm happy to change it to make things more consistent by working in the fraction field of base_ring.  I'll replace the patch with one having this behavior soon.",
    "created_at": "2012-03-24T09:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66086",
    "user": "https://github.com/aghitza"
}
```

I guess I always found the following strange:


```
sage: type(3)
<type 'sage.rings.integer.Integer'>
sage: type(3/1)
<type 'sage.rings.rational.Rational'>
```


and that influenced me in writing this patch.  I don't however have a strong opinion about this, and I'm happy to change it to make things more consistent by working in the fraction field of base_ring.  I'll replace the patch with one having this behavior soon.



---

archive/issue_comments_066087.json:
```json
{
    "body": "By the way, the issue you point out with ZZ coefficients is apparently orthogonal to this patch.  Multivariate polynomials over ZZ are handled by Singular, and the patch does not touch them.  It only modifies the behavior for multivariate polynomials that are implemented as polydict's, such as the ones over finite fields of huge characteristic that this ticket started with.\n\nYour ZZ example behaves the same with or without this patch.  If you find it really bothersome, maybe it can be on a new ticket.",
    "created_at": "2012-03-24T09:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66087",
    "user": "https://github.com/aghitza"
}
```

By the way, the issue you point out with ZZ coefficients is apparently orthogonal to this patch.  Multivariate polynomials over ZZ are handled by Singular, and the patch does not touch them.  It only modifies the behavior for multivariate polynomials that are implemented as polydict's, such as the ones over finite fields of huge characteristic that this ticket started with.

Your ZZ example behaves the same with or without this patch.  If you find it really bothersome, maybe it can be on a new ticket.



---

archive/issue_comments_066088.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-03-24T09:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66088",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066089.json:
```json
{
    "body": "Alex, can you add an example where your patch is called with coefficients in a ring?\n\nAbout `3/1` giving a rational, this is ok for me. Indeed, you don't want the type of the result\nto differ when the division is exact or not: `3/2` and `3/1` should give both rationals.\n\nPaul",
    "created_at": "2012-03-24T09:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66089",
    "user": "https://github.com/zimmermann6"
}
```

Alex, can you add an example where your patch is called with coefficients in a ring?

About `3/1` giving a rational, this is ok for me. Indeed, you don't want the type of the result
to differ when the division is exact or not: `3/2` and `3/1` should give both rationals.

Paul



---

archive/issue_comments_066090.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-03-24T10:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66090",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_066091.json:
```json
{
    "body": "Alright, I'm starting to see what you are objecting to, and I agree with you.  Just to make sure I get this right: even the documented examples from the docstring of integral are inconsistent in this way\n\n\n```\n        EXAMPLES::\n        \n            sage: R.<x> = ZZ[]\n            sage: R(0).integral()\n            0\n            sage: f = R(2).integral(); f\n            2*x\n        \n        Note that since the integral is defined over the same base ring the\n        integral is actually in the base ring.\n        \n        ::\n        \n            sage: f.parent()\n            Univariate Polynomial Ring in x over Integer Ring\n        \n        If the integral isn't defined over the same base ring, then the\n        base ring is extended::\n        \n            sage: f = x^3 + x - 2\n            sage: g = f.integral(); g\n            1/4*x^4 + 1/2*x^2 - 2*x\n            sage: g.parent()\n            Univariate Polynomial Ring in x over Rational Field\n```\n\n\nWe want Sage to be less clever and more consistent, so the integral of 2 should be 2x in QQ[x] rather than in ZZ[x].\n\nOf course, this is fun to implement, because you might have something like:\n\n\n```\nsage: A.<a, b> = PolynomialRing(ZZ)\nsage: C.<c> = PolynomialRing(A)\nsage: D.<d> = PowerSeriesRing(C)\nsage: R.<x> = PolynomialRing(D)\nsage: f = a*x^2 + c*x\nsage: f.parent()\nUnivariate Polynomial Ring in x over Power Series Ring in d over \nUnivariate Polynomial Ring in c over Multivariate Polynomial Ring \nin a, b over Integer Ring\n```\n\n\nWhat I would like to do is have f.integral() live in\n\n```\nUnivariate Polynomial Ring in x over Power Series Ring in d over \nUnivariate Polynomial Ring in c over Multivariate Polynomial Ring \nin a, b over Rational Field\n```\n\n\nSo I want to change to the fraction field at the very bottom of the chain of extensions.  This means starting with R and going down to ZZ step by step, then changing ZZ to QQ and walking back up, changing all the intermediate rings along the way.  It can get expensive, but I guess that's the price to pay for working with such monstrosities.\n\nIf my outline agrees with what you had in mind, I'll produce a new patch based on it.",
    "created_at": "2012-03-24T10:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66091",
    "user": "https://github.com/aghitza"
}
```

Alright, I'm starting to see what you are objecting to, and I agree with you.  Just to make sure I get this right: even the documented examples from the docstring of integral are inconsistent in this way


```
        EXAMPLES::
        
            sage: R.<x> = ZZ[]
            sage: R(0).integral()
            0
            sage: f = R(2).integral(); f
            2*x
        
        Note that since the integral is defined over the same base ring the
        integral is actually in the base ring.
        
        ::
        
            sage: f.parent()
            Univariate Polynomial Ring in x over Integer Ring
        
        If the integral isn't defined over the same base ring, then the
        base ring is extended::
        
            sage: f = x^3 + x - 2
            sage: g = f.integral(); g
            1/4*x^4 + 1/2*x^2 - 2*x
            sage: g.parent()
            Univariate Polynomial Ring in x over Rational Field
```


We want Sage to be less clever and more consistent, so the integral of 2 should be 2x in QQ[x] rather than in ZZ[x].

Of course, this is fun to implement, because you might have something like:


```
sage: A.<a, b> = PolynomialRing(ZZ)
sage: C.<c> = PolynomialRing(A)
sage: D.<d> = PowerSeriesRing(C)
sage: R.<x> = PolynomialRing(D)
sage: f = a*x^2 + c*x
sage: f.parent()
Univariate Polynomial Ring in x over Power Series Ring in d over 
Univariate Polynomial Ring in c over Multivariate Polynomial Ring 
in a, b over Integer Ring
```


What I would like to do is have f.integral() live in

```
Univariate Polynomial Ring in x over Power Series Ring in d over 
Univariate Polynomial Ring in c over Multivariate Polynomial Ring 
in a, b over Rational Field
```


So I want to change to the fraction field at the very bottom of the chain of extensions.  This means starting with R and going down to ZZ step by step, then changing ZZ to QQ and walking back up, changing all the intermediate rings along the way.  It can get expensive, but I guess that's the price to pay for working with such monstrosities.

If my outline agrees with what you had in mind, I'll produce a new patch based on it.



---

archive/issue_comments_066092.json:
```json
{
    "body": "Alex,\n\nin fact I guess your initial patch did what we want. Indeed with your latest example:\n\n```\nsage: g=f/2\nsage: g.parent()\nUnivariate Polynomial Ring in x over Power Series Ring in d over Univariate Polynomial Ring in c over Multivariate Polynomial Ring in a, b over Rational Field\n```\n\nthus the fact of dividing f by an element of the base ring automatically extends it to the corresponding\nfraction field if necessary.\n\nThus I suggest you revert to your first patch (sorry) and add the above example as test.\n\nPaul",
    "created_at": "2012-03-24T11:03:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66092",
    "user": "https://github.com/zimmermann6"
}
```

Alex,

in fact I guess your initial patch did what we want. Indeed with your latest example:

```
sage: g=f/2
sage: g.parent()
Univariate Polynomial Ring in x over Power Series Ring in d over Univariate Polynomial Ring in c over Multivariate Polynomial Ring in a, b over Rational Field
```

thus the fact of dividing f by an element of the base ring automatically extends it to the corresponding
fraction field if necessary.

Thus I suggest you revert to your first patch (sorry) and add the above example as test.

Paul



---

archive/issue_comments_066093.json:
```json
{
    "body": "Does this patch break a major fundamental design decision in both Sage and Magma, namely that / is a constructor for elements of the fraction field.   E.g.,  3/1 has parent QQ.",
    "created_at": "2012-03-24T11:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66093",
    "user": "https://github.com/williamstein"
}
```

Does this patch break a major fundamental design decision in both Sage and Magma, namely that / is a constructor for elements of the fraction field.   E.g.,  3/1 has parent QQ.



---

archive/issue_comments_066094.json:
```json
{
    "body": "William, I don't think this patch (still not ready) will break anything, since I believe it will just\nreturn f/c where f is a polynomial and c an element of the base ring.\n\nAnyway your advice how to best solve this problem is welcome.\n\nPaul",
    "created_at": "2012-03-24T14:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66094",
    "user": "https://github.com/zimmermann6"
}
```

William, I don't think this patch (still not ready) will break anything, since I believe it will just
return f/c where f is a polynomial and c an element of the base ring.

Anyway your advice how to best solve this problem is welcome.

Paul



---

archive/issue_comments_066095.json:
```json
{
    "body": "Replying to [comment:20 was]:\n> Does this patch break a major fundamental design decision in both Sage and Magma, namely that / is a constructor for elements of the fraction field.   E.g.,  3/1 has parent QQ.\n\nHi William, can you have a look at the docstring for p.integral() as it stands now and tell me whether you think it complies with this design decision?  Here is an example:\n\n\n```\nsage: S.<x> = ZZ[]\nsage: p = 2*x\nsage: p.integral()\nx^2\nsage: p.integral().parent()\nUnivariate Polynomial Ring in x over Integer Ring\n```\n\n\nBehind the scenes Sage performed 2/2 and decided that the answer was 1 in ZZ rather than 1 in QQ, so this seems to break the convention.  Also, the answer has a different parent than (3*x).integral(), which is the type of inconsistency that Paul was pointing out before.  So should this stay the way it is, or should this be changed to be more consistent?\n\nBut it gets a tiny bit more complicated than this.  Suppose your coefficients are not ZZ, but rather ZZ[y], where y is a vector of 200 variables.  The integral of 2*x is still `x^2`, but where do we want this `x^2` to live?  Possible answers are (a) ZZ[y][x], (b) Frac(ZZ[y])[x], (c) QQ[y][x].\nThe current behavior is (a) for 2*x and (b) for 3*x, and I am currently leaning toward changing both to (c).  Here's why: you have p in R[x], where R is some coefficient ring.  When you do p.integral(), you are not really dividing p by integers n, but rather the coefficients of p by integers n.  So maybe we should look at what division by n in the coefficient ring R does:\n\n\n```\nsage: R.<y0,y1,y2,y3> = ZZ[]\nsage: S.<x> = R[]\nsage: p = 2*y0\nsage: p.parent()\nMultivariate Polynomial Ring in y0, y1, y2, y3 over Integer Ring\nsage: (p/2).parent()\nMultivariate Polynomial Ring in y0, y1, y2, y3 over Rational Field\nsage: p = 3*y0\nsage: (p/2).parent()\nMultivariate Polynomial Ring in y0, y1, y2, y3 over Rational Field\n```\n\n\nSo p/2 is not in the fraction field of R.  This is what I would like integral() to do as well.\n\nThoughts?",
    "created_at": "2012-03-24T21:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66095",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:20 was]:
> Does this patch break a major fundamental design decision in both Sage and Magma, namely that / is a constructor for elements of the fraction field.   E.g.,  3/1 has parent QQ.

Hi William, can you have a look at the docstring for p.integral() as it stands now and tell me whether you think it complies with this design decision?  Here is an example:


```
sage: S.<x> = ZZ[]
sage: p = 2*x
sage: p.integral()
x^2
sage: p.integral().parent()
Univariate Polynomial Ring in x over Integer Ring
```


Behind the scenes Sage performed 2/2 and decided that the answer was 1 in ZZ rather than 1 in QQ, so this seems to break the convention.  Also, the answer has a different parent than (3*x).integral(), which is the type of inconsistency that Paul was pointing out before.  So should this stay the way it is, or should this be changed to be more consistent?

But it gets a tiny bit more complicated than this.  Suppose your coefficients are not ZZ, but rather ZZ[y], where y is a vector of 200 variables.  The integral of 2*x is still `x^2`, but where do we want this `x^2` to live?  Possible answers are (a) ZZ[y][x], (b) Frac(ZZ[y])[x], (c) QQ[y][x].
The current behavior is (a) for 2*x and (b) for 3*x, and I am currently leaning toward changing both to (c).  Here's why: you have p in R[x], where R is some coefficient ring.  When you do p.integral(), you are not really dividing p by integers n, but rather the coefficients of p by integers n.  So maybe we should look at what division by n in the coefficient ring R does:


```
sage: R.<y0,y1,y2,y3> = ZZ[]
sage: S.<x> = R[]
sage: p = 2*y0
sage: p.parent()
Multivariate Polynomial Ring in y0, y1, y2, y3 over Integer Ring
sage: (p/2).parent()
Multivariate Polynomial Ring in y0, y1, y2, y3 over Rational Field
sage: p = 3*y0
sage: (p/2).parent()
Multivariate Polynomial Ring in y0, y1, y2, y3 over Rational Field
```


So p/2 is not in the fraction field of R.  This is what I would like integral() to do as well.

Thoughts?



---

archive/issue_comments_066096.json:
```json
{
    "body": "OK, I have changed the patch to a new one that achieves objective (c) in the previous comment.  It is also simpler and cleaner than the previous patches.  `integral` now relies on the coefficient rings to do the right thing.  They mostly do, except for polydict, whose behavior is fixed by the patch as well.",
    "created_at": "2012-03-24T23:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66096",
    "user": "https://github.com/aghitza"
}
```

OK, I have changed the patch to a new one that achieves objective (c) in the previous comment.  It is also simpler and cleaner than the previous patches.  `integral` now relies on the coefficient rings to do the right thing.  They mostly do, except for polydict, whose behavior is fixed by the patch as well.



---

archive/issue_comments_066097.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-03-24T23:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66097",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066098.json:
```json
{
    "body": "Alex, I tried to apply your patch to sage-5.0.beta9 but it failed:\n\n```\n\nsage: hg_sage.import_patch(\"trac7711.patch\")\ncd \"/localdisk/tmp/sage-5.0.beta9/devel/sage\" && sage --hg import   \"/localdisk/tmp/sage-5.0.beta9/trac7711.patch\"\napplying /localdisk/tmp/sage-5.0.beta9/trac7711.patch\npatching file sage/rings/polynomial/polynomial_element.pyx\nHunk #1 FAILED at 2369\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej\nabort: patch failed to apply\n```\n\nFor which version is this patch?\n\nPaul",
    "created_at": "2012-03-26T07:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66098",
    "user": "https://github.com/zimmermann6"
}
```

Alex, I tried to apply your patch to sage-5.0.beta9 but it failed:

```

sage: hg_sage.import_patch("trac7711.patch")
cd "/localdisk/tmp/sage-5.0.beta9/devel/sage" && sage --hg import   "/localdisk/tmp/sage-5.0.beta9/trac7711.patch"
applying /localdisk/tmp/sage-5.0.beta9/trac7711.patch
patching file sage/rings/polynomial/polynomial_element.pyx
Hunk #1 FAILED at 2369
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/polynomial_element.pyx.rej
abort: patch failed to apply
```

For which version is this patch?

Paul



---

archive/issue_comments_066099.json:
```json
{
    "body": "> For which version is this patch?\n\nIt's based on sage-4.8.  I have a sage-5.0.beta10 somewhere, I'll rebase it on that soon.",
    "created_at": "2012-03-26T07:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66099",
    "user": "https://github.com/aghitza"
}
```

> For which version is this patch?

It's based on sage-4.8.  I have a sage-5.0.beta10 somewhere, I'll rebase it on that soon.



---

archive/issue_comments_066100.json:
```json
{
    "body": "it seems my sage-5.0.beta9 was corrupted. I'll compile sage-5.0.beta10 from source and try\nagain.\n\nPaul",
    "created_at": "2012-03-26T07:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66100",
    "user": "https://github.com/zimmermann6"
}
```

it seems my sage-5.0.beta9 was corrupted. I'll compile sage-5.0.beta10 from source and try
again.

Paul



---

archive/issue_comments_066101.json:
```json
{
    "body": "I tried on a clean sage-5.0.beta10 and the previous version of the patch did not apply correctly.  I have rebased it now and it should work.",
    "created_at": "2012-03-26T08:10:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66101",
    "user": "https://github.com/aghitza"
}
```

I tried on a clean sage-5.0.beta10 and the previous version of the patch did not apply correctly.  I have rebased it now and it should work.



---

archive/issue_comments_066102.json:
```json
{
    "body": "replying to comment [comment:22]: I guess we should just return `p/2` and let the coercion\nmechanism decide the corresponding parent. In such a way it will ensure that `p.integral()` and `p/2` have the same type.\n\nPaul",
    "created_at": "2012-03-26T15:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66102",
    "user": "https://github.com/zimmermann6"
}
```

replying to comment [comment:22]: I guess we should just return `p/2` and let the coercion
mechanism decide the corresponding parent. In such a way it will ensure that `p.integral()` and `p/2` have the same type.

Paul



---

archive/issue_comments_066103.json:
```json
{
    "body": "I confirm the rebased patch applies cleanly to sage-5.0.beta10.\n\nHowever there is still an issue:\n\n```\nsage: R.<x> = ZZ[]\nsage: R(0).integral().parent()\nUnivariate Polynomial Ring in x over Integer Ring\nsage: R(3).integral().parent()\nUnivariate Polynomial Ring in x over Rational Field\n```\n\nWhy do we get a different parent for zero?\n\nPaul",
    "created_at": "2012-03-26T16:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66103",
    "user": "https://github.com/zimmermann6"
}
```

I confirm the rebased patch applies cleanly to sage-5.0.beta10.

However there is still an issue:

```
sage: R.<x> = ZZ[]
sage: R(0).integral().parent()
Univariate Polynomial Ring in x over Integer Ring
sage: R(3).integral().parent()
Univariate Polynomial Ring in x over Rational Field
```

Why do we get a different parent for zero?

Paul



---

archive/issue_comments_066104.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2012-03-26T16:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66104",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_066105.json:
```json
{
    "body": "Attachment [trac7711.patch](tarball://root/attachments/some-uuid/ticket7711/trac7711.patch) by @aghitza created at 2012-03-26 21:43:57",
    "created_at": "2012-03-26T21:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66105",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac7711.patch](tarball://root/attachments/some-uuid/ticket7711/trac7711.patch) by @aghitza created at 2012-03-26 21:43:57



---

archive/issue_comments_066106.json:
```json
{
    "body": "Ah, that's because the degree of R(0) is negative.  Sorry.  It's fixed in the new patch, and I've added `R(0).integral().parent()` to the doctests.",
    "created_at": "2012-03-26T21:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66106",
    "user": "https://github.com/aghitza"
}
```

Ah, that's because the degree of R(0) is negative.  Sorry.  It's fixed in the new patch, and I've added `R(0).integral().parent()` to the doctests.



---

archive/issue_comments_066107.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-03-26T21:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66107",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_066108.json:
```json
{
    "body": "I get only one doctest failure, but it also fails with vanilla sage-5.0.beta10 and seems\nunrelated:\n\n```\nsage -t  \"devel/sage-7711/sage/misc/sagedoc.py\"             \n\n**********************************************************************\nFile \"/localdisk/tmp/sage-5.0.beta10/devel/sage-7711/sage/misc/sagedoc.py\", line 566:\n    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)\nExpected:\n    True\nGot:\n    Warning, the following Sage documentation hasn't been built,\n    so documentation search results may be incomplete:\n    <BLANKLINE>\n    /localdisk/tmp/sage-5.0.beta10/devel/sage/doc/output/html/de/tutorial\n...\n```\n\n\nThis patch not only fixes the original issue, but improves the coherence of Sage results.\nGood job Alex!\n\nPaul",
    "created_at": "2012-03-27T11:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66108",
    "user": "https://github.com/zimmermann6"
}
```

I get only one doctest failure, but it also fails with vanilla sage-5.0.beta10 and seems
unrelated:

```
sage -t  "devel/sage-7711/sage/misc/sagedoc.py"             

**********************************************************************
File "/localdisk/tmp/sage-5.0.beta10/devel/sage-7711/sage/misc/sagedoc.py", line 566:
    sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
Expected:
    True
Got:
    Warning, the following Sage documentation hasn't been built,
    so documentation search results may be incomplete:
    <BLANKLINE>
    /localdisk/tmp/sage-5.0.beta10/devel/sage/doc/output/html/de/tutorial
...
```


This patch not only fixes the original issue, but improves the coherence of Sage results.
Good job Alex!

Paul



---

archive/issue_comments_066109.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-27T11:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66109",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066110.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-04-02T15:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7711#issuecomment-66110",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_007928.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-04-02T15:23:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7711",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7711#event-7928"
}
```
