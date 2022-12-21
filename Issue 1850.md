# Issue 1850: graphics -- serious bug in parametric plotting of curves.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-19 20:26:06

Assignee: was

This works fine

```
sage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi))
```


This is missing half of the parametric plot!!

```
sage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500)
```


I suspect this may be a bug introduced by me or Bobby M. in refactoring some plotting code. 


---

Comment by was created at 2008-01-19 20:33:02

Very disturbingly, if you render using tachyon you don't see the problem:

```
sage: parametric_plot3d((sin(x), cos(x), x), (x,0,10*pi), plot_points=500, viewer='tachyon')
```


Also, rendering some more complicated things makes it so the problem vanishes.

```
sage: parametric_plot3d((sin(x), cos(x), x+sin(x^2)), (x,0,10*pi), plot_points=500)
```



So this is probably a pretty tricky bug to fix, possibly a bug in jmol.


---

Comment by wjp created at 2008-01-19 21:27:28

This seems to hit a hard-coded point limit of 256 in jmol's `org/jmol/shapespecial/Draw.java`, line 69.

I guess we could either change jmol to support arbitrary numbers of points, or split up  curves in 'subcurves' of at most 256 points each.


---

Comment by robertwb created at 2008-01-20 00:45:10

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-01-20 00:45:10

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-20 00:45:10

Chopping it up seems like the simplest choice, preferably at a point of maximum curvature. Setting MAX_POINTS arbitrarily high would increase the memory footprint of every line, and re-writing it to not be so would probably be a significant amount of work (though I can't figure out why it is so in the first place).


---

Attachment


---

Comment by was created at 2008-01-20 01:35:12

It works well for me.  Thanks Robert!


---

Comment by mabshoff created at 2008-01-20 01:53:55

Resolution: fixed


---

Comment by mabshoff created at 2008-01-20 01:53:55

Merged in Sage 2.10.1.alpha0
