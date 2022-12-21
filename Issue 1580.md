# Issue 1580: notebook shows graphics out of order

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-12-21 08:44:06

Assignee: boothby


```
from sage.plot.plot3d.all import Sphere
Sphere(1).show()
plot(x^3,xmin=0,xmax=1).show()
```


shows the plot first and the sphere second on my computer (old 850 Mhz PIII running ubuntu 7.10).  This is confusing.



---

Comment by cwitty created at 2007-12-21 21:19:54

William says,

```
This will likely happen for everybody.  It is likely caused by the 3d
graphics not
calling the right function to get the next default png filename.
Thanks for reporting it. 
```



---

Attachment


---

Comment by rlm created at 2007-12-23 03:20:26

merged in 2.9.1 rc2


---

Comment by rlm created at 2007-12-23 03:20:26

Resolution: fixed
