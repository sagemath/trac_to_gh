# Issue 3446: notebook -- implement basic account recovery

Issue created by migration from https://trac.sagemath.org/ticket/3446

Original creator: TimothyClemans

Original creation time: 2008-06-17 03:01:30

Assignee: timothyclemans

Make a forgot password page.

User enters username. The Notebook checks if the user's e-mail has been confirmed.

If the e-mail has been confirmed then a new password is generated in the form of a numeral. That password is e-mailed to the user.


---

Comment by was created at 2008-06-17 03:09:28

Changing keywords from "" to "editor_wstein".


---

Attachment


---

Attachment

uses letters with numerals instead of pure numerals


---

Comment by was created at 2008-06-19 23:19:13

I requested that Tom Boothby referee this.


---

Comment by boothby created at 2008-06-24 07:03:20

Works for me


---

Comment by mabshoff created at 2008-06-25 03:56:43

Resolution: fixed


---

Comment by mabshoff created at 2008-06-25 03:56:43

Merged in Sage 3.0.4.alpha1
