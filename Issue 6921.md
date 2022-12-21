# Issue 6921: MATLAB crashes on Snow Leopard due to library conflicts

Issue created by migration from Trac.

Original creator: jjh

Original creation time: 2009-09-11 04:28:16

Assignee: was

When using the MATLAB interface in Sage MATLAB crashes on startup. This is due to library conflicts with Sage.

I have created a (minor) patch to use sage-native-execute when starting MATLAB. This fixes the problems on my machine (OS X 10.6) and the interface now passes all doctests.


---

Attachment


---

Comment by was created at 2009-09-22 14:49:29

I can't test the exact setup, but in all cases using sage-native-execute is a good idea, and this does work on Linux, so positive review.


---

Comment by mvngu created at 2009-09-23 06:36:18

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:49:12

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
