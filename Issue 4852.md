# Issue 4852: graph plotting using @option and @suboption

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-22 18:37:25

Assignee: rlm

CC:  ekirkman

We really probably ought to use the very nice `@`option and `@`suboption functionality for doing plots of graphs. That would make it easier to specify edge/vertex options, for example, and to retrieve existing defaults, etc.



---

Comment by jason created at 2008-12-22 18:40:03

Changing assignee from rlm to jason.


---

Comment by jason created at 2008-12-22 18:40:03

Changing status from new to assigned.


---

Comment by rlm created at 2008-12-22 19:06:07

Emily was working on this at one point. I don't know where that code is now...


---

Comment by jason created at 2008-12-23 03:00:53

This is related a little to #2817.

Emily, were you working on using `@`option and `@`suboption to plot graphs?


---

Comment by rlm created at 2009-07-13 21:34:24

Graph plots currently use `@`option. See `sage/graphs/graph_plot.py`


...invalid?


---

Comment by kcrisman created at 2012-06-01 18:55:32

> Graph plots currently use `@`option. See `sage/graphs/graph_plot.py`

Or at least see `sage.graphs.generic_graph.py`, in particular (in Sage 5.0) [http://hg.sagemath.org/sage-main/file/9ab4ab6e12d0/sage/graphs/generic_graph.py#l13907](http://hg.sagemath.org/sage-main/file/9ab4ab6e12d0/sage/graphs/generic_graph.py#l13907)

> 
> ...invalid?

Probably it could be improved somehow, but we'd want a more specific ticket for this.  Jason, I'm recommending closing this - speak now!


---

Comment by kcrisman created at 2012-06-01 18:55:32

Changing status from new to needs_review.


---

Comment by jason created at 2012-06-01 18:58:29

+1 to closing this vague ticket that seems to be minimally satisfied.


---

Comment by kcrisman created at 2012-06-01 19:00:15

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-06-01 19:00:15

Great.


---

Comment by jdemeyer created at 2012-06-02 12:33:18

Resolution: worksforme
