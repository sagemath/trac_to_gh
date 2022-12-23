# Issue 7274: graphs: Maximum flow algorithms

Issue created by migration from https://trac.sagemath.org/ticket/7274

Original creator: tombuc

Original creation time: 2009-10-23 21:15:13

Assignee: rlm

This is work from Sage Days 16 in Barcelona.

First patch implements Edmonds-Karp and Dinic algorithm for DiGraph. Second one uses this implementation to find maximum matching in bipartite graphs.

I also include worksheet with simple usage example.

Please review. 


---

Attachment

Maximum flow algorithms


---

Attachment

Maximum matching in bipartite graphs


---

Attachment

Example usage


---

Comment by tombuc created at 2009-10-23 21:27:08

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-10-24 00:06:21

I wrote a patch at ticket #6680 including flows and (possibly weighted) matchings ( in the general case ). This patch still hasn't been reviewed, but it could be interesting to compare the performances before merging any of them :-)


---

Comment by rlm created at 2009-12-15 18:09:54

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-15 18:09:54

Patch applies cleanly and passes tests, and I'm ready to approve except for:

1. `def path_iterator(P)` This function needs a docstring. The 100% rule applies here too. Just a simple sentence saying what it does and an example or two will do.


---

Comment by ncohen created at 2009-12-16 19:44:57

As #7592 and #7593 just got reviewed, this patch can not be directly added to sage : there are now functions Graph.flow and Graph.matching available in Sage ( well, in the next version.. )

The problem with these functions is that they still depend on GLPK or CBC, two optional packages that can not be made standard are their licenses are not compatible, so it would be good to have pure Python equivalent.

Several remarks

    * In #7600 and in Graph.coloring, the user can chose which algorithm he would like to use to solve the problem. Maybe the best way is to copy this behaviour in the case of flows and matching to have the two algorithms available.
    * It could be very useful to know how these algorithms compare in terms of performances. This will be much easier to test when flow and matching will be natively in Sage
    * #7634 may not be ready, but time could come soon : with this update the efficiency of the shortest_path method will be improved, and the speed of this implementation too.
    * Somwhere in the code, I saw a call to 

```
path = R.shortest_path(source, sink,by_weight=False, bidirectional=False)
```

      I wondered why you chosed not to use the bidirectional version of the algorithm, as it is expected to be faster.. :-)

Thank you for your work !!!


---

Comment by jason created at 2009-12-18 17:04:29

Apparently #3930 should be closed when this is merged.


---

Comment by ncohen created at 2010-10-09 08:29:30

We have a Python version for max flow through #9350 ... So as this ticket has been here for 10 months now..

Nathann


---

Comment by mvngu created at 2010-10-09 08:35:20

Close as duplicate of #9350.


---

Comment by mvngu created at 2010-10-09 08:35:20

Resolution: duplicate
