# Issue 2560: serious inefficiency in order of points on elliptic curvews over finite fields

Issue created by migration from https://trac.sagemath.org/ticket/2560

Original creator: cremona

Original creation time: 2008-03-16 22:22:45

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

since there is a loution in the interval [lb..ub].  This changes the complexity from O(q^1/2) to O(q^1/4).


---

Comment by cremona created at 2008-03-16 22:31:15

delete - duplicate


---

Comment by mhansen created at 2008-03-16 22:36:53

Duplicate of #2561


---

Comment by mhansen created at 2008-03-16 22:36:53

Resolution: duplicate
