# Issue 9375: more documentation & doctests for BalancedTree, BarbellGraph, BubbleSortGraph, BullGraph, ChvatalGraph

Issue created by migration from https://trac.sagemath.org/ticket/9375

Original creator: mvngu

Original creation time: 2010-06-29 17:33:48

Assignee: jason, ncohen, rlm

As the subject says. 

*Prerequisite:* #9373


---

Attachment


---

Comment by mvngu created at 2010-06-29 17:40:19

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-07-16 03:03:14

Excellent ! You can set this one to "positive review" immediately after #9375 :-)

One unimportant detail, though... You used subgraph_search in your doctests, the follwing way :


```
sage: s_K = g.subgraph_search(K_n1, induced=True) 
sage: s_P = g.subgraph_search(P_n2, induced=True) 
sage: K_n1.is_isomorphic(s_K) 
```


Well, subgraph_search should of course *always* return subgraphs isomorphic to S_k. Actually, the order of the vertices should even be the same, but when it finds nothing, it returns a None, which is_isomorphic may not like... It's not really a problem in this case, as this would report a doctest failure anyway :-)

Nathann


---

Comment by mvngu created at 2010-07-16 05:28:34

Replying to [comment:2 ncohen]:
> You can set this one to "positive review" immediately after #9375 :-)

I don't understand what you mean. Care to elaborate on this point?


---

Comment by ncohen created at 2010-07-16 05:36:14

Sorry, I meant #9373 :-)

It was just to avoid having a ticket A depending on B such that a is positively reviewed while B is not.

Nathann


---

Comment by ncohen created at 2010-07-16 05:36:14

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 02:48:42

Resolution: fixed
