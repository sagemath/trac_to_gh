# Issue 6372: Move a few 3d plot files into plot3d

Issue created by migration from https://trac.sagemath.org/ticket/6372

Original creator: kcrisman

Original creation time: 2009-06-20 19:07:49

Assignee: was

tachyon.py and tri_plot.py really belong in plot/plot3d, and there is an extra texture.py which is unused to remove.


---

Comment by kcrisman created at 2009-06-20 19:12:01

Depends on #6269


---

Attachment

This patch also makes necessary changes in a few other files to allow this, including in the plot3d rest documentation.


---

Comment by mvngu created at 2009-06-24 22:24:17

This also needs a rebase, since #6269 requires a rebase.


---

Comment by mvngu created at 2009-06-25 00:16:22

kcrisman: Can you rebase the patch?


---

Attachment

rebased against Sage 4.1.alpha1


---

Comment by mvngu created at 2009-06-26 01:53:32

The patch `trac_6372-rebased.patch` is rebased against Sage 4.1.alpha1. It depends on #6269 and likely to also depends on #5640. So patches should be applied in the following order:
 1. the rebased patch at #6269
 1. the rebased patch at #5640
 1. the rebased patch on this ticket


---

Comment by boothby created at 2009-06-26 17:41:43

Resolution: fixed
