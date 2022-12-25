# Issue 7676: shortest_path_all pairs in Cython through Floyd Warshall

archive/issues_007676.json:
```json
{
    "body": "Assignee: @rlmill\n\nEverything is explained there :\n\nhttp://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm\n\nIssue created by migration from https://trac.sagemath.org/ticket/7676\n\n",
    "created_at": "2009-12-13T16:33:51Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.5",
    "title": "shortest_path_all pairs in Cython through Floyd Warshall",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7676",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

Everything is explained there :

http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

Issue created by migration from https://trac.sagemath.org/ticket/7676





---

archive/issue_comments_065718.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65718",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_065719.json:
```json
{
    "body": "According to https://ask.sagemath.org/question/44823/sage-floyd-algorithm-in-cython/ SciPy already includes an implementation of this that is quite fast, and should probably be used over any implementation in Sage.",
    "created_at": "2019-01-07T13:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65719",
    "user": "https://github.com/embray"
}
```

According to https://ask.sagemath.org/question/44823/sage-floyd-algorithm-in-cython/ SciPy already includes an implementation of this that is quite fast, and should probably be used over any implementation in Sage.



---

archive/issue_comments_065720.json:
```json
{
    "body": "If nobody else is currently working on this can I go ahead and implement shortest_path_all pair using Floyd warshall algorithm ?",
    "created_at": "2020-02-06T18:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65720",
    "user": "https://github.com/vipul79321"
}
```

If nobody else is currently working on this can I go ahead and implement shortest_path_all pair using Floyd warshall algorithm ?



---

archive/issue_comments_065721.json:
```json
{
    "body": "The first step is to survey the many algorithms we already have with data structures and specific conditions (e.g., weighted, multi edges, loops, etc.).",
    "created_at": "2020-02-07T07:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65721",
    "user": "https://github.com/dcoudert"
}
```

The first step is to survey the many algorithms we already have with data structures and specific conditions (e.g., weighted, multi edges, loops, etc.).



---

archive/issue_comments_065722.json:
```json
{
    "body": "I have surveyed all the algorithm and data structure sage has. All pair shortest path works only for an unweighted graph. Although we can use boost interface for this purpose. But I think sage should have its own implementation of Floyd Warshall algorithm[https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) for a weighted graph with positive or negative edge weights(but with no negative cycles).",
    "created_at": "2020-02-08T08:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65722",
    "user": "https://github.com/vipul79321"
}
```

I have surveyed all the algorithm and data structure sage has. All pair shortest path works only for an unweighted graph. Although we can use boost interface for this purpose. But I think sage should have its own implementation of Floyd Warshall algorithm[https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) for a weighted graph with positive or negative edge weights(but with no negative cycles).



---

archive/issue_comments_065723.json:
```json
{
    "body": "I don't think sage should have it's own implementation if the one of Boost is fast enough. \nYou can give it a try, but I'm not sure you can produce something faster than `'Floyd-Warshall_Boost'`.\n\nNote that we already have a (slow) Python implementation `'Floyd-Warshall-Python'` for weighted graphs, and a Cython implementation `'Floyd-Warshall-Cython'` but for unweighted graphs only.",
    "created_at": "2020-02-08T11:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65723",
    "user": "https://github.com/dcoudert"
}
```

I don't think sage should have it's own implementation if the one of Boost is fast enough. 
You can give it a try, but I'm not sure you can produce something faster than `'Floyd-Warshall_Boost'`.

Note that we already have a (slow) Python implementation `'Floyd-Warshall-Python'` for weighted graphs, and a Cython implementation `'Floyd-Warshall-Cython'` but for unweighted graphs only.



---

archive/issue_comments_065724.json:
```json
{
    "body": "Thanks for your helpful suggestion. I will look into it.",
    "created_at": "2020-02-08T13:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65724",
    "user": "https://github.com/vipul79321"
}
```

Thanks for your helpful suggestion. I will look into it.



---

archive/issue_comments_065725.json:
```json
{
    "body": "I added the `Floyd-Warshall` implementation of `SciPy`. It's working well but it's not as fast as expected. In fact, most of the time is wasted in turning the graph to a Numpy array and then turning the results to required dict of dicts.\n\n\n```\nsage: D = digraphs.RandomDirectedGNP(30, .33)\nsage: for u, v in D.edges(labels=False):\n....:     D.set_edge_label(u, v, randrange(100))\nsage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_Boost')\nCPU times: user 6.44 ms, sys: 517 \u00b5s, total: 6.96 ms\nWall time: 6.56 ms\nsage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_SciPy')\nCPU times: user 30.2 ms, sys: 1.85 ms, total: 32 ms\nWall time: 30.6 ms\n```\n\n\n```\nsage: D = digraphs.RandomDirectedGNP(300, .33)\nsage: for u, v in D.edges(labels=False):\n....:     D.set_edge_label(u, v, randrange(100))\nsage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_Boost')\nCPU times: user 2.73 s, sys: 18.6 ms, total: 2.75 s\nWall time: 2.76 s\nsage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_SciPy')\nCPU times: user 1.95 s, sys: 61.6 ms, total: 2.01 s\nWall time: 2.13 s\n```\n\n----\nNew commits:",
    "created_at": "2021-10-16T16:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65725",
    "user": "https://github.com/dcoudert"
}
```

I added the `Floyd-Warshall` implementation of `SciPy`. It's working well but it's not as fast as expected. In fact, most of the time is wasted in turning the graph to a Numpy array and then turning the results to required dict of dicts.


```
sage: D = digraphs.RandomDirectedGNP(30, .33)
sage: for u, v in D.edges(labels=False):
....:     D.set_edge_label(u, v, randrange(100))
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_Boost')
CPU times: user 6.44 ms, sys: 517 µs, total: 6.96 ms
Wall time: 6.56 ms
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_SciPy')
CPU times: user 30.2 ms, sys: 1.85 ms, total: 32 ms
Wall time: 30.6 ms
```


```
sage: D = digraphs.RandomDirectedGNP(300, .33)
sage: for u, v in D.edges(labels=False):
....:     D.set_edge_label(u, v, randrange(100))
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_Boost')
CPU times: user 2.73 s, sys: 18.6 ms, total: 2.75 s
Wall time: 2.76 s
sage: %time _ = D.shortest_path_all_pairs(by_weight=True, algorithm='Floyd-Warshall_SciPy')
CPU times: user 1.95 s, sys: 61.6 ms, total: 2.01 s
Wall time: 2.13 s
```

----
New commits:



---

archive/issue_comments_065726.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-10-16T16:15:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65726",
    "user": "https://github.com/dcoudert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065727.json:
```json
{
    "body": "So scipy thinks of graphs as matrices, there no special format/backend?",
    "created_at": "2021-12-04T12:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65727",
    "user": "https://github.com/dimpase"
}
```

So scipy thinks of graphs as matrices, there no special format/backend?



---

archive/issue_comments_065728.json:
```json
{
    "body": "When you look at the code of scipy (for instance, https://github.com/scipy/scipy/blob/master/scipy/sparse/csgraph/_shortest_path.pyx), the input parameter is always\n\n```\n    csgraph : array, matrix, or sparse matrix, 2 dimensions\n        The N x N array of distances representing the input graph.\n```\n\nYou can also check method `validate_graph` in https://github.com/scipy/scipy/blob/master/scipy/sparse/csgraph/_validation.py. It may convert from one matrix format to another.",
    "created_at": "2021-12-04T12:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65728",
    "user": "https://github.com/dcoudert"
}
```

When you look at the code of scipy (for instance, https://github.com/scipy/scipy/blob/master/scipy/sparse/csgraph/_shortest_path.pyx), the input parameter is always

```
    csgraph : array, matrix, or sparse matrix, 2 dimensions
        The N x N array of distances representing the input graph.
```

You can also check method `validate_graph` in https://github.com/scipy/scipy/blob/master/scipy/sparse/csgraph/_validation.py. It may convert from one matrix format to another.



---

archive/issue_comments_065729.json:
```json
{
    "body": "So now the question is whether we finalize this ticket or move it to wontfix. Both options are OK for me.",
    "created_at": "2021-12-04T14:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65729",
    "user": "https://github.com/dcoudert"
}
```

So now the question is whether we finalize this ticket or move it to wontfix. Both options are OK for me.



---

archive/issue_comments_065730.json:
```json
{
    "body": "let us merge it",
    "created_at": "2021-12-04T14:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65730",
    "user": "https://github.com/dimpase"
}
```

let us merge it



---

archive/issue_comments_065731.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-12-04T15:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65731",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065732.json:
```json
{
    "body": "Thanks.",
    "created_at": "2021-12-04T15:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65732",
    "user": "https://github.com/dcoudert"
}
```

Thanks.



---

archive/issue_comments_065733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-12-12T15:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7676#issuecomment-65733",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
