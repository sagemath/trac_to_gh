# Issue 6996: turn off axes in new contour plots

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-09-22 21:33:23

Assignee: was

CC:  kcrisman

contour plots should not have axes lines through by default because they may be confused with the contour lines.


---

Attachment


---

Comment by kcrisman created at 2009-09-23 01:09:05

Well, it looks a little weird because of the ticks facing down in the new matplotlib, but certainly that's better than before.  Positive review.


---

Comment by mvngu created at 2009-09-23 23:02:04

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:52:04

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
