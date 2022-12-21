# Issue 1892: notebook -- uploading a data file should give some help about the DATA variable

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-23 14:02:10

Assignee: boothby


```
> The other option which some students tried was the upload a file
> using Data.  It indeed uploads the file to a text cell, but we were
> unable to find out how one accesses it. 

Upload it then access it by typing

open(DATA + 'chapitre.1.txt').read()

This DATA variable is documented in line three if you click on the Help button
in the upper right of the worksheet.  It would also be good if it appeared any
time you upload a file in the confirmation message -- it doesn't right now.  I'll
make a ticket to add this (which will be very easy). 
```



---

Attachment


---

Comment by mabshoff created at 2008-05-12 11:21:50

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-12 11:22:04

Resolution: fixed


---

Comment by mabshoff created at 2008-05-12 11:22:04

Merged in Sage 3.0.2.alpha1
