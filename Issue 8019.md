# Issue 8019: graphics_array messes up dimensions of plots

Issue created by migration from https://trac.sagemath.org/ticket/8019

Original creator: pdehaye

Original creation time: 2010-01-21 00:31:30

Assignee: was

Keywords: graphics_array, scale

The following code should illustrate this, see picture below, everything gets scaled for no reason.

graph = circle((0,0),20)
graph.set_aspect_ratio(1)
graph2 = graphics_array([[graph]*4]*4)
graph2.show()


---

Attachment


---

Comment by pdehaye created at 2010-01-21 08:56:25

Changing keywords from "graphics_array, scale" to "axes_range, axes_pad".


---

Comment by pdehaye created at 2010-01-21 08:56:25

Changing priority from minor to major.


---

Comment by jason created at 2010-09-29 21:44:01

I think the problem is that in the save routine (actually, in the .matplotlib() method), the x and y limits are changed according to the axes_pad setting.  Instead, they should be temporarily changed and then changed back so that the graphic has the same x and y limits as it did when starting.


---

Comment by mhansen created at 2010-12-21 20:36:21

This has been fixed by #10291.


---

Comment by mhansen created at 2010-12-21 20:36:21

Resolution: invalid
