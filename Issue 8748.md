# Issue 8748: Linear Arboricity, Acyclic edge coloring

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-04-23 01:04:32

Assignee: jason, ncohen, rlm

This patch implements LP formulations of Linear Arboricity and Acyclic edge coloring

Nathann Thank you.I got it.

This ticket is the same as #8405. The latter got spam content and the spammer closed the ticket. It would be more trouble and result in confusion to reopen the ticket. So I have moved the ticket over to this one.


---

Comment by mvngu created at 2010-04-23 01:06:38

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-04-23 01:06:38

For an explanation of the Linear Program used to solve this problem, see the LP chapter from :  http://code.google.com/p/graph-theory-algorithms-book/

Nathann


---

Comment by rlm created at 2010-06-21 21:00:46

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-06-21 21:00:46

Failures:

```
sage -t -only-optional=glpk,cbc "devel/sage-main/sage/graphs/graph_coloring.py"
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0-cbc/devel/sage-main/sage/graphs/graph_coloring.py", line 749:
    sage: all([g1.has_edge(e) or g2.has_edge(e) for e in g.edges()])  # optional - GLPK, CBC
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0-cbc/devel/sage-main/sage/graphs/graph_coloring.py", line 922:
    sage: all([ any([gg.has_edge(e) for gg in colors]) for e in g.edges()])     # optional - GLPK, CBC
Expected:
    True
Got:
    False
**********************************************************************
```



---

Comment by ncohen created at 2010-06-21 21:14:08

Yet another graph constructor from networkx, with {} instead of None as labels. A g.edges(labels = False) did the trick :-)

Sorry abou that !

Nathann


---

Comment by ncohen created at 2010-06-21 21:14:08

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-06-21 21:57:09

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by rlm created at 2010-06-29 16:44:16

Resolution: fixed
