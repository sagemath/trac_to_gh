# Issue 1357: the polynomial .roots() method should work with ring=QQbar

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-02 01:28:37

Assignee: cwitty

Something like this should work:

```
sage: x = polygen(ZZ)
sage: (x^2 + x + 1).roots(ring=QQbar)
```

but currently it doesn't.


---

Attachment


---

Comment by rlm created at 2007-12-02 19:23:37

Before:

```
sage: from sage.rings.polynomial.complex_roots import complex_roots
sage: E = EllipticCurve('389a')
sage: f = E.division_polynomial(3)
sage: interval_roots = f.roots(ring=CIF)
sage: x_coords = [QQbar.polynomial_root(f, x_interval[0]) for x_interval in interval_roots]
sage: f = E.defining_polynomial()
sage: y = polygen(QQbar,'y')
sage: points = []
sage: for x in x_coords:
...       g = f(x,y,1)
...       rootsg = complex_roots(g, min_prec=53)
...       for root in rootsg:
...           y_coord = root[0]
...           yy = QQbar.polynomial_root(g, y_coord)
...           points.append([x, yy])
```

After:

```
sage: E = EllipticCurve('389a')
sage: f = E.division_polynomial(3)
sage: x_coords = f.roots(ring=QQbar)
sage: g = E.defining_polynomial()
sage: y = polygen(QQbar, 'y')
sage: points = []
sage: for x in x_coords:
...    h = g(x[0],y,1)
...    rootsh = h.roots(ring=QQbar)
...    for root in rootsh:
...        points.append([x[0], root[0]])
```



---

Comment by mabshoff created at 2007-12-02 20:11:58

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 20:11:58

Resolution: fixed
