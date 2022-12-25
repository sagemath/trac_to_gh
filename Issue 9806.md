# Issue 9806: merge_vertices behavior in a graph with loops

archive/issues_009806.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  brunellus\n\nKeywords: merge_vertices, loops\n\nSuppose G is a graph with loops permitted containing the edge (0, 1).  I would expect that G.merge_vertices([0, 1]) would create a loop (0, 0), but it doesn't:\n\n```\nsage: G = Graph(loops = True)\nsage: G.add_edge(0, 1)\nsage: G.merge_vertices([0, 1])\nsage: G.edges()\n[]\n```\n\nI think either we should change this, or we should write explicitly in the documentation that merge_vertices doesn't create self-loops even when G allows them.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9807\n\n",
    "created_at": "2010-08-26T18:41:52Z",
    "labels": [
        "component: graph theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "merge_vertices behavior in a graph with loops",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9806",
    "user": "https://trac.sagemath.org/admin/accounts/users/tobiasljohnson"
}
```
Assignee: jason, ncohen, rlm

CC:  brunellus

Keywords: merge_vertices, loops

Suppose G is a graph with loops permitted containing the edge (0, 1).  I would expect that G.merge_vertices([0, 1]) would create a loop (0, 0), but it doesn't:

```
sage: G = Graph(loops = True)
sage: G.add_edge(0, 1)
sage: G.merge_vertices([0, 1])
sage: G.edges()
[]
```

I think either we should change this, or we should write explicitly in the documentation that merge_vertices doesn't create self-loops even when G allows them.



Issue created by migration from https://trac.sagemath.org/ticket/9807





---

archive/issue_comments_096260.json:
```json
{
    "body": "See #7304.",
    "created_at": "2012-01-31T14:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9806",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9806#issuecomment-96260",
    "user": "https://trac.sagemath.org/admin/accounts/users/brunellus"
}
```

See #7304.
