# Issue 8330: BipartiteGraph needs to hook delete_vertex() and delete_vertices()

Issue created by migration from https://trac.sagemath.org/ticket/8330

Original creator: rhinton

Original creation time: 2010-02-22 21:23:20

Assignee: rhinton

CC:  rlm jason ncohen

Keywords: BipartiteGraph

BipartiteGraph needs to hook delete_vertex() and delete_vertices().


```
```


It should also hook the add_vertex() and add_edge() (and similar) calls, but not sure of the right way to do this.


---

Comment by jason created at 2010-02-23 00:12:09

When you say "hook", do you mean "define"?


---

Comment by rlm created at 2010-02-23 01:25:38

#1941 is relevant.


---

Comment by rhinton created at 2010-02-23 02:04:38

Yes, I do mean define these methods.  The proposed method definitions just call the corresponding method in Graph, then adjust the partition lists.  So it feels to me like a driver "hook" where you call the existing function but add a little extra functionality before or after.

The patch defines the needed methods including doctests that pass.


---

Comment by rhinton created at 2010-02-23 02:04:38

Changing status from new to needs_review.


---

Comment by rhinton created at 2010-02-24 17:58:45

Changing status from needs_review to needs_work.


---

Comment by rhinton created at 2010-02-24 17:58:45

I just tested graph.py for another potential change, and found that a few doctests fail due to this patch.  Specifically, the tests create BipartiteGraphs (e.g. K23), and the Graph algorithm adds a temp vertex, then deletes it later.  But the new delete_vertex() raises an exception when it can't find the temp vertex in its left or right sets.

So we may need to fix add_vertex before this delete_vertex solution will work.  Or should we do a soft-fail (print a warning?) instead of raising an exception?


---

Comment by rhinton created at 2010-03-02 02:47:27

changing the ticket to handle add and delete methods for completeness


---

Comment by rhinton created at 2010-03-03 01:28:18

Changing status from needs_work to needs_review.


---

Comment by rhinton created at 2010-03-05 02:07:36

REQUIRES #8421. Implements add/delete vertex/vertices and to_undirected to fix a failing doctest elsewhere.


---

Attachment

Hello !!!

Nice patch, applies and does its job... I fixed one or two things... If you think they are ok, you can set this ticket to "positive review" :-)

Nathann


---

Attachment

Well, it has been two weeks and I only fixed three lines, so let's say this ticket is positively reviewed ^^;

Nathann


---

Comment by ncohen created at 2010-04-15 14:25:50

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:48:34

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:48:34

Merged into 4.4.alpha0:
 - trac_8330-bipartite-delete-vertex.patch
 - trac_8330-smallfixes.patch
