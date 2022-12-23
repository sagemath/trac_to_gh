# Issue 8331: BipartiteGraph constructor does not create partitions for dict inputs

Issue created by migration from https://trac.sagemath.org/ticket/8331

Original creator: rhinton

Original creation time: 2010-02-23 01:04:44

Assignee: rlm

CC:  jason rlm

Keywords: BipartiteGraph

The BipartiteGraph constructor does not create partitions for dict inputs.


```
sage: t1 = BipartiteGraph({'a': ['b'], 'b':['c']})
sage: t1.left
...
AttributeError: 'BipartiteGraph' object has no attribute 'left'
```


The problem comes in the constructor in the "other inputs" case.  A Graph object is created, but not all the control paths find a bipartition.



---

Comment by rlm created at 2010-02-23 01:26:36

another duplicate of part of #1941.


---

Attachment

The patch trac_8331-... fixes the bug, adds a doctest, and slightly improves the ReST markup for the constructor.  (I am certainly not an expert.)


---

Comment by rhinton created at 2010-02-23 01:29:33

Changing status from new to needs_review.


---

Comment by rhinton created at 2010-02-23 01:32:16

Changing assignee from rlm to rhinton.


---

Comment by rlm created at 2010-03-02 03:09:36

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-03-02 03:09:36

Works for me :-)


---

Comment by mvngu created at 2010-03-03 14:25:55

Ryan: remember to put a sensible commit message in your patch, together with the ticket number.


---

Comment by mvngu created at 2010-03-03 14:25:55

Resolution: fixed
