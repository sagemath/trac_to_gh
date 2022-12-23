# Issue 9979: Deprecate functionality of `PowerSeriesRing` which conflicts with construction of multivariate power series

Issue created by migration from https://trac.sagemath.org/ticket/9980

Original creator: niles

Original creation time: 2010-09-23 17:44:33

Assignee: malb

CC:  niles

Keywords: power series, deprecation warning

Multivariate power series are implemented by #1956.  As mentioned on that ticket, the existing code for `PowerSeriesRing` did not allow multivariate power series rings to be constructed using the same arguments as multivariate polynomials accept:


```
sage: T = PowerSeriesRing(QQ,3,'t'); T
Multivariate Power Series Ring in t0, t1, t2 over Rational Field

sage: T = PowerSeriesRing(QQ,'t',3); T
Power Series Ring in t over Rational Field
sage: T.default_prec()
3

sage: P = PolynomialRing(QQ,'t',3); P
Multivariate Polynomial Ring in t0, t1, t2 over Rational Field
```


There is a non-trivial body of code (elliptic curves, and maybe p-adics) which makes use of this syntax.


