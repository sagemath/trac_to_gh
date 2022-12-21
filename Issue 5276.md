# Issue 5276: bug in creating polynomial ring over some rings of integers

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-02-15 10:57:05

Assignee: was

Keywords: ring of integers, polynomial ring

This happened to me in 3.3.rc0:


```
sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1])
sage: OK = K.ring_of_integers()
sage: S.<y> = OK[]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/12662/_home_ghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2402)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    281                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    282             name = arg1
--> 283             R = _single_variate(base_ring, name, sparse, implementation)
    284         else:
    285             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    372 
    373         elif base_ring.is_integral_domain():
--> 374             R = m.PolynomialRing_integral_domain(base_ring, name, sparse, implementation)
    375         else:
    376             R = m.PolynomialRing_commutative(base_ring, name, sparse)

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in __init__(self, base_ring, name, sparse, implementation, element_class)
   1041                     raise ValueError, "Unknown implementation %s for ZZ[x]"
   1042         PolynomialRing_commutative.__init__(self, base_ring, name=name,
-> 1043                 sparse=sparse, element_class=element_class)
   1044     
   1045     def _repr_(self):

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in __init__(self, base_ring, name, sparse, element_class)
    994             raise TypeError, "Base ring must be a commutative ring."
    995         PolynomialRing_general.__init__(self, base_ring, name=name,
--> 996                 sparse=sparse, element_class=element_class)
    997 
    998     def quotient_by_principal_ideal(self, f, names=None):

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in __init__(self, base_ring, name, sparse, element_class)
    177                 from sage.rings.polynomial import polynomial_element
    178                 self._polynomial_class = polynomial_element.Polynomial_generic_dense
--> 179         self.__generator = self._polynomial_class(self, [0,1], is_gen=True)
    180         self.__cyclopoly_cache = {}
    181         self._has_singular = False

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__ (sage/rings/polynomial/polynomial_element.c:29516)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc in __call__(self, x)
   1190         Coerce an element into this relative order.
   1191         """
-> 1192         if x.parent() is not self._K:
   1193             x = self._K(x)
   1194         x = self._absolute_order(x) # will test membership

AttributeError: 'int' object has no attribute 'parent'
```




---

Comment by fwclarke created at 2009-03-13 19:05:23

The problem is solved by changes to `__call__` for the class `RelativeOrder` in `sage/rings/number_theory/order.py` to be found in #5508.


---

Comment by mabshoff created at 2009-03-25 08:55:22

To close this we would need a doctest.

Cheers,

Michael


---

Comment by fwclarke created at 2009-03-26 08:49:47

Replying to [comment:2 mabshoff]:
> To close this we would need a doctest.

See lines 1194 to 1204 of sage/rings/number_field/order.py as patched by 
#5508:

```
            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1]) 
            sage: OK = K.ring_of_integers()
            ...

        The following used to fail; see trac #5276::

            sage: S.<y> = OK[]; S
            Univariate Polynomial Ring in y over Relative Order in Number Field in a with defining polynomial x^2 + 2 over its base field
```



---

Comment by mabshoff created at 2009-03-26 20:36:14

Fixed in Sage 3.4.1.alpha0 via #5508. Thanks Francis :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 20:36:14

Resolution: fixed
