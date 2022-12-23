# Issue 7733: Graph(g) and DiGraph(g) do not keep the embedding !

Issue created by migration from https://trac.sagemath.org/ticket/7733

Original creator: ncohen

Original creation time: 2009-12-18 08:25:18

Assignee: rlm

Just try ::


```
sage: g = graphs.PetersenGraph()
sage: g.show()
sage: Graph(g).show()
sage: DiGraph(g).show()
```


The positions are not kept.... Why isn't Graph(g) equivalent to copy(g) ?

Nathann


---

Comment by ncohen created at 2010-02-22 18:17:04

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-22 18:17:04

Two lines !

Nathann


---

Comment by rlm created at 2010-03-02 03:55:28

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-03-02 03:55:28

You must provide doctests in both directions.


---

Comment by ncohen created at 2010-03-02 13:17:45

Done !


---

Comment by ncohen created at 2010-03-02 13:17:45

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by rlm created at 2010-03-06 22:20:42

There is one case which is untested, going from a `Graph` to a `DiGraph`.


---

Comment by rlm created at 2010-03-06 22:20:42

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-03-07 17:04:12

Changing status from needs_work to needs_info.


---

Comment by ncohen created at 2010-03-07 17:04:12

What do you think of line 300 ?


```
sage: g = DiGraph(graphs.PetersenGraph()) 
```


Would you like to see an independent test for it ?

Nathann


---

Comment by rlm created at 2010-03-07 17:57:29

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2010-03-07 17:57:29

Sorry, I must have missed that!


---

Comment by rlm created at 2010-03-07 18:02:21

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-03-07 18:04:56

Thanks :-)


---

Comment by mhansen created at 2010-03-08 20:57:27

Resolution: fixed
