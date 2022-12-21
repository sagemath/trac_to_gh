# Issue 6038: add implicit_plot3d to the reference manual (and maybe an example in the tutorial)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-14 15:26:53

Assignee: tba

CC:  wcauchois

Please add the wonderful implicit_plot3d to the reference manual, and possibly even add an example to the tutorial.


---

Attachment

(This patch is based on Sage 4.0.rc0.)

In order to make the automatically generated reference documentation clearer, I moved the implicit_plot3d() function into a separate file called "implicit_plot3d.py". I see this has been done for some of the other plotting functions as well. I also took the liberty of adding a little bit to the meager section on "Three-Dimensional Plots" in the tour of Sage.


---

Comment by mhansen created at 2009-05-26 16:49:29

Looks good to me.

Merged in Sage 4.0.rc1.


---

Comment by mhansen created at 2009-05-26 16:49:29

Resolution: fixed
