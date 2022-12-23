# Issue 1941: Finish bipartite graph implementation

archive/issues_001941.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  brunellus @maxale tscrim\n\nSystematically go through the functions of graph and generic_graph and see which ones, such as add_vertex, need to be overridden in the bipartite graph class so that everything makes sense. Right now, you can add an edge so that the bipartite graph is no longer bipartite.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1941\n\n",
    "created_at": "2008-01-26T20:11:04Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Finish bipartite graph implementation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1941",
    "user": "rlm"
}
```
Assignee: rlm

CC:  brunellus @maxale tscrim

Systematically go through the functions of graph and generic_graph and see which ones, such as add_vertex, need to be overridden in the bipartite graph class so that everything makes sense. Right now, you can add an edge so that the bipartite graph is no longer bipartite.

Issue created by migration from https://trac.sagemath.org/ticket/1941





---

archive/issue_comments_012315.json:
```json
{
    "body": "\n```\n 1. add to __cmp__ to distinguish Bipartite from other graphs\n 2. loops - this should always be false for bipartite, right? (other functions with \"loops\" in the name)\n 3. density - should this reflect \"bipartite density\"?\n 4. add_vertex - to which side?\n 5. add_vertices - what to do with this?\n 6. clear - left & right too?\n 7. add left_vertices and right_vertices?\n 8. complement?\n 9. copy\n10. add_edge(s)\n11. adjacency_matrix - should this order the vertices a certain way?\n12. add_cycle\n13. add_path\n14. add a function \"bipartite_subgraph\" to preserve class?\n15. bipartite_color, bipartite_sets, is_bipartite\n```\n",
    "created_at": "2008-01-27T18:55:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12315",
    "user": "rlm"
}
```


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

archive/issue_comments_012316.json:
```json
{
    "body": "Also, the automorphism group/canonical label functions need to be called with the correct partitions.",
    "created_at": "2008-03-19T15:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12316",
    "user": "rlm"
}
```

Also, the automorphism group/canonical label functions need to be called with the correct partitions.



---

archive/issue_comments_012317.json:
```json
{
    "body": "see #8329",
    "created_at": "2010-02-23T01:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12317",
    "user": "rlm"
}
```

see #8329



---

archive/issue_comments_012318.json:
```json
{
    "body": "see also #8330",
    "created_at": "2010-02-23T01:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12318",
    "user": "rlm"
}
```

see also #8330



---

archive/issue_comments_012319.json:
```json
{
    "body": "#8331 is also relevant.",
    "created_at": "2010-02-23T01:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12319",
    "user": "rlm"
}
```

#8331 is also relevant.



---

archive/issue_comments_012320.json:
```json
{
    "body": "And another #8350.",
    "created_at": "2010-02-24T18:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12320",
    "user": "rhinton"
}
```

And another #8350.



---

archive/issue_comments_012321.json:
```json
{
    "body": "Also #8425.",
    "created_at": "2010-03-04T22:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12321",
    "user": "rhinton"
}
```

Also #8425.



---

archive/issue_comments_012322.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2022-01-31T10:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12322",
    "user": "dcoudert"
}
```

Changing type from defect to task.



---

archive/issue_comments_012323.json:
```json
{
    "body": "Gathering tickets related to `BipartiteGraph`, open and fixed issues.",
    "created_at": "2022-01-31T10:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12323",
    "user": "dcoudert"
}
```

Gathering tickets related to `BipartiteGraph`, open and fixed issues.



---

archive/issue_comments_012324.json:
```json
{
    "body": "Proposal from [#33261#comment:3](https://trac.sagemath.org/ticket/33261#comment:3)\n> Side note: The complete bipartite graph constructor should return a `BipartiteGraph` object IMO (instead of just a usual `Graph`).\n\nI tried (for complete, random and random regular bipartite graphs) and it's not an easy task:\n- the `__repr__` method of `BipartiteGraph` modifies the name string and so we have to correct several doctests\n- algorithms modifying a graph with the addition of vertices fail since the side is not given. We must either implement specific versions for `BipartiteGraph` or modify these algorithms to work properly with `BipartiteGraph`.\nSo it's not so easy to do",
    "created_at": "2022-02-02T17:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12324",
    "user": "dcoudert"
}
```

Proposal from [#33261#comment:3](https://trac.sagemath.org/ticket/33261#comment:3)
> Side note: The complete bipartite graph constructor should return a `BipartiteGraph` object IMO (instead of just a usual `Graph`).

I tried (for complete, random and random regular bipartite graphs) and it's not an easy task:
- the `__repr__` method of `BipartiteGraph` modifies the name string and so we have to correct several doctests
- algorithms modifying a graph with the addition of vertices fail since the side is not given. We must either implement specific versions for `BipartiteGraph` or modify these algorithms to work properly with `BipartiteGraph`.
So it's not so easy to do



---

archive/issue_comments_012325.json:
```json
{
    "body": "Replying to [comment:19 dcoudert]:\n> Proposal from [#33261#comment:3](https://trac.sagemath.org/ticket/33261#comment:3)\n> > Side note: The complete bipartite graph constructor should return a `BipartiteGraph` object IMO (instead of just a usual `Graph`).\n> \n> I tried (for complete, random and random regular bipartite graphs) and it's not an easy task:\n\nThank you for attempting it.\n\n> - the `__repr__` method of `BipartiteGraph` modifies the name string and so we have to correct several doctests\n\nThis is minor IMO (although it might be good for the two to be consistent); just annoying to do.\n\n> - algorithms modifying a graph with the addition of vertices fail since the side is not given. We must either implement specific versions for `BipartiteGraph` or modify these algorithms to work properly with `BipartiteGraph`.\n\nThis suggests that there is a compatibility issue between the two classes, which is a bug IMO since `BipartiteGraph` is a subclass of `Graph`. We probably need to modify `add_vertex` and `add_edge` to be compatible, such as returning a generic graph. Mainly, I am not sure I agree with the behavior of raising an error when the edge does not give a bipartite graph like in #8744 (although without such a complicated thing of recoloring the bipartite graph).\n\nEssentially, IMO subclasses should behave like the base class but with extra features that utilize the special aspects (sometimes known as the [\"is-a\" test](https://en.wikipedia.org/wiki/Is-a)).",
    "created_at": "2022-02-03T01:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12325",
    "user": "tscrim"
}
```

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

archive/issue_comments_012326.json:
```json
{
    "body": "`BipartiteGraph` adds restrictions to `Graph` and the price to pay is to maintain the partition. When using a `BipartiteGraph`, some operations may be forbidden (edge contraction, etc.) or done with care (`add_vertex`, `add_path`, etc.). Otherwise, the user has to move back to `Graph`.",
    "created_at": "2022-02-03T13:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12326",
    "user": "dcoudert"
}
```

`BipartiteGraph` adds restrictions to `Graph` and the price to pay is to maintain the partition. When using a `BipartiteGraph`, some operations may be forbidden (edge contraction, etc.) or done with care (`add_vertex`, `add_path`, etc.). Otherwise, the user has to move back to `Graph`.



---

archive/issue_comments_012327.json:
```json
{
    "body": "Then it should not be a subclass IMO because of a fundamental incompatibility with some common ABC between `BipartiteGraph` and `Graph` to explicitly prohibit said methods.",
    "created_at": "2022-02-04T01:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1941#issuecomment-12327",
    "user": "tscrim"
}
```

Then it should not be a subclass IMO because of a fundamental incompatibility with some common ABC between `BipartiteGraph` and `Graph` to explicitly prohibit said methods.
