# Issue 4787: Race condition in sage-doctest folder creation

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-12-14 00:58:37

Assignee: gfurnish

There is a race condition in sage-doctest during folder creation at line 586, which is in a function called at line 441.  This can cause doctesting a file to fail with file not found errors.  This is different then the other file not found error that was in ptest.  


---

Attachment


---

Comment by gfurnish created at 2008-12-14 01:50:04

Changing keywords from "" to "mabshoff".


---

Comment by gfurnish created at 2008-12-14 01:50:04

The line numbers in the description above should be switched -- basically in a rare case another sage-doctest can create the directories before this one creates them, but after it has decided they don't already exist.  This tells it to ignore errors on making the directories -- they will still get caught later.


---

Comment by gfurnish created at 2008-12-14 01:50:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-14 04:49:08

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-14 05:43:01

Resolution: fixed


---

Comment by mabshoff created at 2008-12-14 05:43:01

Merged in Sage 3.2.2.rc0
