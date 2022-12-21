# Issue 2661: sage cannot compute floor / ceil of log(8)/log(2)

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-03-24 20:13:01

Assignee: was

This happens because the interval remains centered around an integer.


---

Comment by jason created at 2008-03-24 21:12:16

Some concerns about this were raised on IRC.  It seems that the real problem is telling if log(8)/log(2) is an integer.  The (log(8)/log(2)).simplify_log() function tells us that this is 3.


---

Attachment

looks good to me.


---

Comment by mabshoff created at 2008-03-25 04:48:35

Resolution: fixed


---

Comment by mabshoff created at 2008-03-25 04:48:35

Merged in Sage 2.11.alpha2
