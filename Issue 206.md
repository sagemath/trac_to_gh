# Issue 206: Graphic.append() does not update xmin, xmax etc.

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-01-23 04:46:27

Assignee: was

If I add a bunch of graphics primitives to a Graphic object using the Graphic append() method, the `__xmax`, `__xmin`, `__ymax`, `__ymin` attributes are not updated. Therefore when I try to plot the graphic, nothing shows up. Code for the correct behaviour can be found in the `Graphic.__add__()` method.



---

Comment by rlm created at 2007-08-18 16:36:07

Changing assignee from was to rlm.


---

Comment by rlm created at 2007-08-18 20:45:06

Resolution: fixed


---

Comment by rlm created at 2007-08-18 20:45:06

http://sage.math.washington.edu/home/rlmill/xmin.patch


---

Comment by rlm created at 2007-08-18 21:07:39

Changing status from closed to reopened.


---

Comment by rlm created at 2007-08-18 21:07:39

The correct behaviour is not quite that in Graphic.__add__(), since this is adding two Graphics objects. The reason for this bug is that primitives don't usually remember their xmin/max values, and if they do it's inconsistent.


---

Comment by rlm created at 2007-08-18 21:07:39

Resolution changed from fixed to 


---

Comment by was created at 2007-08-19 01:05:57

After a massive amount of discussion, we decided that there should be no Graphic.append method.  It just doesn't even make sense.   So we removed it and closed this bug.


---

Comment by was created at 2007-08-19 01:05:57

Changing assignee from rlm to agc.


---

Comment by was created at 2007-08-19 01:05:57

Changing status from reopened to new.


---

Comment by was created at 2007-08-19 01:06:34

Resolution: fixed
