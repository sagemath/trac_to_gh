# Issue 7734: edge_coloring ( and possibly vertex_coloring ) loop forever when GLPK is not installed

Issue created by migration from https://trac.sagemath.org/ticket/7734

Original creator: ncohen

Original creation time: 2009-12-18 08:45:30

Assignee: rlm

CC:  rlm

As the title says... :-)


---

Attachment


---

Comment by ncohen created at 2009-12-18 09:03:05

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-18 21:23:55

1. There should always be an example of the bug you are fixing in the patch, always always always. We need a mug shot, so the bug doesn't show its face again :) I added this, as well as several other tests, which have exposed other corner case bugs, such as:

```
sage: g = Graph(20)
sage: vertex_coloring(g, hex_colors=True)
{'#ff0000': 0}
```

I've fixed these.

2. It seems to take some time to add constraints to the problem, which is pointless if no solver is installed. Can you add a patch that runs a trivial test before setting up the problem, to see if it is installed?


---

Comment by rlm created at 2009-12-18 21:23:55

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by ncohen created at 2009-12-19 08:24:53

Thank you for your help !!!

Concerning your second point : do you have an example for which it takes some time ? I would also like to try to improve it a bit :-)


---

Comment by rlm created at 2009-12-19 08:39:53

Replying to [comment:5 ncohen]:
> Thank you for your help !!!
> 
> do you have an example for which it takes some time ? I would also like to try to improve it a bit :-)
> 


```
sage: from sage.graphs.graph_coloring import vertex_coloring
sage: g = graphs.CirculantGraph(120, [2,3,5,7])
sage: vertex_coloring(g)
```

It takes longer to set up the constraint than to solve the problem, on my laptop.


---

Comment by ncohen created at 2009-12-19 08:49:40

I just created #7740 to deal with the problem of speed. What would you advise for the detection of the solver ? At the moment, only the "solve" command requires an optional package to be installed, do you think it would be worth changing this and make the whole class depend on GLPK or CBC ?

Nathann


---

Comment by mhansen created at 2009-12-19 20:13:01

Resolution: fixed
