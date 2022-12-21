# Issue 9532: fix uncontrolled randomness in sage/graphs

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2010-07-17 20:12:40

Assignee: cwitty

CC:  rlm

There are several places in sage/graphs that use random numbers that aren't under the control of randstate.pyx.  I'm going to fix them now.



---

Attachment


---

Comment by cwitty created at 2010-07-17 22:49:21

OK, the patch is up.  I fixed all the randomness I found (except for two calls in two versions of random_stress, which I left alone except for a comment).


---

Comment by cwitty created at 2010-07-17 22:49:21

Changing status from new to needs_review.


---

Comment by rlm created at 2010-07-19 11:40:42

Looks good to me.


---

Comment by rlm created at 2010-07-19 11:40:42

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 02:49:34

Resolution: fixed
