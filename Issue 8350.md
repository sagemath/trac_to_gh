# Issue 8350: BipartiteGraph override add_vertex() and add_vertices()

Issue created by migration from https://trac.sagemath.org/ticket/8350

Original creator: rhinton

Original creation time: 2010-02-24 18:04:42

Assignee: rhinton

CC:  rlm jason

Keywords: BipartiteGraph

BipartiteGraph needs to override add_vertex() and add_vertices() to properly partition the vertices.


```
sage: bg = BipartiteGraph()
sage: bg.add_vertex('a')  # this vertex should go left or right
sage: (bg.left, bg.right)  # one of these should contain vertex 'a'
([], [])
```





---

Comment by rhinton created at 2010-02-24 18:13:32

How about this solution:

1(a).  To properly add a vertex to a BipartiteGraph object, specify keyword left or right as True.

```
sage: bg = BipartiteGraph()
sage: bg.add_vertex('a', left=True)  # new syntax
sage: bg.left
['a']
```


1(b).  add_vertices() can use a list for left or right (default right to None).  We could also allow left/right to be a single boolean and apply that to every element in the list.

```
sage: bg = BipartiteGraph()
sage: bg.add_vertices(['a', 'b', 'c'], left=[True, False, True])
```


2.  With no specific instruction, add_vertex will convert the current BipartiteGraph back to a Graph.  (Is this allowed/possible?)

```
sage: g = BipartiteGraph()
sage: g.add_vertex('a')  # no left/right specified, so revert to a Graph
sage: g
Graph on 1 vertex
sage: type(g)
<class 'sage.graphs.graph.Graph'>
```



---

Comment by rhinton created at 2010-02-24 18:15:08

Forgot to add pointer to mega-ticket #1941.


---

Comment by rhinton created at 2010-02-26 15:50:17

I'm not sure part (2) above is good.  For example, someone takes their BipartiteGraph `bg`, calls `graph.is_circular_planar()` (this is one of the currently failing doctests) and gets back a !Graph with exactly the same vertex and edge sets -- but no longer a BipartiteGraph.

The obvious alternative is to raise an exception when given insufficient information.  This means any !Graph algorithms -- like the one in `is_circular_planar` may fail when applied to BipartiteGraphs.  So the !Graph class will be gradually littered with tests of the object's class like it is now for `self._directed`.

At what point is it better to subsume BipartiteGraph as an attribute of !Graph -- like `._directed`?  Or should BipartiteGraph not inherit from !Graph at all to avoid this problem?


---

Comment by jason created at 2010-02-26 16:46:22

rhinton: you bring up a very good point about the organization of the graph classes.

The main point behind the bipartite graph class is that it is represented more efficiently than the normal graphs are, right?  That's a storage layer question, which seems like it should be a lower-level thing than the algorithm layer.  Maybe in the long run, it would be better to create a backend for bipartite graphs (like the cgraph backend, or the networkx backend).

Since algorithms should only call functions that are in the public interface of the backend, algorithms should just work.  We might have to augment the public interface between backends and the graph theory code to handle the extra arguments (like in add_vertex) for different backends, though.


---

Comment by rhinton created at 2010-02-26 17:19:17

jason: thanks for the reply, see also my sage-devel post that I was finishing as you posted here. :-)

Replying to [comment:4 jason]:
> ...snip...
> The main point behind the bipartite graph class is that it is represented more efficiently than the normal graphs are, right?  That's a storage layer question, which seems like it should be a lower-level thing than the algorithm layer.  Maybe in the long run, it would be better to create a backend for bipartite graphs (like the cgraph backend, or the networkx backend).

No, it's not an issue of efficiency.  BipartiteGraph subclasses from Graph and so inherits most of its functionality that way.  *Additionally*, the .left and .right attributes indicate the vertex partition.  Most of the problems come from adding vertices without specifying a partition (e.g. GenericGraph.is_circular_planar()), removing vertices without updating the partition (old delete_vertex, see #8330), or assuming everything is either a Graph or DiGraph (e.g. GenericGraph.union()).

> Since algorithms should only call functions that are in the public interface of the backend, algorithms should just work.  We might have to augment the public interface between backends and the graph theory code to handle the extra arguments (like in add_vertex) for different backends, though.

Yes, to a point.  Since all Python methods are "virtual", overriding a few methods like delete_vertex and add_vertex will work for many cases.  You're right, though, some of the Graph and GenericGraph code will need to be aware of the BipartiteGraph case.  Or I gave some other options in the sage-devel post.  :-)

Thanks!  -Ryan


---

Comment by rhinton created at 2010-03-02 02:56:17

Resolution: duplicate


---

Comment by rhinton created at 2010-03-02 02:56:17

merged with #8330
