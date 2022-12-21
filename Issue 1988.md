# Issue 1988: doctest fallout -- osx ppc 10.4 overflow error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 03:38:38

Assignee: was

On fermat, an OS X 10.4 G5 ppc


```
         [21.2 s]
sage -t  devel/sage-main/sage/plot/plot3d/parametric_surface.pyx**********************************************************************
File "parametric_surface.pyx", line 96:
    sage: show(S)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[8]>", line 1, in <module>
        show(S)###line 96:
    sage: show(S)
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
      File "<doctest __main__.example_1[5]>", line 4, in f
        x = cos(a)*(cos(u)*sinh(v)-cos(Integer(3)*u)*sinh(Integer(3)*v)/Integer(3))+             sin(a)*(sin(u)*cosh(v)-sin(Integer(3)*u)*cosh(Integer(3)*v)/Integer(3))
    OverflowError: math range error
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_parametric_surface.pyx
         [9.1 s]

```



---

Comment by craigcitro created at 2008-01-31 06:13:07

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-01-31 06:13:07

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-01-31 06:13:07

This was easy enough -- somewhere someone uses u,v instead of uu,vv.


---

Attachment

Looks good to me. Nice catch.


---

Comment by mabshoff created at 2008-01-31 06:20:56

Merged in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-01-31 06:20:56

Resolution: fixed
