# Issue 5195: Multivariate factorization raises NotImplementedError in sage-3.3.alpha3

Issue created by migration from https://trac.sagemath.org/ticket/5195

Original creator: SimonKing

Original creation time: 2009-02-06 10:06:18

Assignee: malb

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


---

Comment by malb created at 2009-02-06 11:28:00

Resolution: wontfix


---

Comment by malb created at 2009-02-06 11:28:00

This is 'wontfix'
 * by default Sage will always attempt to give an answer which is provably correct
 * we can't give that answer for multivariate factoring because of a bug in Singular
 * thus we need to raise an error.
