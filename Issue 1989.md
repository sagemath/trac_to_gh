# Issue 1989: doctest fallout -- osx ppc 10.4 matrix index out of range

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 03:40:55

Assignee: was

This is with sage-2.10.1.rc3 -- ppc osx 10.4:


```
sage -t  devel/sage-main/sage/plot/plot3d/list_plot3d.py    **********************************************************************
File "list_plot3d.py", line 81:
    sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        show(list_plot3d([[Integer(1), Integer(1), Integer(1), Integer(1)], [Integer(1), Integer(2), Integer(1), Integer(2)], [Integer(1), Integer(1), Integer(3), Integer(1)], [Integer(1), Integer(2), Integer(1), Integer(4)]]))###line 81:     sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))
      File "/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py", line 916, in show
        return x.show(*args, **kwds)
      File "base.pyx", line 510, in sage.plot.plot3d.base.Graphics3d.show
        T = self._prepare_for_tachyon(frame, axes, frame_aspect_ratio, aspect_ratio, zoom)
      File "base.pyx", line 315, in sage.plot.plot3d.base.Graphics3d._prepare_for_tachyon
        a_min, a_max = self._box_for_aspect_ratio(aspect_ratio, box_min, box_max)
      File "base.pyx", line 326, in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio
        a_min, a_max = self._safe_bounding_box()
      File "base.pyx", line 108, in sage.plot.plot3d.base.Graphics3d._safe_bounding_box
        a_min, a_max = self.bounding_box()
      File "parametric_surface.pyx", line 162, in sage.plot.plot3d.parametric_surface.ParametricSurface.bounding_box
        self.triangulate()
      File "parametric_surface.pyx", line 201, in sage.plot.plot3d.parametric_surface.ParametricSurface.triangulate
        raise
      File "parametric_surface.pyx", line 196, in sage.plot.plot3d.parametric_surface.triangulate
        self.eval_grid(urange, vrange)
      File "parametric_surface.pyx", line 391, in sage.plot.plot3d.parametric_surface.ParametricSurface.eval_grid
        res.x, res.y, res.z = self.f(u, v)
      File "/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.py", line 134, in <lambda>
        f = lambda i,j: (i,j,float(m[int(i),int(j)]))
      File "matrix0.pyx", line 558, in sage.matrix.matrix0.Matrix.__getitem__
      File "matrix0.pyx", line 321, in sage.matrix.matrix0.Matrix.check_bounds
    IndexError: matrix index out of range
**********************************************************************
1 items had failures:
   1 of  17 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_list_plot3d.py
```



---

Comment by craigcitro created at 2008-01-31 06:14:12

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-01-31 06:14:12

The patch on ticket #1988 fixes this, too.


---

Comment by craigcitro created at 2008-01-31 06:14:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-31 06:23:00

Fixed in Sage 2.10.1.rc4 via merging the fix at #1988


---

Comment by mabshoff created at 2008-01-31 06:23:00

Resolution: fixed
