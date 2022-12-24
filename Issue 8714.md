# Issue 8714: add Bellman-Ford algorithm for shortest paths

archive/issues_008714.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  wdj dkrenn dcoudert ncohen\n\nI'm using #698 as a wish list of items to add to the graph theory module of Sage. The purpose of this ticket is to implement the [Bellman-Ford](http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) algorithm for finding shortest paths in a weighted graph `G` that may have negative weights. If `G` doesn't have negative weights, Dijkstra's algorithm can be used. However, if `G` has negative weights, we fall back on the Bellman-Ford algorithm. The Bellman-Ford algorithm is able to handle graphs with negative weights, but not graphs that have negative-weight cycles. See also the function [BellmanFord](http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html) in Mathematica's [Combinatorica](http://reference.wolfram.com/mathematica/Combinatorica/guide/CombinatoricaPackage.html) package. See this [graph theory book](http://code.google.com/p/graph-theory-algorithms-book/) for an algorithmic presentation of the Bellman-Ford algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8714\n\n",
    "created_at": "2010-04-19T06:30:38Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add Bellman-Ford algorithm for shortest paths",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8714",
    "user": "mvngu"
}
```
Assignee: jason, ncohen, rlm

CC:  wdj dkrenn dcoudert ncohen

I'm using #698 as a wish list of items to add to the graph theory module of Sage. The purpose of this ticket is to implement the [Bellman-Ford](http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) algorithm for finding shortest paths in a weighted graph `G` that may have negative weights. If `G` doesn't have negative weights, Dijkstra's algorithm can be used. However, if `G` has negative weights, we fall back on the Bellman-Ford algorithm. The Bellman-Ford algorithm is able to handle graphs with negative weights, but not graphs that have negative-weight cycles. See also the function [BellmanFord](http://reference.wolfram.com/mathematica/Combinatorica/ref/BellmanFord.html) in Mathematica's [Combinatorica](http://reference.wolfram.com/mathematica/Combinatorica/guide/CombinatoricaPackage.html) package. See this [graph theory book](http://code.google.com/p/graph-theory-algorithms-book/) for an algorithmic presentation of the Bellman-Ford algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/8714





---

archive/issue_comments_079509.json:
```json
{
    "body": "Here is an implementation by David Joyner:\n\n```\ndef bellman_ford(Gamma, s):\n    \"\"\"\n    Computes the shortest distance from s to all other vertices in Gamma.\n    If Gamma has a negative weight cycle, then return an error.\n\n    INPUT:\n\n    - Gamma -- a graph.\n    - s -- the source vertex.\n\n    OUTPUT:\n\n    - (d,p) -- pair of dictionaries keyed on the list of vertices,\n      which store the distance and shortest paths.\n\n    REFERENCE:\n\n    http://en.wikipedia.org/wiki/Bellman-Ford_algorithm\n    \"\"\"\n    P = []\n    dist = {}\n    predecessor = {}\n    V = Gamma.vertices()\n    E = Gamma.edges()\n    for v in V:\n        if v == s:\n            dist[v] = 0\n        else:\n            dist[v] = infinity\n        predecessor[v] = 0\n    for i in range(1, len(V)):\n        for e in E:\n            u = e[0]\n            v = e[1]\n            wt = e[2]\n            if dist[u] + wt < dist[v]:\n                dist[v] = dist[u] + wt\n                predecessor[v] = u\n    # check for negative-weight cycles\n    for e in E:\n\tu = e[0]\n        v = e[1]\n        wt = e[2]\n        if dist[u] + wt < dist[v]:\n            raise ValueError(\"Graph contains a negative-weight cycle\")\n    return dist, predecessor\n```\n\n\nAnd some examples:\n\n\n```\nsage: M = matrix([[0,1,4,0], [0,0,1,5], [0,0,0,3], [0,0,0,0]])\nsage: G = Graph(M, format=\"weighted_adjacency_matrix\")\nsage: bellman_ford(G, G.vertices()[0])\n  {0: 0, 1: 1, 2: 2, 3: 5}\n```\n\n\nand \n\n\n```\nsage: M = matrix([[0,1,0,0],[1,0,-4,1],[1,1,0,0],[0,0,1,0]])\nsage: G = DiGraph(M, format = \"weighted_adjacency_matrix\")\nsage: bellman_ford(G, G.vertices()[0])\n---------------------------------------------------------------------------\n...\nValueError: Graph contains a negative-weight cycle\n```\n",
    "created_at": "2010-04-23T03:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79509",
    "user": "mvngu"
}
```

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

archive/issue_comments_079510.json:
```json
{
    "body": "Bellman-Ford is available in `networkx 1.6`. I added the dependency #12806, where the upgrade to 1.6 happens.\n\nWhen #12806 is done, we can add an interface in the graph class for Bellman-Ford algorithm, which should be done with this ticket here.",
    "created_at": "2012-04-03T23:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79510",
    "user": "dkrenn"
}
```

Bellman-Ford is available in `networkx 1.6`. I added the dependency #12806, where the upgrade to 1.6 happens.

When #12806 is done, we can add an interface in the graph class for Bellman-Ford algorithm, which should be done with this ticket here.



---

archive/issue_comments_079511.json:
```json
{
    "body": "Hello,\n\nI have checked the networkx implementation of the Bellman-Ford algorithm ([See here](https://networkx.lanl.gov/trac/browser/networkx/networkx/algorithms/shortest_paths/weighted.py)) and we can propose a better implementation.\n\nThis is a first implementation that can certainly be improved. Its advantage is that in the best case the time complexity is in O(|V|+|E|) and in the worst case, it is O(|V|.|E|). It uses a set to maintain the set of active vertices, that is vertices for which a change has been performed during previous round.\n\n```\ndef bellman_ford(G, s):\n    \"\"\"\n    some documentation\n    \"\"\"\n    from sage.rings.infinity import Infinity\n    P = []\n    dist = {}\n    predecessor = {}\n    V = G.vertices()\n    N = G.num_verts()\n    E = G.edges()\n    for v in V:\n        if v == s:\n            dist[v] = 0\n        else:\n            dist[v] = Infinity\n        predecessor[v] = 0\n    W = {}\n    for e in E:\n        W[(e[0],e[1])] = e[2]\n        W[(e[1],e[0])] = e[2]\n    A = set([s])\n    B = set()\n    cpt = 0\n    while len(A) > 0 and cpt < N:\n        while len(A) > 0:\n            u = A.pop()\n            for v in G.neighbor_iterator(u):\n                if dist[u] + W[(u,v)] < dist[v]:\n                    dist[v] = dist[u] + W[u,v]\n                    predecessor[v] = u\n                    B.add(v)\n        A = B.copy()\n        B.clear()\n        cpt += 1\n    # check for negative-weight cycles\n    for e in E:\n\tu = e[0]\n        v = e[1]\n        wt = e[2]\n        if dist[u] + wt < dist[v]:\n            raise ValueError(\"Graph contains a negative-weight cycle\")\n    return dist, predecessor\n```\n\n\nThe implementation can be adapted to graphs and digraphs.\n\nLet me know if you think it is a good idea to write this patch.\n\nBest,\nD.",
    "created_at": "2012-06-20T17:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79511",
    "user": "dcoudert"
}
```

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

archive/issue_comments_079512.json:
```json
{
    "body": "I have a better implementation, but I don't know exactly \n- Where to place it: generic_graph.py or generic_graph_pyx.pyx for more efficiency\n- The best name: shortest_paths_BellmanFord ?\n- What to return: dictionary with distances and dictionary with predecessors or paths?\n\nWell, some minor details ;-)",
    "created_at": "2012-06-21T09:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79512",
    "user": "dcoudert"
}
```

I have a better implementation, but I don't know exactly 
- Where to place it: generic_graph.py or generic_graph_pyx.pyx for more efficiency
- The best name: shortest_paths_BellmanFord ?
- What to return: dictionary with distances and dictionary with predecessors or paths?

Well, some minor details ;-)



---

archive/issue_comments_079513.json:
```json
{
    "body": "Well, it depends on whether you want to optimize it in C a bit or not.. In this case the choice is made for you as you would need a Cython file.\n\nYou could also use the \"distance_all_pairs\" file.\n\nI would say that the best name would be.... no name ? A hidden function. Then function would then be accessed through the usual methods of graphs/digraphs, like \"distance\", \"shortest path\", \"distances all pairs\", with a special flag or just automatically if there happen to be negative weights on the edges... What do you think ? It would be weird to create a new function for that if we have many already, especially if you wonder what it should return -- in this case it would have to return what the function calling it expects... \n\nWe should be able to talk about in in a few days `:-)`\n\nNathann",
    "created_at": "2012-06-22T11:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79513",
    "user": "ncohen"
}
```

Well, it depends on whether you want to optimize it in C a bit or not.. In this case the choice is made for you as you would need a Cython file.

You could also use the "distance_all_pairs" file.

I would say that the best name would be.... no name ? A hidden function. Then function would then be accessed through the usual methods of graphs/digraphs, like "distance", "shortest path", "distances all pairs", with a special flag or just automatically if there happen to be negative weights on the edges... What do you think ? It would be weird to create a new function for that if we have many already, especially if you wonder what it should return -- in this case it would have to return what the function calling it expects... 

We should be able to talk about in in a few days `:-)`

Nathann



---

archive/issue_comments_079514.json:
```json
{
    "body": "At first I can add it to generic_graph.py, and let to others to option to improve the implementation in C.\n\nI will propose a patch over the week end.",
    "created_at": "2012-06-22T12:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79514",
    "user": "dcoudert"
}
```

At first I can add it to generic_graph.py, and let to others to option to improve the implementation in C.

I will propose a patch over the week end.



---

archive/issue_comments_079515.json:
```json
{
    "body": "Hello!\n\nIs there anything new with this patch? BF would be a very useful algorithm to have in Sage!",
    "created_at": "2013-04-06T12:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79515",
    "user": "azi"
}
```

Hello!

Is there anything new with this patch? BF would be a very useful algorithm to have in Sage!



---

archive/issue_comments_079516.json:
```json
{
    "body": "I don't have a lot of free time these days and it takes some time to write the documentation and doctests. I will try to commit soon.",
    "created_at": "2013-04-06T13:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79516",
    "user": "dcoudert"
}
```

I don't have a lot of free time these days and it takes some time to write the documentation and doctests. I will try to commit soon.



---

archive/issue_comments_079517.json:
```json
{
    "body": "Attachment [trac_8714.patch](tarball://root/attachments/some-uuid/ticket8714/trac_8714.patch) by dcoudert created at 2013-04-06 15:42:56",
    "created_at": "2013-04-06T15:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79517",
    "user": "dcoudert"
}
```

Attachment [trac_8714.patch](tarball://root/attachments/some-uuid/ticket8714/trac_8714.patch) by dcoudert created at 2013-04-06 15:42:56



---

archive/issue_comments_079518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-06T15:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79518",
    "user": "dcoudert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079519.json:
```json
{
    "body": "I have uploaded the first part of the patch: the hidden bellman-ford function. You can already try it (and reviewed it) via `G.__bellman_ford__(source node)`  where G is either a graph or a digraph, with or without loops and multiple edges, with negative edge weights, etc.\n\nIt remains the long/boring part to call that function from other functions, add optional arguments and tests, etc. I don't have time to do it now, so anyone is welcome to contribute.\n\nI set the patch to needs review, but it should be needs work.\n\nDavid.",
    "created_at": "2013-04-06T15:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79519",
    "user": "dcoudert"
}
```

I have uploaded the first part of the patch: the hidden bellman-ford function. You can already try it (and reviewed it) via `G.__bellman_ford__(source node)`  where G is either a graph or a digraph, with or without loops and multiple edges, with negative edge weights, etc.

It remains the long/boring part to call that function from other functions, add optional arguments and tests, etc. I don't have time to do it now, so anyone is welcome to contribute.

I set the patch to needs review, but it should be needs work.

David.



---

archive/issue_comments_079520.json:
```json
{
    "body": "> I set the patch to needs review, but it should be needs work.\n\nWell, then.. `O_o`\n\nNathann",
    "created_at": "2013-05-12T09:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79520",
    "user": "ncohen"
}
```

> I set the patch to needs review, but it should be needs work.

Well, then.. `O_o`

Nathann



---

archive/issue_comments_079521.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-05-12T09:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79521",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079522.json:
```json
{
    "body": "Attachment [trac_8714.2.patch](tarball://root/attachments/some-uuid/ticket8714/trac_8714.2.patch) by dcoudert created at 2013-09-15 14:07:48\n\nFinally, this patch is ready to be reviewed!\n\nThe method is now transparently called when negative weights are detected. I have also added an optional parameter that could be used e.g. in patch #13380.\n\n\napply: trac_8714.2.patch",
    "created_at": "2013-09-15T14:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79522",
    "user": "dcoudert"
}
```

Attachment [trac_8714.2.patch](tarball://root/attachments/some-uuid/ticket8714/trac_8714.2.patch) by dcoudert created at 2013-09-15 14:07:48

Finally, this patch is ready to be reviewed!

The method is now transparently called when negative weights are detected. I have also added an optional parameter that could be used e.g. in patch #13380.


apply: trac_8714.2.patch



---

archive/issue_comments_079523.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-09-15T16:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79523",
    "user": "dcoudert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079524.json:
```json
{
    "body": "Attachment [trac_8714_addon1.patch](tarball://root/attachments/some-uuid/ticket8714/trac_8714_addon1.patch) by chapoton created at 2013-10-20 12:23:40",
    "created_at": "2013-10-20T12:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79524",
    "user": "chapoton"
}
```

Attachment [trac_8714_addon1.patch](tarball://root/attachments/some-uuid/ticket8714/trac_8714_addon1.patch) by chapoton created at 2013-10-20 12:23:40



---

archive/issue_comments_079525.json:
```json
{
    "body": "I have made a small review patch, mainly changing minor cosmetic details.",
    "created_at": "2013-10-20T12:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79525",
    "user": "chapoton"
}
```

I have made a small review patch, mainly changing minor cosmetic details.



---

archive/issue_comments_079526.json:
```json
{
    "body": "Hello,\n\nI haven't received notification for the addon patch.\n\nThe addon patch is ok (install, test, etc.).\n\nThank you for this improvement. I let you decide for the status of the patch.\n\nDavid.",
    "created_at": "2013-11-08T19:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79526",
    "user": "dcoudert"
}
```

Hello,

I haven't received notification for the addon patch.

The addon patch is ok (install, test, etc.).

Thank you for this improvement. I let you decide for the status of the patch.

David.



---

archive/issue_comments_079527.json:
```json
{
    "body": "Yoooooooooooo !\n\nI just reviewed this patch, and I don't see anything wrong. Several questions/remarks, though :\n- the `weights` dictionary is actually (in memory) a copy of the whole graph. Isn't it better to create a normalized copy of the graph and work on this only ?\n- Why `__bellman_ford__` and not just `_bellman_ford` ? Isn't the `__` only for special Python functions ?\n- You say that loops are supported, but I don't see how. Where do you detect if there is a negative loop somewhere, for instance ?\n- your function `ee` compares the vertices' name, and that's tricky. Sometimes the vertices of a graph are not integers, can be sets (KneserGraph for instance) and comparing them doesn't work as expected.\n\nBesides:\n- I modified a bit the behaviour of your modifications to `shortest_paths`, as this dictionary only needs to contain an entry for a target when such a path exists. I also used the fact that your Bellman Ford implementation satisfies `pred[t] = [t]` whenever `dist[t] == Infinity`.\n- From the looks of `.all_pairs_shortest_path`, perhaps we should create a hidden function for the code of `Floyd-Warshall_Python`. Not urgent, just cleaning stuff.\n\nI added my patch as a git commit, to which the two previous hg patches belong. The new branch is u/ncohen/8714.\n\nHave fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuun ! `;-)`\n\nNathann",
    "created_at": "2013-12-05T20:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79527",
    "user": "ncohen"
}
```

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

archive/issue_comments_079528.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2013-12-05T20:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79528",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079529.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-12-05T20:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79529",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_079530.json:
```json
{
    "body": "I had a short look at this patch and corrected a few obvious typos.\n\nReplying to [comment:18 ncohen]:\n> - You say that loops are supported, but I don't see how. Where do you detect if there is a negative loop somewhere, for instance ?\n\nIf there is a negative loop somewhere, `max_number_of_loops` is reached and the code raises a `ValueError`.\n----\nNew commits:",
    "created_at": "2014-05-14T11:37:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79530",
    "user": "cheuberg"
}
```

I had a short look at this patch and corrected a few obvious typos.

Replying to [comment:18 ncohen]:
> - You say that loops are supported, but I don't see how. Where do you detect if there is a negative loop somewhere, for instance ?

If there is a negative loop somewhere, `max_number_of_loops` is reached and the code raises a `ValueError`.
----
New commits:



---

archive/issue_comments_079531.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-14T16:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79531",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079532.json:
```json
{
    "body": "Thank you for pushing this patch. I had no time to do it in the last months, and I still don't know how to use git...\n\nI had a quick look at proposed changes.\n\ntypo: algorith -> algorithm\n\n```\n- INPUTS:\n+ For more information on the Bellman-Ford algorith, see the\n```\n\n\nI have some doubt about the recursive function  `def build_paths(v):`.\nI suggest to have a loop instead of recursive calls. You never know how long will be the path, and its never a good idea to have 1000 or more recursive calls...\n\n\nThanks.",
    "created_at": "2014-05-15T08:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79532",
    "user": "dcoudert"
}
```

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

archive/issue_comments_079533.json:
```json
{
    "body": "Replying to [comment:18 ncohen]:\n> - your function `ee` compares the vertices' name, and that's tricky. Sometimes the vertices of a graph are not integers, can be sets (KneserGraph for instance) and comparing them doesn't work as expected.\n\nApparently, the function `ee` serves to orient an undirected graph. One could probably replace the comparison of the labels by a comparison of the `id` which would serve the same purpose (have a unique orientation).\n\nHowever: is there any advantage of using the Bellman-Ford algorithm (as compared to Dijkstra) in the undirected case? If all edges have non-negative weight, Dijkstra should be more efficient. If there is an edge with negative weight (and this edge is reachable from the start vertex), then Bellman-Ford will detect it as a negative circuit (just take this edge in both directions repeatedly) and fail anyway. \n\nThere is a method for computing shortest paths in undirected graphs with conservative weights (negative edge weights allowed, but no undirected cycle (different vertices!) of negative weight), cf. Corollary 12.13 in Korte and Vygen, Combinatorial Optimization (5th edition). But this has nothing to do with Bellman-Ford.\n\nMy proposal would be to remove the code for undirected graphs in this proposed patch, which would increase readability IMHO, remove the problem with this `ee` function and would, in my opinion, not loose any useful functionality. I do not know whether this would still belong to `generic_graph`, though.",
    "created_at": "2014-05-15T11:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79533",
    "user": "cheuberg"
}
```

Replying to [comment:18 ncohen]:
> - your function `ee` compares the vertices' name, and that's tricky. Sometimes the vertices of a graph are not integers, can be sets (KneserGraph for instance) and comparing them doesn't work as expected.

Apparently, the function `ee` serves to orient an undirected graph. One could probably replace the comparison of the labels by a comparison of the `id` which would serve the same purpose (have a unique orientation).

However: is there any advantage of using the Bellman-Ford algorithm (as compared to Dijkstra) in the undirected case? If all edges have non-negative weight, Dijkstra should be more efficient. If there is an edge with negative weight (and this edge is reachable from the start vertex), then Bellman-Ford will detect it as a negative circuit (just take this edge in both directions repeatedly) and fail anyway. 

There is a method for computing shortest paths in undirected graphs with conservative weights (negative edge weights allowed, but no undirected cycle (different vertices!) of negative weight), cf. Corollary 12.13 in Korte and Vygen, Combinatorial Optimization (5th edition). But this has nothing to do with Bellman-Ford.

My proposal would be to remove the code for undirected graphs in this proposed patch, which would increase readability IMHO, remove the problem with this `ee` function and would, in my opinion, not loose any useful functionality. I do not know whether this would still belong to `generic_graph`, though.



---

archive/issue_comments_079534.json:
```json
{
    "body": "Replying to [comment:26 dcoudert]:\n> typo: algorith -> algorithm\n> {{{\n> - INPUTS:\n> + For more information on the Bellman-Ford algorith, see the\n> }}}\n\nI do not understand your comment, I corrected a typo algorith -> algorithm in [a27064f](http://git.sagemath.org/sage.git/commit/?id=a27064f6972402144b7fd5748f6e524d30194870) and cannot find another occurrence of \"algorith,\"",
    "created_at": "2014-05-15T11:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79534",
    "user": "cheuberg"
}
```

Replying to [comment:26 dcoudert]:
> typo: algorith -> algorithm
> {{{
> - INPUTS:
> + For more information on the Bellman-Ford algorith, see the
> }}}

I do not understand your comment, I corrected a typo algorith -> algorithm in [a27064f](http://git.sagemath.org/sage.git/commit/?id=a27064f6972402144b7fd5748f6e524d30194870) and cannot find another occurrence of "algorith,"



---

archive/issue_comments_079535.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-16T06:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79535",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_079536.json:
```json
{
    "body": "I fixed two issues with the code. This includes a simple doctest for the (previously broken for negative edge weights) function shortest_paths. IMHO, doctests should be included for the other\nchanged functions, too.",
    "created_at": "2014-05-16T07:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79536",
    "user": "cheuberg"
}
```

I fixed two issues with the code. This includes a simple doctest for the (previously broken for negative edge weights) function shortest_paths. IMHO, doctests should be included for the other
changed functions, too.



---

archive/issue_comments_079537.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2015-08-24T06:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79537",
    "user": "cheuberg"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_079538.json:
```json
{
    "body": "Bellman-Ford has now been implemented in #18931. As discussed in [#18931 comment 15](http://trac.sagemath.org/ticket/18931#comment:15), the performance has not yet been compared with the code here.\n\nHowever, the branch attached to this ticket no longer merges with develop and very much work would be needed. Moreover, this ticket has not had any activity for 15 months. My suggestion is to close this ticket here as a duplicate.",
    "created_at": "2015-08-24T06:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79538",
    "user": "cheuberg"
}
```

Bellman-Ford has now been implemented in #18931. As discussed in [#18931 comment 15](http://trac.sagemath.org/ticket/18931#comment:15), the performance has not yet been compared with the code here.

However, the branch attached to this ticket no longer merges with develop and very much work would be needed. Moreover, this ticket has not had any activity for 15 months. My suggestion is to close this ticket here as a duplicate.



---

archive/issue_comments_079539.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-08-24T09:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79539",
    "user": "dcoudert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079540.json:
```json
{
    "body": "Actually I tried this patch a few days ago and I fully agree that it has to be fully rewritten. Moreover, to be competitive with respect to #18931, the algorithm has to be cythonized.\nSo let's close this ticket, and if later we decide to give a try to a fresh cython implementation, we can do it in another ticket.\nBest,\nDavid.",
    "created_at": "2015-08-24T09:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79540",
    "user": "dcoudert"
}
```

Actually I tried this patch a few days ago and I fully agree that it has to be fully rewritten. Moreover, to be competitive with respect to #18931, the algorithm has to be cythonized.
So let's close this ticket, and if later we decide to give a try to a fresh cython implementation, we can do it in another ticket.
Best,
David.



---

archive/issue_comments_079541.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-09-12T13:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8714#issuecomment-79541",
    "user": "vbraun"
}
```

Resolution: wontfix
