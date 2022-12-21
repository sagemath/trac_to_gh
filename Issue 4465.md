# Issue 4465: zero-length errors give division error instead of just drawing a point.

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-08 03:03:22

Assignee: was

This is an error to a custom patch that we have to the matplotlib code so that we can have arrows that are shortened by a certain number of points.


```
This week, I was drawing plot vector field using two ways : (1) plot_vector_field and (2) by simply suming up plenty of arrows as I wished. Since their was a fixed point somewhere, I came up with the problem of drawing a zero length arrow. Using sage 3.1.4, I get a zero division error. Where is this division from? The example below show that it is not from the slope as it can draw a vertical arrow.

sage: arrow((1, 1), (2, 1))
sage: arrow((1, 1), (1, 2))
sage: arrow((1, 1), (1, 1))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last) :
...
/home/slabbe/sage/local/lib/python2.5/site-packages/matplotlib/arrow_line.pyc in draw(self, renderer)
    100         pixel_vector = (orig_t.transform_point(points[1]) - orig_t.transform_point(points[0]))
    101         pixel_length=math.sqrt(sum(pixel_vector**2))
--> 102         clip_fraction = renderer.points_to_pixels(self._arrowshorten)/pixel_length
    103         head_clip_fraction = renderer.points_to_pixels(self._arrowshorten+self._arrowheadlength*0.8)/pixel_length
    104

ZeroDivisionError: float division

In my problem, I would have been happy if arrow(x,x) would draw simply a point. I know I can define my own arrow but maybe sage's arrow could behave like myarrow ?
```



---

Comment by jason created at 2008-11-08 03:04:10

Changing status from new to assigned.


---

Comment by jason created at 2008-11-08 03:04:10

Changing assignee from was to jason.


---

Comment by jason created at 2009-01-26 16:08:49

This should be fixed by #4774


---

Comment by jason created at 2009-02-13 17:38:42

This is still a problem after #4774.  We should probably take care of this in our arrow-drawing code, then, instead of just passing things on to matplotlib.


---

Comment by mhansen created at 2009-06-04 23:33:42

Resolution: invalid


---

Comment by mhansen created at 2009-06-04 23:33:42

This works fine in 4.0.1.rc1:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: arrow((1, 1), (1, 1))
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
sage: 
```

