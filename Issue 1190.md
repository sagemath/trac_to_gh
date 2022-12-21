# Issue 1190: [with patch] fix spkg-check invocation when SAGE_CHECK is non-empty

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-17 06:46:57

Assignee: mabshoff

We call spkg-check when the env variable SAGE_CHECK is non-empty. This didn't work, but the attached patch fixes that.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2007-11-21 07:27:02

updated rev 2 - incorporates suggestions by malb


---

Attachment

Please apply only Sage-2.8.12-fix-spkg-check-invocation.2.patch 

Cheers,

Michael


---

Comment by cwitty created at 2007-11-21 07:34:23

The code changes look good to me (although I didn't actually test it).


---

Comment by mabshoff created at 2007-11-21 07:58:17

Resolution: fixed


---

Comment by mabshoff created at 2007-11-21 07:58:17

Merged in 2.8.13.rc2.
