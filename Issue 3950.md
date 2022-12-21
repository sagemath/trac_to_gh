# Issue 3950: notebook -- template(s) for generating worksheet listings

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-08-25 18:05:19

Assignee: boothby

Make templates to replace `notebook.html_worksheet_list_public` and `notebook.html_worksheet_list_for_user` 

Create a new folder to do this. Maybe use `{% include %`}

Relies on #3949.


---

Comment by mhansen created at 2008-10-24 00:01:02

Timothy, are you planning on finishing this in the near future, or do you want me to?


---

Comment by TimothyClemans created at 2008-10-24 10:41:19

Don't apply extcode_3950.patch. Do apply extcode_3950_1.patch


---

Comment by TimothyClemans created at 2008-11-09 01:26:50

Apply extcode_3950_1.patch, extcode_3950_2.patch, trac_3950.patch, and sage-3950_part2.patch


---

Comment by TimothyClemans created at 2008-11-10 04:17:27

Also apply sage-3950_part3.patch


---

Comment by TimothyClemans created at 2008-11-10 04:31:40

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-11-10 04:31:40

Changing status from new to assigned.


---

Comment by mhansen created at 2008-11-28 21:57:16

This should be done in a way such that there is a template for each html_* method in notebook.py (and worksheet.py) and then the templates just use the {%include%} directive to build them out of these pieces.  This makes things easy to change / update.

For example, the topbar should be in its own template so that it can be reused by what ever needs it.  As it is now, there would be lots of duplicate HTML code floating around.


---

Comment by TimothyClemans created at 2008-11-29 23:24:25

I haven't made a template for every html_* yet but the worksheet listing template now uses several templates.


---

Attachment


---

Attachment


---

Attachment

I attached my changes as trac_3950-2.patch.  trac_3950-folded.patch is a patch showing the combined effect of the two patches.  It is helpful for reviewing purposes, but the two other ones are the ones that should be applied for credit reasons.


---

Comment by mabshoff created at 2008-12-04 14:55:37

Resolution: fixed


---

Comment by mabshoff created at 2008-12-04 14:55:37

Merged all three patches in Sage 3.2.2.alpha0
