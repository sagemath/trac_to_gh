# Issue 8782: pari does not work under Cygwin

Issue created by migration from https://trac.sagemath.org/ticket/8782

Original creator: mhansen

Original creation time: 2010-04-27 16:04:30

Assignee: tbd

We need to do the same fix with paripriv.h as we do on Solaris.

There is an spkg at http://sage.math.washington.edu/home/mhansen/cygwin_port/pari-2.3.3.p9.spkg


---

Comment by mhansen created at 2010-04-27 16:04:40

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-05-24 23:52:21

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2010-05-24 23:52:21

This needs to be rebased on the new PARI.


---

Comment by mhansen created at 2010-05-25 22:49:25

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-05-25 22:49:25

There is a new rebased spkg up at http://sage.math.washington.edu/home/mhansen/pari-2.3.5.p1.spkg

This is the one that should be reviewd / included.


---

Comment by was created at 2010-05-26 00:45:14

Resolution: fixed
