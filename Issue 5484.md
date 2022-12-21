# Issue 5484: improve quotients of univariate polynomial rings

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-03-11 08:16:23

Assignee: was

CC:  jpflori

Roi Docampo and I noticed the following at Sage Days 14.

This works:

```
sage: R.<x,y> = ZZ[]
sage: R.quo(R.ideal(2))
Quotient of Multivariate Polynomial Ring in x, y over Integer Ring by the ideal (2)
```


But this doesn't:

```
sage: R.<x> = ZZ[]
sage: R.quo(R.ideal(2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/aghitza/.sage/temp/cartan/12118/_home_aghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.CommutativeRing.quo (sage/rings/ring.c:5717)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ring.so in sage.rings.ring.CommutativeRing.quotient (sage/rings/ring.c:5624)()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc in QuotientRing(R, I, names)
    120     try:
    121         if I.is_principal():
--> 122             return R.quotient_by_principal_ideal(I.gen(), names)
    123     except (AttributeError, NotImplementedError):
    124         pass

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.pyc in quotient_by_principal_ideal(self, f, names)
   1004         """
   1005         import sage.rings.polynomial.polynomial_quotient_ring
-> 1006         return sage.rings.polynomial.polynomial_quotient_ring.PolynomialQuotientRing(self, f, names)
   1007     
   1008 

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_quotient_ring.pyc in PolynomialQuotientRing(ring, polynomial, names)
    133     c = polynomial.leading_coefficient()
    134     if not c.is_unit():
--> 135         raise TypeError, "polynomial must have unit leading coefficient"
    136     R = ring.base_ring()
    137     if isinstance(R, sage.rings.integral_domain.IntegralDomain):

TypeError: polynomial must have unit leading coefficient
```




---

Comment by AlexGhitza created at 2009-03-11 08:26:02

Changing component from algebraic geometry to commutative algebra.


---

Comment by AlexGhitza created at 2009-03-11 08:26:02

Changing assignee from was to malb.


---

Comment by bruno created at 2015-04-22 15:21:15

Changing status from new to needs_review.


---

Comment by bruno created at 2015-04-22 15:21:15

I made the following proposition:

Suppose that `R = PolynomialRing(S,'x')` for some ring `S`, and `f` is a polynomial over `S`. 
* Keep the same thing if `f` has degree `> 0` or `f` is a unit, that is return `PolynomialQuotientRing(S, f, 'x')`;
* Return `PolynomialRing(S.quo(f), 'x')` when `f` is a non-unit constant.

In particular:

```
sage: R = ZZ['x']
sage: R.quo(2)
Univariate Polynomial Ring in x over Ring of integers modulo 2 (using NTL)
```


Does this make sense?
----
New commits:


---

Comment by chapoton created at 2015-06-01 07:52:18

doc does not build, see patchbot report

you wrongly replaced a TEST: by TEST::


---

Comment by chapoton created at 2015-06-01 07:52:18

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-06-01 08:51:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by bruno created at 2015-06-01 08:52:41

Changing status from needs_work to needs_review.


---

Comment by bruno created at 2015-06-01 08:52:41

Replying to [comment:9 chapoton]:
> doc does not build, see patchbot report
> 
> you wrongly replaced a TEST: by TEST::

Should work now. Sorry for the same mistake on two distinct tickets ;-)


---

Comment by darij created at 2015-06-06 22:04:01

Sorry, but the new quotient rings don't play well with the quotient ring interface (or what could be reasonably expected to be the quotient ring interface):


```
sage: R = ZZ['x']
sage: x = R.gen()
sage: J = R.ideal(2)
sage: T = R.quotient_by_principal_ideal(J)
sage: T(x)
x
sage: T.lift(_)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-30-260465055124> in <module>()
----> 1 T.lift(_)

/home/skraeling/sage/src/sage/structure/parent.pyx in sage.structure.parent.Parent.__getattr__ (build/cythonized/sage/structure/parent.c:7885)()
    839             return self.__cached_methods[name]
    840         except KeyError:
--> 841             attr = getattr_from_other_class(self, self._category.parent_class, name)
    842             self.__cached_methods[name] = attr
    843             return attr

/home/skraeling/sage/src/sage/structure/misc.pyx in sage.structure.misc.getattr_from_other_class (build/cythonized/sage/structure/misc.c:1582)()
    251         dummy_error_message.cls = type(self)
    252         dummy_error_message.name = name
--> 253         raise dummy_attribute_error
    254     try:
    255         attribute = getattr(cls, name)

AttributeError: 'PolynomialRing_dense_mod_p_with_category' object has no attribute 'lift'
```



---

Comment by bruno created at 2015-06-08 09:20:20

Replying to [comment:12 darij]:
> Sorry, but the new quotient rings don't play well with the quotient ring interface (or what could be reasonably expected to be the quotient ring interface):

What do you suggest? I can imagine three solutions:
* Make `R.quotient_by_principal_ideal(R.ideal(2))` return a `Polynomial_quotient_ring`: I doubt this is in principle impossible, but at least it requires quite a lot of changes. 
* Keep `R.quotient_by_principal_ideal(R.ideal(2))` return a `TypeError`
* Implement a `lift` method for `PolynomialRing_dense_mod_p`.

None of the three solutions is really fine to my mind, so feel free to suggest another one!


---

Comment by darij created at 2015-06-08 09:54:43

I fear I cannot help here. If you ask me, the whole system is broken. Methods like "quotient" should not return rings but quotient homomorphisms, and these homomorphisms (not their images) should have `lift` attributes...


---

Comment by saraedum created at 2016-05-04 16:25:25

I agree that the system is broken. However, I think that the proposed change improves the situation. I think what we should do here is add a comment stating what the previous comment says. After that I think it would be good to go. What do you think?


---

Comment by saraedum created at 2016-05-04 16:25:30

Changing status from needs_review to needs_info.
