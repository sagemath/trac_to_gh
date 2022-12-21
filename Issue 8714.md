# Issue 8714: add Bellman-Ford algorithm for shortest paths

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-19 06:30:38

Assignee: jason, ncohen, rlm

CC:  wdj dkrenn dcoudert ncohen

I'm using #698 as a wish list of items to add to the graph theory module of Sage. The purpose of this ticket is to implement the [Bellman-Ford](http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) algorithm for finding shortest paths in a weighted graph `G` that may have negative weights. If `G` doesn't have negative weights, Dijkstra's algorithm can be used. However, if `G` has negative weights, we fall back on the Bellman-Ford algorithm. The Bellman-Ford algorithm is able to handle graphs with negative weights, but not graphs that have negative-weight cycles. See also the function [BellmanFord](http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html) in Mathematica's [Combinatorica](http://reference.wolfram.com/mathematica/Combinatorica/guide/CombinatoricaPackage.html) package. See this [graph theory book](http://code.google.com/p/graph-theory-algorithms-book/) for an algorithmic presentation of the Bellman-Ford algorithm.


---

Comment by mvngu created at 2010-04-23 03:31:40

Here is an implementation by David Joyner:

```
def bellman_ford(Gamma, s):
    """
    Computes the shortest distance from s to all other vertices in Gamma.
    If Gamma has a negative weight cycle, then return an error.

    INPUT:

    - Gamma -- a graph.
    - s -- the source vertex.

    OUTPUT:

    - (d,p) -- pair of dictionaries keyed on the list of vertices,
      which store the distance and shortest paths.

    REFERENCE:

    http://en.wikipedia.org/wiki/Bellman-Ford_algorithm
    """
    P = []
    dist = {}
    predecessor = {}
    V = Gamma.vertices()
    E = Gamma.edges()
    for v in V:
        if v == s:
            dist[v] = 0
        else:
            dist[v] = infinity
        predecessor[v] = 0
    for i in range(1, len(V)):
        for e in E:
            u = e[0]
            v = e[1]
            wt = e[2]
            if dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt
                predecessor[v] = u
    # check for negative-weight cycles
    for e in E:
	u = e[0]
        v = e[1]
        wt = e[2]
        if dist[u] + wt < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    return dist, predecessor
```


And some examples:


```
sage: M = matrix([[0,1,4,0], [0,0,1,5], [0,0,0,3], [0,0,0,0]])
sage: G = Graph(M, format="weighted_adjacency_matrix")
sage: bellman_ford(G, G.vertices()[0])
  {0: 0, 1: 1, 2: 2, 3: 5}
```


and 


```
sage: M = matrix([[0,1,0,0],[1,0,-4,1],[1,1,0,0],[0,0,1,0]])
sage: G = DiGraph(M, format = "weighted_adjacency_matrix")
sage: bellman_ford(G, G.vertices()[0])
---------------------------------------------------------------------------
...
ValueError: Graph contains a negative-weight cycle
```



---

Comment by dkrenn created at 2012-04-03 23:23:24

Bellman-Ford is available in `networkx 1.6`. I added the dependency #12806, where the upgrade to 1.6 happens.

When #12806 is done, we can add an interface in the graph class for Bellman-Ford algorithm, which should be done with this ticket here.


---

Comment by dcoudert created at 2012-06-20 17:29:18

Hello,

I have checked the networkx implementation of the Bellman-Ford algorithm ([See here](https://networkx.lanl.gov/trac/browser/networkx/networkx/algorithms/shortest_paths/weighted.py)) and we can propose a better implementation.

This is a first implementation that can certainly be improved. Its advantage is that in the best case the time complexity is in O(|V|+|E|) and in the worst case, it is O(|V|.|E|). It uses a set to maintain the set of active vertices, that is vertices for which a change has been performed during previous round.

```
def bellman_ford(G, s):
    """
    some documentation
    """
    from sage.rings.infinity import Infinity
    P = []
    dist = {}
    predecessor = {}
    V = G.vertices()
    N = G.num_verts()
    E = G.edges()
    for v in V:
        if v == s:
            dist[v] = 0
        else:
            dist[v] = Infinity
        predecessor[v] = 0
    W = {}
    for e in E:
        W[(e[0],e[1])] = e[2]
        W[(e[1],e[0])] = e[2]
    A = set([s])
    B = set()
    cpt = 0
    while len(A) > 0 and cpt < N:
        while len(A) > 0:
            u = A.pop()
            for v in G.neighbor_iterator(u):
                if dist[u] + W[(u,v)] < dist[v]:
                    dist[v] = dist[u] + W[u,v]
                    predecessor[v] = u
                    B.add(v)
        A = B.copy()
        B.clear()
        cpt += 1
    # check for negative-weight cycles
    for e in E:
	u = e[0]
        v = e[1]
        wt = e[2]
        if dist[u] + wt < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    return dist, predecessor
```


The implementation can be adapted to graphs and digraphs.

Let me know if you think it is a good idea to write this patch.

Best,
D.


---

Comment by dcoudert created at 2012-06-21 09:26:03

I have a better implementation, but I don't know exactly 
- Where to place it: generic_graph.py or generic_graph_pyx.pyx for more efficiency
- The best name: shortest_paths_BellmanFord ?
- What to return: dictionary with distances and dictionary with predecessors or paths?

Well, some minor details ;-)


---

Comment by ncohen created at 2012-06-22 11:37:23

Well, it depends on whether you want to optimize it in C a bit or not.. In this case the choice is made for you as you would need a Cython file.

You could also use the "distance_all_pairs" file.

I would say that the best name would be.... no name ? A hidden function. Then function would then be accessed through the usual methods of graphs/digraphs, like "distance", "shortest path", "distances all pairs", with a special flag or just automatically if there happen to be negative weights on the edges... What do you think ? It would be weird to create a new function for that if we have many already, especially if you wonder what it should return -- in this case it would have to return what the function calling it expects... 

We should be able to talk about in in a few days `:-)`

Nathann


---

Comment by dcoudert created at 2012-06-22 12:06:06

At first I can add it to generic_graph.py, and let to others to option to improve the implementation in C.

I will propose a patch over the week end.


---

Comment by azi created at 2013-04-06 12:56:32

Hello!

Is there anything new with this patch? BF would be a very useful algorithm to have in Sage!


---

Comment by dcoudert created at 2013-04-06 13:40:11

I don't have a lot of free time these days and it takes some time to write the documentation and doctests. I will try to commit soon.


---

Attachment


---

Comment by dcoudert created at 2013-04-06 15:49:50

Changing status from new to needs_review.


---

Comment by dcoudert created at 2013-04-06 15:49:50

I have uploaded the first part of the patch: the hidden bellman-ford function. You can already try it (and reviewed it) via `G.__bellman_ford__(source node)`  where G is either a graph or a digraph, with or without loops and multiple edges, with negative edge weights, etc.

It remains the long/boring part to call that function from other functions, add optional arguments and tests, etc. I don't have time to do it now, so anyone is welcome to contribute.

I set the patch to needs review, but it should be needs work.

David.


---

Comment by ncohen created at 2013-05-12 09:32:05

> I set the patch to needs review, but it should be needs work.

Well, then.. `O_o`

Nathann


---

Comment by ncohen created at 2013-05-12 09:32:05

Changing status from needs_review to needs_work.


---

Attachment

Finally, this patch is ready to be reviewed!

The method is now transparently called when negative weights are detected. I have also added an optional parameter that could be used e.g. in patch #13380.


apply: trac_8714.2.patch


---

Comment by dcoudert created at 2013-09-15 16:44:09

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by chapoton created at 2013-10-20 12:32:42

I have made a small review patch, mainly changing minor cosmetic details.


---

Comment by dcoudert created at 2013-11-08 19:16:07

Hello,

I haven't received notification for the addon patch.

The addon patch is ok (install, test, etc.).

Thank you for this improvement. I let you decide for the status of the patch.

David.


---

Comment by ncohen created at 2013-12-05 20:07:46

Yoooooooooooo !

I just reviewed this patch, and I don't see anything wrong. Several questions/remarks, though :
- the `weights` dictionary is actually (in memory) a copy of the whole graph. Isn't it better to create a normalized copy of the graph and work on this only ?
- Why `__bellman_ford__` and not just `_bellman_ford` ? Isn't the `__` only for special Python functions ?
- You say that loops are supported, but I don't see how. Where do you detect if there is a negative loop somewhere, for instance ?
- your function `ee` compares the vertices' name, and that's tricky. Sometimes the vertices of a graph are not integers, can be sets (KneserGraph for instance) and comparing them doesn't work as expected.

Besides:
- I modified a bit the behaviour of your modifications to `shortest_paths`, as this dictionary only needs to contain an entry for a target when such a path exists. I also used the fact that your Bellman Ford implementation satisfies `pred[t] = [t]` whenever `dist[t] == Infinity`.
- From the looks of `.all_pairs_shortest_path`, perhaps we should create a hidden function for the code of `Floyd-Warshall_Python`. Not urgent, just cleaning stuff.

I added my patch as a git commit, to which the two previous hg patches belong. The new branch is u/ncohen/8714.

Have fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuun ! `;-)`

Nathann


---

Comment by git created at 2013-12-05 20:09:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by ncohen created at 2013-12-05 20:11:21

Changing status from needs_review to needs_info.


---

Comment by cheuberg created at 2014-05-14 11:37:19

I had a short look at this patch and corrected a few obvious typos.

Replying to [comment:18 ncohen]:
> - You say that loops are supported, but I don't see how. Where do you detect if there is a negative loop somewhere, for instance ?

If there is a negative loop somewhere, `max_number_of_loops` is reached and the code raises a `ValueError`.
----
New commits:


---

Comment by git created at 2014-05-14 16:11:06

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dcoudert created at 2014-05-15 08:08:13

Thank you for pushing this patch. I had no time to do it in the last months, and I still don't know how to use git...

I had a quick look at proposed changes.

typo: algorith -> algorithm

```
- INPUTS:
+ For more information on the Bellman-Ford algorith, see the
```


I have some doubt about the recursive function  `def build_paths(v):`.
I suggest to have a loop instead of recursive calls. You never know how long will be the path, and its never a good idea to have 1000 or more recursive calls...


Thanks.


---

Comment by cheuberg created at 2014-05-15 11:18:47

Replying to [comment:18 ncohen]:
> - your function `ee` compares the vertices' name, and that's tricky. Sometimes the vertices of a graph are not integers, can be sets (KneserGraph for instance) and comparing them doesn't work as expected.

Apparently, the function `ee` serves to orient an undirected graph. One could probably replace the comparison of the labels by a comparison of the `id` which would serve the same purpose (have a unique orientation).

However: is there any advantage of using the Bellman-Ford algorithm (as compared to Dijkstra) in the undirected case? If all edges have non-negative weight, Dijkstra should be more efficient. If there is an edge with negative weight (and this edge is reachable from the start vertex), then Bellman-Ford will detect it as a negative circuit (just take this edge in both directions repeatedly) and fail anyway. 

There is a method for computing shortest paths in undirected graphs with conservative weights (negative edge weights allowed, but no undirected cycle (different vertices!) of negative weight), cf. Corollary 12.13 in Korte and Vygen, Combinatorial Optimization (5th edition). But this has nothing to do with Bellman-Ford.

My proposal would be to remove the code for undirected graphs in this proposed patch, which would increase readability IMHO, remove the problem with this `ee` function and would, in my opinion, not loose any useful functionality. I do not know whether this would still belong to `generic_graph`, though.


---

Comment by cheuberg created at 2014-05-15 11:21:59

Replying to [comment:26 dcoudert]:
> typo: algorith -> algorithm
> {{{
> - INPUTS:
> + For more information on the Bellman-Ford algorith, see the
> }}}

I do not understand your comment, I corrected a typo algorith -> algorithm in [a27064f](http://git.sagemath.org/sage.git/commit/?id=a27064f6972402144b7fd5748f6e524d30194870) and cannot find another occurrence of "algorith,"


---

Comment by git created at 2014-05-16 06:59:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cheuberg created at 2014-05-16 07:03:51

I fixed two issues with the code. This includes a simple doctest for the (previously broken for negative edge weights) function shortest_paths. IMHO, doctests should be included for the other
changed functions, too.


---

Comment by cheuberg created at 2015-08-24 06:54:31

Changing status from needs_info to needs_review.


---

Comment by cheuberg created at 2015-08-24 06:54:31

Bellman-Ford has now been implemented in #18931. As discussed in [#18931 comment 15](http://trac.sagemath.org/ticket/18931#comment:15), the performance has not yet been compared with the code here.

However, the branch attached to this ticket no longer merges with develop and very much work would be needed. Moreover, this ticket has not had any activity for 15 months. My suggestion is to close this ticket here as a duplicate.


---

Comment by dcoudert created at 2015-08-24 09:11:42

Changing status from needs_review to positive_review.


---

Comment by dcoudert created at 2015-08-24 09:11:42

Actually I tried this patch a few days ago and I fully agree that it has to be fully rewritten. Moreover, to be competitive with respect to #18931, the algorithm has to be cythonized.
So let's close this ticket, and if later we decide to give a try to a fresh cython implementation, we can do it in another ticket.
Best,
David.


---

Comment by vbraun created at 2015-09-12 13:58:34

Resolution: wontfix
