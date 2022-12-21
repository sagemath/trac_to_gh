# Issue 5468: matrix creation over laurent polynomial rings

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2009-03-10 18:30:00

Assignee: malb


```
A.<Y> = QQ[]
R.<X> = LaurentPolynomialRing(A)
matrix(R,2,2,[X,0,0,1])
```

gives a

```
TypeError: Unable to coerce X (<type 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'>) to Rational
```


The same problem occurs with `LaurentSeriesRing`, but not with `PowerSeriesRing`.

I have not tried to chase where the problem actually comes from.


---

Comment by mhansen created at 2010-01-19 22:00:06

This is fixed by #3617


---

Comment by mvngu created at 2010-01-23 08:14:38

Closed as fixed by #3617.


---

Comment by mvngu created at 2010-01-23 08:14:38

Resolution: fixed
