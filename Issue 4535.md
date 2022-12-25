# Issue 4535: refactoring in plot/*

archive/issues_004535.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  timothyclemans\n\nThe main goals of this ticket are to split up plot.py so that it's not 4500 lines long and change the way the bounding boxes are computed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4535\n\n",
    "created_at": "2008-11-16T13:12:43Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "refactoring in plot/*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4535",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein

CC:  timothyclemans

The main goals of this ticket are to split up plot.py so that it's not 4500 lines long and change the way the bounding boxes are computed.

Issue created by migration from https://trac.sagemath.org/ticket/4535





---

archive/issue_comments_033724.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-16T13:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33724",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033725.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-11-16T13:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33725",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_033726.json:
```json
{
    "body": "One remark: All the newly created files are missing copyright headers.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T18:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33726",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

One remark: All the newly created files are missing copyright headers.

Cheers,

Michael



---

archive/issue_comments_033727.json:
```json
{
    "body": "If we are moving to be more based on matplotlib, it would be nice if we could draw stuff in matplotlib and easily convert the result to a sage Graphics object, so we could then add it to other sage graphics objects, etc.\n\nIn other words, it would be great if this worked:\n\nsage: a=pylab.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)\nsage: Graphics(a)",
    "created_at": "2008-11-18T12:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33727",
    "user": "https://github.com/jasongrout"
}
```

If we are moving to be more based on matplotlib, it would be nice if we could draw stuff in matplotlib and easily convert the result to a sage Graphics object, so we could then add it to other sage graphics objects, etc.

In other words, it would be great if this worked:

sage: a=pylab.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
sage: Graphics(a)



---

archive/issue_comments_033728.json:
```json
{
    "body": "I really like this patch reading it.  But it doesn't apply:\n\n\n```\npatching file sage/calculus/desolvers.py\nHunk #1 succeeded at 39 with fuzz 2 (offset 2 lines).\npatching file sage/geometry/polyhedra.py\nHunk #1 FAILED at 30\n1 out of 1 hunk FAILED -- saving rejects to file sage/geometry/polyhedra.py.rej\npatching file sage/plot/animate.py\nHunk #1 FAILED at 60\nHunk #2 FAILED at 120\nHunk #6 succeeded at 253 with fuzz 2 (offset 14 lines).\n2 out of 6 hunks FAILED -- saving rejects to file sage/plot/animate.py.rej\npatching file sage/plot/plot.py\nHunk #17 FAILED at 1261\nHunk #18 FAILED at 2349\n2 out of 24 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\nabort: patch failed to apply\n```\n\n\nAssuming it works, it gets copyright headers, and passes all doctests (in the whole tree), I will give this a positive review.",
    "created_at": "2008-11-27T17:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33728",
    "user": "https://github.com/williamstein"
}
```

I really like this patch reading it.  But it doesn't apply:


```
patching file sage/calculus/desolvers.py
Hunk #1 succeeded at 39 with fuzz 2 (offset 2 lines).
patching file sage/geometry/polyhedra.py
Hunk #1 FAILED at 30
1 out of 1 hunk FAILED -- saving rejects to file sage/geometry/polyhedra.py.rej
patching file sage/plot/animate.py
Hunk #1 FAILED at 60
Hunk #2 FAILED at 120
Hunk #6 succeeded at 253 with fuzz 2 (offset 14 lines).
2 out of 6 hunks FAILED -- saving rejects to file sage/plot/animate.py.rej
patching file sage/plot/plot.py
Hunk #17 FAILED at 1261
Hunk #18 FAILED at 2349
2 out of 24 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```


Assuming it works, it gets copyright headers, and passes all doctests (in the whole tree), I will give this a positive review.



---

archive/issue_comments_033729.json:
```json
{
    "body": "Attachment [trac_4535.patch](tarball://root/attachments/some-uuid/ticket4535/trac_4535.patch) by @mwhansen created at 2008-11-27 21:34:37",
    "created_at": "2008-11-27T21:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33729",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4535.patch](tarball://root/attachments/some-uuid/ticket4535/trac_4535.patch) by @mwhansen created at 2008-11-27 21:34:37



---

archive/issue_comments_033730.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-11-27T21:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33730",
    "user": "https://github.com/mwhansen"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_033731.json:
```json
{
    "body": "The rebased patch applies cleanly to my Sage 3.2.1.alpha3 merge tree. I am doing a sage -ba right now (with a nuke build directory) followed by doctesting to make 100% sure all import issues have been truly fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T22:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The rebased patch applies cleanly to my Sage 3.2.1.alpha3 merge tree. I am doing a sage -ba right now (with a nuke build directory) followed by doctesting to make 100% sure all import issues have been truly fixed.

Cheers,

Michael



---

archive/issue_comments_033732.json:
```json
{
    "body": "This definitely needs some work - most likely those are overwhelmingly import issues:\n\n```\n        sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/tests/book_stein_ent.py # 3 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 2 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 7 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/groebner_fan.py # 156 doctests failed\n        sage -t -long devel/sage/sage/rings/padics/padic_base_generic.py # 3 doctests failed\n        sage -t -long devel/sage/sage/plot/matrix_plot.py # 5 doctests failed\n        sage -t -long devel/sage/sage/plot/contour_plot.py # 12 doctests failed\n        sage -t -long devel/sage/sage/numerical/optimize.py # 1 doctests failed\n        sage -t -long devel/sage/sage/plot/plot.py # 4 doctests failed\n        sage -t -long devel/sage/sage/matrix/matrix2.pyx # 3 doctests failed\n        sage -t -long devel/sage/sage/gsl/ode.pyx # 4 doctests failed\n        sage -t -long devel/sage/sage/functions/transcendental.py # 1 doctests failed\n        sage -t -long devel/sage/sage/functions/piecewise.py # 15 doctests failed\n        sage -t -long devel/sage/sage/finance/time_series.pyx # 7 doctests failed\n        sage -t -long devel/doc/tut/tut.tex # 4 doctests failed\n        sage -t -long devel/doc/const/const.tex # 1 doctests failed\n```\n\nNote that I nuked my build directory and did a -ba.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T23:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This definitely needs some work - most likely those are overwhelmingly import issues:

```
        sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/tests/book_stein_ent.py # 3 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_element.pyx # 2 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # 7 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/groebner_fan.py # 156 doctests failed
        sage -t -long devel/sage/sage/rings/padics/padic_base_generic.py # 3 doctests failed
        sage -t -long devel/sage/sage/plot/matrix_plot.py # 5 doctests failed
        sage -t -long devel/sage/sage/plot/contour_plot.py # 12 doctests failed
        sage -t -long devel/sage/sage/numerical/optimize.py # 1 doctests failed
        sage -t -long devel/sage/sage/plot/plot.py # 4 doctests failed
        sage -t -long devel/sage/sage/matrix/matrix2.pyx # 3 doctests failed
        sage -t -long devel/sage/sage/gsl/ode.pyx # 4 doctests failed
        sage -t -long devel/sage/sage/functions/transcendental.py # 1 doctests failed
        sage -t -long devel/sage/sage/functions/piecewise.py # 15 doctests failed
        sage -t -long devel/sage/sage/finance/time_series.pyx # 7 doctests failed
        sage -t -long devel/doc/tut/tut.tex # 4 doctests failed
        sage -t -long devel/doc/const/const.tex # 1 doctests failed
```

Note that I nuked my build directory and did a -ba.

Cheers,

Michael



---

archive/issue_comments_033733.json:
```json
{
    "body": "And while I am complaining:\n\n```\nanimate.py: 91% (11 of 12)\narrow.py: 87% (7 of 8)\naxes.py: 26% (5 of 19)\nbar_chart.py: 83% (5 of 6)\ncircle.py: 42% (3 of 7)\ncontour_plot.py: 42% (3 of 7)\ndisk.py: 33% (2 of 6)\njava3d.py: 0% (0 of 1)\nline.py: 90% (10 of 11)\nmatrix_plot.py: 33% (2 of 6)\nmisc.py: 72% (13 of 18)\nnetworkx_graph.py: 25% (1 of 4)\nplot3d/base.pyx: 5% (4 of 76)\nplot3d/index_face_set.pyx: 21% (7 of 32)\nplot3d/list_plot3d.py: 16% (1 of 6)\nplot3d/parametric_plot3d.py: 20% (1 of 5)\nplot3d/parametric_surface.pyx: 14% (2 of 14)\nplot3d/platonic.py: 71% (5 of 7)\nplot3d/plot3d.py: 33% (2 of 6)\nplot3d/shapes.pyx: 16% (5 of 31)\nplot3d/shapes2.py: 21% (5 of 23)\nplot3d/texture.py: 12% (1 of 8)\nplot3d/transform.pyx: 7% (1 of 14)\nplot_field.py: 42% (3 of 7)\nplot.py: 70% (41 of 58)\npoint.py: 44% (4 of 9)\npolygon.py: 20% (2 of 10)\nprimitive.py: 71% (5 of 7)\ntachyon.py: 8% (5 of 58)\ntext.py: 12% (1 of 8)\ntexture.py: 0% (0 of 6)\ntri_plot.py: 0% (0 of 20)\n\nOverall weighted coverage score:  30.3%\nTotal number of functions:  510\n```\n\nThis is more or less unchanged from pre-refactoring, so no need to make this an issue with this patch:\n\n```\nanimate.py: 90% (10 of 11)\naxes.py: 26% (5 of 19)\njava3d.py: 0% (0 of 1)\nmisc.py: 70% (12 of 17)\nplot3d/base.pyx: 5% (4 of 76)\nplot3d/index_face_set.pyx: 21% (7 of 32)\nplot3d/list_plot3d.py: 16% (1 of 6)\nplot3d/parametric_plot3d.py: 20% (1 of 5)\nplot3d/parametric_surface.pyx: 14% (2 of 14)\nplot3d/platonic.py: 71% (5 of 7)\nplot3d/plot3d.py: 33% (2 of 6)\nplot3d/shapes.pyx: 16% (5 of 31)\nplot3d/shapes2.py: 21% (5 of 23)\nplot3d/texture.py: 12% (1 of 8)\nplot3d/transform.pyx: 7% (1 of 14)\nplot.py: 57% (93 of 161)\ntachyon.py: 8% (5 of 58)\ntexture.py: 0% (0 of 6)\ntri_plot.py: 0% (0 of 20)\n\nOverall weighted coverage score:  30.3%\nTotal number of functions:  515\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T00:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And while I am complaining:

```
animate.py: 91% (11 of 12)
arrow.py: 87% (7 of 8)
axes.py: 26% (5 of 19)
bar_chart.py: 83% (5 of 6)
circle.py: 42% (3 of 7)
contour_plot.py: 42% (3 of 7)
disk.py: 33% (2 of 6)
java3d.py: 0% (0 of 1)
line.py: 90% (10 of 11)
matrix_plot.py: 33% (2 of 6)
misc.py: 72% (13 of 18)
networkx_graph.py: 25% (1 of 4)
plot3d/base.pyx: 5% (4 of 76)
plot3d/index_face_set.pyx: 21% (7 of 32)
plot3d/list_plot3d.py: 16% (1 of 6)
plot3d/parametric_plot3d.py: 20% (1 of 5)
plot3d/parametric_surface.pyx: 14% (2 of 14)
plot3d/platonic.py: 71% (5 of 7)
plot3d/plot3d.py: 33% (2 of 6)
plot3d/shapes.pyx: 16% (5 of 31)
plot3d/shapes2.py: 21% (5 of 23)
plot3d/texture.py: 12% (1 of 8)
plot3d/transform.pyx: 7% (1 of 14)
plot_field.py: 42% (3 of 7)
plot.py: 70% (41 of 58)
point.py: 44% (4 of 9)
polygon.py: 20% (2 of 10)
primitive.py: 71% (5 of 7)
tachyon.py: 8% (5 of 58)
text.py: 12% (1 of 8)
texture.py: 0% (0 of 6)
tri_plot.py: 0% (0 of 20)

Overall weighted coverage score:  30.3%
Total number of functions:  510
```

This is more or less unchanged from pre-refactoring, so no need to make this an issue with this patch:

```
animate.py: 90% (10 of 11)
axes.py: 26% (5 of 19)
java3d.py: 0% (0 of 1)
misc.py: 70% (12 of 17)
plot3d/base.pyx: 5% (4 of 76)
plot3d/index_face_set.pyx: 21% (7 of 32)
plot3d/list_plot3d.py: 16% (1 of 6)
plot3d/parametric_plot3d.py: 20% (1 of 5)
plot3d/parametric_surface.pyx: 14% (2 of 14)
plot3d/platonic.py: 71% (5 of 7)
plot3d/plot3d.py: 33% (2 of 6)
plot3d/shapes.pyx: 16% (5 of 31)
plot3d/shapes2.py: 21% (5 of 23)
plot3d/texture.py: 12% (1 of 8)
plot3d/transform.pyx: 7% (1 of 14)
plot.py: 57% (93 of 161)
tachyon.py: 8% (5 of 58)
texture.py: 0% (0 of 6)
tri_plot.py: 0% (0 of 20)

Overall weighted coverage score:  30.3%
Total number of functions:  515
```


Cheers,

Michael



---

archive/issue_comments_033734.json:
```json
{
    "body": "Attachment [trac_4535-fixes.patch](tarball://root/attachments/some-uuid/ticket4535/trac_4535-fixes.patch) by @mwhansen created at 2008-11-28 02:51:32",
    "created_at": "2008-11-28T02:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33734",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4535-fixes.patch](tarball://root/attachments/some-uuid/ticket4535/trac_4535-fixes.patch) by @mwhansen created at 2008-11-28 02:51:32



---

archive/issue_comments_033735.json:
```json
{
    "body": "Attachment [trac_4535-pickle_jar.patch](tarball://root/attachments/some-uuid/ticket4535/trac_4535-pickle_jar.patch) by @mwhansen created at 2008-11-28 02:51:44",
    "created_at": "2008-11-28T02:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33735",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4535-pickle_jar.patch](tarball://root/attachments/some-uuid/ticket4535/trac_4535-pickle_jar.patch) by @mwhansen created at 2008-11-28 02:51:44



---

archive/issue_comments_033736.json:
```json
{
    "body": "I've attached 2 patches which fix the above issues.",
    "created_at": "2008-11-28T02:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33736",
    "user": "https://github.com/mwhansen"
}
```

I've attached 2 patches which fix the above issues.



---

archive/issue_comments_033737.json:
```json
{
    "body": "With the two new patches all tests including the pickle jar passes. Positive review extended via William.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T04:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33737",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the two new patches all tests including the pickle jar passes. Positive review extended via William.

Cheers,

Michael



---

archive/issue_comments_033738.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T05:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33738",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.1.rc0



---

archive/issue_comments_033739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T05:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4535#issuecomment-33739",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004781.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-28T05:30:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4535",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4535#event-4781"
}
```
