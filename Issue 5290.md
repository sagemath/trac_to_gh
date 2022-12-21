# Issue 5290: Sage 3.3.rc1: Sage fails to start due to dangling missed import in plot.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-17 02:17:57

Assignee: mabshoff

It wasn't my fault, but patch is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-17 02:18:03

Changing status from new to assigned.


---

Comment by jason created at 2009-02-17 05:36:26

We all agree that the correct fix is to *delete* the offending line, not just comment it out.


---

Attachment


---

Comment by jason created at 2009-02-17 05:44:15

If the patch is changed to deleting the line instead of just commenting it out, positive review.  It fixes my rc1 so that it starts up.


---

Attachment


---

Comment by mabshoff created at 2009-02-17 06:58:04

Resolution: fixed


---

Comment by mabshoff created at 2009-02-17 06:58:04

Merged both patches in Sage 3.3.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-17 07:08:22

Ok, changing the review to an offical positive review.

Cheers,

Michael
