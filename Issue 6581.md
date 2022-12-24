# Issue 6581: Groebner basis not working over symbolic ring

archive/issues_006581.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wstein malb\n\nI'm not sure if this is a problem in the multivariate polynomials (which seem to raise the actual error) or somewhere in the symbolics.\n\nsage: R2.<a,b> = SR[]\nsage: I2 = [a*b+a, a*a] * R2\nsage: G2 = I2.groebner_basis()\nverbose 0 (2247: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n...\nAttributeError: 'MPolynomialRing_polydict' object has no attribute 'monomial_divides'\nsage:\n\nIssue created by migration from https://trac.sagemath.org/ticket/6581\n\n",
    "created_at": "2009-07-21T17:11:12Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Groebner basis not working over symbolic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6581",
    "user": "rhinton"
}
```
Assignee: tbd

CC:  wstein malb

I'm not sure if this is a problem in the multivariate polynomials (which seem to raise the actual error) or somewhere in the symbolics.

sage: R2.<a,b> = SR[]
sage: I2 = [a*b+a, a*a] * R2
sage: G2 = I2.groebner_basis()
verbose 0 (2247: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
...
AttributeError: 'MPolynomialRing_polydict' object has no attribute 'monomial_divides'
sage:

Issue created by migration from https://trac.sagemath.org/ticket/6581





---

archive/issue_comments_053726.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-11-15T13:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53726",
    "user": "AlexGhitza"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_053727.json:
```json
{
    "body": "The failure is because the polynomials' parent is of type `MPolynomialRing_polydict`, but `MPolynomialRing_polydict_domain` is the type with the necessary methods `monomial_divides`, `monomial_pairwise_prime`, etc.\n\n* Should a polynomial ring in this case always initialize as `..._domain`?\n* If not, is there an easy option to create the ideal of such a ring? (in this case, at most a documentation change is necessary)\n* If no such method currently exists, what would be the best way to let the user do this?\n  a. Have the user create `R2` as above, then call a (new) function that makes it re-initialize as `..._domain`? or\n  b. Have a new creation mechanism for such rings, e.g., a symbolic ring `SD` that is a domain, and thus can be initialized as `..._domain`?",
    "created_at": "2012-01-26T20:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53727",
    "user": "john_perry"
}
```

The failure is because the polynomials' parent is of type `MPolynomialRing_polydict`, but `MPolynomialRing_polydict_domain` is the type with the necessary methods `monomial_divides`, `monomial_pairwise_prime`, etc.

* Should a polynomial ring in this case always initialize as `..._domain`?
* If not, is there an easy option to create the ideal of such a ring? (in this case, at most a documentation change is necessary)
* If no such method currently exists, what would be the best way to let the user do this?
  a. Have the user create `R2` as above, then call a (new) function that makes it re-initialize as `..._domain`? or
  b. Have a new creation mechanism for such rings, e.g., a symbolic ring `SD` that is a domain, and thus can be initialized as `..._domain`?



---

archive/issue_comments_053728.json:
```json
{
    "body": "I don't think GB computations over SR make sense. How do we compare with zero, e.g., this: `cos(x)^2 *X + sin(x)^2 * X - X`. How do we decide divisibility, e.g. is \"cos(x)\" zero?",
    "created_at": "2012-01-26T20:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53728",
    "user": "malb"
}
```

I don't think GB computations over SR make sense. How do we compare with zero, e.g., this: `cos(x)^2 *X + sin(x)^2 * X - X`. How do we decide divisibility, e.g. is "cos(x)" zero?



---

archive/issue_comments_053729.json:
```json
{
    "body": "I've had situations where you can still compute a Groebner basis with some indeterminate coefficients. It's annoying to have to do all the work by hand, though. I can see implementing this with a warning that it may not make sense.",
    "created_at": "2012-01-26T21:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53729",
    "user": "john_perry"
}
```

I've had situations where you can still compute a Groebner basis with some indeterminate coefficients. It's annoying to have to do all the work by hand, though. I can see implementing this with a warning that it may not make sense.



---

archive/issue_comments_053730.json:
```json
{
    "body": "If you only want symbolic variables, wouldn't this work:\n\n\n```\nsage: P.<a,b,c> = QQ[]\nsage: K = Frac(P)\nsage: P.<x,y> = PolynomialRing(K)\nsage: P\nMultivariate Polynomial Ring in x, y over Fraction Field of Multivariate Polynomial Ring in a, b, c over Rational Field\n```\n\n\nThis gets mapped to a Singular ring with parameters, i.e., to this one:\n\n\n```\n> ring r = (0,a,b,c),(x,y,z),dp;\n> r;\n//   characteristic : 0\n//   3 parameter    : a b c \n//   minpoly        : 0\n//   number of vars : 3\n//        block   1 : ordering dp\n//                  : names    x y z\n//        block   2 : ordering C\n```\n\n\nSo, this works:\n\n\n```\nsage: singular(P)\n//   characteristic : 0\n//   3 parameter    : a b c \n//   minpoly        : 0\n//   number of vars : 2\n//        block   1 : ordering dp\n//                  : names    x y\n//        block   2 : ordering C\nsage: I = Ideal([P.random_element(), P.random_element()])\nsage: %time gb = I.groebner_basis()\n```\n\n\nbut it's slow.",
    "created_at": "2012-01-26T22:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53730",
    "user": "malb"
}
```

If you only want symbolic variables, wouldn't this work:


```
sage: P.<a,b,c> = QQ[]
sage: K = Frac(P)
sage: P.<x,y> = PolynomialRing(K)
sage: P
Multivariate Polynomial Ring in x, y over Fraction Field of Multivariate Polynomial Ring in a, b, c over Rational Field
```


This gets mapped to a Singular ring with parameters, i.e., to this one:


```
> ring r = (0,a,b,c),(x,y,z),dp;
> r;
//   characteristic : 0
//   3 parameter    : a b c 
//   minpoly        : 0
//   number of vars : 3
//        block   1 : ordering dp
//                  : names    x y z
//        block   2 : ordering C
```


So, this works:


```
sage: singular(P)
//   characteristic : 0
//   3 parameter    : a b c 
//   minpoly        : 0
//   number of vars : 2
//        block   1 : ordering dp
//                  : names    x y
//        block   2 : ordering C
sage: I = Ideal([P.random_element(), P.random_element()])
sage: %time gb = I.groebner_basis()
```


but it's slow.



---

archive/issue_comments_053731.json:
```json
{
    "body": "Here's a smaller example:\n\n```\nsage: P.<a> = QQ[]               \nsage: K = Frac(P)\nsage: P.<x,y,z> = PolynomialRing(K)\nsage: I = Ideal([P.random_element(), P.random_element(), P.random_element()])\nsage: I\nIdeal (((a^2 - 3/4*a - 1)/(a^2 + a))*y*z + ((2/3*a^2 - 5/3*a - 1)/(-9*a^2 + 5/6*a - 9/2))*z^2 + ((3/2*a^2 - a - 5/2)/(-1/20*a - 5/57))*x + ((2/3*a^2 - a - 1)/(-1/2*a^2 + 5*a + 7/4))*y + (7/3*a^2 - 5*a - 1)/(1/3*a^2 - 1/3*a + 3), ((1/2*a^2 - a - 1/2)/(-a^2 + 7))*x*y + ((-5/6*a^2 + 3*a - 1)/(-a^2 + 2/3*a - 1/4))*x*z + ((a^2 + 3/5*a + 1)/(-6*a^2 - a + 95))*y*z + ((-3*a^2 + 21/2)/(-a^2 - 1/5*a - 1))*z^2 + ((-1/3*a - 1/2)/(-1/3*a^2 - 1/8*a - 3))*z, ((a^2 + a)/(-3/2*a^2 - 1/3*a - 1))*x*y + 1/2*a*y^2 + ((1/31*a^2 - 1/8)/(-4*a^2 + 1/5*a - 2/3))*x*z + ((a^2 - a)/(a^2 - 1/20*a - 1/2))*z^2 + (-1/15*a^2 + 1/315*a + 7/15)*y) of Multivariate Polynomial Ring in x, y, z over Fraction Field of Univariate Polynomial Ring in a over Rational Field\nsage: %time gb = I.groebner_basis()\nCPU times: user 0.08 s, sys: 0.02 s, total: 0.09 s\nWall time: 0.33 s\nsage: gb[-1]\ny*z + ((-5472*a^4 + 8208*a^3 + 21888*a^2 + 8208*a)/(73872*a^4 - 62244*a^3 - 31806*a^2 - 20862*a - 36936))*z^2 + ((-2216160*a^4 - 738720*a^3 + 5171040*a^2 + 3693600*a)/(73872*a^3 + 74196*a^2 - 171072*a - 129600))*x + ((-98496*a^4 + 49248*a^3 + 295488*a^2 + 147744*a)/(73872*a^4 - 794124*a^3 + 221616*a^2 + 932634*a + 258552))*y + (517104*a^4 - 590976*a^3 - 1329696*a^2 - 221616*a)/(73872*a^4 - 129276*a^3 + 646380*a^2 - 424764*a - 664848)\n```\n",
    "created_at": "2012-01-26T22:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53731",
    "user": "malb"
}
```

Here's a smaller example:

```
sage: P.<a> = QQ[]               
sage: K = Frac(P)
sage: P.<x,y,z> = PolynomialRing(K)
sage: I = Ideal([P.random_element(), P.random_element(), P.random_element()])
sage: I
Ideal (((a^2 - 3/4*a - 1)/(a^2 + a))*y*z + ((2/3*a^2 - 5/3*a - 1)/(-9*a^2 + 5/6*a - 9/2))*z^2 + ((3/2*a^2 - a - 5/2)/(-1/20*a - 5/57))*x + ((2/3*a^2 - a - 1)/(-1/2*a^2 + 5*a + 7/4))*y + (7/3*a^2 - 5*a - 1)/(1/3*a^2 - 1/3*a + 3), ((1/2*a^2 - a - 1/2)/(-a^2 + 7))*x*y + ((-5/6*a^2 + 3*a - 1)/(-a^2 + 2/3*a - 1/4))*x*z + ((a^2 + 3/5*a + 1)/(-6*a^2 - a + 95))*y*z + ((-3*a^2 + 21/2)/(-a^2 - 1/5*a - 1))*z^2 + ((-1/3*a - 1/2)/(-1/3*a^2 - 1/8*a - 3))*z, ((a^2 + a)/(-3/2*a^2 - 1/3*a - 1))*x*y + 1/2*a*y^2 + ((1/31*a^2 - 1/8)/(-4*a^2 + 1/5*a - 2/3))*x*z + ((a^2 - a)/(a^2 - 1/20*a - 1/2))*z^2 + (-1/15*a^2 + 1/315*a + 7/15)*y) of Multivariate Polynomial Ring in x, y, z over Fraction Field of Univariate Polynomial Ring in a over Rational Field
sage: %time gb = I.groebner_basis()
CPU times: user 0.08 s, sys: 0.02 s, total: 0.09 s
Wall time: 0.33 s
sage: gb[-1]
y*z + ((-5472*a^4 + 8208*a^3 + 21888*a^2 + 8208*a)/(73872*a^4 - 62244*a^3 - 31806*a^2 - 20862*a - 36936))*z^2 + ((-2216160*a^4 - 738720*a^3 + 5171040*a^2 + 3693600*a)/(73872*a^3 + 74196*a^2 - 171072*a - 129600))*x + ((-98496*a^4 + 49248*a^3 + 295488*a^2 + 147744*a)/(73872*a^4 - 794124*a^3 + 221616*a^2 + 932634*a + 258552))*y + (517104*a^4 - 590976*a^3 - 1329696*a^2 - 221616*a)/(73872*a^4 - 129276*a^3 + 646380*a^2 - 424764*a - 664848)
```




---

archive/issue_comments_053732.json:
```json
{
    "body": "Would this work when we place some assumptions on the variables; e.g., `a<sup>2+b</sup>2==1`? That was my particular situations, and I was under the impression that doing it in the way you suggest won't work for that.",
    "created_at": "2012-01-26T23:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53732",
    "user": "john_perry"
}
```

Would this work when we place some assumptions on the variables; e.g., `a<sup>2+b</sup>2==1`? That was my particular situations, and I was under the impression that doing it in the way you suggest won't work for that.



---

archive/issue_comments_053733.json:
```json
{
    "body": "(Sorry, I meant assumptions on the coefficients.)",
    "created_at": "2012-01-26T23:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53733",
    "user": "john_perry"
}
```

(Sorry, I meant assumptions on the coefficients.)



---

archive/issue_comments_053734.json:
```json
{
    "body": "This might be naive, but can't you add `a<sup>2+b</sup>2 - 1` to your ideal?",
    "created_at": "2012-01-26T23:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53734",
    "user": "malb"
}
```

This might be naive, but can't you add `a<sup>2+b</sup>2 - 1` to your ideal?



---

archive/issue_comments_053735.json:
```json
{
    "body": "Replying to [comment:9 malb]:\n> This might be naive, but can't you add `a<sup>2+b</sup>2 - 1` to your ideal?\n\nDoesn't that change the ideal? These are elements of the base ring.",
    "created_at": "2012-01-27T00:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53735",
    "user": "john_perry"
}
```

Replying to [comment:9 malb]:
> This might be naive, but can't you add `a<sup>2+b</sup>2 - 1` to your ideal?

Doesn't that change the ideal? These are elements of the base ring.



---

archive/issue_comments_053736.json:
```json
{
    "body": "Hey, I got it to work.\n\n```\nsage: R.<a,b> = QQ[]\nsage: I = R.ideal(a^2+b^2-1)\nsage: R2 = QuotientRing(R,I)\nsage: K = Frac(R2)\nsage: P.<x,y,z> = K[]\nsage: f = (a^2+b^2)*x + 1\nsage: g = x + 1\nsage: f - g\n0\n```\n\nSorry -- I'm a bit slow sometimes. :-)\n\nOkay, so we should mark this as \"invalid/wontfix\" or something like that? Or do we wait to see if the original reporter has a scenario in mind that really does require `SR`?",
    "created_at": "2012-01-27T01:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53736",
    "user": "john_perry"
}
```

Hey, I got it to work.

```
sage: R.<a,b> = QQ[]
sage: I = R.ideal(a^2+b^2-1)
sage: R2 = QuotientRing(R,I)
sage: K = Frac(R2)
sage: P.<x,y,z> = K[]
sage: f = (a^2+b^2)*x + 1
sage: g = x + 1
sage: f - g
0
```

Sorry -- I'm a bit slow sometimes. :-)

Okay, so we should mark this as "invalid/wontfix" or something like that? Or do we wait to see if the original reporter has a scenario in mind that really does require `SR`?



---

archive/issue_comments_053737.json:
```json
{
    "body": "Unfortunately, your construction bombs out when we try to construct an actual ideal:\n\n\n```\nsage: R.<a,b> = QQ[]\nsage: I = R.ideal(a^2+b^2-1)\nsage: R2 = QuotientRing(R,I)\nsage: K = Frac(R2)\nsage: P.<x,y,z> = K[]\nsage: f = (a^2+b^2)*x + 1\nsage: g = x + 1\nsage: f - g\n0\nsage: Ideal([f,g])\nNotImplementedError\n```\n",
    "created_at": "2012-01-27T08:28:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53737",
    "user": "malb"
}
```

Unfortunately, your construction bombs out when we try to construct an actual ideal:


```
sage: R.<a,b> = QQ[]
sage: I = R.ideal(a^2+b^2-1)
sage: R2 = QuotientRing(R,I)
sage: K = Frac(R2)
sage: P.<x,y,z> = K[]
sage: f = (a^2+b^2)*x + 1
sage: g = x + 1
sage: f - g
0
sage: Ideal([f,g])
NotImplementedError
```




---

archive/issue_comments_053738.json:
```json
{
    "body": "It works (initially) if you do this:\n\n```\nsage: J = P.ideal([f,g])\n```\n\n...but then you can't do anything with `J`. The characteristic isn't set in `R2`. Curiously, I can still work with ideals in `R2`.\n\nLikewise,\n\n```\nsage: Z7 = QuotientRing(ZZ,7*ZZ)\nsage: Z7.characteristic()\n...\nNotImplementedError:\n```\n\nWow. We should probably look at that one day. `;-)`\n\nAnyway, do you know offhand why one needs the characteristic, but not the other?",
    "created_at": "2012-01-27T16:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53738",
    "user": "john_perry"
}
```

It works (initially) if you do this:

```
sage: J = P.ideal([f,g])
```

...but then you can't do anything with `J`. The characteristic isn't set in `R2`. Curiously, I can still work with ideals in `R2`.

Likewise,

```
sage: Z7 = QuotientRing(ZZ,7*ZZ)
sage: Z7.characteristic()
...
NotImplementedError:
```

Wow. We should probably look at that one day. `;-)`

Anyway, do you know offhand why one needs the characteristic, but not the other?



---

archive/issue_comments_053739.json:
```json
{
    "body": "Nope, unfortunately, I don't.",
    "created_at": "2012-01-27T17:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53739",
    "user": "malb"
}
```

Nope, unfortunately, I don't.



---

archive/issue_comments_053740.json:
```json
{
    "body": "> Anyway, do you know offhand why one needs the characteristic, but not the other?\n\nBingo. In lines 302--307 of `multi_polynomial_sequence.py` we encounter:\n\n```\n    if k.characteristic() != 2:\n        return PolynomialSequence_generic(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)\n    elif k.degree() == 1:\n        return PolynomialSequence_gf2(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)\n    elif k.degree() > 1:\n        return PolynomialSequence_gf2e(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)\n```\n\nI can make this work via judicious use of a `try`/`catch`. I found some other instances where it tried to compute a Singular representation of itself (the `reduce` function in `multi_polynomial_element`, for instance). That has allowed me to compute several Gr\u00f6bner bases successfully, including one similar to the ideal you couldn't get to work:\n\n```\nsage: J = R2.ideal([(a^2+b^2)*x + y, x+y])\nsage: J\nIdeal (x + y, x + y) of Multivariate Polynomial Ring in x, y over Fraction Field of\nQuotient of Multivariate Polynomial Ring in a, b over Rational Field by the ideal\n(a^2 + b^2 - 1)\nsage: J.groebner_basis()\nverbose 0 (2854: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to\nvery slow toy implementation.\n[x + y]\n```\n\nI think the patch is worth adding. However, I'm still not sure this is what the original requester wanted. Should I open a new ticket?",
    "created_at": "2012-01-28T05:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53740",
    "user": "john_perry"
}
```

> Anyway, do you know offhand why one needs the characteristic, but not the other?

Bingo. In lines 302--307 of `multi_polynomial_sequence.py` we encounter:

```
    if k.characteristic() != 2:
        return PolynomialSequence_generic(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)
    elif k.degree() == 1:
        return PolynomialSequence_gf2(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)
    elif k.degree() > 1:
        return PolynomialSequence_gf2e(parts, ring, immutable=immutable, cr=cr, cr_str=cr_str)
```

I can make this work via judicious use of a `try`/`catch`. I found some other instances where it tried to compute a Singular representation of itself (the `reduce` function in `multi_polynomial_element`, for instance). That has allowed me to compute several Gröbner bases successfully, including one similar to the ideal you couldn't get to work:

```
sage: J = R2.ideal([(a^2+b^2)*x + y, x+y])
sage: J
Ideal (x + y, x + y) of Multivariate Polynomial Ring in x, y over Fraction Field of
Quotient of Multivariate Polynomial Ring in a, b over Rational Field by the ideal
(a^2 + b^2 - 1)
sage: J.groebner_basis()
verbose 0 (2854: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to
very slow toy implementation.
[x + y]
```

I think the patch is worth adding. However, I'm still not sure this is what the original requester wanted. Should I open a new ticket?



---

archive/issue_comments_053741.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-02-02T01:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53741",
    "user": "john_perry"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053742.json:
```json
{
    "body": "I decided to upload the patch here. I didn't think a doctest was appropriate, but I can add one if desired.",
    "created_at": "2012-02-02T01:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53742",
    "user": "john_perry"
}
```

I decided to upload the patch here. I didn't think a doctest was appropriate, but I can add one if desired.



---

archive/issue_comments_053743.json:
```json
{
    "body": "Whoops -- the patch introduces doctest failures. I'll look into them.",
    "created_at": "2012-02-02T01:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53743",
    "user": "john_perry"
}
```

Whoops -- the patch introduces doctest failures. I'll look into them.



---

archive/issue_comments_053744.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-02T01:49:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53744",
    "user": "john_perry"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_053745.json:
```json
{
    "body": "Okay, that was pretty dumb. Fixed now. Added a doctest while I was at it.",
    "created_at": "2012-02-02T02:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53745",
    "user": "john_perry"
}
```

Okay, that was pretty dumb. Fixed now. Added a doctest while I was at it.



---

archive/issue_comments_053746.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-02T02:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53746",
    "user": "john_perry"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053747.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-02T10:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53747",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053748.json:
```json
{
    "body": "Looks good.",
    "created_at": "2012-02-02T10:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53748",
    "user": "malb"
}
```

Looks good.



---

archive/issue_comments_053749.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-05T11:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53749",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_053750.json:
```json
{
    "body": "You should replace the line number in\n\n```\nverbose 0 (2854: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation\n```\n\nby \"...\" because the line number will change all the time.",
    "created_at": "2012-02-05T11:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53750",
    "user": "jdemeyer"
}
```

You should replace the line number in

```
verbose 0 (2854: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation
```

by "..." because the line number will change all the time.



---

archive/issue_comments_053751.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-07T17:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53751",
    "user": "john_perry"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053752.json:
```json
{
    "body": "Sorry, I should have thought of that myself.\n\nI remembered this time to check the box to replace the file of the same name, so I've changed the directions (& link) on which patch to apply.",
    "created_at": "2012-02-07T17:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53752",
    "user": "john_perry"
}
```

Sorry, I should have thought of that myself.

I remembered this time to check the box to replace the file of the same name, so I've changed the directions (& link) on which patch to apply.



---

archive/issue_comments_053753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-07T21:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53753",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053754.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-11T00:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53754",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_053755.json:
```json
{
    "body": "Please write a proper commit message for your patch, use `hg qrefresh -e` for this.",
    "created_at": "2012-02-11T00:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53755",
    "user": "jdemeyer"
}
```

Please write a proper commit message for your patch, use `hg qrefresh -e` for this.



---

archive/issue_comments_053756.json:
```json
{
    "body": "Attachment [trac_6581_enable_more_ideals_for_toy_buchberger.patch](tarball://root/attachments/some-uuid/ticket6581/trac_6581_enable_more_ideals_for_toy_buchberger.patch) by john_perry created at 2012-02-11 15:23:15",
    "created_at": "2012-02-11T15:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53756",
    "user": "john_perry"
}
```

Attachment [trac_6581_enable_more_ideals_for_toy_buchberger.patch](tarball://root/attachments/some-uuid/ticket6581/trac_6581_enable_more_ideals_for_toy_buchberger.patch) by john_perry created at 2012-02-11 15:23:15



---

archive/issue_comments_053757.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-11T15:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53757",
    "user": "john_perry"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053758.json:
```json
{
    "body": "I should have thought of that, too. Sorry again...",
    "created_at": "2012-02-11T15:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53758",
    "user": "john_perry"
}
```

I should have thought of that, too. Sorry again...



---

archive/issue_comments_053759.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-11T23:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53759",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053760.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-14T14:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6581",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6581#issuecomment-53760",
    "user": "jdemeyer"
}
```

Resolution: fixed
