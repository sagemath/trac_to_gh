# Issue 3949: notebook -- move all HTML in twist.py to templates

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-25 16:10:35

Assignee: boothby

Move the HTML in twist.py in the classes/functions ` ForgotPassPage, ListOfUsers, message, Worksheet_rating_info, and RegConfirmation. `

Relies on #3937


---

Comment by TimothyClemans created at 2008-08-25 17:39:30

Ignore the class ` Worksheet_rating_info `


---

Attachment


---

Comment by malb created at 2008-09-24 11:04:59

See #3923


---

Attachment


---

Comment by mhansen created at 2008-10-23 23:31:47

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2008-10-23 23:31:47

Changing status from new to assigned.


---

Attachment

I've rebased this against 3.2.alpha0 and moved the templates into sage/server/notebook/templates/

Apply only the last two patches: trac_3949.patch and extcode_3949.patch


---

Comment by mabshoff created at 2008-10-25 23:01:13

Merged trac_3949.patch and extcode_3949.patch in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-25 23:01:13

Resolution: fixed
