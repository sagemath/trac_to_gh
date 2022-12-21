# Issue 3577: [with patch; needs review] numpy -- don't import into sage on startup (take 2)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 23:34:11

Assignee: cwitty

This is a followup to #3561.  It makes it so numpy is definiteley not imported on startup, and even has a test to ensure this. 


---

Attachment


---

Comment by mhansen created at 2008-07-07 00:30:04

Passes tests in finance/ and modules/.  Looks good to me.


---

Comment by mabshoff created at 2008-07-07 02:59:21

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 02:59:21

Merged in Sage 3.0.4.alpha2. Note that due to a merge conflict #3580 deals with follow up.
