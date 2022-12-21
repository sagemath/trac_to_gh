# Issue 9140: construct the normalized laplacian matrix for a graph

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-06-04 19:56:44

Assignee: jason, ncohen, rlm

CC:  ncohen rlm

This patch adds a "normalized" option to the laplacian_matrix method to return the normalized Laplacian matrix.


---

Attachment


---

Comment by jason created at 2010-06-04 20:31:12

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-06-04 20:57:21

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-06-04 20:57:21

Does its job, and applies fine on top of the 100000 dependencies of ticket #8922. It is better not to merge this ticket to sage until all these tickets are merged too, by the way, to avoid having to rebase them all.

Positive review !

Nathann


---

Comment by jason created at 2010-06-04 21:09:25

hehe...that's a tricky way to get me to review #8922 and dependencies :)


---

Comment by ncohen created at 2010-06-04 21:11:50

I'm really sorry about this but... Minh was kind enough to rebase most of those, and I spent so much time struggling with those dependencies myself.... I really don't want to do it all again....ever :-D

Nathann


---

Comment by jason created at 2010-06-04 21:12:40

I totally agree about not having to rebase!


---

Comment by mhansen created at 2010-06-06 07:19:03

Resolution: fixed
