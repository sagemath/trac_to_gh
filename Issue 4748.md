# Issue 4748: pass to quotient ring for exp

Issue created by migration from https://trac.sagemath.org/ticket/4748

Original creator: robertwb

Original creation time: 2008-12-10 00:08:49

Assignee: somebody

This works

```
sage: sqrt(1+x+O(x^5))
1 + 1/2*x - 1/8*x^2 + 1/16*x^3 - 5/128*x^4 + O(x^5)
```


One would expect this to work: 


```
sage: R.<x> = ZZ[[]]
sage: exp(x+O(x^5))
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 8415, in __call__
    return x.exp()
  File "power_series_ring_element.pyx", line 1383, in sage.rings.power_series_ring_element.PowerSeries.exp (sage/rings/power_series_ring_element.c:9850)
  File "power_series_ring_element.pyx", line 1305, in sage.rings.power_series_ring_element.PowerSeries.solve_linear_de (sage/rings/power_series_ring_element.c:9707)
  File "power_series_ring_element.pyx", line 1648, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11103)
  File "power_series_ring_element.pyx", line 1650, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11124)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 252, in __call__
    return C(self, x, check, is_gen, construct=construct)
  File "polynomial_integer_dense_flint.pyx", line 224, in sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint.__init__ (sage/rings/polynomial/polynomial_integer_dense_flint.cpp:4981)
  File "parent.pyx", line 293, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3828)
  File "parent.pyx", line 284, in sage.structure.parent.__call__ (sage/structure/parent.c:3712)
  File "rational.pyx", line 2288, in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:14682)
TypeError: no conversion of this rational to integer
```



---

Comment by mvngu created at 2009-07-26 04:34:10

Both don't work:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sqrt(1+x+O(x^5))
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/.sage/temp/sage.math.washington.edu/14884/_home_mvngu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/big_oh.pyc in O(x)
     85     elif isinstance(x, padic_generic_element.pAdicGenericElement):
     86          return x.parent()(0, absprec = x.valuation())
---> 87     raise ArithmeticError, "O(x) not defined"
     88 
     89 

ArithmeticError: O(x) not defined
sage: R.<x> = ZZ[[]]
sage: exp(x+O(x^5))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/14884/_home_mvngu__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/functions/log.pyc in __call__(self, x, prec)
     68         if not isinstance(x, (Integer, Rational)):
     69             try:
---> 70                 return x.exp()
     71             except AttributeError:
     72                 pass

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element.PowerSeries.exp (sage/rings/power_series_ring_element.c:13120)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element.PowerSeries.solve_linear_de (sage/rings/power_series_ring_element.c:12933)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:14864)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4150)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3448)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_with_args (sage/structure/coerce_maps.c:3262)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)
    310                 x = x.Polrev()
    311 
--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)
    313 
    314     def is_integral_domain(self):

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_integer_dense_flint.so in sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint.__init__ (sage/rings/polynomial/polynomial_integer_dense_flint.cpp:5367)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:21689)()

TypeError: no conversion of this rational to integer
```



---

Comment by robertwb created at 2009-07-27 10:43:21

I meant 


```
sage: R.<x> = ZZ[]   
sage: sage: sqrt(1+x+O(x^5))
1 + 1/2*x - 1/8*x^2 + 1/16*x^3 - 5/128*x^4 + O(x^5)
```

