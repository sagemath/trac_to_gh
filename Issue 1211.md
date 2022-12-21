# Issue 1211: NTL crash in polynomial remainder over ZZ

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-11-19 22:20:06

Assignee: malb

Keywords: ntl polynomial remainder ZZ crash segfault


```
sage: x = ZZ['x'].0
sage: x^2 % (2*x - 1)
DivRem: quotient not defined over ZZ
/Users/ncalexan/sage/local/bin/sage-sage: line 218: 28251 Abort trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"

Process SAGE exited abnormally with code 134
```


Mac OS X 10.4 Intel Core2Duo, Darwin mero.local 8.10.1 Darwin Kernel Version 8.10.1: Wed May 23 16:33:00 PDT 2007; root:xnu-792.22.5~1/RELEASE_I386 i386 i386


---

Comment by dmharvey created at 2007-12-01 15:11:14

Changing assignee from malb to dmharvey.


---

Comment by dmharvey created at 2007-12-01 15:11:14

Changing status from new to assigned.


---

Comment by dmharvey created at 2007-12-01 17:13:48

I'm about to attach a patch that fixes this (and also fixes division by zero crash too).


```
sage: R.<x> = PolynomialRing(ZZ)
sage: x^2 % (2*x - 1)
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/Users/david/sage-2.8.14/<ipython console> in <module>()

/Users/david/sage-2.8.14/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__mod__()

/Users/david/sage-2.8.14/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem()

<type 'exceptions.ArithmeticError'>: division not exact in Z[x] (consider coercing to Q[x] first)
sage: x^2 % 0
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/Users/david/sage-2.8.14/<ipython console> in <module>()

/Users/david/sage-2.8.14/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__mod__()

/Users/david/sage-2.8.14/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem()

<type 'exceptions.ArithmeticError'>: division by zero polynomial
sage: (2*x^2) % (2*x)
0
```



---

Attachment


---

Comment by cwitty created at 2007-12-01 23:33:26

Looks good, and all doctests still pass in sage/rings/polynomial/.


---

Comment by mabshoff created at 2007-12-02 00:14:53

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 00:14:53

Merged in 2.8.15.alpha2.
