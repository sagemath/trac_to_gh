# Issue 1859: 3d and 2d graphics -- some unification

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-20 01:27:25

Assignee: was

Make it so that the following sort of thing works:


```
sage: sphere() + plot(sin(x), (x,0,10))
sage: plot(sin(x), (x,0,10)).graphic3d()
```


and


```
sage: plot(sin(x), (x,0,10)).show(viewer='jmol')
```


In each case the plot would be rendered using 3d primitives instead of 2d primitives, when possible -- primitives that aren't implemented in 3d would degrade or be removed.   Basically make a way of _coercing_ 2d plots into the world of 3d plots. 

This would make it possible to view whole arrays, groups, whatever of 2d plots all organized in some spatial way in 3d, and also to zoom in very close, etc., on 2d plots.



---

Comment by robertwb created at 2008-01-20 01:44:05

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-01-20 01:44:05

Changing status from new to assigned.


---

Attachment


---

Comment by robertwb created at 2008-01-20 04:22:23

I've implemented turning most 2d primitives into 3d primitives, e.g. 


```
sage: sphere(aspect_ratio=[1,1,1]) + plot(sin(x), 0, 10)
sage: sum([plot(z*sin(x), 0, 10).plot3d(z) for z in range(10)])
```



---

Comment by was created at 2008-01-20 05:05:55

AWESOME!!

Just playing around

```
sage: var('x y'); p1 = parametric_plot3d((x,y,0), (x,-2,2), (y,-2,2), color='red', opacity=0.5)
(x, y)
sage: p2 = plot(sin(x),(-2,2)).plot3d().translate(0,0,0.1)
sage: p1 + p2 + sphere((0,0,1),0.01) + polygon([(0,0), (0,1), (1,2), (2,0)]).plot3d().translate((0,0,-0.1)) + sphere((0,0,-1),0.1)

```



---

Comment by mabshoff created at 2008-01-20 05:24:24

Merged in Sage 2.10.1.alpha0


---

Comment by mabshoff created at 2008-01-20 05:24:24

Resolution: fixed
