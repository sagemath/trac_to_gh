# Issue 1941: Finish bipartite graph implementation

Issue created by migration from https://trac.sagemath.org/ticket/1941

Original creator: rlm

Original creation time: 2008-01-26 20:11:04

Assignee: rlm

CC:  brunellus @maxale tscrim

Systematically go through the functions of graph and generic_graph and see which ones, such as add_vertex, need to be overridden in the bipartite graph class so that everything makes sense. Right now, you can add an edge so that the bipartite graph is no longer bipartite.


---

Comment by rlm created at 2008-01-27 18:55:00


```
 1. add to __cmp__ to distinguish Bipartite from other graphs
 2. loops - this should always be false for bipartite, right? (other functions with "loops" in the name)
 3. density - should this reflect "bipartite density"?
 4. add_vertex - to which side?
 5. add_vertices - what to do with this?
 6. clear - left & right too?
 7. add left_vertices and right_vertices?
 8. complement?
 9. copy
10. add_edge(s)
11. adjacency_matrix - should this order the vertices a certain way?
12. add_cycle
13. add_path
14. add a function "bipartite_subgraph" to preserve class?
15. bipartite_color, bipartite_sets, is_bipartite
```



---

Comment by rlm created at 2008-03-19 15:12:38

Also, the automorphism group/canonical label functions need to be called with the correct partitions.


---

Comment by rlm created at 2010-02-23 01:24:39

see #8329


---

Comment by rlm created at 2010-02-23 01:25:50

see also #8330


---

Comment by rlm created at 2010-02-23 01:27:11

#8331 is also relevant.


---

Comment by rhinton created at 2010-02-24 18:15:40

And another #8350.


---

Comment by rhinton created at 2010-03-04 22:32:12

Also #8425.


---

Comment by dcoudert created at 2022-01-31 10:31:52

Changing type from defect to task.


---

Comment by dcoudert created at 2022-01-31 10:31:52

Gathering tickets related to `BipartiteGraph`, open and fixed issues.


---

Comment by dcoudert created at 2022-02-02 17:51:39

Proposal from [#33261#comment:3](https://trac.sagemath.org/ticket/33261#comment:3)
> Side note: The complete bipartite graph constructor should return a `BipartiteGraph` object IMO (instead of just a usual `Graph`).

I tried (for complete, random and random regular bipartite graphs) and it's not an easy task:
- the `__repr__` method of `BipartiteGraph` modifies the name string and so we have to correct several doctests
- algorithms modifying a graph with the addition of vertices fail since the side is not given. We must either implement specific versions for `BipartiteGraph` or modify these algorithms to work properly with `BipartiteGraph`.
So it's not so easy to do


---

Comment by tscrim created at 2022-02-03 01:27:33

Replying to [comment:19 dcoudert]:
> Proposal from [#33261#comment:3](https://trac.sagemath.org/ticket/33261#comment:3)
> > Side note: The complete bipartite graph constructor should return a `BipartiteGraph` object IMO (instead of just a usual `Graph`).
> 
> I tried (for complete, random and random regular bipartite graphs) and it's not an easy task:

Thank you for attempting it.

> - the `__repr__` method of `BipartiteGraph` modifies the name string and so we have to correct several doctests

This is minor IMO (although it might be good for the two to be consistent); just annoying to do.

> - algorithms modifying a graph with the addition of vertices fail since the side is not given. We must either implement specific versions for `BipartiteGraph` or modify these algorithms to work properly with `BipartiteGraph`.

This suggests that there is a compatibility issue between the two classes, which is a bug IMO since `BipartiteGraph` is a subclass of `Graph`. We probably need to modify `add_vertex` and `add_edge` to be compatible, such as returning a generic graph. Mainly, I am not sure I agree with the behavior of raising an error when the edge does not give a bipartite graph like in #8744 (although without such a complicated thing of recoloring the bipartite graph).

Essentially, IMO subclasses should behave like the base class but with extra features that utilize the special aspects (sometimes known as the ["is-a" test](https://en.wikipedia.org/wiki/Is-a)).


---

Comment by dcoudert created at 2022-02-03 13:13:50

`BipartiteGraph` adds restrictions to `Graph` and the price to pay is to maintain the partition. When using a `BipartiteGraph`, some operations may be forbidden (edge contraction, etc.) or done with care (`add_vertex`, `add_path`, etc.). Otherwise, the user has to move back to `Graph`.


---

Comment by tscrim created at 2022-02-04 01:09:40

Then it should not be a subclass IMO because of a fundamental incompatibility with some common ABC between `BipartiteGraph` and `Graph` to explicitly prohibit said methods.
