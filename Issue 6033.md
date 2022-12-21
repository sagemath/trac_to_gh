# Issue 6033: Bring plot/disk.py to 100% coverage

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-05-13 01:38:15

Assignee: tba

Bring plot/disk.py to 100% coverage.


---

Attachment


---

Comment by kcrisman created at 2009-05-13 01:42:05

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-05-13 01:42:05

This patch brings coverage to 100% for plot/disk.py, clarifies that disk really means sector/wedge of a circle, and adds a plot3d method for disks.

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.


---

Comment by kcrisman created at 2009-05-13 01:42:05

Changing assignee from tba to kcrisman.


---

Comment by mabshoff created at 2009-05-14 05:36:15

No review, no milestone 4.0 ;)

Cheers,

Michael


---

Comment by kcrisman created at 2009-05-14 16:17:52

Both depend on #6023


---

Attachment

apply on top of previous patches


---

Attachment

I added the 'color' synonym to rgbcolor and changed the docs accordingly.  I also added another sentence.

Positive review for kcrisman's patches.  kcrisman: can you review my patch?


---

Attachment

Positive review of referee patch; jason, can you review this final patch which makes a couple things more clear (e.g. if someone tried to plot the first example without using thickness and then view it, they might get confused, 2nd example should keep color since that is part of the subplot rendering, etc.)?  

Then apply all four patches once reviewed.  I had some trouble attaching the last one, so if there are two identical ones with the same name only use one of them!


---

Comment by mhansen created at 2009-06-04 19:37:28

The last patch looks fine to me.

Merged in 4.0.1.rc1.


---

Comment by mhansen created at 2009-06-04 19:37:28

Resolution: fixed
