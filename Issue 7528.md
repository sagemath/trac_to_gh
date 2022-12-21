# Issue 7528: Orientation of a graph with bounded out-degree

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-11-25 09:56:20

Assignee: rlm

Given an undirected graph and an integer k, it is possible to find through the flow algorithm an orientation of it such that any vertex has an out-degree of at most k ( or say that this is impossible )


---

Comment by ncohen created at 2009-12-05 14:16:03

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 17:32:29

Changing status from needs_review to needs_info.


---

Comment by rlm created at 2009-12-15 17:32:29

I'm ready to give this a positive review, except there is a conflict:


```
Given a complete bipartite graph `K_{n,m}`, the minimum  
outdegree of an orientation is  
`\left\lceil \frac {nm} {n+m}\right\rceil`:: 

sage: g = graphs.CompleteBipartiteGraph(3,4) 
sage: o = g.minimum_outdegree_orientation() # optional - requires GLPK or CBC 
sage: max(o.out_degree()) == ceil((4*3)/(3+4)) # optional - requires GLPK or CBC 
True
```


Should "the minimum outdegree" be "the smallest possible maximum outdegree", or something similar?


---

Comment by ncohen created at 2009-12-16 01:09:24

Changing status from needs_info to needs_review.


---

Attachment

Indeed ! ( corrected )


---

Comment by rlm created at 2009-12-16 03:14:06

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 21:32:22

Resolution: fixed
