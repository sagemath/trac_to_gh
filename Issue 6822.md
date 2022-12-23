# Issue 6822: "empty" .spkg files in binary builds confusing

Issue created by migration from https://trac.sagemath.org/ticket/6822

Original creator: robertwb

Original creation time: 2009-08-25 04:46:21

Assignee: tbd

CC:  jhpalmieri

Followup to #4504. Maybe we should ship .txt rather than .spkg placeholders, and update the build system to understand them.


---

Comment by mvngu created at 2009-08-25 05:05:47

See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f66ee83da5ef679f) thread. It was where this issue started.


---

Attachment


---

Attachment


---

Comment by jhpalmieri created at 2012-10-06 00:00:23

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2012-10-06 00:00:23

Changing keywords from "" to "bdist spkg".


---

Comment by jhpalmieri created at 2012-10-06 00:00:23

Here's a simple-minded approach.


---

Comment by jdemeyer created at 2012-10-06 09:56:05

Probably good, but we should only merge this with #13574.


---

Comment by jdemeyer created at 2012-10-08 12:44:23

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-11-12 21:56:54

Resolution: fixed
