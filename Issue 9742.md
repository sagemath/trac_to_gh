# Issue 9742: Sorting edges of a graph

Issue created by migration from https://trac.sagemath.org/ticket/9742

Original creator: rbeezer

Original creation time: 2010-08-13 17:22:10

Assignee: jason, ncohen, rlm

This patch adds a "key" argument to allow custom sorting of the output of the graph method edges(). It adds to the documentation to make it clear that vertices will not always have a default sort order and thus edges may not always sort properly or as expected.

See:

#9741 

http://groups.google.com/group/sage-devel/browse_thread/thread/40ac90ee3f28d723/ 

http://groups.google.com/group/sage-devel/browse_thread/thread/5adbb850f787373c/




---

Comment by rbeezer created at 2010-08-13 17:31:48

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2010-09-07 20:51:54

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-09-07 20:51:54

Nothing to add ! Positive review `:-)`

Nathann


---

Comment by mpatel created at 2010-09-15 22:52:42

Resolution: fixed
