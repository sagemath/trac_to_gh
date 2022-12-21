# Issue 6382: implement additive_order for points on an elliptic curve

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-21 23:39:34

Assignee: was

CC:  mhansen mvngu

This should work:


```
sage: E = EllipticCurve('11a'); P = E.torsion_subgroup().gens()[0]; P
(5 : 5 : 1)
sage: P.additive_order()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/Users/wstein/.sage/temp/resid_tg105.upc.es/5930/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.ModuleElement.additive_order (sage/structure/element.c:8113)()

NotImplementedError: 
sage: P.order()
5
```



---

Comment by davidloeffler created at 2009-07-20 19:56:06

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-20 19:56:06

Changing assignee from was to davidloeffler.


---

Comment by cremona created at 2009-07-25 17:36:05

This is a duplicate of #3108 whic hhas a patch waiting review.  This ticket can terefore be closed.


---

Comment by jason created at 2009-10-06 19:27:47

Please note the request to close this.


---

Comment by mhansen created at 2009-10-07 04:02:37

Duplicate of #3108.


---

Comment by mhansen created at 2009-10-07 04:02:37

Resolution: duplicate
