# Issue 1542: R package doesn't notice if rpy fails to build

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-12-17 02:49:05

Assignee: craigcitro

I think the title says it all; the issue is that no return value is checked, so R doesn't know that anything is wrong. The attached patch just adds a check in spkg-install to make sure everything went okay with the rpy install.


---

Comment by craigcitro created at 2007-12-17 02:52:45

The patch is against r-2.6.1.p6.spkg (I forgot to mention that above, though it probably goes without saying).


---

Comment by craigcitro created at 2007-12-17 02:59:02

Changing status from new to assigned.


---

Attachment

Posted new version of the patch, which reflects the updated name for the rpy-1.0.1.p0.spkg. (I also added a variable so that the rpy spkg name only appears once, instead of twice, making it less likely that someone would accidentally change one and not the other.)


---

Comment by rlm created at 2007-12-18 02:04:29

Merged in 2.9.1.alpha1


---

Comment by rlm created at 2007-12-18 02:04:29

Resolution: fixed
