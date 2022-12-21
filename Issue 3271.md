# Issue 3271: inject and MPolynomialRing  -- the inject_on command doesn't support MPolynomialRing

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-22 13:39:45

Assignee: malb

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




---

Comment by burcin created at 2008-05-22 13:58:52

I thought `MPolynomialRing` was set to be deprecated, see #2353.


---

Comment by burcin created at 2008-05-22 16:36:48

Resolution: duplicate


---

Comment by burcin created at 2008-05-22 16:36:48

This is a duplicate of #1414.
