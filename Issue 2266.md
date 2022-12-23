# Issue 2266: give shortest_paths an optional endpoint

archive/issues_002266.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  jason mvngu brunellus\n\nImplement an optional input, `v=None` to the function `shortest_paths`, which would then only return the shortest paths from `u` to `v`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2266\n\n",
    "created_at": "2008-02-22T21:27:54Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "title": "give shortest_paths an optional endpoint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2266",
    "user": "rlm"
}
```
Assignee: rlm

CC:  jason mvngu brunellus

Implement an optional input, `v=None` to the function `shortest_paths`, which would then only return the shortest paths from `u` to `v`.

Issue created by migration from https://trac.sagemath.org/ticket/2266





---

archive/issue_comments_015012.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2266#issuecomment-15012",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015013.json:
```json
{
    "body": "CC'ing myself.",
    "created_at": "2009-06-27T00:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2266#issuecomment-15013",
    "user": "mvngu"
}
```

CC'ing myself.



---

archive/issue_comments_015014.json:
```json
{
    "body": "I don't think we need to update `shortest_paths` as there already exists a method `shortest_path` which takes input `u` and `v` and outputs the single shortest path between them.",
    "created_at": "2020-01-30T11:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2266#issuecomment-15014",
    "user": "@akshat1136"
}
```

I don't think we need to update `shortest_paths` as there already exists a method `shortest_path` which takes input `u` and `v` and outputs the single shortest path between them.



---

archive/issue_comments_015015.json:
```json
{
    "body": "If the question is to get all shortest paths from u to v, then:\n- For unweighted graphs, we have `all_paths_iterator` and `all_simple_paths` that list paths by increasing length and that accept as input an optional list of starting / ending nodes.\n- For weighted graphs without negative edge weights, we have `shortest_simple_paths` that yields shortest simple paths from u to v by increasing weights. Non-simple paths should be treated in #28076.\n- For graphs with negative weight cycles, the problem of finding a path in NP-hard. We can use ILP. We can do better if we have negative weight edges but no negative weight cycles.",
    "created_at": "2022-05-01T08:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2266#issuecomment-15015",
    "user": "dcoudert"
}
```

If the question is to get all shortest paths from u to v, then:
- For unweighted graphs, we have `all_paths_iterator` and `all_simple_paths` that list paths by increasing length and that accept as input an optional list of starting / ending nodes.
- For weighted graphs without negative edge weights, we have `shortest_simple_paths` that yields shortest simple paths from u to v by increasing weights. Non-simple paths should be treated in #28076.
- For graphs with negative weight cycles, the problem of finding a path in NP-hard. We can use ILP. We can do better if we have negative weight edges but no negative weight cycles.
