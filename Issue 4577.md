# Issue 4577: [with patch, needs review] simple interface to scipy.optimize.leastsq

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2008-11-21 15:06:00

Assignee: whuss

This patch adds a function `find_fit()`, which works similarly to Mathematica's `FindFit[]`.




---

Attachment


---

Attachment

Code looks reasonable, passes doctests.

Apply both patches.


---

Comment by mabshoff created at 2008-11-23 09:46:20

Resolution: fixed


---

Comment by mabshoff created at 2008-11-23 09:46:20

Merged both patches in Sage 3.2.1.alpha0
