# Issue 4382: [with patch; needs review] notebook -- use sage-native-execute for ssh'ing for remote pexpect

Issue created by migration from https://trac.sagemath.org/ticket/4382

Original creator: was

Original creation time: 2008-10-29 22:44:29

Assignee: boothby

This patch fixes a major bug that would make it nearly impossible to setup a secure sage server. 
All it does is make sure ssh runs without the Sage environment setup, which is good because of version mismatches.  


---

Attachment

Patch is good, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-30 03:23:35

Resolution: fixed


---

Comment by mabshoff created at 2008-10-30 03:23:35

Merged in Sage 3.2.alpha2
