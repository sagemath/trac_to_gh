# Issue 1672: 2.9.2.alpha0: #1666 related plot3d doctest failures

archive/issues_001672.json:
```json
{
    "body": "Assignee: robertwb\n\nWith the bundle from #1666 applied I got the following doctest failures:\n\n```\nsage -t  devel/sage-main/sage/plot/plot.py                  \n**********************************************************************\nFile \"plot.py\", line 2590:\n    sage: show(parametric_plot( (5*cos(x), 5*sin(x), x), -12, 12, plot_points=150, color=\"red\"))\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_52[3]>\", line 1, in <module>\n        show(parametric_plot( (Integer(5)*cos(x), Integer(5)*sin(x), x), -Integer(12), Integer(12), plot_points=Integer(150), color=\"red\"))###line 2590:\n    sage: show(parametric_plot( (5*cos(x), 5*sin(x), x), -12, 12, plot_points=150, color=\"red\"))\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 2594, in parametric_plot\n        return plot(funcs, tmin, tmax, parametric=True, show=show, **kwargs)\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 2410, in __call__\n        G = self._call(funcs, *args, **kwds)\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py\", line 2439, in _call\n        raise ValueError, \"use parametric_plot3d for parametric plots in 3d dimensions.\"\n    ValueError: use parametric_plot3d for parametric plots in 3d dimensions.\n**********************************************************************\n\n\nsage -t  devel/sage-main/sage/plot/plot3d/examples.py       \n**********************************************************************\nFile \"examples.py\", line 5:\n    age: S = sum(sphere(0.5,color=((i-4)/8.0, 0.5, (4-i)/8.0)).translate((sin(i),cos(i),i)) for i in [-4,-3.5,..4])\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[0]>\", line 1, in <module>\n        S = sum(sphere(RealNumber('0.5'),color=((i-Integer(4))/RealNumber('8.0'), RealNumber('0.5'), (Integer(4)-i)/RealNumber('8.0'))).translate((sin(i),cos(i),i)) for i in (ellipsis_range(-Integer(4),-RealNumber('3.5'),Ellipsis,Integer(4))))###line 5:\n    age: S = sum(sphere(0.5,color=((i-4)/8.0, 0.5, (4-i)/8.0)).translate((sin(i),cos(i),i)) for i in [-4,-3.5,..4])\n      File \"<doctest __main__.example_0[0]>\", line 1, in <genexpr>\n        S = sum(sphere(RealNumber('0.5'),color=((i-Integer(4))/RealNumber('8.0'), RealNumber('0.5'), (Integer(4)-i)/RealNumber('8.0'))).translate((sin(i),cos(i),i)) for i in (ellipsis_range(-Integer(4),-RealNumber('3.5'),Ellipsis,Integer(4))))###line 5:\n    age: S = sum(sphere(0.5,color=((i-4)/8.0, 0.5, (4-i)/8.0)).translate((sin(i),cos(i),i)) for i in [-4,-3.5,..4])\n    NameError: global name 'sphere' is not defined\n**********************************************************************\nFile \"examples.py\", line 8:\n    age: B = Box([1,2,4], color=(0.5,0.5,1), opacity=0.5) + frame3d([1,2,4])\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[1]>\", line 1, in <module>\n        B = Box([Integer(1),Integer(2),Integer(4)], color=(RealNumber('0.5'),RealNumber('0.5'),Integer(1)), opacity=RealNumber('0.5')) + frame3d([Integer(1),Integer(2),Integer(4)])###line 8:\n    age: B = Box([1,2,4], color=(0.5,0.5,1), opacity=0.5) + frame3d([1,2,4])\n    TypeError: frame3d() takes exactly 2 arguments (1 given)\n**********************************************************************\nFile \"examples.py\", line 9:\n    age: show(B + S)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        show(B + S)###line 9:\n    age: show(B + S)\n    NameError: name 'B' is not defined\n**********************************************************************\n\nsage -t  devel/sage-main/sage/plot/plot3d/index_face_set.pyx\n**********************************************************************\nFile \"index_face_set.pyx\", line 610:\n    sage: S.jmol_repr(S.default_render_params())\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[2]>\", line 1, in <module>\n        S.jmol_repr(S.default_render_params())###line 610:\n    sage: S.jmol_repr(S.default_render_params())\n      File \"shapes.pyx\", line 214, in sage.plot.plot3d.shapes.Cylinder.jmol_repr\n        return ParametricSurface.jmol_repr(self, render_params)\n      File \"parametric_surface.pyx\", line 116, in sage.plot.plot3d.parametric_surface.ParametricSurface.jmol_repr\n        return IndexFaceSet.jmol_repr(self, render_params)\n      File \"index_face_set.pyx\", line 646, in sage.plot.plot3d.index_face_set.IndexFaceSet.jmol_repr\n        if render_params.output_archive:\n    AttributeError: 'RenderParams' object has no attribute 'output_archive'\n**********************************************************************\n\n\nsage -t  devel/sage-main/sage/plot/plot3d/parametric_plot3d.py\n**********************************************************************\nFile \"parametric_plot3d.py\", line 54:\n    sage: var('u')\nExpected nothing\nGot:\n    u\n**********************************************************************\nFile \"parametric_plot3d.py\", line 63:\n    sage: var('u,v')\nExpected nothing\nGot:\n    (u, v)\n**********************************************************************\nFile \"parametric_plot3d.py\", line 78:\n    sage: var('t')\nExpected nothing\nGot:\n    t\n**********************************************************************\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1672\n\n",
    "created_at": "2008-01-03T18:03:11Z",
    "labels": [
        "graphics",
        "critical",
        "bug"
    ],
    "title": "2.9.2.alpha0: #1666 related plot3d doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1672",
    "user": "mabshoff"
}
```
Assignee: robertwb

With the bundle from #1666 applied I got the following doctest failures:

```
sage -t  devel/sage-main/sage/plot/plot.py                  
**********************************************************************
File "plot.py", line 2590:
    sage: show(parametric_plot( (5*cos(x), 5*sin(x), x), -12, 12, plot_points=150, color="red"))
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[3]>", line 1, in <module>
        show(parametric_plot( (Integer(5)*cos(x), Integer(5)*sin(x), x), -Integer(12), Integer(12), plot_points=Integer(150), color="red"))###line 2590:
    sage: show(parametric_plot( (5*cos(x), 5*sin(x), x), -12, 12, plot_points=150, color="red"))
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py", line 2594, in parametric_plot
        return plot(funcs, tmin, tmax, parametric=True, show=show, **kwargs)
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py", line 2410, in __call__
        G = self._call(funcs, *args, **kwds)
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py", line 2439, in _call
        raise ValueError, "use parametric_plot3d for parametric plots in 3d dimensions."
    ValueError: use parametric_plot3d for parametric plots in 3d dimensions.
**********************************************************************


sage -t  devel/sage-main/sage/plot/plot3d/examples.py       
**********************************************************************
File "examples.py", line 5:
    age: S = sum(sphere(0.5,color=((i-4)/8.0, 0.5, (4-i)/8.0)).translate((sin(i),cos(i),i)) for i in [-4,-3.5,..4])
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[0]>", line 1, in <module>
        S = sum(sphere(RealNumber('0.5'),color=((i-Integer(4))/RealNumber('8.0'), RealNumber('0.5'), (Integer(4)-i)/RealNumber('8.0'))).translate((sin(i),cos(i),i)) for i in (ellipsis_range(-Integer(4),-RealNumber('3.5'),Ellipsis,Integer(4))))###line 5:
    age: S = sum(sphere(0.5,color=((i-4)/8.0, 0.5, (4-i)/8.0)).translate((sin(i),cos(i),i)) for i in [-4,-3.5,..4])
      File "<doctest __main__.example_0[0]>", line 1, in <genexpr>
        S = sum(sphere(RealNumber('0.5'),color=((i-Integer(4))/RealNumber('8.0'), RealNumber('0.5'), (Integer(4)-i)/RealNumber('8.0'))).translate((sin(i),cos(i),i)) for i in (ellipsis_range(-Integer(4),-RealNumber('3.5'),Ellipsis,Integer(4))))###line 5:
    age: S = sum(sphere(0.5,color=((i-4)/8.0, 0.5, (4-i)/8.0)).translate((sin(i),cos(i),i)) for i in [-4,-3.5,..4])
    NameError: global name 'sphere' is not defined
**********************************************************************
File "examples.py", line 8:
    age: B = Box([1,2,4], color=(0.5,0.5,1), opacity=0.5) + frame3d([1,2,4])
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[1]>", line 1, in <module>
        B = Box([Integer(1),Integer(2),Integer(4)], color=(RealNumber('0.5'),RealNumber('0.5'),Integer(1)), opacity=RealNumber('0.5')) + frame3d([Integer(1),Integer(2),Integer(4)])###line 8:
    age: B = Box([1,2,4], color=(0.5,0.5,1), opacity=0.5) + frame3d([1,2,4])
    TypeError: frame3d() takes exactly 2 arguments (1 given)
**********************************************************************
File "examples.py", line 9:
    age: show(B + S)
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        show(B + S)###line 9:
    age: show(B + S)
    NameError: name 'B' is not defined
**********************************************************************

sage -t  devel/sage-main/sage/plot/plot3d/index_face_set.pyx
**********************************************************************
File "index_face_set.pyx", line 610:
    sage: S.jmol_repr(S.default_render_params())
Exception raised:
    Traceback (most recent call last):
      File "/Users/mabshoff/sage-2.9.2.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        S.jmol_repr(S.default_render_params())###line 610:
    sage: S.jmol_repr(S.default_render_params())
      File "shapes.pyx", line 214, in sage.plot.plot3d.shapes.Cylinder.jmol_repr
        return ParametricSurface.jmol_repr(self, render_params)
      File "parametric_surface.pyx", line 116, in sage.plot.plot3d.parametric_surface.ParametricSurface.jmol_repr
        return IndexFaceSet.jmol_repr(self, render_params)
      File "index_face_set.pyx", line 646, in sage.plot.plot3d.index_face_set.IndexFaceSet.jmol_repr
        if render_params.output_archive:
    AttributeError: 'RenderParams' object has no attribute 'output_archive'
**********************************************************************


sage -t  devel/sage-main/sage/plot/plot3d/parametric_plot3d.py
**********************************************************************
File "parametric_plot3d.py", line 54:
    sage: var('u')
Expected nothing
Got:
    u
**********************************************************************
File "parametric_plot3d.py", line 63:
    sage: var('u,v')
Expected nothing
Got:
    (u, v)
**********************************************************************
File "parametric_plot3d.py", line 78:
    sage: var('t')
Expected nothing
Got:
    t
**********************************************************************
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1672





---

archive/issue_comments_010612.json:
```json
{
    "body": "I merged the latest bundle from #1670 and there are additional doctest failures. It is fallout from removing the show() method. William will fix those soonish, but patches are welcome nonetheless:\n\n```\n        sage -t  devel/sage-main/sage/structure/sage_object.pyx\n        sage -t  devel/sage-main/sage/plot/plot3d/base.pyx\n        sage -t  devel/sage-main/sage/plot/plot3d/examples.py\n        sage -t  devel/sage-main/sage/plot/plot3d/parametric_plot3d.py\n        sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py\n        sage -t  devel/sage-main/sage/plot/plot.py\n        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_point.py\n        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py\n        sage -t  devel/sage-main/sage/functions/special.py\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T12:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10612",
    "user": "mabshoff"
}
```

I merged the latest bundle from #1670 and there are additional doctest failures. It is fallout from removing the show() method. William will fix those soonish, but patches are welcome nonetheless:

```
        sage -t  devel/sage-main/sage/structure/sage_object.pyx
        sage -t  devel/sage-main/sage/plot/plot3d/base.pyx
        sage -t  devel/sage-main/sage/plot/plot3d/examples.py
        sage -t  devel/sage-main/sage/plot/plot3d/parametric_plot3d.py
        sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py
        sage -t  devel/sage-main/sage/plot/plot.py
        sage -t  devel/sage-main/sage/groups/perm_gps/cubegroup.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_point.py
        sage -t  devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
        sage -t  devel/sage-main/sage/functions/special.py
```


Cheers,

Michael



---

archive/issue_comments_010613.json:
```json
{
    "body": "I didn't remove the show method.  I just made it less necessary.",
    "created_at": "2008-01-04T17:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10613",
    "user": "was"
}
```

I didn't remove the show method.  I just made it less necessary.



---

archive/issue_comments_010614.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-04T17:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10614",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010615.json:
```json
{
    "body": "Changing assignee from robertwb to was.",
    "created_at": "2008-01-04T17:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10615",
    "user": "was"
}
```

Changing assignee from robertwb to was.



---

archive/issue_comments_010616.json:
```json
{
    "body": "this fixes all doctest issues with sage-2.9.2.rc0",
    "created_at": "2008-01-04T17:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10616",
    "user": "was"
}
```

this fixes all doctest issues with sage-2.9.2.rc0



---

archive/issue_comments_010617.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-04T18:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10617",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010618.json:
```json
{
    "body": "Attachment\n\nMerged in 2.9.2.rc1.",
    "created_at": "2008-01-04T18:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10618",
    "user": "mabshoff"
}
```

Attachment

Merged in 2.9.2.rc1.



---

archive/issue_comments_010619.json:
```json
{
    "body": "part 2 of 2",
    "created_at": "2008-01-04T18:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10619",
    "user": "was"
}
```

part 2 of 2



---

archive/issue_comments_010620.json:
```json
{
    "body": "Attachment\n\nI also applied trac-1672.part2.patch in 2.9.2.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-04T19:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1672",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1672#issuecomment-10620",
    "user": "mabshoff"
}
```

Attachment

I also applied trac-1672.part2.patch in 2.9.2.rc1.

Cheers,

Michael
