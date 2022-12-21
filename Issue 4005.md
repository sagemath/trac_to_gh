# Issue 4005: [with patch, needs review] sage-coverage screws up with lambda functions as default arguments

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-30 18:53:14

Assignee: mabshoff




---

Comment by rlm created at 2008-08-30 18:54:21

Apply to scripts repo.


---

Attachment

This patch is motivated by

```
    def min_spanning_tree(self, weight_function=lambda e: 1,
                          algorithm='Kruskal',
                          starting_vertex=None ):
```

from sage/graphs/graph.py.

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 23:57:59

rlm points out that this is not perfect, but it fixes this one specific issue. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 23:59:39

Resolution: fixed


---

Comment by mabshoff created at 2008-08-30 23:59:39

Merged in Sage 3.1.2.alpha3
