# Issue 924: the matplotlib spkg patches break underlying functionality

Issue created by migration from https://trac.sagemath.org/ticket/924

Original creator: cwitty

Original creation time: 2007-10-18 21:43:22

Assignee: was

The matplotlib spkg overwrites lib/matplotlib/ticker.py with its own version.  This breaks "tick" formatting (the numbers displayed on the X and Y axis); the result is that these numbers display in scientific notation far more often than is reasonable.  (Note that this does not affect most Sage usage, since Sage turns off the matplotlib axes and draws its own.  However, Sage users should still be able to use the matplotlib package with its documented interface if they prefer.)

Note that fixing this (restoring the original ticker.py), and making no other changes, will break plotting for people who have old versions of .sage/matplotlibrc, because their matplotlibrc will not specify values for axes.formatter.limits (which is read by line 271 of ticker.py).  This should be fixed either by figuring out how to safely upgrade people's matplotlibrc (possibly hard), or by changing matplotlib so that default values for axes.formatter.limits are used if the matplotlibrc does not specify values.


---

Comment by cwitty created at 2007-10-18 21:51:00

Actually, looking closer, I see that matplotlib already has code to set a default for axes.formatter.limits, in lib/matplotlib/__init__.py; but that code is removed by overwriting __init__.py by a much older version from patches/.


---

Comment by cwitty created at 2007-12-19 15:42:24

Changing to a closer milestone, since the bug affects somebody besides me: http://groups.google.com/group/sage-support/browse_thread/thread/edd4829f01dbbcf0/7dfec273f7ba4032#7dfec273f7ba4032


---

Comment by was created at 2007-12-21 00:18:15

I have posted a new spkg here:

http://sagemath.org/packages/experimental/matplotlib-0.91.1.spkg

DO NOT Just apply this yet.  I tested building on many systems
and it works.  However, some doctests in plot.py fail, due to changes
in matplotlib.  So it is *essential* that this ticket not be closed
and the above spkg not included in sage until a corresponding patch
against the sage library is created and posted here.


---

Comment by was created at 2007-12-21 00:22:10

Changing status from new to assigned.


---

Comment by was created at 2007-12-21 19:31:09

Changing priority from major to blocker.


---

Attachment


---

Comment by rlm created at 2007-12-22 00:43:55

merged in 2.9.1 alpha3


---

Comment by rlm created at 2007-12-22 00:43:55

Resolution: fixed
