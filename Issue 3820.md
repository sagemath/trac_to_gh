# Issue 3820: notebook -- sometimes published worksheets are listed as being published by pub.

Issue created by migration from https://trac.sagemath.org/ticket/3820

Original creator: was

Original creation time: 2008-08-12 16:17:51

Assignee: boothby

notebook -- sometimes published worksheets are listed as being published by pub; this should *never* be the case. 


---

Comment by mhansen created at 2009-01-24 05:26:37

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-24 05:26:37

I've added a test in the selenium suite for this.


---

Comment by mhansen created at 2009-01-24 05:26:37

Changing assignee from boothby to mhansen.


---

Comment by mabshoff created at 2009-02-02 05:05:50

This patch needs to be rebased unless there is some dependency I am not aware of:

```
sage-3.3.alpha4/devel/sage$ patch -p1 < trac_3820.patch\?format\=raw 
patching file sage/server/notebook/templates/worksheet_listing.html
Hunk #1 succeeded at 130 (offset 1 line).
Hunk #2 FAILED at 178.
1 out of 2 hunks FAILED -- saving rejects to file sage/server/notebook/templates/worksheet_listing.html.rej
```


Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-02-15 04:23:50

I've put up a rebased patch which applies against rc0.


---

Comment by TimothyClemans created at 2009-03-16 20:32:47

looks good

* note that if original worksheet is deleted then the owner cell on the published worksheets page is blank


---

Comment by mabshoff created at 2009-03-25 08:35:11

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 08:35:11

Resolution: fixed
