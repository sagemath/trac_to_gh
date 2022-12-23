# Issue 800: make _sig_on and _sig_off faster when stacked

Issue created by migration from https://trac.sagemath.org/ticket/800

Original creator: craigcitro

Original creation time: 2007-10-03 06:35:24

Assignee: tornaria

Gonzalo brought up the following very good idea: one should rewrite the code for _sig_on and _sig_off to keep a counter of how many _sig_on calls it has seen, and run less than the full amount of code (i.e. nothing involving system calls) if we've already had a _sig_on. Then _sig_off can just decrement the counter, and only do the "real work" if it's being decremented to zero.


---

Comment by malb created at 2009-01-24 12:45:33

Changing type from defect to enhancement.


---

Comment by malb created at 2009-01-25 19:03:26

Changing assignee from tornaria to malb.


---

Comment by malb created at 2009-01-25 19:03:26

Changing status from new to assigned.


---

Comment by jdemeyer created at 2010-10-06 09:07:19

This should be implemented as part of #9678.


---

Comment by jdemeyer created at 2011-01-14 17:38:54

Fixed by #9678.


---

Comment by jdemeyer created at 2011-01-14 17:38:54

Changing status from new to needs_review.


---

Comment by mariah created at 2011-05-13 15:15:08

If this is a sage-duplicate/invalid/wontfix, then I believe this ticket can be closed.


---

Comment by mariah created at 2011-05-13 15:15:08

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-15 14:41:07

Resolution: duplicate
