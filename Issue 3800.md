# Issue 3800: Problem with Cusp constructor

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-08-10 12:04:44

Assignee: craigcitro

There are several issues with the `Cusp.__init__` method. Here's an example:


```
sage: Cusp(1/3,0)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/sage/local/lib/python2.5/site-packages/sage/modular/cusps.py in __init__(self, a, b, construct, parent)
    194 
    195         elif isinstance(a, Rational):
--> 196             a = a/b
    197             self.__a = a.numer()
    198             self.__b = a.denom()

/Users/craigcitro/element.pyx in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9074)()

/Users/craigcitro/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5100)()

/Users/craigcitro/element.pyx in sage.structure.element.RingElement.__div__ (sage/structure/element.c:9057)()

/Users/craigcitro/coerce.pxi in sage.structure.element._div_c (sage/structure/element.c:16420)()

/Users/craigcitro/rational.pyx in sage.rings.rational.Rational._div_c_impl (sage/rings/rational.c:8135)()

ZeroDivisionError: Rational division by zero
```


This is relevant, since some computations with modular symbols on `GammaH` can lead to exactly this problem. 

The attached patch rewrites the `__init__` method, slightly improving the speed, and vastly improving the consistency. In particular, it was possible to construct two different cusps which both claimed to be `Infinity` (namely `(1,0)` and `(-1,0)`). 

In the process of doing this, I exposed several bits of code that were taking advantage of this "loophole," which then needed to be fixed. In an attempt to make things more clear, I ended up doctesting all of `sage/modular/modsym/boundary.py`, so that's also included.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-08-11 05:40:22

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 05:40:22

Merged both patches in Sage 3.1.alpha1
