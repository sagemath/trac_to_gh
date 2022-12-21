# Issue 2812: [with patch; needs review] notebook.py doctests

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-04-05 18:56:51

Assignee: was




---

Attachment

do not apply 2812_1.patch this patch corrects the encoding error


---

Comment by TimothyClemans created at 2008-04-05 20:16:18

I just noticed that the doctests for users and user are the same. I'll fix that as soon as I get back.


---

Comment by TimothyClemans created at 2008-04-05 20:41:26

fixes users() and user() doctests are the same issue


---

Attachment

made sure dictonaries were sorted and changed 'mat' to 'password' and 'mark' to 'newpassword' in create_default_users() doctests


---

Attachment

Looks good to me.  I've combined all the need patches into 2812.patch so that is the only one that needs to be applied.


---

Comment by mabshoff created at 2008-04-05 22:00:32

Merged 2812.patch in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-05 22:00:32

Resolution: fixed
