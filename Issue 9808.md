# Issue 9808: Graph.num_edges() gives wrong answer

archive/issues_009808.json:
```json
{
    "body": "Assignee: someone\n\nKeywords: num_edges,multiedges\n\nIf G is a graph with multiedges that contains two copies of an edge e, and you delete one of the copies, num_edges() doesn't go down by one.  For example,\n\n```\nsage: G = Graph(multiedges = True)\nsage: G.add_edges([(0,1), (0,1)])\nsage: G.delete_edge(0,1)\nsage: G.num_edges()\n2\nsage: G.edges()\n[(0, 1, None)]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9809\n\n",
    "created_at": "2010-08-26T20:32:56Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Graph.num_edges() gives wrong answer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9808",
    "user": "tobiasljohnson"
}
```
Assignee: someone

Keywords: num_edges,multiedges

If G is a graph with multiedges that contains two copies of an edge e, and you delete one of the copies, num_edges() doesn't go down by one.  For example,

```
sage: G = Graph(multiedges = True)
sage: G.add_edges([(0,1), (0,1)])
sage: G.delete_edge(0,1)
sage: G.num_edges()
2
sage: G.edges()
[(0, 1, None)]
```



Issue created by migration from https://trac.sagemath.org/ticket/9809





---

archive/issue_comments_096733.json:
```json
{
    "body": "Changing assignee from someone to somebody.",
    "created_at": "2010-08-26T20:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9808#issuecomment-96733",
    "user": "tobiasljohnson"
}
```

Changing assignee from someone to somebody.



---

archive/issue_comments_096734.json:
```json
{
    "body": "The problem is fixed at #8395.",
    "created_at": "2010-12-04T13:07:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9808#issuecomment-96734",
    "user": "mvngu"
}
```

The problem is fixed at #8395.



---

archive/issue_comments_096735.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-12-05T11:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9808#issuecomment-96735",
    "user": "jdemeyer"
}
```

Resolution: duplicate
