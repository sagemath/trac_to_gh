# Issue 4745: [with patch, needs review] Dsage performance is poor

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-12-09 07:23:01

Assignee: gfurnish

CC:  mhansen

DSage latency is poor, this patch seeks to improve this by a combination of pushing jobs and improving the speed of which new results are detected.  This is the first of many patches that could be made to organically improve DSage, so this is a small patch which should have big results (but there is still plenty of work to be done on DSage.)


---

Attachment

Apply on top of first patch.


---

Comment by gfurnish created at 2008-12-09 08:54:53

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-09 08:54:53

For the record this last patch fixed a race condition that could *potentially* cause #3746 (but theres no guarentee there isn't a different race condition).


---

Comment by gfurnish created at 2008-12-09 18:40:47

Fix for doctest failure upon reenabling.


---

Attachment

Mike,

can you put this on your to review list? It would be nice if this went into 3.2.2.

Cheers,

Michael


---

Attachment

I attached a folded patch since I wanted one for the review.  Really good work on this!  It make DSage way more useable.

Just merge the -combined patch.


---

Comment by mabshoff created at 2008-12-11 15:27:40

Merged trac_4745-combined.patch in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 15:27:40

Resolution: fixed
