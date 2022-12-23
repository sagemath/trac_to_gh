# Issue 6002: parametric_plot3d appears not to give the correct axes values

Issue created by migration from https://trac.sagemath.org/ticket/6002

Original creator: wcauchois

Original creation time: 2009-05-07 06:31:27

Assignee: was

CC:  mvngu

Alden Walker describes the bug in a sage-support thread:
> When I run:

> `parametric_plot( (cos(t), sqrt(2)*sin(t)) , (t,0,2*pi))`

> I get a nice 2d parametric plot, with the top of the ellipse clearly
> hitting close to 1.5 on the y-axis.  When I run:

> `parametric_plot3d( (cos(t), 1 , sqrt(2)*sin(t)), (t,0,2*pi))`

> The top of the ellipse really looks like it's at z=1, and the whole
> thing looks a lot like a circle.

Even though the bounding box is reported to be `((-1.0, 1.0, -1.41293...), (1.0, 1.0, 1.41293...))`, jmol labels the axes as (-1, 1), (-1, 1), and (0, 2).

If we construct the curve manually:


```
var('t')
from sage.plot.plot import var_and_list_of_values
_, vals = var_and_list_of_values((0, 2*pi), 75)
w = []
for t in vals:
    w.append(map(float, (cos(t), 1, sqrt(2)*sin(t))))
```


Then notice that while `line3d(w)` is still incorrect, `line3d(w[0:43])` looks correct -- that is, plotting only part of the graph eliminates the error somehow. Quite curious!


---

Comment by jason created at 2009-09-24 18:11:07

#6930 fixes this.


---

Comment by mvngu created at 2009-09-25 08:20:35

Close as duplicate of #6930.


---

Comment by mvngu created at 2009-09-25 08:20:35

Resolution: duplicate
