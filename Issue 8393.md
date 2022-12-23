# Issue 8393: bring plot3d.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/8393

Original creator: mhampton

Original creation time: 2010-02-28 14:36:59

Assignee: was

CC:  kcrisman

Keywords: coverage, doctests, plot3d

plot3d.py is only missing three doctests to get to 100%:

```
sage -coverage devel/sage-p1/sage/plot/plot3d/plot3d.py 
----------------------------------------------------------------------
devel/sage-p1/sage/plot/plot3d/plot3d.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-p1/sage/plot/plot3d/plot3d.py: 81% (13 of 16)

Missing documentation:
	 * triangle(self, a, b, c, color = None):
	 * smooth_triangle(self, a, b, c, da, db, dc, color = None):
	 * axes(scale=1, radius=None, **kwds):
```



---

Comment by kcrisman created at 2012-07-07 03:35:24


```

$ ../../sage -coverage sage/plot/plot3d/plot3d.py 
----------------------------------------------------------------------
sage/plot/plot3d/plot3d.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE sage/plot/plot3d/plot3d.py: 100% (18 of 18)
----------------------------------------------------------------------
```

This was fixed by #12491.


---

Comment by kcrisman created at 2012-07-07 03:35:24

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-07-07 03:35:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-07-17 08:33:35

Resolution: duplicate
