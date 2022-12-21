# Issue 8655: Fix graph genus (broken on multigraphs?)

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2010-04-06 19:42:13

Assignee: jason, ncohen, rlm


```
sage: G = Graph(multiedges=True)
sage: G.add_edge(0,1)
sage: G.add_edge(0,1)
sage: G.genus()
1
sage: G.to_simple().genus()
0
```


Adding parallel edges to a graph never changes the minimal genus.  I'm concerned that genus() might be entirely broken... but maybe it's just on multigraphs?  At the very least, removing parallel edges will speed things up and fix this bug.


---

Attachment

Depends on #8691


---

Comment by boothby created at 2010-05-21 21:35:19

Changing status from new to needs_review.


---

Comment by rlm created at 2010-05-25 23:55:20

Everything applies cleanly and tests pass. I'll be willing to give this the thumbs up if the author wants to walk me through the code a little at Sage Days.


---

Comment by rlm created at 2010-05-27 21:48:12

Changing assignee from jason, ncohen, rlm to rlm.


---

Comment by rlm created at 2010-05-27 21:48:12

line 220 (raise MemoryError, "Error allocating memory for graph genus a")
also 228 (...)

 --> insert comment regarding free-ing automatically via dealloc


line 231 -> probably a bitset way to do this faster


line 296 -> memcpy = better good doing thing

cdef list darts_to_verts (orbit_v?) in line 327


---

Comment by boothby created at 2010-05-27 22:48:24

ammendments to satisfy reviewer


---

Attachment

Regarding "line 231 -> probably a bitset way to do this faster", I agree, there probably is, but I'd rather not peek any further into the cgraph structure than necessary.


---

Comment by rlm created at 2010-05-27 23:03:15

Maths speeds up!


---

Comment by rlm created at 2010-05-27 23:03:15

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 22:07:50

Resolution: fixed
