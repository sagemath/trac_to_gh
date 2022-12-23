# Issue 2950: point3d misinterpret arguments

Issue created by migration from https://trac.sagemath.org/ticket/2950

Original creator: novoselt

Original creation time: 2008-04-18 05:46:16

Assignee: was

If point3d is called with 3 points and the first point is a vector, there is a strange error. The first three calls below work, the forth should work, but it does not (tested on sage.math, version 2.11):


```
sage: from sage.plot.plot3d.all import line3d, point3d
sage: pl = point3d([(1, 0, 0), (0, 1, 0), (-1, -1, 0)])
sage: pl = point3d([(1, 0, 0), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])
sage: pl = point3d([vector(ZZ,(1, 0, 0)), (-1, -1, 0)])
sage: pl = point3d([vector(ZZ,(1, 0, 0)), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number
```




---

Comment by shumow created at 2009-01-23 07:25:08

fix to sage/plot/plot3d/shapes2.py


---

Comment by shumow created at 2009-01-23 07:28:16

Changing assignee from was to shumow.


---

Attachment


---

Attachment

I added a doctest to make sure that this works.


---

Comment by shumow created at 2009-01-24 06:15:36

Mike's patch is good and should be applied as well.


---

Comment by mabshoff created at 2009-01-28 15:17:46

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 15:17:46

Merged both patches in Sage 3.3.alpha3
