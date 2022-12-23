# Issue 7930: strange bug for elliptic curves over number fields

Issue created by migration from https://trac.sagemath.org/ticket/7930

Original creator: wuthrich

Original creation time: 2010-01-14 15:00:57

Assignee: cremona

CC:  cremona was robertwb

The following code


```
E = EllipticCurve('99d1')

R.<X> = QQ[]
K.<t> = NumberField(X^3 + X^2 - 2*X - 1)
L.<s> = NumberField(X^3 + X^2 - 36*X - 4)

EK = E.base_extend(K)
toK = EK.torsion_order()
da = EK.local_data()

EL = E.base_extend(L)
da = EL.local_data()
```


produces a `TypeError`. Having played around with this for hours, I believe that all lines in the above code are necessary to produce the bug. Especially both the torsion and local data computations over another field. I have no idea whatsoever of where to look for the error.



---

Comment by wuthrich created at 2010-01-14 15:01:51

More precisely it produces

```
Traceback (most recent call last):    
  File "", line 1, in <module>
    
  File "/tmp/tmpJwKYhV/___code___.py", line 23, in <module>
    da = EK.local_data()
  File "", line 1, in <module>
    
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 437, in local_data
    return [self._get_local_data(pr, proof) for pr in primes]
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_number_field.py", line 487, in _get_local_data
    self._local_data[P, proof] = EllipticCurveLocalData(self, P, proof)
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 159, in __init__
    self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 704, in _tate
    cp = 1 + _pcubicroots(b, c, d)
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_local_data.py", line 536, in _pcubicroots
    return sum([rr[1] for rr in PolynomialRing(F, 'x')([d, c, b, 1]).roots()],0)
  File "parent.pyx", line 538, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3109)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:3000)
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.py", line 312, in _element_constructor_
    return C(self, x, check, is_gen, construct=construct, **kwds)
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element_generic.py", line 604, in __init__
    Polynomial_generic_dense.__init__(self, parent, x, check, is_gen)
  File "polynomial_element.pyx", line 5111, in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__ (sage/rings/polynomial/polynomial_element.c:34951)
  File "residue_field.pyx", line 975, in sage.rings.residue_field.ResidueFiniteField_givaro.__call__ (sage/rings/residue_field.c:9062)
TypeError
```



---

Comment by cremona created at 2010-01-14 16:10:48

In the middle of Tate's algorithm it needs to know how many roots a cubic mod P has, where P is the prime, and in doing this it constructs the polynomial ring over the residue field on the fly.  These poly rings are constructed in such a way that for each field the rings is only constructed once (I think).  the errors a re something which goes wrong in that construction.

I am CC'ing robertwb who I hope will be able to help!


---

Comment by robertwb created at 2010-01-14 18:31:12

No time to look t it now, but I've added this to my bug hit list for this upcoming week.


---

Comment by wuthrich created at 2010-01-24 15:49:45

Note that in #7935 we have added a #random to line 1026 in ell_number_field.py, because the output of the minimal_global_model produced two differnt answers. Maybe this is linked to this bug and the #random can be removed once the issue here is fixed.


  This is very strange. For that curve E2, I sometimes get
  {{{
  Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (12289755603565800754*a-75759141535687466985)*x + (51556320144761417221790307379*a-317814501841918807353201512829) over Number Field in a with defining polynomial x^2 - 38
  }}}
  but sometimes I get 
  {{{
  Elliptic Curve defined by y^2 + a*x*y + (a+1)*y = x^3 + (a+1)*x^2 + (368258520200522046806318444*a-2270097978636731786720859345)*x + (8456608930173478039472018047583706316424*a-52130038506793883217874390501829588391299) over Number Field in a with defining polynomial x^2 - 38
  }}}


---

Comment by cremona created at 2010-01-24 16:48:50

Note that E has bad reductions at 3 and 11, which are both inert in both those cubic fields.  That means that when we are finding the local data for each field, we construct the residue fields which are of order `3^3` and `11^3` in each case, but the generating polynomial (called the "modulus" in the finite field constructors) will be different, namely `X^3 + X^2 - 2*X - 1` and then `X^3 + X^2 - 36*X - 4`.

This might help debugging the session will have more than one field of the same order, with different defining polynomials.


---

Comment by wuthrich created at 2010-03-11 12:56:11

Any news on this ?


---

Comment by cremona created at 2010-06-24 15:37:37

This problem seems to have gone away now -- in 4.4.4 the above script works fine.  Can we close the ticket?


---

Comment by wuthrich created at 2010-06-24 17:04:15

Almost. Here is a patch that adds the example as a doctest (in a _function so as not to appear in the documentation) to make sure that the bug does not appear again in the future.
Because we are not certain what caused the bug in the first place.


---

Comment by wuthrich created at 2010-06-24 17:05:19

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-06-24 17:14:11

exported against 4.4.4.alpha0


---

Attachment

Looks good & tests fine on 4.4.4.alpha0.


---

Comment by cremona created at 2010-06-24 20:37:21

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-20 07:12:40

Resolution: fixed
