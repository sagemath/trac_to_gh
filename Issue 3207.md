# Issue 3207: upgrade jsmath to version 3.5

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-05-14 22:33:14

Assignee: boothby

The newest version is 3.5, from March 2008.  The attached patch upgrades the jsmath.


---

Attachment

Apply to the extcode repository


---

Comment by jason created at 2008-05-14 22:36:07

uh, wait, something doesn't seem to be working correctly with this...


---

Comment by jason created at 2008-05-14 22:37:25

Never mind, I just had to refresh the page to get rid of the old cached version.  The patch seems fine.


---

Comment by mhampton created at 2008-05-24 20:48:39

Changing assignee from boothby to mhampton.


---

Comment by mhampton created at 2008-05-24 21:01:13

This is hard to systematically test, but I tried out some new features like the auto-bold from <B> tags, and they seem to work.  It might be good if one more person gave it a shot before merging though.


---

Comment by mhampton created at 2008-05-24 21:01:13

Changing assignee from mhampton to somebody.


---

Comment by craigcitro created at 2008-06-20 04:53:40

When this gets merged, mabshoff will remind wstein to check this.


---

Comment by mabshoff created at 2008-06-23 06:52:00

Merged in Sage 3.0.4.alpha0


---

Comment by mabshoff created at 2008-06-23 06:52:00

Resolution: fixed
