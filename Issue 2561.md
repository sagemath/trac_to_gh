# Issue 2561: serious inefficiency in order of points on elliptic curvews over finite fields

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-03-16 22:23:45

Assignee: was

Keywords: elliptic curves

In sage/elliptic_curves/sll_points.py in the function ` EllipticCurvePoint_finite_field.order()` a tiny blunder causes a huge inefficiency.  The BSGS function is used to find a multiple of the order of the point (when the group order is not yet known), and the existing code

```
                M = self._bsgs(E(0),0,ub)
```

should be

```
                M = self._bsgs(E(0),lb,ub)
```

since there is a lsolution in the interval [lb..ub].  This changes the complexity from `O(q^1/2)` to `O(q^1/4)`.




---

Attachment


---

Comment by ncalexan created at 2008-03-16 23:42:33

Looks fine to me, apply.


---

Comment by mabshoff created at 2008-03-16 23:55:51

Doctests pass with "-long", so another positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 23:56:35

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 23:56:35

Merged in Sage 2.10.4.final
