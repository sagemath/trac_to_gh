# Issue 8031: make graph_editor also available as a *method* on graphs

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-21 20:05:00

Assignee: rlm

CC:  chapoton

This is nice:


```
g = graphs.CompleteGraph(5)
graph_editor(g)
```


but this would be even better:

```
g = graphs.CompleteGraph(5)
g.edit()
```


It could also fit into a framework where we have "edit" methods for all kinds of objects in Sage, including matrices, elliptic curves, etc.,.   These could be implemented using `@`interact in many cases. 


---

Comment by jdemeyer created at 2014-10-16 08:32:24

Changing component from graph theory to notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by dimpase created at 2020-08-25 09:36:34

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-09-30 09:19:03

Changing keywords from "" to "graph_editor".


---

Comment by chapoton created at 2021-01-01 14:23:25

Resolution: invalid
