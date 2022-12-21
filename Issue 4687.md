# Issue 4687: Points on  Elliptic Curve over GF(2)

Issue created by migration from Trac.

Original creator: rishi

Original creation time: 2008-12-03 18:00:27

Assignee: tbd

CC:  cremona


```

sage: E=EllipticCurve(GF(2),[0, 0, 1, 1, 1])
sage: E
Elliptic Curve defined by y^2 + y = x^3 + x +1 over Finite Field of size 2
sage: E.points()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Volumes/Panther/sage/<ipython console> in <module>()

/Volumes/Panther/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.pyc in points(self)
    214         from sage.structure.sequence import Sequence
    215         if self.base_ring().is_prime_field():
--> 216             v = self._points_via_group_structure()
    217         else:
    218             v =self._points_fast_sqrt()

/Volumes/Panther/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.pyc in _points_via_group_structure(self)
    165 
    166         H0=[self(0)]
--> 167         for m in range(1,ni[0]): H0.append(H0[-1]+pts[0])
    168         if len(ni)==1:   # cyclic case
    169             return H0

IndexError: list index out of range

```



---

Comment by mabshoff created at 2008-12-04 14:16:16

I guess the category number theory might be more appropriate. Also CCing John just in case he might be interested in this ticket and not aware of its existence.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 14:16:16

Changing component from algebra to number theory.


---

Comment by mabshoff created at 2008-12-04 14:16:16

Changing assignee from tbd to was.


---

Attachment


---

Comment by cremona created at 2008-12-04 14:34:06

Thanks for the bug report:  the code did not handle the case of a trivial group properly!  Your curve is essentially the only example of that (and did appear in a doctest elsewhere).

The attached patch fixes this, adding doctests to show that all three cases (#gens=0,1,2) can be handled.  It is based on 3.2.1.


---

Comment by rishi created at 2008-12-04 17:36:11

Works good.


---

Comment by mabshoff created at 2008-12-04 18:28:18

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-04 18:28:18

Resolution: fixed
