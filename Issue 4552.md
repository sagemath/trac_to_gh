# Issue 4552: notebook -- when email system on, registration is broken

Issue created by migration from Trac.

Original creator: TimothyClemans

Original creation time: 2008-11-19 18:00:43

Assignee: boothby

CC:  wjp

Depends on #4551


---

Attachment


---

Comment by boothby created at 2009-01-22 00:56:53

Timothy -- please describe the problem that this is supposed to fix.  "Depends on #4551" is insufficient.


---

Comment by TimothyClemans created at 2009-01-22 00:59:27

If the email config is set to True then registration doesn't work.


---

Attachment

modified patch without dependency on #4551


---

Comment by wjp created at 2009-09-01 18:45:17

I modified the attached patch to remove the dependency on #4551. (Only apply `trac_4552-notebook_account_email.patch`)

To elaborate on the problem a little bit: the problem was that the value of the 'email' input box was never read from the form. As a result, when the verification code tries to access it, the server gets a KeyError.

For what it's worth, I give a positive review to adding 'email' to 'input_boxes', which is how Timothy's patch fixes the problem.


---

Comment by wjp created at 2009-09-07 09:52:08

It turns out the dependency on #4551 was really a dependency on #4135. Now that that has been merged, positive review.

Note to release manager: apply only the _original_ patch (`sage-4552.patch`)


---

Comment by mvngu created at 2009-09-07 17:45:16

Resolution: fixed


---

Comment by mvngu created at 2009-09-07 17:45:16

Merged `sage-4552.patch`.
