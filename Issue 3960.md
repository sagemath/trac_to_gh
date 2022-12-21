# Issue 3960: "edit this" on published worksheets doesn't work anymore in 3.1.1

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2008-08-26 18:27:26

Assignee: boothby

Way to reproduce:

 - start notebook
 - create worksheet
 - publish worksheet
 - go to "published worksheets"
 - click published worksheet

result:

"edit this" or "edit a copy" link lead to another "published" version, not a normal worksheet

expected result:

an editable worksheet

NOTE: This worked properly in 3.0.6


---

Comment by mabshoff created at 2008-08-27 07:56:02

This is definitely a blocker for 3.1.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-27 07:56:02

Changing priority from critical to blocker.


---

Comment by itolkov created at 2008-08-27 16:21:24

I believe that this is because somewhere the wrong username is taken into account. Here is an example: publish a worksheet, and navigate to it. The link should say "edit this", not "edit a copy".

Alternatively, I found that the username passed to worksheet_html() in notebook.py is "pub", but was unable to find the source of the problem.


---

Comment by mhansen created at 2008-09-03 00:53:00

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-03 00:53:00

Changing assignee from boothby to mhansen.


---

Attachment


---

Comment by mabshoff created at 2008-09-04 01:43:55

This patch fixes the issue and Mike walked through the code with me. Positive review. Mike is also writing a Selenium doctest for this bug, so we will catch it in the future.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 02:02:46

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 02:02:46

Merged in Sage 3.1.2.rc0
