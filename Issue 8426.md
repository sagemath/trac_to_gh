# Issue 8426: polynomial * constant does not work if constant is a numpy type

Issue created by migration from https://trac.sagemath.org/ticket/8426

Original creator: jason

Original creation time: 2010-03-03 05:17:18

Assignee: AlexGhitza

CC:  was robertwb

This should work:


```
import numpy
R.<x>=RR[]
x*numpy.float32('23.0')
```


Instead, I get:

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/tmp/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6994)()

TypeError: unsupported operand parent(s) for '*': 'Univariate Polynomial Ring in x over Real Field with 53 bits of precision' and '<type 'numpy.float32'>'
```


Note that this does work:


```
sage: numpy.float32('23.0')*x
23.0000000000000*x
```




---

Comment by mmezzarobba created at 2014-03-15 18:55:24

Now works, but see #15695.


---

Comment by vdelecroix created at 2015-03-28 11:57:50

Hello,

I propose to close this as duplicates because of #18076 that fixes it. With the branch applied I got

```
sage: import numpy
sage: R.<x> = RR[]
sage: x * numpy.float32('23.0')
23.0000000000000*x
```

and even the pushout works

```
sage: R.<x> = ZZ[]
sage: x * numpy.float32('23.0')
23.0*x
sage: parent(_)
Univariate Polynomial Ring in x over Real Double Field
```


Vincent


---

Comment by vdelecroix created at 2015-03-28 11:57:50

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-04-23 09:40:14

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-23 14:52:09

Resolution: duplicate
