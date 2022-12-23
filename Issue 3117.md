# Issue 3117: bug in quotient polynomial rings when using funny term order

Issue created by migration from https://trac.sagemath.org/ticket/3117

Original creator: was

Original creation time: 2008-05-07 03:08:55

Assignee: malb

Hi,

Whether or not an element of R/I is zero must not depend on the term order. However, behold:

```
sage: R.<x,y> = PolynomialRing(QQ, order='neglex')
sage: Q.<xbar,ybar> = R.quotient(y^2 - x^3 - x -1)
sage: xbar
0
```


whereas

```
sage: R.<x,y> = PolynomialRing(QQ, order='lex')
sage: Q.<xbar,ybar> = R.quotient(y^2 - x^3 - x -1)
sage: xbar
xbar
sage: xbar != 0
True
```


NOTE: I don't even know what neglex is ("negative lex", whatever that is). 



---

Comment by malb created at 2008-05-07 07:50:25

neglex is a local ordering (x < 1) and thus I'm not sure what the expected result should be. See

 http://www.sagemath.org/doc/html/ref/module-sage.rings.polynomial.term-order.html

for details on neglex.


---

Comment by malb created at 2008-06-03 14:52:59

Resolution: invalid


---

Comment by malb created at 2008-06-03 14:52:59

Michael Brickenstein wrote (my translation):

```
y^2 - x^3 - x -1
is a unit in Singular if you calculate in 'ls'. If you take a quotient of 
that zero is the answer.

Singular there works with the localisation of the polynomial ring 
by all polynomials with constant leading term. Check a commutative 
algebra book about localisation.
```

