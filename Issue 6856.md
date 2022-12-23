# Issue 6856: cancel button in notebook user settings not working

Issue created by migration from https://trac.sagemath.org/ticket/6856

Original creator: wjp

Original creation time: 2009-09-01 15:09:35

Assignee: boothby

The cancel button in the 'Settings' page of a notebook user is not working because of a missing 'username' template argument to `account_settings.html`. (There's a redirect to a broken path when pressing the button now.)


---

Attachment


---

Comment by wjp created at 2009-09-01 15:15:16

To reproduce, log in to the notebook, press 'Settings' at the top right, and then press 'Cancel'.


---

Comment by ddrake created at 2009-09-01 23:23:46

A one-line patch that fixes the problem! Positive review.


---

Comment by mvngu created at 2009-09-03 07:03:34

Resolution: fixed
