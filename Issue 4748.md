# Issue 4748: pass to quotient ring for exp

archive/issues_004748.json:
```json
{
    "body": "Assignee: somebody\n\nThis works\n\n```\nsage: sqrt(1+x+O(x^5))\n1 + 1/2*x - 1/8*x^2 + 1/16*x^3 - 5/128*x^4 + O(x^5)\n```\n\n\nOne would expect this to work: \n\n\n```\nsage: R.<x> = ZZ[[]]\nsage: exp(x+O(x^5))\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 8415, in __call__\n    return x.exp()\n  File \"power_series_ring_element.pyx\", line 1383, in sage.rings.power_series_ring_element.PowerSeries.exp (sage/rings/power_series_ring_element.c:9850)\n  File \"power_series_ring_element.pyx\", line 1305, in sage.rings.power_series_ring_element.PowerSeries.solve_linear_de (sage/rings/power_series_ring_element.c:9707)\n  File \"power_series_ring_element.pyx\", line 1648, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11103)\n  File \"power_series_ring_element.pyx\", line 1650, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11124)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 252, in __call__\n    return C(self, x, check, is_gen, construct=construct)\n  File \"polynomial_integer_dense_flint.pyx\", line 224, in sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint.__init__ (sage/rings/polynomial/polynomial_integer_dense_flint.cpp:4981)\n  File \"parent.pyx\", line 293, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3828)\n  File \"parent.pyx\", line 284, in sage.structure.parent.__call__ (sage/structure/parent.c:3712)\n  File \"rational.pyx\", line 2288, in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:14682)\nTypeError: no conversion of this rational to integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4748\n\n",
    "created_at": "2008-12-10T00:08:49Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "pass to quotient ring for exp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4748",
    "user": "robertwb"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/4748





---

archive/issue_comments_035935.json:
```json
{
    "body": "Both don't work:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sqrt(1+x+O(x^5))\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n| Sage Version 4.1, Release Date: 2009-07-09                         |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mvngu/.sage/temp/sage.math.washington.edu/14884/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/big_oh.pyc in O(x)\n     85     elif isinstance(x, padic_generic_element.pAdicGenericElement):\n     86          return x.parent()(0, absprec = x.valuation())\n---> 87     raise ArithmeticError, \"O(x) not defined\"\n     88 \n     89 \n\nArithmeticError: O(x) not defined\nsage: R.<x> = ZZ[[]]\nsage: exp(x+O(x^5))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/mvngu/.sage/temp/sage.math.washington.edu/14884/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/functions/log.pyc in __call__(self, x, prec)\n     68         if not isinstance(x, (Integer, Rational)):\n     69             try:\n---> 70                 return x.exp()\n     71             except AttributeError:\n     72                 pass\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element.PowerSeries.exp (sage/rings/power_series_ring_element.c:13120)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element.PowerSeries.solve_linear_de (sage/rings/power_series_ring_element.c:12933)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/power_series_ring_element.so in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:14864)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4150)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_with_args (sage/structure/coerce_maps.c:3448)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_with_args (sage/structure/coerce_maps.c:3262)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring.pyc in _element_constructor_(self, x, check, is_gen, construct, **kwds)\n    310                 x = x.Polrev()\n    311 \n--> 312         return C(self, x, check, is_gen, construct=construct, **kwds)\n    313 \n    314     def is_integral_domain(self):\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_integer_dense_flint.so in sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint.__init__ (sage/rings/polynomial/polynomial_integer_dense_flint.cpp:5367)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4130)()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:21689)()\n\nTypeError: no conversion of this rational to integer\n```\n",
    "created_at": "2009-07-26T04:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4748#issuecomment-35935",
    "user": "mvngu"
}
```

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

archive/issue_comments_035936.json:
```json
{
    "body": "I meant \n\n\n```\nsage: R.<x> = ZZ[]   \nsage: sage: sqrt(1+x+O(x^5))\n1 + 1/2*x - 1/8*x^2 + 1/16*x^3 - 5/128*x^4 + O(x^5)\n```\n",
    "created_at": "2009-07-27T10:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4748#issuecomment-35936",
    "user": "robertwb"
}
```

I meant 


```
sage: R.<x> = ZZ[]   
sage: sage: sqrt(1+x+O(x^5))
1 + 1/2*x - 1/8*x^2 + 1/16*x^3 - 5/128*x^4 + O(x^5)
```

