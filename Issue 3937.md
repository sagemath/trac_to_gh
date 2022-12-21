# Issue 3937: notebook -- move HTML for account settings page to Jinja template

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-23 20:34:05

Assignee: boothby

Relies on #3923


---

Attachment


---

Comment by malb created at 2008-09-24 11:04:38

See #3923


---

Attachment


---

Attachment


---

Comment by mhansen created at 2008-10-23 23:16:35

I've rebased this against 3.2.alpha0 and moved the template to sage/server/notebook/templates/.

Apply only the last two patches: trac_3937.patch and extcode_3937.patch


---

Comment by mhansen created at 2008-10-23 23:16:35

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2008-10-23 23:16:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-25 22:55:23

Resolution: fixed


---

Comment by mabshoff created at 2008-10-25 22:55:23

Merged trac_3937.patch and extcode_3937.patch in Sage 3.2.alpha1
