# Issue 5666: forming ideals in IntegerModRing_generic does not work

Issue created by migration from https://trac.sagemath.org/ticket/5666

Original creator: cremona

Original creation time: 2009-04-02 15:41:15

Assignee: tbd

It is impossible to create ideals in rings of the form Integers mod n:


```
sage: R = Integers(10)
sage: R.ideal(1)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/5831/_home_masgaj__sage_init_sage_0.py
in <module>()

/local/jec/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc
in ideal(self, *gens, **kwds)
   487             gens = gens[0]
   488         from
sage.rings.polynomial.multi_polynomial_libsingular import
MPolynomialRing_libsingular
--> 489         if not
isinstance(self.__R,MPolynomialRing_libsingular) and not
self.__R._has_singular:
   490             # pass through
   491             MPolynomialRing_generic.ideal(self,gens,**kwds)

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has
no attribute '_has_singular'
sage: R.ideal([2,4])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

(as above)
```


It looks as if the ideal() method for class  `QuotientRing_generic ` is
only really geared to polynomial ring quotients.




---

Attachment


---

Comment by was created at 2010-01-17 06:36:24

Changing status from new to needs_review.


---

Comment by rbeezer created at 2010-01-18 05:20:32

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-01-18 05:20:32

Passes tests and allows creation of ideals within rings of integers mod n.

But it seems the resulting ideals still need some work, for example `_contains_()` in `rings.ideal.Ideal_generic` is not implemented.


```
sage: R=Integers(40)
sage: Q=R.ideal([2,3])
sage: type(Q)
<class 'sage.rings.ideal.Ideal_generic'>
sage: 1 in Q
------------------
NotImplementedError
<snip>
```



---

Comment by rlm created at 2010-01-18 22:41:43

Resolution: fixed
