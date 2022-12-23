# Issue 7853: block_and_cut_vertices is inconsistent when graph has one vertex

Issue created by migration from https://trac.sagemath.org/ticket/7853

Original creator: jason

Original creation time: 2010-01-06 06:06:06

Assignee: rlm

CC:  hartke rlm ncohen

Currently, block_and_cut_vertices says that the vertex in a single-vertex graph is a cut vertex:


```
sage: Graph(1).blocks_and_cut_vertices()
([0], [0])
```


According to the definition of cut vertices given in the documentation of the function, a cut vertex, when removed, increases the connected components of the graph.  Either that documentation should be changed to mention a corner case, or (preferably), the above computation should look like:


```
sage: Graph(1).blocks_and_cut_vertices()
([0], [])
```




---

Comment by ncohen created at 2010-01-06 10:24:07

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-01-06 10:24:07

Here it is ! Actually the answer [0],[0] seemed deliberate in the code, but my tests with the patch applied did not show any error coming from the fix :-)

( Apply on top of patches from #7634 )

Nathann


---

Comment by ncohen created at 2010-01-06 10:24:21

Apply on top of patches from #7634


---

Comment by rlm created at 2010-01-06 16:26:20

Changing status from needs_review to positive_review.


---

Attachment

Looks good to me.


---

Comment by rlm created at 2010-01-13 04:51:06

Resolution: fixed
