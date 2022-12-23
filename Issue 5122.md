# Issue 5122: point -- plotting bug for point(Elliptic curve point)

Issue created by migration from https://trac.sagemath.org/ticket/5122

Original creator: was

Original creation time: 2009-01-28 20:09:46

Assignee: was

This should draw a point at the origin in 2d:

```
E = EllipticCurve('37a')
P = E([0,0])
point(P)
```


It used to work but is now broken.


---

Comment by jason created at 2009-01-28 21:41:07

Can you point out a Sage version that this worked in?  That'll make it easier to see what change broke it.


---

Comment by jason created at 2009-01-28 21:41:53

Duh, from the mailing list, 3.1.1 apparently had a working version.


---

Comment by jason created at 2009-01-28 22:01:28

I would say that this is correct behavior, since point() is very specifically documented to plot 2d or 3d points (i.e., lists of coordinates) and not more esoteric objects like points on elliptic curves.

A long time ago (5 months ago?), point() would call P.plot(), which is funny since then you could do point(anything) and it would plot correctly.

For now, the correct thing to do would be to call P.plot() or plot(P), which correctly calls the plot method of P (especially after #5121 is applied).


---

Comment by jason created at 2009-01-28 22:08:24

As near as I can tell, the above stopped working in http://www.sagemath.org/hg/sage-main/rev/a54786a80034

This was about 5 months ago.


---

Comment by was created at 2009-01-29 00:55:11

Resolution: wontfix
