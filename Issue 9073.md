# Issue 9073: Handle multigraphs better in planarity

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2010-05-28 03:57:01

Assignee: AlexGhitza

CC:  rlm


```
sage: G = Graph({0:[1,1]}, multiedges=True)
sage: G.is_planar()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/mnt/usb1/scratch/boothby/sage-4.4.2/<ipython console> in <module>()

/mnt/usb1/scratch/boothby/sage-4.4.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in is_planar(self, on_embedding, kuratowski, set_embedding, set_pos)
   2217             from sage.graphs.planarity import is_planar
   2218             G = self.to_undirected()
-> 2219             planar = is_planar(G,kuratowski=kuratowski,set_pos=set_pos,set_embedding=set_embedding)
   2220             if kuratowski:
   2221                 bool_result = planar[0]

/mnt/usb1/scratch/boothby/sage-4.4.2/local/lib/python2.6/site-packages/sage/graphs/planarity.so in sage.graphs.planarity.is_planar (sage/graphs/planarity.c:1327)()

KeyError: -1
sage: G = Graph({0:[1,1,1,1,1,1,1,1,1,1,1,1,1]}, multiedges=True)
sage: G.is_planar()
False
```



---

Comment by boothby created at 2010-05-28 04:00:59

Changing priority from major to minor.


---

Comment by boothby created at 2010-05-28 04:00:59

Changing component from algebra to graph theory.


---

Comment by boothby created at 2010-05-28 04:00:59

Changing assignee from AlexGhitza to jason, ncohen, rlm.


---

Comment by rlm created at 2010-06-15 19:43:11

Changing status from new to needs_review.


---

Comment by boothby created at 2010-06-17 19:49:26

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2010-06-17 19:49:26

works!


---

Comment by boothby created at 2010-06-17 19:52:39

Changing status from positive_review to needs_work.


---

Comment by boothby created at 2010-06-17 19:52:39

oops, jumped the gun.  we need to check for loops, too.


```
sage: G = Graph(loops=True)
sage: G.add_edge(0,0)
sage: G.add_edge(1,0)
sage: G.is_planar(set_embedding=True)
sage: G.get_embedding()
Traceback (click to the left of this block for traceback)
...
Exception: Looped graph on 2 vertices has been modified and the
embedding is no longer valid.
```



---

Comment by boothby created at 2010-06-17 20:00:44

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by boothby created at 2010-06-17 20:01:47

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:48:23

Resolution: fixed
