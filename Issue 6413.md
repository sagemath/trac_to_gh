# Issue 6413: Retrieving the multiplication-by-p isogeny on elliptic curves over fields of characteristic p fails.

Issue created by migration from Trac.

Original creator: hlaw

Original creation time: 2009-06-25 18:23:38

Assignee: tba

CC:  defeo jpflori lorenz


```
sage: p = 11
sage: E = EllipticCurve(GF(p), [1,1])
sage: E.multiplication_by_m(p)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/hlaw/.sage/temp/resid_tg082.upc.es/80890/_Users_hlaw__sage_init_sage_0.py in <module>()

/Users/hlaw/src/sage-4.0.1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.pyc in multiplication_by_m(self, m, x_only)
   2133         #  and hence 2*my+a1*mx+a3 = (1/m)*(2*y+a1*x+a3)*d(mx)/dx
   2134 
-> 2135         my = ((2*y+a1*x+a3)*mx.derivative(x)/m - a1*mx-a3)/2
   2136 
   2137         return mx, my

/Users/hlaw/src/sage-4.0.1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10361)()

/Users/hlaw/src/sage-4.0.1/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6105)()

/Users/hlaw/src/sage-4.0.1/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10342)()

/Users/hlaw/src/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement._div_ (sage/rings/fraction_field_element.c:5805)()

/Users/hlaw/src/sage-4.0.1/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement.__init__ (sage/rings/fraction_field_element.c:1954)()

ZeroDivisionError: fraction field element division by zero
```

One can see from the line that causes the error that the calculation of the _y_-component of the isogeny involves a division by _m_, which in this case is the characteristic of the ground field.



---

Comment by cremona created at 2009-07-09 08:30:21

I wrote the offending line of code, knowing full well that it would not work in the inseparable case.  I may or may not have made a ticket at the time, but likely not.

When someone writes code to deal with the inseparable case, just make sure that it continues to be efficient in the separable case!


---

Comment by AlexGhitza created at 2010-01-01 23:39:12

Changing component from algebraic geometry to elliptic curves.
