# Issue 9485: Fix strongly_connected_components_digraph to actually do something

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-07-12 18:55:21

Assignee: jason, ncohen, rlm

CC:  sage-combinat rlm

Keywords: strongly connected components

Graphs produced with strongly_connected_components_digraph had no
edges in them due to a typo in the code:


```
    sage: g = DiGraph({0:[1,2,3],1:[2],2:[1,3]})
    sage: scc_digraph = g.strongly_connected_components_digraph()
    sage: scc_digraph.vertices()
    [{0}, {3}, {1, 2}]
    sage: scc_digraph.edges()
    []
```


After this patch, the result is more likely to be correct:


```
    [({0}, {3}, None), ({0}, {1, 2}, None), ({1, 2}, {3}, None)]
```




---

Attachment


---

Comment by nthiery created at 2010-07-12 19:03:34

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-07-12 23:11:14

Oops... Some very, very bad typo ... Thank youuuuuuu ! :-)

Nathann


---

Comment by ncohen created at 2010-07-12 23:11:14

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-07-13 13:41:54

Thanks for the instantaneous review!

And thanks as well for the original code. It was still quicker for me to fix it than to have to implement it myself :-)


---

Comment by mpatel created at 2010-07-21 02:49:04

Resolution: fixed
