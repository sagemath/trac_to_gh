# Issue 9581: edge_incident bug in generic_graph.py

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-07-23 07:13:18

Assignee: vdelecroix

CC:  ncohen rmiller

Keywords: graph

Currently, the edge_incident method of generic graph calls edge_boundary which first take a lot of time and secondly does not work


```
sage: G = Graph(loops=True)
sage: G.add_edge(0,0)
sage: G.edges()
[(0, 0, None)]
sage: list(G.edge_iterator(0))
[(0, 0, None)]
sage: G.edges_incident(0)
[]
```


The ticket also aims to reduce multiple calls (edge_boundary does not call directly vertex_iterator as it should).


---

Comment by ncohen created at 2010-07-23 10:11:50

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-07-23 10:11:50

Excellent ! Thank youuuuuuuuuuuuuu !!

Your patch is very nice, applies fine and everything.. I would just like to append a short line, because of a missing "if". If you agree with this, let's say this ticket is positively reviewed ! :-)

Nathann


---

Attachment

Nathan, Why did you put this ticket as needs_review? It seems to be important to be a lot more explicit in the definition of each function of generic_graph and implement all the cases in examples... perhaps it is the matter of another ticket...


---

Comment by ncohen created at 2010-07-24 02:39:27

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-07-24 02:39:27

Hello ! Well, if you think it needs more documenation or tests, this ticket certainly is the one that should contain it...  I thought the behaviour of these functions did not change that much, only "internal modifications", so... But I'm sorry for this, all you just said is better done here ! :-)


---

Comment by vdelecroix created at 2010-10-10 10:20:07

apply only this patch which takes care of Nathan remark


---

Attachment


---

Comment by vdelecroix created at 2010-10-10 10:20:24

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-10-10 17:54:54

Hello !!! I can not apply this patch on 4.6.alpha3, looks like it needs to be rebased `^^;`

Nathann


---

Comment by ncohen created at 2010-10-10 17:54:54

Changing status from needs_review to needs_work.


---

Attachment

rebased version (apply only this one)


---

Comment by vdelecroix created at 2010-10-11 08:02:12

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-10-11 12:27:05

Positive review to this rebased version `:-)`

Nathann


---

Comment by ncohen created at 2010-10-11 12:27:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:07:22

Resolution: fixed
