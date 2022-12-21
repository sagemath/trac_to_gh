# Issue 484: multivariate polynomial coercion bug

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2007-08-23 16:53:19

Assignee: was


```
sage: x,y=PolynomialRing(QQ,2,"xy").gens()
sage: f = 5*x+y-5
sage: f(1,1)
 1
sage: type(f(1,1))
 <type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
```


I usually think of the values of a polynomial as belonging to the
ground ring as opposed to the polynomial ring.


---

Comment by mabshoff created at 2007-08-30 12:21:45

Works for me now:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.3.alpha2, Release Date: 2007-08-29                |
| Type notebook() for the GUI, and license() for information.        |
sage: x,y=PolynomialRing(QQ,2,"xy").gens()
sage: f = 5*x+y-5
sage: f(1,1)
1
sage: type(f(1,1))
<type 'sage.rings.rational.Rational'>
```


I guess credit should go to Robert or William.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 12:21:45

Changing component from algebraic geometry to basic arithmetic.


---

Comment by mabshoff created at 2007-08-30 12:21:45

Resolution: fixed
