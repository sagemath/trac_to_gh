# Issue 1581: 3d graphics do not show all objects by default

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-12-21 08:58:06

Assignee: was


```
from sage.plot.plot3d.all import Sphere
Sphere(.1).translate(1,2,3).show()
```


does not adjust the viewpoint, etc. to include the sphere, so it confusingly looks like a blank plot until, for example, the interactive version is rotated around.  It would be nice to have at least some part of the plot, if not the whole thing, visible by default.


---

Comment by robertwb created at 2007-12-30 10:55:31

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-30 10:55:31

Changing status from new to assigned.


---

Comment by robertwb created at 2007-12-30 10:56:30

I've done a little bit of work on bounding boxes, this is what I think we should be using. (There are more sophisticated bounding methods, but I don't think we'll need them for out application.)


---

Comment by was created at 2008-01-01 10:30:04

This patch fixes the problem, plus does a *lot* of other work.  This is a snapshot --  it is not suitable for inclusion in the next version of Sage as is -- probably many 3d doctests still fail.


---

Attachment

This has already been resolved included in Sage.


---

Comment by robertwb created at 2008-01-15 06:14:01

Resolution: fixed
