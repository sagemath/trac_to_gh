# Issue 1737: ctl-c doesn't exit job in parametric_plot3d

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-01-09 17:40:24

Assignee: was

The following paraterization of the Mobius strip
takes a very long time and won't quit when ctl-c is
used:

sage: u,v = var("u,v")
sage: parametric_plot3d([cos(u)*(1+v*cos(u/2)), sin(u)*(1+v*cos(u/2)), v*sin(u/2)], (-2, 2), (-2, 2)).show()
^D
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...

This error message repeats ever time you proess ctl-c.


---

Comment by wdj created at 2008-01-09 18:10:59

This works much faster:
sage: parametric_plot3d([0.5*cos(u)*(1+v*cos(u/2)), 0.5*sin(u)*(1+v*cos(u/2)), v*sin(u/2)], (u,-2, 2), (v,-2, 2)).show()

and is more efficient.


---

Comment by was created at 2008-01-18 16:24:14

This is fixed by #1833.


---

Comment by mabshoff created at 2008-01-21 04:13:49

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 04:13:49

Merged in Sage 2.10.1.alpha1 (patch from #1833)
