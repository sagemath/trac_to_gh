# Issue 5450: plotting a vector as a point plots a sphere, not a point

Issue created by migration from https://trac.sagemath.org/ticket/5450

Original creator: jason

Original creation time: 2009-03-06 21:44:22

Assignee: was

Presumably, plotting a point is more efficient.  However, 


```
vector([1,2,3]).plot(plot_type='point')
```


plots a sphere instead of a point3d (or point2d, if 2-dimensional).  This should be changed to plot a point.


---

Comment by jason created at 2009-03-06 21:44:27

Changing assignee from was to jason.


---

Comment by jason created at 2009-03-06 21:44:27

Changing status from new to assigned.


---

Comment by jason created at 2009-03-06 21:55:02

Another performance enhancement would be using a line3d with arrow_head=True instead of an arrow3d command.  I think that would also preserve aspect ratio better anyway.


---

Comment by jason created at 2009-03-06 22:02:18

using the line3d command instead of the arrow3d command I think would be more in line with the result of vector([1,2]).plot().plot3d() (which I believe uses the line3d command).


---

Attachment

This should make plotting lots of 3d vector arrows or points significantly faster.


---

Comment by robertwb created at 2009-04-16 06:22:47

Looks good.


---

Comment by mabshoff created at 2009-04-16 11:45:04

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 11:45:04

Resolution: fixed
