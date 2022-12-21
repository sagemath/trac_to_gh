# Issue 9182: Jacobian of a Hyperelliptic curve doesn't coerces correctly

Issue created by migration from Trac.

Original creator: aly.deines

Original creation time: 2010-06-08 00:37:34

Assignee: AlexGhitza

Keywords: Point, Hyperelliptic curve

When defining a point on the Jacobian of a Hyperellptic curve, 
if a coordinate is an integer, it does not get coerced to polynomial and the following error raised:
raise TypeError, "Argument P (= %s) must have length 2."%P
For example:

```
sage: F.<a> = GF(3)
sage: R.<x> = F[]
sage: f = x^5-1
sage: C = HyperellipticCurve(f)
sage: J = C.jacobian()
sage: X = J(F)
sage: a = x^2-x+1
sage: b = -x +1
sage: c = x-1
sage: d = 0 
sage: D1 = X([a,b])
sage: D2 = X([c,d])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/aly/Desktop/sage-4.3.1/<ipython console> in <module>()

/home/aly/Desktop/sage-4.3.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/jacobian_homset.py in __call__(self, P)
     86                 if is_SchemeMorphism(P1) and is_SchemeMorphism(P2):
     87                     return self(P1) - self(P2)
---> 88             raise TypeError, "Argument P (= %s) must have length 2."%P
     89         elif isinstance(P,JacobianMorphism_divisor_class_field) and self == P.parent():
     90             return P

TypeError: Argument P (= [x + 2, 0]) must have length 2.
sage: D2 = X([c,R(d)])                                                                               
sage: D2
(x + 2, y)


```



---

Comment by aly.deines created at 2010-06-08 00:54:17

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2010-06-08 13:47:24

Those double colon lines should look like they do in the examples here:

http://www.sagemath.org/doc/developer/conventions.html

Without those extra newlines, it won't process correctly. Also, the code coming after a double colon should be further indented than the colons.


---

Attachment


---

Comment by aly.deines created at 2010-06-08 15:01:20

Ok, changed.


---

Comment by rlm created at 2010-06-08 17:35:47

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-08 17:35:47

Changing priority from trivial to minor.


---

Comment by rlm created at 2010-06-08 17:35:47

Looks good to me.


---

Comment by mhansen created at 2010-06-09 02:34:10

Resolution: fixed
