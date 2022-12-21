# Issue 1089: [with patch] graphs: update subgraph to handle a list of edges

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-03 20:48:47

Assignee: mhansen

Keywords: graphs

Here is an update to the subgraph function to handle a list of edges.  If edges are not specified, then it reverts to the original functionality (returning an induced subgraph).

I also fix a doctest that should have been complaining in transitive_reduction and make the doctests in min_spanning_tree make more sense.


---

Attachment

Jason,

Please include a fresh patch that comes from a clean install of sage 2.8.11. The base version does not match. Also, the function subgraph(vertices) returns the induced subgraph with the given vertices and *all* edges from the original graph whose endpoints are in vertices. Perhaps the current function should be renamed induced_subgraph, and you could make a separate subgraph_from_edges() function. It also occurs to me that we don't yet have an is_subgraph fucntion...

Cheers,

Robert M


---

Comment by rlm created at 2007-11-03 23:33:02

Jason,

I should have mentioned to apply the patches in #1088 to the clean version first, then patch on top of that.

Thanks, Robert M


---

Comment by jason created at 2007-11-04 03:18:46

Robert,

You're right, #1088 should be applied first.  This patch modifies a doctest in #1088 to be more sensible.  I was going to include the better doctest in #1088 to keep both patches more self-contained, but then the doctests wouldn't have passed after only applying #1088.  Did applying this patch after #1088 resolve the issue or would you still like me to rebase against 2.8.11?

As to the subgraph function: I think it's a reasonable idea to say that the subgraph function returns a graph that is the intersection of what is currently in the graph and the restrictions that you pass relating to vertices and edges (as represented by a list of "allowable" vertices and/or edges you pass the subgraph function).  If you pass just a restriction on the vertices to include in the subgraph, then there is no restriction on the edges and you get an induced subgraph.  If you pass a restriction on the edges, then you get a graph with the same vertices as the original graph, but with possibly fewer edges (that is what the added doctest tests).  If you pass a restriction on both the edges and vertices, then the returned graph only has vertices from the vertex set you passed and edges from the edge set you passed.  I don't think that we need to make several different functions for this feature.  But if you think it would be clearer to have several functions, let me know.

One of the things I'm trying to do here is consolidate functionality when it makes sense so that we don't end up having hundreds of different functions that people have to remember.  I guess the question here is whether it makes sense.

As for the is_subgraph function, I believe that that problem is quite a bit harder (in a technical sense) than the graph isomorphism problem, even if you restrict to induced subgraphs.  I suppose it would be fairly easy, though, to implement an is_induced_subgraph function by taking k-subsets of the vertices and asking if the induced subgraph is isomorphic to a given graph.

A related feature request is for functions dealing with graph minors (constructing minors, asking if a graph is a minor of another, etc.).

Thanks for your comments and suggestions!


---

Comment by rlm created at 2007-11-06 19:14:49

Jason,

The reason I was asking you to rebase is that I already patched up the doctests from 1088 (the second patch there). As far as patches go, you can do one of the following:

1) Wait for sage-2.8.12 to be released, and do a patch on top of that.

2) Apply *both* patches in ticket 1088 to a fresh 2.8.11, and do a patch on top of that.

You've convinced me that these functionalities should be in the same function. I was just thinking that the name "subgraph" was a little misleading for a function name. Under your interpretation, all of these would be induced subgraphs, so to speak. I don't know if induced_subgraph is better, since the first thing anyone would look for would be subgraph anyway, and it's shorter to type...

Indeed, the subgraph isomorphism problem is NP-complete, but I was just talking about *is* subgraph, as a subset. Same vertices, same exact edges. I could see this being useful in some situations.


---

Attachment

Corrected bugs, rebased against 2.8.12, and put in more comprehensive doctests.


---

Comment by jason created at 2007-11-13 23:45:19

The subgraph_edges-updated.patch should be applied instead of the subgraph_edges.patch.


---

Comment by rlm created at 2007-11-15 18:59:07

Looks good to me.


---

Comment by mabshoff created at 2007-11-19 21:42:51

Resolution: fixed


---

Comment by mabshoff created at 2007-11-19 21:42:51

Merged in 2.8.13.alpha1.
