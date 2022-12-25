# Issue 732: graphs: enum changes behavior depending on boundary vertices

archive/issues_000732.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graphs\n\nThe enum() function for graphs will change behavior depending on if the boundary is set and if 'quick' is passed.\n\n\n```\nsage: from sage.graphs.graph import enum\nsage: g=Graph({0:[1,2],1:[3]})\nsage: g.set_boundary([1])\nsage: enum(g)\n23112\nsage: enum(g,quick=True)\n27012\n```\n\n\nThis unexpected behavior happens because g.vertices() returns the boundary vertices first, I think.\n\nIssue created by migration from https://trac.sagemath.org/ticket/732\n\n",
    "created_at": "2007-09-21T19:03:06Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "graphs: enum changes behavior depending on boundary vertices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/732",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graphs

The enum() function for graphs will change behavior depending on if the boundary is set and if 'quick' is passed.


```
sage: from sage.graphs.graph import enum
sage: g=Graph({0:[1,2],1:[3]})
sage: g.set_boundary([1])
sage: enum(g)
23112
sage: enum(g,quick=True)
27012
```


This unexpected behavior happens because g.vertices() returns the boundary vertices first, I think.

Issue created by migration from https://trac.sagemath.org/ticket/732





---

archive/issue_comments_004284.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-13T16:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/732#issuecomment-4284",
    "user": "https://github.com/jasongrout"
}
```

Resolution: fixed



---

archive/issue_comments_004285.json:
```json
{
    "body": "This works now that vertices() sorts the vertices it returns (as of 2.8.6, I believe).",
    "created_at": "2007-10-13T16:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/732#issuecomment-4285",
    "user": "https://github.com/jasongrout"
}
```

This works now that vertices() sorts the vertices it returns (as of 2.8.6, I believe).
