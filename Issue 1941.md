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
