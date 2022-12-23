# Issue 3918: notebook -- MAJOR BUG involving uploading file from URL

Issue created by migration from https://trac.sagemath.org/ticket/3918

Original creator: was

Original creation time: 2008-08-20 23:17:14

Assignee: boothby

1. Go to Data --> Upload File
2. Select a URL that takes "forever" to download.
3. Now the ENTIRE SERVER hangs "forever".  

This is clearly very much not good. 


---

Comment by mhansen created at 2008-09-08 10:25:03

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2008-09-08 10:25:03

Changing status from new to assigned.


---

Attachment


---

Comment by TimothyClemans created at 2008-09-08 11:12:46

For review, I first reproduced the bug using sage-3.1.1 and then tried to reproduce it with the patch applied. The bug seems to be fixed with the patch applied. I also made sure that uploading a file worked in general.


---

Comment by mabshoff created at 2008-09-09 00:40:30

Resolution: fixed


---

Comment by mabshoff created at 2008-09-09 00:40:30

Merged in Sage 3.1.2.rc1
