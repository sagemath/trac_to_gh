# Issue 8597: point(vector((2,3,4))) is broken

Issue created by migration from https://trac.sagemath.org/ticket/8597

Original creator: slabbe

Original creation time: 2010-03-24 15:14:00

Assignee: was

CC:  kcrisman

The following works :


```
sage: point((2,3))

sage: point((2,3,4))

sage: point(vector((2,3)))
```


but the following doesn't :


```
sage: point(vector((2,3,4)))
Traceback (most recent call last):

/Users/slabbe/<ipython console> in <module>()

/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/point.pyc in point(points, **kwds)
    300     except (ValueError, TypeError):
    301         from sage.plot.plot3d.shapes2 import point3d
--> 302         return point3d(points, **kwds)
    303 
    304 @rename_keyword(color='rgbcolor')

/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/plot3d/shapes2.pyc in point3d(v, size, **kwds)
    712         return Point(v, size, **kwds)
    713     else:
--> 714         A = sum([Point(z, size, **kwds) for z in v])
    715         A._set_extra_kwds(kwds)
    716         return A

/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/plot3d/shapes2.pyc in __init__(self, center, size, **kwds)
    478     def __init__(self, center, size=1, **kwds):
    479         PrimitiveObject.__init__(self, **kwds)
--> 480         self.loc = (float(center[0]), float(center[1]), float(center[2]))
    481         self.size = size
    482         self._set_extra_kwds(kwds)

TypeError: 'sage.rings.integer.Integer' object does not support indexing
```




---

Comment by jason created at 2010-05-26 15:31:52

Changing keywords from "" to "beginner".


---

Comment by ryan created at 2011-01-09 05:18:19

The problem happens in sage.plot.plot3d.shapes2

it should be calling `return Point(v, size, **kwds)`, but instead executes `A = sum([Point(z, size, **kwds) for z in v])`  

I think there is something wrong with the if condition.


---

Comment by ryan created at 2011-01-09 05:38:13

Changing status from new to needs_review.


---

Comment by ryan created at 2011-01-09 05:38:52

`point(vector((2,3,4)))` should work now


---

Attachment

fixes point for 3d vectors


---

Comment by ryan created at 2011-01-09 06:19:00

latest patch includes small improvement that was suggested to me.


---

Comment by aly.deines created at 2011-01-09 23:39:51

Looks good, but it needs a doctest.  I've added one in the following patch.


---

Comment by aly.deines created at 2011-01-09 23:40:23

adds a doctest


---

Attachment

The second patch does not apply on top of the first.

Only the second patch with doctest should be applied.  Otherwise, it's all good.


---

Comment by jthurber created at 2011-01-10 11:25:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:19:44

Resolution: fixed
