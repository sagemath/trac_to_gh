# Issue 2570: make apply_and_flatten for hg_sage

Issue created by migration from https://trac.sagemath.org/ticket/2570

Original creator: craigcitro

Original creation time: 2008-03-17 10:36:02

Assignee: was

One could add functionality to `hg_sage` to make it take a list of patches or bundles, apply each and rollback (but not revert!) until either (1) no patches are left, or (2) an error occurs. This would allow one to flatten patches and bundles by using this, then commiting.


---

Comment by kcrisman created at 2012-06-01 17:54:43

This could still be useful, but given recent developments (i.e., increasing developer use of just hg and probably eventual switch to git) we can put this on sage-wishlist.


---

Comment by chapoton created at 2014-03-14 19:31:25

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-03-14 19:31:25

we have switched to git, this is obsolete


---

Comment by mmezzarobba created at 2014-03-15 13:27:24

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:41:14

Resolution: wontfix
