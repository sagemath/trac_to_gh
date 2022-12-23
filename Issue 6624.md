# Issue 6624: remove json function from server/simple/twist.py

Issue created by migration from https://trac.sagemath.org/ticket/6624

Original creator: ddrake

Original creation time: 2009-07-26 05:38:49

Assignee: boothby

CC:  jason

In twist.py, we have our own json-encoding function, which is no longer necessary now that we use Python 2.6. It should be removed.


---

Comment by ddrake created at 2009-07-26 07:59:41

This ticket depends on #6251, which has been merged in 4.1.1.alpha1.


---

Comment by ddrake created at 2009-07-26 08:02:56

Replying to [comment:1 ddrake]:
> This ticket depends on #6251, which has been merged in 4.1.1.alpha1.

Ack. No, that's wrong. It *hasn't* been merged as I write this (although it almost certainly will be very soon). Also, I'm going to make a patch that depends on _both_ patches at #6251.


---

Comment by ddrake created at 2009-07-26 08:02:56

Changing status from new to assigned.


---

Comment by ddrake created at 2009-07-26 08:02:56

Changing assignee from boothby to ddrake.


---

Comment by mpatel created at 2010-02-01 08:25:11

I've #6576 closed as a duplicate of this ticket.


---

Comment by kcrisman created at 2013-06-14 17:12:36

I assume that this is completely outdated with the new notebook (as well as the cell server)?


---

Comment by kcrisman created at 2013-06-14 17:12:46

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-06-14 18:37:06

Note that #11409 would remove this completely.


---

Comment by kcrisman created at 2013-06-14 18:37:06

Changing status from needs_review to needs_info.


---

Comment by chapoton created at 2014-02-17 12:38:26

There is no longer any twist.py. Can we close this ticket ?


---

Comment by jdemeyer created at 2014-02-21 22:20:05

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2014-02-21 22:37:57

Resolution: wontfix
