# Issue 9059: some shortcuts for "is_H-free" tests

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-05-26 22:34:40

Assignee: jason, ncohen, rlm

Some useful tests :

    * is_even_hole_free
    * is_odd_hole_free
    * is_odd_antihole_free

May be worth a dedicated function... :-)

Nathann



---

Comment by ncohen created at 2010-06-06 11:01:12

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-06-13 16:58:59

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-13 16:58:59

Well, as odd_antihole_free is just g.complement().is_odd_hole_free, let this patch just define the first two :-)

Nathann


---

Attachment

Looks good to me.


---

Comment by rlm created at 2010-06-21 20:45:44

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:46:25

Resolution: fixed
