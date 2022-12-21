# Issue 2682: [with patch] balanced product for generators/iterators

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-03-27 06:22:55

Assignee: somebody

Products of lists were balanced, but for iterators the factors were multiplied in sequence (which can greatly degrade performance). This patch addresses that. 


---

Attachment


---

Comment by boothby created at 2008-04-10 04:51:29

This has been around for a while, but wasn't tagged "needs review".


---

Comment by mhansen created at 2008-04-10 18:57:16

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2008-04-10 18:57:16

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-10 18:57:16

Looks good to me.


---

Comment by mabshoff created at 2008-04-11 22:35:04

Merged in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-11 22:35:04

Resolution: fixed
