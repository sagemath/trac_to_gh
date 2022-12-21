# Issue 1381: optimized algorithm for some FractionField substitutions

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-12-03 10:12:23

Assignee: somebody

FractionField substitutions can be quite painfully slow because they result in many many gcd computations.  Attached is a patch which does some book-keeping to alleviate this bottleneck.  The code of this patch needs to be hooked into the !__call!__ method of the FractionFieldElement and MPolynomial_elements (or whatever it is called).  I think it would also make sense for univariate Polynomial_element.

Some benchmarks:

```
sage: R.<x,y,z>=QQ[]
sage: f1=(x+y)/(x^2-z^2) # small fraction
sage: f2=(x+y+z+x^2+y^2+z^2)/(x^2-z^2)  # bigger fraction
sage: d1={x:z^2,y:x}     # substitution of simple monomials
sage: d2={x:z^-2,y:z/x}  # substitution of things in the fraction field
**************
sage: timeit f1.subs(d1)
1000 loops, best of 3: 1.63 ms per loop
sage: timeit fast_subst(f1,d1)
1000 loops, best of 3: 528 µs per loop
**************
sage: timeit f2.subs(d1)
100 loops, best of 3: 2.4 ms per loop
sage: timeit fast_subst(f2,d1)
1000 loops, best of 3: 681 µs per loop
**************
sage: timeit f1.subs(d2)
100 loops, best of 3: 2.04 ms per loop
sage: timeit fast_subst(f1,d2)
1000 loops, best of 3: 635 µs per loop
**************
sage: timeit f2.subs(d2)
100 loops, best of 3: 2.85 ms per loop
sage: timeit fast_subst(f2,d2)
1000 loops, best of 3: 834 µs per loop
```


Note that the book-keeping is mostly arrays of int exponents.  This indicates to me that a cython version of this might be much improved.

I'll get around to integrating this patch myself sometime, but here it is if anyone really wants it sooner.


---

Attachment

fast_subst prototype
