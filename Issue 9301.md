# Issue 9301: Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents

Issue created by migration from Trac.

Original creator: comick

Original creation time: 2010-06-21 23:11:15

Assignee: jason, mvngu, ncohen, rlm

CC:  nathann.cohen@gmail.com

Keywords: graph,label

Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents. Discussion and example here: http://groups.google.com/group/sage-devel/browse_thread/thread/310fba4f1c119e63#



---

Attachment

Patch


---

Comment by comick created at 2010-06-21 23:12:33

Changing status from new to needs_review.


---

Comment by rlm created at 2010-07-17 14:07:41

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-07-17 14:07:41

Since this is a bug fix, you need to include a doctest which illustrates the bug you are fixing.


---

Comment by comick created at 2010-08-21 22:59:28

Doctest for bad behavior.


---

Comment by comick created at 2010-08-21 23:00:51

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

Replaces previous patch - added trac # to commit message.


---

Comment by rlm created at 2010-08-31 17:56:54

There is a fly in the ointment:

During one of the last NetworkX upgrades, many common Sage graph constructors were modified to give empty dictionaries as labels instead of None. I have been intending to fix many of Sage's graph generators not to depend on NetworkX (since simply constructing a CGraph would be much quicker), and revert the edge situation back to having labels equal to `None`. But until that happens, this patch causes several failures:


```
sage -t -long "devel/sage-main/sage/graphs/generic_graph.py"
sage -t -long "devel/sage-main/sage/graphs/base/sparse_graph.pyx"
sage -t -long "devel/sage-main/sage/graphs/graph.py"
```


Also, I've changed the "Report Upstream" since here we *are* the upstream.


---

Comment by rlm created at 2010-08-31 17:56:54

Changing status from needs_review to needs_work.


---

Comment by dcoudert created at 2021-10-19 12:55:50

It seems that this issue has been fixed long time ago. So I propose to close this ticket.


---

Comment by dcoudert created at 2021-10-19 12:55:50

Changing status from needs_work to positive_review.


---

Comment by mkoeppe created at 2021-10-25 15:39:21

Resolution: invalid
