# Issue 8498: bug in has_good_reduction for a point on an elliptic curve over a number field

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2010-03-11 10:39:16

Assignee: cremona

Jean Gillibert reported me the following bug. Define


```
E = EllipticCurve('11a1')
K.<t> = NumberField(x^2+47)
EK = E.base_extend(K)
T = EK(5,5)
P = EK(-2, -1/2*t - 1/2)
p = K.ideal(11)
```


Then the following works fine


```
sage: T.has_good_reduction(p)
False
```


but not this one :


```
P.has_good_reduction(p)
```




---

Comment by wuthrich created at 2010-03-11 10:39:56

More precisely, I get the error


```
/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_point.pyc in has_good_reduction(self, P)
   1554         F = Emin.defining_polynomial()
   1555         for v in F.variables():
-> 1556             if F.derivative(v)(xyz).valuation(P) == 0:
   1557                 return True
   1558         return False

/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2743)()

/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2844)()

/home/pmzcw/prog/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)()

AttributeError: 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular' object has no attribute 'valuation'
```



---

Comment by cremona created at 2010-03-11 13:27:22

I'll look into this -- my code :(


---

Comment by cremona created at 2010-03-11 14:40:50

This is weird:  I evaluate a polynomial f in K[X,Y,Z] at a triple [x,y,z], but the value lands up not in K but in K[X,Y,Z] again (as a constant polynomial, rather than an actual constant in K).  This is not what the `_call__` function for multivariable polynomials says.  I can fix this here, but it is symptomatic of a deeper problem.


---

Attachment

Applies to 4.3.4.alpha1


---

Comment by cremona created at 2010-03-11 15:26:08

Patch attached, applies to 4.3.4.alpha1.  I tested everything in sage/schemes/elliptic curves, and included a doctest example showing that the example above now works.


---

Comment by cremona created at 2010-03-11 15:26:08

Changing status from new to needs_review.


---

Comment by cremona created at 2010-03-11 15:26:08

Changing keywords from "" to "good reduction points".


---

Comment by wuthrich created at 2010-03-11 21:12:24

All tests pass. Thanks for the very fast resolution of this.

As you said, the patch fixes the problem for the `has_good_reduction` function, but the same issue may arise else where. Could you open another ticket for the general problem ?


---

Comment by wuthrich created at 2010-03-11 21:12:24

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-03-11 22:08:54

Replying to [comment:5 wuthrich]:
> All tests pass. Thanks for the very fast resolution of this.
> 
> As you said, the patch fixes the problem for the `has_good_reduction` function, but the same issue may arise else where. Could you open another ticket for the general problem ?

See #8502


---

Comment by mvngu created at 2010-03-12 04:53:11

Resolution: fixed
