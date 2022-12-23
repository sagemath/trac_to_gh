# Issue 1729: disable password prompt on initial startup

Issue created by migration from https://trac.sagemath.org/ticket/1729

Original creator: robertwb

Original creation time: 2008-01-09 06:07:20

Assignee: boothby

Because the user can always do notebook(reset=True) it isn't a security risk to automatically log you in the web page that pops up. 

This patch fixes this issue. 



---

Attachment


---

Comment by was created at 2008-01-09 06:08:44

There is no patch attacheD?!


---

Comment by robertwb created at 2008-01-09 06:09:52

Sorry, took me more than 18 seconds to attach the patch.


---

Attachment

Robert's patch works for me, but adds noise to the log.  Revised patch removes the noise.


---

Comment by was created at 2008-01-09 06:53:15

sage: notebook(secure=False)
is now broken.


---

Attachment


---

Comment by robertwb created at 2008-01-09 07:21:25

Changing assignee from boothby to robertwb.


---

Comment by robertwb created at 2008-01-09 07:21:25

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-09 14:54:06

Resolution: fixed


---

Comment by mabshoff created at 2008-01-09 14:54:06

Merged in Sage 2.10.alpha1. Specifically I merged

 * 1729-notebook-login.2.patch
 * inotebook-fix.patch

Cheers,

Michael
