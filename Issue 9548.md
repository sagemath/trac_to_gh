# Issue 9548: Sage does not support infinities with complex direction

Issue created by migration from https://trac.sagemath.org/ticket/9548

Original creator: fredrik.johansson

Original creation time: 2010-07-19 08:27:56

Assignee: AlexGhitza

This should do something reasonable:


```
sage: Infinity * I
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)

/home/fredrik/sage/<ipython console> in <module>()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11428)()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6123)()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11356)()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._mul_ (sage/symbolic/expression.cpp:11042)()

ArithmeticError: x*Infinity with non real x encountered.
```



---

Comment by mmezzarobba created at 2014-02-02 11:40:02

`I*Infinity` now returns an element of the symbolic ring. I'm leaving the ticket open (as a wishlist item), though, since it would probably make sense to make infinities with complex direction more similar to ±∞.


---

Comment by rws created at 2015-04-21 14:42:19

This may be a stupid question but now that we have complex (unsigned) infinity, shouldn't that be the result of `I*Infinity`?


---

Comment by mmezzarobba created at 2015-04-22 09:51:11

I don't know. It would definitely be useful to be able to write things like integrals from 0 to i∞, (1+i)∞, or exp(iθ)∞. Whether `I*infinity` should return on of these “directional” infinities or unsigned infinity is another question. Without thinking, I'd say `I*PlusInfinity()` should return the former and `I*UnsignedInfinity()` the latter.
