# Issue 2553: dsage unit tests fail on linux

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-03-16 21:41:26

Assignee: yi

Various users have reported that the dsage unit tests fail on linux. This is a known issue and a fix is being worked on by me. 


---

Attachment


---

Comment by yi created at 2008-03-17 02:21:45

This patch disables the unit tests when people run the tests using the sage-maketest script.


---

Attachment

fixes unit tests on linux 32bit.


---

Comment by yi created at 2008-03-23 03:25:44

Attached pb_unittest.patch which should fix the unittest failures on 32bit machines.


---

Comment by mhansen created at 2008-04-07 01:15:29

pb_unittest.patch does not apply cleanly for me with 3.0.alpha1


---

Attachment

This patch should apply cleanly against 3.0.alpha5.


---

Comment by was created at 2008-04-20 23:22:07

also apply this to the scripts repo


---

Attachment

REFEREE REPORT:

I tested this on a bunch of platforms and it works.

I read the code and it looks sane.

COMPLAINT: there is not a *single* line of documentation or comments anywhere
that explain why the new version works when the original didn't or what is
going on.  Shame!  But I still give this a positive review so we can start
testing again.

TO USE: Apply  pb_unittest.2.patch to hg_sage and scripts-2553.patch to hg_scripts


---

Comment by was created at 2008-04-20 23:25:58

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-04-21 02:31:13

Merged pb_unittest.2.patch and scripts-2553.patch in Sage 3.0.rc1


---

Comment by mabshoff created at 2008-04-21 02:31:13

Resolution: fixed
