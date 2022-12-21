# Issue 6552: bug in depth-first searching

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-07-18 10:28:04

Assignee: rlm

CC:  rlm

Here is a bug in the depth-first searching of a graph:


```

sage: D = DiGraph( { 0: [1,2,3], 1: [4,5], 2: [5], 3: [6], 5: [7], 6: [7], 7: [0]})
sage: list(D.depth_first_search(0, ignore_direction=True))                         
[0, 7, 6, 5, 3, 2, 1, 4]
```


It should be `[0, 7, 6, 3, 5, 2, 1, 4]`.




---

Comment by jason created at 2009-07-18 10:48:19

I also added a bunch of features to the graph traversal functions and put in a lot more doctests.


---

Comment by rlm created at 2009-07-18 18:15:35

I say you remove the

```
#        for v,d in queue: 
#            seen.add(v) 
```

in `depth_first_search` and everything looks good!


---

Attachment


---

Comment by jason created at 2009-07-18 19:16:39

Good catch!  I deleted those two lines and posted an updated patch.  Thanks for reviewing this so fast!


---

Comment by mvngu created at 2009-07-20 17:24:05

Resolution: fixed


---

Comment by mvngu created at 2009-07-20 17:37:25

This will have to wait for Sage 4.1.1.alpha1. Apparently, I accidentally closed this as being merged in 4.1.1.alpha0.


---

Comment by mvngu created at 2009-07-20 17:37:25

Resolution changed from fixed to 


---

Comment by mvngu created at 2009-07-20 17:37:25

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-07-23 03:37:20

Resolution: fixed
