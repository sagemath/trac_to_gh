# Issue 5451: Bug in addition of rational functions over a finite field

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-03-07 14:35:16

Assignee: tbd

Keywords: rational function addition

Alex Lara reported on sage-support on 20090307:

```
I recently upgrade sage from 3.2.3 to 3.3. I'm also have sage 3.1.1
The thing is that the following commands give different results:

F.<theta>=FiniteField(9)
A.<t> = PolynomialRing(F)
K.<t> = FractionField(A)
f= 2/(t^2+2*t); g =t^9/(t^18 + t^10 + t^2);f+g

In 3.1.1 gives the right answer (I guess) but in 3.2.3 give an error:

ZeroDivisionError                         Traceback (most recent call
last)
...
ZeroDivisionError: division by zero in finite field.
```


In more detail that traceback is

```
ZeroDivisionError                         Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/30503/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.__add__ (sage/structure/element.c:5746)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement._add_ (sage/rings/fraction_field_element.c:3975)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.PrincipalIdealDomainElement.gcd (sage/structure/element.c:11697)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in _gcd(self, other)
    558         Return the GCD of self and other, as a monic polynomial.
    559         """
--> 560         g = EuclideanDomainElement._gcd(self, other)
    561         c = g.leading_coefficient()
    562         if c.is_unit():

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.EuclideanDomainElement._gcd (sage/structure/element.c:11939)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in quo_rem(self, other)
    542         Q = P.zero_element()
    543         while R.degree() >= B.degree():
--> 544             aaa = R.leading_coefficient()/B.leading_coefficient()
    545             diff_deg=R.degree()-B.degree()
    546             Q += P(aaa).shift(diff_deg)

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9099)()

/home/john/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/finite_field_givaro.so in sage.rings.finite_field_givaro.FiniteField_givaroElement._div_ (sage/rings/finite_field_givaro.cpp:9661)()

ZeroDivisionError: division by zero in finite field.
```


which shows that somewhere in a gcd computation, a leading coefficient of 0 is being returned.


---

Comment by cremona created at 2009-03-07 14:54:41

In sage/rings/polynomial/polynomial_ring_generic.py, in the function quo_rem, the test of other.is_zero() is sometimes returning False despite other being zero!  I added some print statements and here is an example:

```
in quo_rem (parent = Univariate Polynomial Ring in t over Finite Field in theta of size 3^2)...
self =  t
other =  0
other.is_zero() =  False
A =  t
B =  0
---------------------------------------------------------------------------
ZeroDivisionError  
```


That is as far as I got.


---

Comment by ylchapuy created at 2009-03-07 15:18:24

Replying to [comment:1 cremona]:

This is a consequence of this:

```
sage: A.<x>=GF(9,'a')[]
sage: A(0).shift(7).degree()
6
```



---

Comment by ylchapuy created at 2009-03-07 15:21:55

Replying to [comment:2 ylchapuy]:
replying to myself: see also #5434


---

Comment by cremona created at 2009-03-07 15:30:01

Thanks ylchpuy: I checked that applying the patch at 5434 makes this problem go away.

Hence this ticket can be scrapped, unless we want to add a doctest somewhere.


---

Comment by cremona created at 2009-03-09 13:18:53

In a newly built 3.4.rc1 I can conform that the problem has indeed been solved by the other bug fix mentioned in this ticket:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<theta>=FiniteField(9)
sage: A.<t> = PolynomialRing(F)
sage: K.<t> = FractionField(A)
sage: f= 2/(t^2+2*t); g =t^9/(t^18 + t^10 + t^2);f+g
(2*t^15 + 2*t^14 + 2*t^13 + 2*t^12 + 2*t^11 + 2*t^10 + 2*t^9 + t^7 + t^6 + t^5 + t^4 + t^3 + t^2 + t + 1)/(t^17 + t^9 + t)
```

| Sage Version 3.4.rc1, Release Date: 2009-03-08                     |
| Type notebook() for the GUI, and license() for information.        |
This ticket can therefore be closed.


---

Comment by burcin created at 2009-03-25 17:55:48

Resolution: fixed


---

Comment by burcin created at 2009-03-25 17:55:48

This ticket seems to have slipped under mabshoff's radar. I can verify that it is fixed in 3.4.


---

Comment by mabshoff created at 2009-03-25 19:05:58

Hmm, what about a doctest then?

Cheers,

Michael


---

Attachment

add doctest


---

Comment by burcin created at 2009-03-25 20:33:16

Right, nothing gets past you. :)

attachment:trac_5451-ratfun_doctest.patch adds the doctest.

Cheers,
Burcin


---

Comment by burcin created at 2009-03-25 20:33:16

Changing status from closed to reopened.


---

Comment by burcin created at 2009-03-25 20:33:16

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-03-25 22:18:58

Looks good to me. This is consistent with the result from Sage 3.2 :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 23:01:45

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 23:01:45

Resolution: fixed
