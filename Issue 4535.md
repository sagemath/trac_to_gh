# Issue 4535: refactoring in plot/*

Issue created by migration from https://trac.sagemath.org/ticket/4535

Original creator: mhansen

Original creation time: 2008-11-16 13:12:43

Assignee: was

CC:  timothyclemans

The main goals of this ticket are to split up plot.py so that it's not 4500 lines long and change the way the bounding boxes are computed.


---

Comment by mhansen created at 2008-11-16 13:13:49

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-16 13:13:49

Changing assignee from was to mhansen.


---

Comment by mabshoff created at 2008-11-16 18:08:27

One remark: All the newly created files are missing copyright headers.

Cheers,

Michael


---

Comment by jason created at 2008-11-18 12:56:29

If we are moving to be more based on matplotlib, it would be nice if we could draw stuff in matplotlib and easily convert the result to a sage Graphics object, so we could then add it to other sage graphics objects, etc.

In other words, it would be great if this worked:

sage: a=pylab.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
sage: Graphics(a)


---

Comment by was created at 2008-11-27 17:24:47

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

Attachment


---

Comment by mhansen created at 2008-11-27 21:35:12

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-11-27 22:58:18

The rebased patch applies cleanly to my Sage 3.2.1.alpha3 merge tree. I am doing a sage -ba right now (with a nuke build directory) followed by doctesting to make 100% sure all import issues have been truly fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-27 23:42:34

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

Comment by mabshoff created at 2008-11-28 00:10:58

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

Attachment


---

Attachment


---

Comment by mhansen created at 2008-11-28 02:52:29

I've attached 2 patches which fix the above issues.


---

Comment by mabshoff created at 2008-11-28 04:00:54

With the two new patches all tests including the pickle jar passes. Positive review extended via William.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-28 05:30:32

Merged all three patches in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-28 05:30:32

Resolution: fixed
