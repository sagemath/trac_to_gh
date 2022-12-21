# Issue 7671: strongly_connected_components in c_graphs

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-12-12 18:13:25

Assignee: rlm

The function strongly_connected_components uses Networkx for the moment. As c_graphs are to become the standard implementation of graphs in Sage, this function should be rewritten in Cython.


---

Comment by ncohen created at 2010-02-22 21:21:37

Done here, with small other things :-)

Nathann


---

Comment by ncohen created at 2010-02-22 21:21:37

Changing status from new to needs_review.


---

Comment by rlm created at 2010-03-02 03:13:16

Typo: "conaitning"


---

Comment by rlm created at 2010-03-02 03:48:03

All tests pass. Works for me, if the typo gets fixed


---

Comment by rlm created at 2010-03-02 03:48:03

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by ncohen created at 2010-03-02 08:53:40

Done !


---

Comment by mvngu created at 2010-03-03 14:17:20

Resolution: fixed
