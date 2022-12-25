# Issue 1989: doctest fallout -- osx ppc 10.4 matrix index out of range

archive/issues_001989.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is with sage-2.10.1.rc3 -- ppc osx 10.4:\n\n\n```\nsage -t  devel/sage-main/sage/plot/plot3d/list_plot3d.py    **********************************************************************\nFile \"list_plot3d.py\", line 81:\n    sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[9]>\", line 1, in <module>\n        show(list_plot3d([[Integer(1), Integer(1), Integer(1), Integer(1)], [Integer(1), Integer(2), Integer(1), Integer(2)], [Integer(1), Integer(1), Integer(3), Integer(1)], [Integer(1), Integer(2), Integer(1), Integer(4)]]))###line 81:     sage: show(list_plot3d([[1, 1, 1, 1], [1, 2, 1, 2], [1, 1, 3, 1], [1, 2, 1, 4]]))\n      File \"/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 916, in show\n        return x.show(*args, **kwds)\n      File \"base.pyx\", line 510, in sage.plot.plot3d.base.Graphics3d.show\n        T = self._prepare_for_tachyon(frame, axes, frame_aspect_ratio, aspect_ratio, zoom)\n      File \"base.pyx\", line 315, in sage.plot.plot3d.base.Graphics3d._prepare_for_tachyon\n        a_min, a_max = self._box_for_aspect_ratio(aspect_ratio, box_min, box_max)\n      File \"base.pyx\", line 326, in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio\n        a_min, a_max = self._safe_bounding_box()\n      File \"base.pyx\", line 108, in sage.plot.plot3d.base.Graphics3d._safe_bounding_box\n        a_min, a_max = self.bounding_box()\n      File \"parametric_surface.pyx\", line 162, in sage.plot.plot3d.parametric_surface.ParametricSurface.bounding_box\n        self.triangulate()\n      File \"parametric_surface.pyx\", line 201, in sage.plot.plot3d.parametric_surface.ParametricSurface.triangulate\n        raise\n      File \"parametric_surface.pyx\", line 196, in sage.plot.plot3d.parametric_surface.triangulate\n        self.eval_grid(urange, vrange)\n      File \"parametric_surface.pyx\", line 391, in sage.plot.plot3d.parametric_surface.ParametricSurface.eval_grid\n        res.x, res.y, res.z = self.f(u, v)\n      File \"/Users/was/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.py\", line 134, in <lambda>\n        f = lambda i,j: (i,j,float(m[int(i),int(j)]))\n      File \"matrix0.pyx\", line 558, in sage.matrix.matrix0.Matrix.__getitem__\n      File \"matrix0.pyx\", line 321, in sage.matrix.matrix0.Matrix.check_bounds\n    IndexError: matrix index out of range\n**********************************************************************\n1 items had failures:\n   1 of  17 in __main__.example_1\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_list_plot3d.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1989\n\n",
    "created_at": "2008-01-31T03:40:55Z",
    "labels": [
        "component: graphics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "doctest fallout -- osx ppc 10.4 matrix index out of range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1989",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

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


Issue created by migration from https://trac.sagemath.org/ticket/1989





---

archive/issue_comments_012850.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-01-31T06:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1989#issuecomment-12850",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_012851.json:
```json
{
    "body": "The patch on ticket #1988 fixes this, too.",
    "created_at": "2008-01-31T06:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1989#issuecomment-12851",
    "user": "https://github.com/craigcitro"
}
```

The patch on ticket #1988 fixes this, too.



---

archive/issue_comments_012852.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-31T06:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1989#issuecomment-12852",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012853.json:
```json
{
    "body": "Fixed in Sage 2.10.1.rc4 via merging the fix at #1988",
    "created_at": "2008-01-31T06:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1989#issuecomment-12853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 2.10.1.rc4 via merging the fix at #1988



---

archive/issue_events_002145.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-31T06:23:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1989",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1989#event-2145"
}
```



---

archive/issue_comments_012854.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-31T06:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1989#issuecomment-12854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
