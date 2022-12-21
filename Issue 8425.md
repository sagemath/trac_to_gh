# Issue 8425: BipartiteGraph add_edge allows bipartite property to be violated.

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2010-03-03 01:35:07

Assignee: rhinton

CC:  rlm jason ncohen

Keywords: BipartiteGraph, add_edge

add_edge() needs to be overridden in BipartiteGraph in order to preserve the bipartite property of the graph.

```
sage: # non-bipartite graphs are rejected by the constructor
sage: BipartiteGraph(Graph({0:[1,2], 1:[2]}))
Traceback (most recent call last)
...
TypeError: Input graph is not bipartite!

sage: # but the same graph can be constructed edge-by-edge without raising an error
sage: bg = BipartiteGraph()
sage: bg.add_vertices([0,1,2], left=[True,False,True])
sage: bg.add_edges([(0,1), (1,2)])  # good so far
sage: bg.add_edge(2,0)  # should raise exception!
```



---

Comment by rhinton created at 2010-03-03 01:36:14

One of the "core" routines to overload from #1941.


---

Comment by rhinton created at 2010-03-04 22:41:23

Patch applied after other patches in this order:

applying trac_8331-bipartite-dict-initializer.patch
applying trac_8329-bipartite-graph-copy.patch
applying trac_8421-bipartite-partition-sets.patch
applying trac_8330-bipartite-delete-vertex.patch
applying trac_8425-bipartite-add-edge.patch

Their functionality is more-or-less mutually exclusive, but they all add functions to about the same place in bipartite_graph.py.


---

Attachment

apply after #8331, #8329, and #8421


---

Comment by rhinton created at 2010-03-05 02:09:59

Changing status from new to needs_review.


---

Comment by rlm created at 2010-03-06 22:25:31

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-03-06 22:25:31

Hunk failures applying to Sage-4.3.4.alpha0 + #8329 + #8421. Please rebase.


---

Comment by rhinton created at 2010-03-24 18:26:47

Changing status from needs_work to needs_review.


---

Comment by rhinton created at 2010-03-24 18:26:47

Sorry for the delay and mixup.

REQUIRES: #8421 + #8329 + #8330

I don't know how to change the "patch" section above to reflect this....


---

Comment by ncohen created at 2010-04-01 13:20:53

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-04-01 13:20:53

Hello !!!

I have to admit I do not really like this one :-/

I seldom work on this BipartiteGraph class, and I understand you usally know which are your left and right sets, but I have to admit I would not want to see an error raised when I am building a valid bipartite graph, without taking care of the sets myself. For example :


```
sage: g = BipartiteGraph(2*graphs.GridGraph([4,4]))
sage: g.add_edge(0,30)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/usr/local/sage/devel/sage-bip/sage/graphs/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/graphs/bipartite_graph.pyc in add_edge(self, u, v, label)
    690         # check for endpoints in different partitions
    691         if self.left.issuperset((u,v)) or self.right.issuperset((u,v)):
--> 692             raise RuntimeError('Edge vertices must lie in different partitions.')
    693 
    694         # add the edge

RuntimeError: Edge vertices must lie in different partitions.
```


And to be honest, I really would like to be able to deal with Bipartite Graphs without having to specify myself in which set my vertices are... What would you think of setting a vertex to "left" if the users does not specify left=True or right=True, and modify a bit add_edge ? This way, the edge could be added immediately if the two vertices at its ends are in different sets, and if they are not the colors could be changed whenever possible to fit the graph with a new edge ?

Actually, when a graph is bipartite and split in two sets, you can add an edge in exactly two situations : 

- The colors between the endpoints are different

- The colors are the same, but the vertices belong to two different connected components

So two solutions : 

- Add an edge if the colors are different. If they are not, check that there is no path from one vertex to the other, and if it is the case reverse the coloring of one of the two components and add the edge

- Fix a partition for any connected component, and maintain them updated. 


The problem is that the first makes of add_edge a linear-time function. The second way keeps it to O(1), but we would have to update the list of connected components, even if it is not so hard. The truth is I do not know what is best for this class, and I'm eager to learn your advice on it. It is also possible to add a flag like "allow_set_modifications" if you want to keep the possibility to refuse an addition in somec ases... But anyway this should be mentionned in the docstrings :-)

Nathann


---

Comment by rhinton created at 2010-04-22 01:44:07

Thanks for helping!  Sorry for the slow response: apparently trac decided to stop sending me email notifications.

Your suggestions are good.  They would make BipartiteGraph much easier to work with.  Not that the current approach is invalid -- some people might take offense if their left/right sets started changing without permission.  Of course, we can always add a keyword flag to prevent set modification and essentially keep the current behavior.

My selfish suggestion is to allow this patch to go through because it fixes an important deficiency in BipartiteGraph.  Right now BG is broken.  This patch fixes it, although it doesn't handle the left/right sets automatically.  I would love to see an additional ticket to add this convenience.  (I'm happy to review it!)  In particular, this handling would make the left/right keywords for add_vertex optional and obviate some of the dirty tricks I played during BipartiteGraph initialization.

The docstring test shows that an exception is raised.  Would you like me to add verbiage above saying that it is an error for the two endpoints to be in the same partition?


---

Comment by ncohen created at 2010-04-22 08:07:15

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-04-22 08:07:15

> The docstring test shows that an exception is raised.  Would you like me to add verbiage above saying that it is an error for the two endpoints to be in the same partition?

Well, it is already the case, as the Exception raised is "RuntimeError: Edge vertices must lie in different partitions". Well, I can understand you would like to have a *functional* BipartiteGraph as soon as possible, so I'm giving this ticket a positive review !

The tests pass, the documentation is fine, and it clearly is a necessary fix :-)

Nathann


---

Comment by ncohen created at 2010-04-22 08:07:23

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-04-22 08:15:12

See #8744 for the previous comments :-)

Nathann


---

Comment by was created at 2010-04-29 05:38:42

Resolution: fixed
