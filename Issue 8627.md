# Issue 8627: cannot coerce p-adic capped-rel to capped-abs

Issue created by migration from https://trac.sagemath.org/ticket/8627

Original creator: dmharvey

Original creation time: 2010-03-30 00:47:56

Assignee: roed

(sage 4.3.1)


```
sage: R.<a> = Zq(25, type="capped-abs")
sage: R(1/a)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/david/<ipython console> in <module>()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4956)()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap._call_ (sage/structure/coerce_maps.c:2434)()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap._call_ (sage/structure/coerce_maps.c:2332)()

/Users/david/sage-4.3.1/local/lib/python2.6/site-packages/sage/rings/padics/padic_ZZ_pX_CA_element.so in sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.__init__ (sage/rings/padics/padic_ZZ_pX_CA_element.cpp:4574)()

TypeError: Cannot convert sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement to sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement
```




---

Comment by roed created at 2016-02-16 20:39:09

Works now.  Need to add a doctest.


---

Comment by rozenszt created at 2016-03-21 15:55:19

There is already a doctest for this.


---

Comment by rozenszt created at 2016-03-21 15:55:19

Changing status from new to needs_review.


---

Comment by rozenszt created at 2016-03-21 15:55:41

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-03-26 12:01:02

Resolution: invalid
