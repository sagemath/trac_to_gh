# Issue 6431: no call method from Laurent series into Power series ring

Issue created by migration from https://trac.sagemath.org/ticket/6431

Original creator: ncalexan

Original creation time: 2009-06-27 04:39:42

Assignee: malb

CC:  robertwb was

Keywords: Laurent series power series call method


```
sage: CDF[['t']]( ~(~CDF[['t']].gen()^2) )
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/Documents/School/period_matrix/riemann_surface.py in <module>()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/power_series_ring.pyc in __call__(self, f, prec, check)
    378             v = sage_eval(f.Eltseq())
    379             return self(v) * (self.gen(0)**f.Valuation())
--> 380         return self.__power_series_class(self, f, prec, check=check)
    381         
    382     def construction(self):

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/power_series_poly.so in sage.rings.power_series_poly.PowerSeries_poly.__init__ (sage/rings/power_series_poly.c:2307)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4150)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3448)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_with_args (sage/structure/coerce_maps.c:3262)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    310                 x = x.Polrev()
    311 
--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)
    313 
    314     def is_integral_domain(self):

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element_generic.pyc in __init__(self, parent, x, check, is_gen, construct)
    581 class Polynomial_generic_dense_field(Polynomial_generic_dense, Polynomial_generic_field):
    582     def __init__(self, parent, x=None, check=True, is_gen = False, construct=False):
--> 583         Polynomial_generic_dense.__init__(self, parent, x, check, is_gen)
    584 
    585 

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__ (sage/rings/polynomial/polynomial_element.c:35169)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleField_class.__call__ (sage/rings/complex_double.c:3596)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3058)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2949)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleField_class._element_constructor_ (sage/rings/complex_double.c:4022)()

/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/rings/complex_double.so in sage.rings.complex_double.ComplexDoubleElement.__init__ (sage/rings/complex_double.c:5765)()

TypeError: a float is required
```



---

Comment by rws created at 2014-03-15 15:07:46

I think that the problem here is not the failing conversion from Laurent series to polynomial but that the construction `CDF[This is the Trac macro *'t'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'t'-macro)(..)` (or substitute any other ring) tries to convert to `CDF` not `CDF[This is the Trac macro *'t'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'t'-macro)` as expected. Right?


---

Comment by pbruin created at 2014-04-11 16:45:41

No, the problem is that `PowerSeriesRing._element_constructor_(self, f)` does not currently accept Laurent series.  Here is another example:

```
sage: L.<q> = LaurentSeriesRing(QQ)
sage: P = L.power_series_ring()
sage: P(q)
Traceback (most recent call last):
...
TypeError: Unable to coerce q (<type 'sage.rings.laurent_series_ring_element.LaurentSeries'>) to Rational
```

Working on a patch...


---

Comment by pbruin created at 2014-04-11 18:04:51

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-04-13 08:05:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-14 16:55:55

Resolution: fixed
