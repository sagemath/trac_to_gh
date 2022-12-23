# Issue 2989: [with patch; needs review] notebook -- issue with how the notebook is run that breaks it sometimes; also fix a typo in pid.

Issue created by migration from https://trac.sagemath.org/ticket/2989

Original creator: was

Original creation time: 2008-04-21 14:41:26

Assignee: boothby

I made very minor harmless change to how the notebook twisted daemon is started, which makes it more robust.   Also, it was completely broken on my system until I made this change.  This is probably related to us updating to a new version of twistd.

The change is just to cd into the notebook directory before starting the tracd server.  That's it. 


---

Attachment

fails to apply against alpha5 :(


---

Attachment


---

Comment by was created at 2008-04-22 04:57:59

Resolution: fixed
