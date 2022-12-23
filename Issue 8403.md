# Issue 8403: Steiner Tree

Issue created by migration from https://trac.sagemath.org/ticket/8403

Original creator: ncohen

Original creation time: 2010-02-28 17:57:45

Assignee: rlm

CC:  jason

Here is a patch containing the function Graph.steiner_tree.

It consists in finding in a graph, given a set S of vertices, a tree in G of minimum weight/cardinality containing the vertices from S. 

Everything is explained in the docstrings anyway :-)

Nathann


---

Comment by ncohen created at 2010-02-28 17:58:44

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-04-08 21:21:08

For an explanation of the Linear Program used to solve this problem, see the LP chapter from : http://code.google.com/p/graph-theory-algorithms-book/

Nathann


---

Comment by rlm created at 2010-06-17 21:08:24

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-06-17 21:08:24

I don't think that, as you claim, minimum spanning trees can be computed in linear time.


---

Comment by ncohen created at 2010-06-18 11:04:40

And you are right. I was thinking about spanning trees, as I usually do not care about weights, but min spanning trees require a bit longer. nlog(n) is enough , even if better can be achieved, by first sorting the edges according to their weights, then greedily building a spanning tree..


---

Comment by ncohen created at 2010-06-18 11:14:41

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-06-18 11:14:41

Here it is !

Nathann


---

Attachment

Replying to [comment:5 ncohen]:
> And you are right. I was thinking about spanning trees, as I usually do not care about weights...

I don't think spanning tree is linear: the standard method is a BFS/DFS, which is still worst case quadratic. I know this is no longer relevant here, but I want to make sure I have this right. If you do know of a linear time spanning tree algorithm, I'm curious about it.


---

Comment by ncohen created at 2010-06-18 19:02:16

That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)

Nathann


---

Comment by rlm created at 2010-06-19 00:06:22

Replying to [comment:8 ncohen]:
> That's what I call linear -- not according to the the number of vertices, but according to the size of the input : n+m :-)

Aha, thanks for clarifying. If you approve of my part2, set the ticket to positive-- all looks good to me!


---

Comment by ncohen created at 2010-06-20 17:46:59

Changing status from needs_review to positive_review.


---

Attachment

Thank you again ! :-)

Nathann


---

Comment by rlm created at 2010-06-28 18:15:40

apply before part 2


---

Attachment


---

Comment by rlm created at 2010-06-29 16:49:24

Resolution: fixed
