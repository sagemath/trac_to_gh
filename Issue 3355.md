# Issue 3355: invoke the libdir rewrite script on "sage -upgrade"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-03 05:33:54

Assignee: cwitty

All the *.la files in $SAGE_LOCAL/lib have their libdir variable rewritten when Sage is moved. Do this also when installing any spkg since we might have moved the tree. This will likely cause a number of upgrade problems.

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:21:47

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:21:47

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by kini created at 2012-03-21 00:04:34

* *Priority* changed from _critical_ to _major_

If we've released for years and years without fixing this, it doesn't make sense to keep it as critical.

... just kidding!


---

Comment by jdemeyer created at 2013-03-28 22:57:03

`sage-location` actually does this now.


---

Comment by jdemeyer created at 2013-03-28 22:57:03

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-03-28 22:57:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-29 19:00:51

Resolution: worksforme
