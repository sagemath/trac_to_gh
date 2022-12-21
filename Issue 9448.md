# Issue 9448: make it clearer not to edit sources in site-packages

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2010-07-07 10:20:04

Assignee: mvngu

CC:  was cremona jhpalmieri

Suggested approaches during SD23 lightning talk:

Add a big note in the developer guide around where the location of the cloned branch is mentioned

Add an extra field in the source introspection pointing to the sage source file. (Suggested by John Cremona)


---

Comment by jdemeyer created at 2010-07-07 13:38:37

Changing type from enhancement to defect.


---

Attachment


---

Comment by jdemeyer created at 2010-11-12 21:24:43

I know it does not nearly address all the issues in the ticket, but at least this doc patch is a start...


---

Comment by jdemeyer created at 2010-11-12 21:24:43

Changing keywords from "" to "doc".


---

Comment by jdemeyer created at 2010-11-12 21:24:43

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-11-13 08:42:09

I'm OK with the added documentation in [attachment:9448.patch]. Note that that patch introduces a trivial typo, which is fixed in [attachment:trac-9448_reviewer.patch]. If my reviewer patch is OK, then the whole ticket gets a positive review.


---

Comment by jdemeyer created at 2010-11-13 10:12:51

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-15 23:26:18

Resolution: fixed
