# Issue 3272: [with patch, needs review] Bug in sparse polynomials over finite fields

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-05-22 21:49:12

Assignee: craigcitro

Someone reported the following bug on `sage-support`:


```
sage: A.<T> = PolynomialRing(Integers(5),sparse=True)
sage: f = T^2+1
sage: B = A.quo(f)
sage: C.<s> = PolynomialRing(B)
Univariate Quotient Polynomial Ring in Tbar over Ring of integers
modulo 5 with modulus T^2 + 1
Traceback (most recent call last):
...
TypeError: gen must be of PARI type t_INT
```


The problem was two-fold: `polynomial_element_generic.__init__` had two `elif` clauses in the wrong order (so that the code for pari `gen`s was never run), and further the code for pari `gen`s was wrong. This patch fixes both, and adds a doctest.




---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-05-23 07:05:08

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 07:05:08

Merged in Sage 3.0.2.rc0
