# Issue 5917: Failing conversions for multipolynomial rings over fraction fields

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-04-28 10:48:22

Assignee: malb

Keywords: polynomial ring fraction field conversion

The following is with sage-3.4.1 on sage.math:

Setting:

```
sage: F1 = FractionField(PolynomialRing(QQ,'a'))
sage: R11 = F1['x']
sage: R12 = F1['x','y']
sage: F2 = FractionField(PolynomialRing(QQ,['a','b']))
sage: R21 = F2['x']
sage: R22 = F2['x','y']
```


Here I try various conversions, some of them go boom:

```
sage: F1('a')
a
sage: F2('a')
a
sage: R11('a')
a
sage: R12('a')
Traceback (most recent call last):
...
TypeError: unable to convert string
sage: R21('a')
a
sage: R22('a')
Traceback (most recent call last):
...
TypeError: unable to convert string
sage: R11(F1('a'))
a
sage: R12(F1('a'))
a
sage: R21(F2('a'))
a
sage: R22(F2('a'))
a
sage: F1(R11(F1('a')))
a
sage: F1(R12(F1('a')))
Traceback (most recent call last)
...
TypeError: unable to convert a to a rational
sage: F2(R21(F2('a')))
a
sage: F2(R22(F2('a')))
Traceback (most recent call last)
...
TypeError:
```


Note that in the last example there is no error message. So, it seems to be different from the previous error ("unable to convert a to a rational")

*__Conclusion:__*
 * Conversion from string to fraction field is OK both with one and two variables.
 * Conversion from a string to a univariate polynomial ring over a fraction field works, but fails for multivariate polynomial rings over a fraction field.
 * Conversion from a fraction field to a polynomial ring over this fraction field works both uni- and multivariately.
 * Conversion of a _scalar_ element of a _multivariate_ polynomial ring over a fraction field into that fraction field fails. The univariate case seems ok. The error seems to depend on the number of variables of the fraction field.

Since conversion is something very elementary, I consider it a critical bug if it does not work (but not a blocker since it doesn't affect coercion). 

Probably it is too late for sage-3.4.2, so, I give it the Milestone 4.0.


---

Comment by Bouillaguet created at 2013-01-03 10:26:53

This has (apparently?) been fixed. At the very least, in sage 5.5 these examples no longer raise any exceptions...


---

Comment by Bouillaguet created at 2013-01-03 10:26:53

Changing status from new to needs_review.


---

Comment by Bouillaguet created at 2013-01-04 16:29:30

Add doctest to make sure it won't happen again


---

Comment by Bouillaguet created at 2013-01-04 16:30:09

Changing keywords from "polynomial ring fraction field conversion" to "polynomial ring fraction field conversion trivial beginner".


---

Attachment


---

Comment by SimonKing created at 2013-01-21 11:00:38

Since the patchbot does not complain and the added tests do ensure that the bug remains fixed, I'm giving it a positive review.


---

Comment by SimonKing created at 2013-01-21 11:00:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-25 13:06:01

Resolution: fixed
