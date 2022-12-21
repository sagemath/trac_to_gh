# Issue 1919: improve base fields of DualAbelainGroup

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-01-25 02:41:58

Assignee: joyner

CC:  tscrim jhpalmieri

In sage/groups/abelian_gps/dual_abelian_group_element.py, the __call__
method uses some code which must be modified if the base field is finite.
Specifically, "zeta = F.gen()" must be changed.


---

Comment by chapoton created at 2017-09-13 19:15:02

Changing status from new to needs_review.


---

Comment by chapoton created at 2017-09-13 19:15:02

New commits:


---

Comment by chapoton created at 2017-09-20 18:15:02

another interesting one, simple enough


---

Comment by tscrim created at 2017-09-20 21:06:53

LGTM.


---

Comment by tscrim created at 2017-09-20 21:06:53

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-09-24 13:04:01

Resolution: fixed
