# Issue 8151: wrong file permissions in lie-2.2.2.p3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/8151

Original creator: dimpase

Original creation time: 2010-02-02 09:25:20

Assignee: tbd

some file permissions are  wrong (600 or 700) in 4.3.1, 
namely 
src/README 
src/box/
 
(so they become unreadable to the world when the thing is installed as root) 


---

Comment by kini created at 2012-05-26 06:50:49

Changing status from new to needs_review.


---

Comment by kini created at 2012-05-26 06:50:49

This is fixed by #12983.


---

Comment by kini created at 2012-05-26 06:51:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-15 09:11:24

Resolution: duplicate
