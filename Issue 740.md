# Issue 740: Implement standard transformations for elliptic curves & points

Issue created by migration from https://trac.sagemath.org/ticket/740

Original creator: cremona

Original creation time: 2007-09-23 18:04:16

Assignee: John Cremona

Keywords: elliptic curve point

Implement standard transformations for elliptic curves & points similar to pari's ellchangecurve()/ellchangepoint() with the following functionality, to apply to class EllipticCurve_generic and class EllipticCurvePoint().

Functionality:
(1) basic operations on transformations coded as [u,r,s,t] with u!=0, including composition and inversion (since they form a group)
(2) apply transform to a curve to get a new curve
(3) apply transform to a point to get a new point (since points belong to curves this would create the transformed curve too, which seems a waste)
(4) given two curves, test whether they are isomorphic and return either "false" or "true, [u,r,s,t]", probably only in characteristic>3 at first.

This should be very easy (and in fact is contained in the functionality provided by /extcode/pari/cremona/ell_utils.gp  but the intention is to do it in python as a simple thing for me to practice on before I try to do something more substantial.


---

Comment by cremona created at 2007-09-23 21:43:29

Changing assignee from John Cremona to cremona.


---

Comment by robertwb created at 2007-12-05 19:00:47

Changing priority from minor to major.


---

Comment by robertwb created at 2007-12-05 19:00:47

Done, at least for characteristic != 2,3. See #1239.


---

Comment by cremona created at 2008-01-09 21:43:36

Elliptic curve isomorphism code only works when the characteristic is not 2 or 3.  I expect to submit a patch shortly.


```
jec@fermat%sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.3, Release Date: 2008-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: E=EllipticCurve(GF(2),[1,0,0,0,1])
sage: E.is_isomorphic(E)
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/home/src/sage-2.9.1.1/devel/<ipython console> in <module>()

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in is_isomorphic(self, other)
   1337         else:
   1338             try:
-> 1339                 phi = self.isomorphism_to(other)
   1340                 return True
   1341             except ValueError:

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in isomorphism_to(self, other)
   1315                 To:   Abelian group of points on Elliptic Curve defined by y^2 + y = x^3 + (-1)*x over Number Field in a with defining polynomial x^3 - 7
   1316         """
-> 1317         return weierstrass_morphism.WeierstrassIsomorphism(self, other)
   1318
   1319     def is_isomorphic(self, other):

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/weierstrass_morphism.py in __init__(self, E, F)
     46             if u.parent() is not K or K.is_exact() and u**12 != D:
     47                 raise ValueError, "Elliptic curves not isomorphic."
---> 48             s = (a1*u - b1)/2
     49             r = (a2*u**2 + a1*s*u - s**2 - b2)/3
     50             t = (a3*u**3 - a1*r*u + 2*r*s - b3)/2

/home/src/sage-2.9.1.1/devel/element.pyx in sage.structure.element.RingElement.__div__()

/home/src/sage-2.9.1.1/devel/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/home/src/sage-2.9.1.1/devel/element.pyx in sage.structure.element.RingElement.__div__()

/home/src/sage-2.9.1.1/devel/coerce.pxi in sage.structure.element._div_c()

/home/src/sage-2.9.1.1/devel/integer_mod.pyx in sage.rings.integer_mod.IntegerMod_int._div_c_impl()

<type 'exceptions.ZeroDivisionError'>: Inverse does not exist.
```



---

Comment by cremona created at 2008-01-10 09:27:05

It's also broken for characteristics >3:

```
jec@fermat%sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.3, Release Date: 2008-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: F=GF(13) # contains 12th roots of unity
sage: z=F.multiplicative_generator()
sage: E=EllipticCurve(F,[1,0,0,0,1])
sage: Ez=E.change_weierstrass_model([z,0,0,0])
sage: E.is_isomorphic(Ez)
False
```


The patch I will post will do this properly.


---

Attachment

Attached patch fixes the bugs (was made against 2.9.3)


---

Comment by robertwb created at 2008-01-25 21:07:24

The bundle applies cleanly, and for the most part looks good, including all the characteristic 2,3 stuff. However, I am having trouble testing it out too much because of all of the "return none" (note the lowercase, rather than capital N). This seems to indicate that there are insufficient doctests as well. Could you please re-submit a bundle with these fixes (and also, that doesn't mix TABS and SPACES). 

It looks like your (u,r,s,t) is the inverse of what my (u,r,s,t) was, but that shouldn't matter as long as people haven't started depending on this directly. 

For things that extend Morphism, `_call_` is used rather than `__call__` For efficiency reasons (e.g. in the coercion model), so this needs to be changed back. 


```
# I don't know how to make this function visible in Sage!  JEC 
```


You were able to resolve this, right?


```
# IMHO the restriction to curves having the same base ring is too strict!  JEC 
```


I would like others to comment on this, but it seems to me that clearly one has non-isomorphic objects if one changes the base ring. The current implementation of `EllipticCurve` represents an elliptic curve over a fixed base field (hence it makes sense to ask about it's rank, etc.) 

(In response to `EllipticCurve_generic.integral_weierstrass_model()`)

```
### The following functions should not be in ell_generic.py but in ell_rational_field.py!  JEC 
```

This makes sense for elliptic curves over number fields too, right? Or any field in which one can construct the ring of integers). 


```
###  I do not think we should allow quadratic_twist() in characteristic 2, or when j=0 or j=1728.  JEC 
}}} 
Should we throw an error, or indicate (in the docstring or elsewhere) that the result may not be uniquely determined?


---

Attachment

This coimpletely replaces the previous patch (eciso.hg)


---

Attachment

Minor additional patch to 8087.patch (fix 2 doctests)


---

Comment by robertwb created at 2008-01-29 04:53:07

Looks really good to me! I even agree that this is the correct way to handle different base fields 


```
sage: K = NumberField(x^2-17, 'a')
sage: EK = E.change_ring(K)
sage: E.is_isomorphic(EK)
False
sage: E.isomorphism_to(EK)

Generic morphism:
  From: Abelian group of points on Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 - 10*x - 10 over Rational Field
  To:   Abelian group of points on Elliptic Curve defined by y^2 + x*y + y = x^3 + x^2 + (-10)*x + (-10) over Number Field in a with defining polynomial x^2 - 17
  Via:  (u,r,s,t) = (1, 0, 0, 0)
```


Ready for inclusion.


---

Comment by mabshoff created at 2008-01-29 12:29:06

Resolution: fixed


---

Comment by mabshoff created at 2008-01-29 12:29:06

Merged 8087.patch and 8088.patch in Sage 2.10.1.rc3
