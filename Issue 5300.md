# Issue 5300: do #5291 -- don't save too many snapshots -- more efficiently

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-18 00:49:30

Assignee: boothby

It should not be necessary to do any file io at all to do #5291.  Of course, we should also just be storing diffs somehow...


---

Comment by rbeezer created at 2009-03-09 04:05:05

See related info in #5459


---

Comment by kcrisman created at 2014-09-18 16:59:57

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-09-18 16:59:57

I'm going to suggest this is close enough to #6833 and https://github.com/sagemath/sagenb/issues/216 to close.  At any rate, that is probably what will end up happening to solve this, if anything of that sort actually happens with sagenb before its oft-predicted demise ;-)


---

Comment by kcrisman created at 2014-09-18 17:00:03

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-18 17:57:22

Resolution: duplicate
