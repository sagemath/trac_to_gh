# Issue 2146: PolyBoRi random_element is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-13 03:49:00

Assignee: malb

CC:  malb

See below. 


```
sage: R.<x,y,z> = BooleanPolynomialRing(3)
sage: R.random_element()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/multi_polynomial_ring_generic.pyx in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.random_element()

/Users/was/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialRing.__call__()

<type 'exceptions.TypeError'>: cannot convert <type 'dict'> to BooleanPolynomial
sage: 

```


By the way, wouldn't it be better to call it `PolynomialBooleanRing` instead
of `BooleanPolynomialRing`?  I suggest this for two reasons:
   1. It is PolyBoRi, after all, not BoPolyRi.
   2. The other Sage polynomial ring(s) starts with "Polynomial"


---

Comment by burcin created at 2008-02-13 18:05:43

Renaming `BooleanPolynomialRing` is now #2149.


---

Comment by burcin created at 2008-02-17 14:21:13

Add random_element to BooleanPolynomialRing


---

Attachment

attachment:2146-BooelanPolynomial_random_element.patch adds a `random_element` method to `BooleanPolynomialRing`.

The doctests for errors work only after applying the patch for `sage-doctest` at ticket:2193.


---

Comment by burcin created at 2008-02-17 16:40:48

Changing status from new to assigned.


---

Comment by burcin created at 2008-02-17 16:40:48

Changing assignee from malb to burcin.


---

Comment by ncalexan created at 2008-02-19 00:41:28

Looks good to me.

The docstrings are not formatted nicely -- they should be wrapped at 78 chars.


---

Comment by mabshoff created at 2008-02-19 15:02:22

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-19 15:02:22

Resolution: fixed
