# Issue 1361: reimplement graph generation

Issue created by migration from https://trac.sagemath.org/ticket/1361

Original creator: rlm

Original creation time: 2007-12-02 04:39:43

Assignee: mhansen

Keywords: graphs

Changes:
 1. Redefine order to be number of edges.
 1. Start with empty graph.
 1. Augment by adding 1 edge.
 1. Cython-ize.


---

Comment by rlm created at 2007-12-02 04:41:13

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-02 04:41:13

Changing status from new to assigned.


---

Attachment


---

Comment by rlm created at 2007-12-02 07:31:48

Implementing in Cython should have little effect, since what is in Python is certainly not the bottleneck.


---

Comment by cwitty created at 2007-12-02 07:49:29

Looks good to me.  (Code looks reasonable, doctests pass in sage/graphs/.)


---

Comment by mabshoff created at 2007-12-02 08:09:11

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 08:09:11

Merged in 2.8.15.alpha2.
