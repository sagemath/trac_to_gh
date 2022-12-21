# Issue 3108: implement additive_order for elliptic curve points

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-06 01:53:51

Assignee: was


```
sage: E = EllipticCurve(GF(5),[1..5])
sage: P = E.lift_x(0)
sage: P
(0 : 2 : 1)
sage: P.additive_order()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/was/papers/submitted/kolyconj/<ipython console> in <module>()

/Users/was/papers/submitted/kolyconj/element.pyx in sage.structure.element.ModuleElement.additive_order()

<type 'exceptions.NotImplementedError'>: 
sage: P.order()
3
```



---

Comment by was created at 2008-05-06 01:53:59

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-20 19:48:07

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:48:07

Changing component from number theory to elliptic curves.


---

Attachment


---

Comment by cremona created at 2009-07-24 22:22:35

Done: I defined additive_order to be a synonym for order (in 3 places) with relevant doctests.


---

Comment by wuthrich created at 2009-08-17 12:09:31

Fine.

Maybe David Loeffler, working on abelian groups, wants this differently. 
By now, this should go in.

chris.


---

Comment by mvngu created at 2009-08-22 22:13:30

Resolution: fixed
