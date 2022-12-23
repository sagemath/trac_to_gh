# Issue 8830: polybori-0.6.4.spkg causes crashes on exit

Issue created by migration from https://trac.sagemath.org/ticket/8830

Original creator: wjp

Original creation time: 2010-04-30 12:53:29

Assignee: tbd

Per the discussion on #8192, the polybori spkg there caused crashes and valgrind errors on exit.

The new spkg to fix this created by Alexander Dreyer and Minh Nguyen is at:

http://sage.math.washington.edu/home/mvngu/spkg/standard/polybori/polybori-0.6.4.p0.spkg

I tested it, and it gets rid of the valgrind errors and crashes.


---

Comment by wjp created at 2010-04-30 12:53:39

Changing status from new to needs_review.


---

Comment by wjp created at 2010-04-30 12:53:44

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-05-01 05:02:58

Resolution: fixed


---

Comment by AlexanderDreyer created at 2010-08-19 20:34:19

#9768 should fix the dynamic libraries finally.
