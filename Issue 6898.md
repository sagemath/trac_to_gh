# Issue 6898: update the installation guide

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-06 10:29:20

Assignee: tba

As the subject says.


---

Comment by mvngu created at 2009-09-06 10:31:50

based on Sage 4.1.1


---

Attachment


---

Comment by mhansen created at 2009-09-07 21:02:07

I don't understand the part about running "./sage" first to set up environment variables or which files you're referring to when you say that they should run "./sage -br main" to regenerate local files.


---

Attachment

apply on top of other patch


---

Comment by jhpalmieri created at 2009-09-22 23:36:59

I agree with mhansen.  I've created a second patch which rewrites that part of the documentation.  I'll give mvngu's patch a positive review, subject to this change.  If my part is okay, the whole thing should get a positive review.


---

Comment by mvngu created at 2009-09-23 01:18:27

Merged both patches.


---

Comment by mvngu created at 2009-09-23 01:18:27

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:42:33

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
