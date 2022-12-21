# Issue 7569: random_vertex and random_edge functions

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-12-01 10:15:12

Assignee: rlm

CC:  abmasse

In many algorithms we want to find a random vertex or a random edge in a graph. It is also very often required to find, given a vertex, one edge adjacent to it ( for example in depth first or breadth first search ).

This should be possible easily, and most importantly efficiently ( if possible, directly written in C ) as DFS and BFS are very slow when written in python ( same problem with Floyd Warshall for all_pairs_shortest_path and networkX's distance function )


---

Comment by ncohen created at 2010-02-23 10:25:18

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-02-23 10:25:46

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-02-23 10:29:02

Changing status from positive_review to needs_work.


---

Comment by ncohen created at 2010-02-23 10:29:09

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-03-02 03:56:59

All patches must include doctests, especially new functions.


---

Comment by rlm created at 2010-03-02 03:56:59

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-03-02 08:55:44

I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)

Nathann


---

Comment by rlm created at 2010-03-04 17:06:37

Replying to [comment:6 ncohen]:
> I agree, but I did not know how to comment a random generator.... How would you do that ? ;-)
> 
> Nathann

There are several ways, e.g.

```
sage: v = G.random_vertex()
sage: v in G
sage: G.has_vertex(v)
True
```

etc.
You can also do

```
sage: G.random_edge(labels=False)
(...,...)
sage: G.random_edge(labels=True)
(...,...,...)
```



---

Comment by ncohen created at 2010-03-04 17:23:48

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-03-04 17:23:48

Got it !

Here is the new version :-)

Nathann


---

Comment by abmasse created at 2010-03-21 21:34:36

Hello, Nathann !
I guess this patch won't be hard to review. I have a question, though. Why do you have the `**kwds` parameter ? It seems to me that there shouldn't be any parameter at all. Or if you want to keep the same parameters as for the `vertex_iterator` and `edge_iterator` functions, wouldn't it be better to use the same names (`vertices` for `vertex_iterator` for instance) ?
What do you think ? If you still prefer to keep the `**kwds` argument, then I think it would be better to indicate at least that these are passed to the `vertex_iterator` and `edge_iterator` functions.


---

Comment by ncohen created at 2010-03-22 09:51:42

Hello !! 

I added this parameter because I can not stand the fact that Graph.edges() returns triples instead of pairs, so I constantly use the labels = False argument :-)

Patch updated !

Nathann


---

Attachment


---

Comment by abmasse created at 2010-03-22 16:30:34

Review patch with formatting of code and doc -- apply on top of Nathann's patch


---

Comment by abmasse created at 2010-03-22 16:34:27

Changing status from needs_review to positive_review.


---

Attachment

I've tested this patch on sage 4.3.4. All tests passed, and the documentation generated with the `browse_sage_doc` function looks ok (we really need to include those graph files in the tree for the reference manual). I made a few changes, only consisting of formatting of code and documentation.

Positive review.


---

Comment by ncohen created at 2010-03-22 16:38:10

Thank you very much again :-)

Nathann


---

Comment by jhpalmieri created at 2010-04-15 05:59:42

Merged in 4.4.alpha0:

 - trac_7569.patch
 - trac_7569_review-abm.patch


---

Comment by jhpalmieri created at 2010-04-15 05:59:42

Resolution: fixed
