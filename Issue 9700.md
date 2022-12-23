# Issue 9700: Export check_edge_label from sparse_graph.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9700

Original creator: rhinton

Original creation time: 2010-08-06 19:38:52

Assignee: rhinton

CC:  rlm ncohen

Keywords: graphs, Cython, sparse

The current `sparse_graph.pxd` does not export `check_edge_label`, which is necessary to translate Python object edge labels to the internal integer indices.  Exporting this function call enables writing Cython code based on the fast sparse graph implementation.



---

Comment by rhinton created at 2010-08-06 20:43:34

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-08-07 02:12:57

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-08-07 02:12:57

One line.... Positively reviewed :-)

Nathann


---

Comment by rlm created at 2010-08-07 03:29:45

Agreed!


---

Comment by mpatel created at 2010-08-07 05:08:39

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-07 05:08:39

Can someone prepend the ticket number to the patch commit string?


---

Comment by mhansen created at 2010-08-07 06:35:27

Changing status from needs_work to positive_review.


---

Attachment

Done.


---

Comment by mpatel created at 2010-08-09 09:49:06

Resolution: fixed
