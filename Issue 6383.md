# Issue 6383: implement additive_order for points on an elliptic curve

Issue created by migration from https://trac.sagemath.org/ticket/6383

Original creator: was

Original creation time: 2009-06-21 23:39:37

Assignee: was

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

Comment by davidloeffler created at 2009-06-27 07:53:35

This seems to be a duplicate of #6382.


---

Comment by rlm created at 2009-07-08 20:31:24

Resolution: duplicate
