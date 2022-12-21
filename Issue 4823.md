# Issue 4823: [with patch, needs review]

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-12-18 00:26:15

Assignee: was

CC:  cpernet

The fix at #3887 computes way to many primes, making det and hnf very slow. The attached patch resolves this issue and still gives correct output. 


---

Attachment


---

Comment by cpernet created at 2008-12-18 00:30:34

Resolution: fixed


---

Comment by cpernet created at 2008-12-18 00:30:34

Patch looks correct and passes doctests.


---

Comment by craigcitro created at 2008-12-18 00:37:27

Changing status from closed to reopened.


---

Comment by craigcitro created at 2008-12-18 00:37:27

I think we need to leave this as "open" until mabshoff merges the patch.


---

Comment by craigcitro created at 2008-12-18 00:37:27

Resolution changed from fixed to 


---

Comment by was created at 2008-12-18 01:12:52

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2008-12-18 06:24:15

How about a title for this ticket?

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-18 14:58:40

Merged in Sage 3.2.2.rc2


---

Comment by mabshoff created at 2008-12-18 14:58:40

Resolution: fixed
