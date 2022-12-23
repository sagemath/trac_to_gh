# Issue 8690: sage -pkg should add checksums as in #329

Issue created by migration from https://trac.sagemath.org/ticket/8690

Original creator: ddrake

Original creation time: 2010-04-15 00:40:11

Assignee: tbd

In #329, a method for adding checksums to spkg files to verify their integrity is proposed; if we implement that method, it would be very useful to have `sage -pkg` automatically add those checksums. Making `sage -pkg`  the canonical way to produce a spkg file will be convenient for users and allow us to guarantee that the spkg conforms to our standards.

This ticket depends on #8679 and #329.


---

Comment by jdemeyer created at 2014-11-06 15:54:40

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-11-06 15:54:40

Obsolete


---

Comment by jdemeyer created at 2014-11-06 15:54:45

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-11-07 16:49:20

Resolution: wontfix
