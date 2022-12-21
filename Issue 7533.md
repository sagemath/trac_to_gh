# Issue 7533: Implement distance graphs

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-11-26 07:02:45

Assignee: rlm

Keywords: distance graph

Create a new graph from an old graph by making vertices of the new graph adjacent exactly when they are a certain distance apart in the old graph.  This construction is useful in algebraic graph theory.


---

Attachment


---

Comment by rbeezer created at 2009-11-26 07:05:51

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-11-26 09:39:21

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-11-26 09:39:21

Hello !!!!

Several comments :
    * I very often meet people interested in the graph which contains an edge fo any pair of vertices at distance _at most_ d ( and not _exactly_ d as you do ). Well, the only fact that you need it means that it should be possible in Sage, but could you include in your patch something about distance "at most" d ? Actually, I was thinking of an argument d being:
        * An integer, in which case all the vertices at distance "at most" d are linked
        * A list of integers, in which case all the vertices whose distance belongs to the list are linked
      In this situation, to obtain the result you want you would need to write distance_graph([8]).

    * You are computing the distances between any pair of vertices, and computing distance(x,y) is not the best way to do so. The Floyd-Marshall algorithms does it way faster : see Graph.shortest_path_all_pairs ( you will obtain the distances between any pair of vertices, plus some information on how to build the shortest path. You are not interested in this, but it costs nothing more to compute it ! )
    * If the complexity is the same, could you replace self.vertex_iterator by just "self" ?
    * This function could also be useful in the case of DiGraphs

Short of this, the documentation/tests are excellent and this patch will definitely be used !!!

Nathann


---

Comment by rbeezer created at 2009-11-27 06:52:50

Hi Nathann,

Thanks for the excellent suggestions.  I'll get a list argument working and look at using the shortest path routine.

Someplace in the code I got the impression the iterator is faster (by about a factor of 2).

I've tested the code for digraphs, but really am only interested in undirected graphs at the moment.  With some time, I could easily generalize it later.

Rob


---

Comment by rbeezer created at 2009-11-27 09:01:40

Changing status from needs_work to needs_review.


---

Attachment

New patch addresses two of Nathann's suggestions.

1.  A list of distances, or a single distance, are now possible.  New doctests illustrate this and aslo show how to build the graph with all the distances *less than or equal* to a specified value.

2.  Using `shortest_path_all_pairs()` turns out, surprisingly, to be much slower.  It added about 37 seconds to running the tests for the file (from 80 seconds to 117 seconds).  For the odd graph with parameter 5 (on 126 vertices), the "all pair" version took about 20 seconds while the version in the current patch (which uses `.distance()`) takes a bit over 2 seconds.


---

Comment by ncohen created at 2009-11-27 12:18:29

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-11-27 12:18:29

Positive review !!! You changed the definition to have d ( integer ) represent an unique distance, and not range(distance), which is not the best for my usage, but clearly the best for Sage and for comprehension. Good idea.

I created ticket #7540 about the difference in speed, which is an oddness we must fix ...

Positive review, excellent patch !

Nathann


---

Comment by mhansen created at 2009-11-29 05:57:55

Resolution: fixed
