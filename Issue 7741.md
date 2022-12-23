# Issue 7741: Can't construct a rational fraction from a symbolic one.

Issue created by migration from https://trac.sagemath.org/ticket/7741

Original creator: hivert

Original creation time: 2009-12-19 09:12:57

Assignee: robertwb

CC:  burcin

Keywords: Fraction Field, coercion

Given a symbolic expression which is a rational fraction sage refuse to convert it to a element of the Field of rational fraction:

```
hivert@boxen:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: fr = (1+x)/(1+x+x^2)
sage: Fld = FractionField(PolynomialRing(QQ,x))
sage: Fld(fr)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1181, 0))
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
[...]

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

[...]

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    304                 x = x.numerator() * x.denominator().inverse_of_unit()
    305             else:
--> 306                 raise TypeError, "denominator must be a unit"
    307
    308         elif isinstance(x, pari_gen):

TypeError: denominator must be a unit
```


It seems that it needs to convert is to a polynomial. Of course if one convert numerator and denominator separately everything is Ok:

```
sage: Fld((1+x))/(1+x+x^2)
(x + 1)/(x^2 + x + 1)
```


I'm not sure about which component should be selected... Is it algebra, calculus or coercion...

Florent


---

Comment by robertwb created at 2010-01-17 10:04:02

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2010-01-17 11:49:25

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-18 22:45:09

Changing status from positive_review to needs_work.


---

Attachment

rebased to 4.4.4


---

Comment by davidloeffler created at 2010-06-29 09:42:08

Changing status from needs_work to needs_review.


---

Comment by demosd235 created at 2010-07-14 09:58:16

Changing status from needs_review to needs_work.


---

Comment by demosd235 created at 2010-07-14 09:58:16

William points out that `denominator is 1` will fail unless denominator is the Python int 1, and nothing else...

Is this really preferable to `denominator == 1`?

PS, Passes tests in `sage/rings/fraction_field_element.pyx`


---

Comment by robertwb created at 2010-07-29 05:47:35

Changing status from needs_work to needs_review.


---

Attachment

Actually, the "is 1" was intentional, as I wasn't thinking of taking that path if the user passed in a ring element (as opposed to the default value) and didn't want to make the default value None and handle it everywhere. In retrospect, I think it's fine for it to be equal to 1.


---

Comment by burcin created at 2010-09-25 10:49:32

apply only attachment:7741-symbolic-frac-fixed.patch.


---

Comment by burcin created at 2010-09-25 10:49:32

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-29 04:25:13

Resolution: fixed
