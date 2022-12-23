# Issue 8421: Change BipartiteGraph .left and .right to sets

Issue created by migration from https://trac.sagemath.org/ticket/8421

Original creator: rhinton

Original creation time: 2010-03-02 16:05:50

Assignee: rlm

CC:  rlm jason ncohen

Keywords: BipartiteGraph, partitions, sets

The documentation describes the 'left' and 'right' attributes of BipartiteGrpah as sets.  And deleting vertices is much more efficient if they are.  But they are currently stored as lists.

```
sage: bg = BipartiteGraph(graphs.CycleGraph(4))
sage: bg.left
[0, 2]
```


Of course, it's easy to change from one to the other.  But we will get better performance from sets.



---

Comment by rhinton created at 2010-03-02 16:28:28

Changing assignee from rlm to rhinton.


---

Comment by rhinton created at 2010-03-02 16:49:52

Changing status from new to needs_review.


---

Comment by rhinton created at 2010-03-02 16:49:52

Patch implements change.  It sits on my MQ stack on top of #8331 and #8329, but I don't think either of these are required.


---

Attachment

updated commit message


---

Comment by rlm created at 2010-03-06 22:18:59

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:46:47

Merged "trac_8421-bipartite-partition-sets.patch" into 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-15 23:46:47

Resolution: fixed
