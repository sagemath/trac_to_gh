# Issue 8350: BipartiteGraph override add_vertex() and add_vertices()

archive/issues_008350.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @rlmill @jasongrout\n\nKeywords: BipartiteGraph\n\nBipartiteGraph needs to override add_vertex() and add_vertices() to properly partition the vertices.\n\n\n```\nsage: bg = BipartiteGraph()\nsage: bg.add_vertex('a')  # this vertex should go left or right\nsage: (bg.left, bg.right)  # one of these should contain vertex 'a'\n([], [])\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8350\n\n",
    "created_at": "2010-02-24T18:04:42Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "BipartiteGraph override add_vertex() and add_vertices()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8350",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rhinton

CC:  @rlmill @jasongrout

Keywords: BipartiteGraph

BipartiteGraph needs to override add_vertex() and add_vertices() to properly partition the vertices.


```
sage: bg = BipartiteGraph()
sage: bg.add_vertex('a')  # this vertex should go left or right
sage: (bg.left, bg.right)  # one of these should contain vertex 'a'
([], [])
```




Issue created by migration from https://trac.sagemath.org/ticket/8350





---

archive/issue_comments_074444.json:
```json
{
    "body": "How about this solution:\n\n1(a).  To properly add a vertex to a BipartiteGraph object, specify keyword left or right as True.\n\n```\nsage: bg = BipartiteGraph()\nsage: bg.add_vertex('a', left=True)  # new syntax\nsage: bg.left\n['a']\n```\n\n\n1(b).  add_vertices() can use a list for left or right (default right to None).  We could also allow left/right to be a single boolean and apply that to every element in the list.\n\n```\nsage: bg = BipartiteGraph()\nsage: bg.add_vertices(['a', 'b', 'c'], left=[True, False, True])\n```\n\n\n2.  With no specific instruction, add_vertex will convert the current BipartiteGraph back to a Graph.  (Is this allowed/possible?)\n\n```\nsage: g = BipartiteGraph()\nsage: g.add_vertex('a')  # no left/right specified, so revert to a Graph\nsage: g\nGraph on 1 vertex\nsage: type(g)\n<class 'sage.graphs.graph.Graph'>\n```\n",
    "created_at": "2010-02-24T18:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74444",
    "user": "https://github.com/rhinton"
}
```

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

archive/issue_comments_074445.json:
```json
{
    "body": "Forgot to add pointer to mega-ticket #1941.",
    "created_at": "2010-02-24T18:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74445",
    "user": "https://github.com/rhinton"
}
```

Forgot to add pointer to mega-ticket #1941.



---

archive/issue_comments_074446.json:
```json
{
    "body": "I'm not sure part (2) above is good.  For example, someone takes their BipartiteGraph `bg`, calls `graph.is_circular_planar()` (this is one of the currently failing doctests) and gets back a !Graph with exactly the same vertex and edge sets -- but no longer a BipartiteGraph.\n\nThe obvious alternative is to raise an exception when given insufficient information.  This means any !Graph algorithms -- like the one in `is_circular_planar` may fail when applied to BipartiteGraphs.  So the !Graph class will be gradually littered with tests of the object's class like it is now for `self._directed`.\n\nAt what point is it better to subsume BipartiteGraph as an attribute of !Graph -- like `._directed`?  Or should BipartiteGraph not inherit from !Graph at all to avoid this problem?",
    "created_at": "2010-02-26T15:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74446",
    "user": "https://github.com/rhinton"
}
```

I'm not sure part (2) above is good.  For example, someone takes their BipartiteGraph `bg`, calls `graph.is_circular_planar()` (this is one of the currently failing doctests) and gets back a !Graph with exactly the same vertex and edge sets -- but no longer a BipartiteGraph.

The obvious alternative is to raise an exception when given insufficient information.  This means any !Graph algorithms -- like the one in `is_circular_planar` may fail when applied to BipartiteGraphs.  So the !Graph class will be gradually littered with tests of the object's class like it is now for `self._directed`.

At what point is it better to subsume BipartiteGraph as an attribute of !Graph -- like `._directed`?  Or should BipartiteGraph not inherit from !Graph at all to avoid this problem?



---

archive/issue_comments_074447.json:
```json
{
    "body": "rhinton: you bring up a very good point about the organization of the graph classes.\n\nThe main point behind the bipartite graph class is that it is represented more efficiently than the normal graphs are, right?  That's a storage layer question, which seems like it should be a lower-level thing than the algorithm layer.  Maybe in the long run, it would be better to create a backend for bipartite graphs (like the cgraph backend, or the networkx backend).\n\nSince algorithms should only call functions that are in the public interface of the backend, algorithms should just work.  We might have to augment the public interface between backends and the graph theory code to handle the extra arguments (like in add_vertex) for different backends, though.",
    "created_at": "2010-02-26T16:46:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74447",
    "user": "https://github.com/jasongrout"
}
```

rhinton: you bring up a very good point about the organization of the graph classes.

The main point behind the bipartite graph class is that it is represented more efficiently than the normal graphs are, right?  That's a storage layer question, which seems like it should be a lower-level thing than the algorithm layer.  Maybe in the long run, it would be better to create a backend for bipartite graphs (like the cgraph backend, or the networkx backend).

Since algorithms should only call functions that are in the public interface of the backend, algorithms should just work.  We might have to augment the public interface between backends and the graph theory code to handle the extra arguments (like in add_vertex) for different backends, though.



---

archive/issue_comments_074448.json:
```json
{
    "body": "jason: thanks for the reply, see also my sage-devel post that I was finishing as you posted here. :-)\n\nReplying to [comment:4 jason]:\n> ...snip...\n> The main point behind the bipartite graph class is that it is represented more efficiently than the normal graphs are, right?  That's a storage layer question, which seems like it should be a lower-level thing than the algorithm layer.  Maybe in the long run, it would be better to create a backend for bipartite graphs (like the cgraph backend, or the networkx backend).\n\nNo, it's not an issue of efficiency.  BipartiteGraph subclasses from Graph and so inherits most of its functionality that way.  *Additionally*, the .left and .right attributes indicate the vertex partition.  Most of the problems come from adding vertices without specifying a partition (e.g. GenericGraph.is_circular_planar()), removing vertices without updating the partition (old delete_vertex, see #8330), or assuming everything is either a Graph or DiGraph (e.g. GenericGraph.union()).\n\n> Since algorithms should only call functions that are in the public interface of the backend, algorithms should just work.  We might have to augment the public interface between backends and the graph theory code to handle the extra arguments (like in add_vertex) for different backends, though.\n\nYes, to a point.  Since all Python methods are \"virtual\", overriding a few methods like delete_vertex and add_vertex will work for many cases.  You're right, though, some of the Graph and GenericGraph code will need to be aware of the BipartiteGraph case.  Or I gave some other options in the sage-devel post.  :-)\n\nThanks!  -Ryan",
    "created_at": "2010-02-26T17:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74448",
    "user": "https://github.com/rhinton"
}
```

jason: thanks for the reply, see also my sage-devel post that I was finishing as you posted here. :-)

Replying to [comment:4 jason]:
> ...snip...
> The main point behind the bipartite graph class is that it is represented more efficiently than the normal graphs are, right?  That's a storage layer question, which seems like it should be a lower-level thing than the algorithm layer.  Maybe in the long run, it would be better to create a backend for bipartite graphs (like the cgraph backend, or the networkx backend).

No, it's not an issue of efficiency.  BipartiteGraph subclasses from Graph and so inherits most of its functionality that way.  *Additionally*, the .left and .right attributes indicate the vertex partition.  Most of the problems come from adding vertices without specifying a partition (e.g. GenericGraph.is_circular_planar()), removing vertices without updating the partition (old delete_vertex, see #8330), or assuming everything is either a Graph or DiGraph (e.g. GenericGraph.union()).

> Since algorithms should only call functions that are in the public interface of the backend, algorithms should just work.  We might have to augment the public interface between backends and the graph theory code to handle the extra arguments (like in add_vertex) for different backends, though.

Yes, to a point.  Since all Python methods are "virtual", overriding a few methods like delete_vertex and add_vertex will work for many cases.  You're right, though, some of the Graph and GenericGraph code will need to be aware of the BipartiteGraph case.  Or I gave some other options in the sage-devel post.  :-)

Thanks!  -Ryan



---

archive/issue_comments_074449.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-03-02T02:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74449",
    "user": "https://github.com/rhinton"
}
```

Resolution: duplicate



---

archive/issue_comments_074450.json:
```json
{
    "body": "merged with #8330",
    "created_at": "2010-03-02T02:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8350#issuecomment-74450",
    "user": "https://github.com/rhinton"
}
```

merged with #8330



---

archive/issue_events_008540.json:
```json
{
    "actor": "@rhinton",
    "created_at": "2010-03-02T02:56:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8350",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8350#event-8540"
}
```
