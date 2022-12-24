# Issue 3271: inject and MPolynomialRing  -- the inject_on command doesn't support MPolynomialRing

archive/issues_003271.json:
```json
{
    "body": "Assignee: @malb\n\nAdd support for MPolynomialRing to inject_on() command.   This is likely very easy. \n\n\n```\n>\n> Dear sage community,\n>\n> I am new to sage, so please forgive me if I am reporting well-known\n> behaviour here.\n> When generating multivariate polynomial rings, some (seemingly) odd\n> things can happen:\n>\n> 1. Sage seems to guess the meaning of 'x' in some cases:\n>\n> sage: QX=MPolynomialRing(QQ,2,'xy'); QX\n> Multivariate Polynomial Ring in x, y over Rational Field\n> sage: x in QX     # no variables assinged to indeterminates yet...\n> False\n\nThat is the predefined symbolic x that is defined at startup\nbefore you do anything.   Unless you explicitly assign the\ngens of QX to variables (or set auto injection on), \nthey won't be bound to variables. \n\nsage: type(x)\n<class 'sage.calculus.calculus.SymbolicVariable'>\nsage: QX=MPolynomialRing(QQ,2,'xy')\nsage: type(x)\n<class 'sage.calculus.calculus.SymbolicVariable'>\nsage: QX.gens()\n(x, y)\nsage: type(QX.gens()[0])\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n\nYou might like the inject_on() mode:\n\nsage: inject_on()\nRedefining: Frac FreeMonoid GF FractionField FiniteField PolynomialRing quotient NumberField LaurentSeriesRing quo \nsage: QX=PolynomialRing(QQ,2,'xy')\nDefining x, y\nsage: type(x)\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\nsage: type(y)\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\n\n\nWARNING: inject_on only works with the PolynomialRing command, not the\nMPolynomialRing command.   Either the latter should be supported, or \nthe command should be removed entirely. \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3271\n\n",
    "created_at": "2008-05-22T13:39:45Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "inject and MPolynomialRing  -- the inject_on command doesn't support MPolynomialRing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3271",
    "user": "@williamstein"
}
```
Assignee: @malb

Add support for MPolynomialRing to inject_on() command.   This is likely very easy. 


```
>
> Dear sage community,
>
> I am new to sage, so please forgive me if I am reporting well-known
> behaviour here.
> When generating multivariate polynomial rings, some (seemingly) odd
> things can happen:
>
> 1. Sage seems to guess the meaning of 'x' in some cases:
>
> sage: QX=MPolynomialRing(QQ,2,'xy'); QX
> Multivariate Polynomial Ring in x, y over Rational Field
> sage: x in QX     # no variables assinged to indeterminates yet...
> False

That is the predefined symbolic x that is defined at startup
before you do anything.   Unless you explicitly assign the
gens of QX to variables (or set auto injection on), 
they won't be bound to variables. 

sage: type(x)
<class 'sage.calculus.calculus.SymbolicVariable'>
sage: QX=MPolynomialRing(QQ,2,'xy')
sage: type(x)
<class 'sage.calculus.calculus.SymbolicVariable'>
sage: QX.gens()
(x, y)
sage: type(QX.gens()[0])
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>

You might like the inject_on() mode:

sage: inject_on()
Redefining: Frac FreeMonoid GF FractionField FiniteField PolynomialRing quotient NumberField LaurentSeriesRing quo 
sage: QX=PolynomialRing(QQ,2,'xy')
Defining x, y
sage: type(x)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: type(y)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>


WARNING: inject_on only works with the PolynomialRing command, not the
MPolynomialRing command.   Either the latter should be supported, or 
the command should be removed entirely. 
```



Issue created by migration from https://trac.sagemath.org/ticket/3271





---

archive/issue_comments_022639.json:
```json
{
    "body": "I thought `MPolynomialRing` was set to be deprecated, see #2353.",
    "created_at": "2008-05-22T13:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3271#issuecomment-22639",
    "user": "@burcin"
}
```

I thought `MPolynomialRing` was set to be deprecated, see #2353.



---

archive/issue_comments_022640.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-05-22T16:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3271#issuecomment-22640",
    "user": "@burcin"
}
```

Resolution: duplicate



---

archive/issue_comments_022641.json:
```json
{
    "body": "This is a duplicate of #1414.",
    "created_at": "2008-05-22T16:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3271#issuecomment-22641",
    "user": "@burcin"
}
```

This is a duplicate of #1414.
