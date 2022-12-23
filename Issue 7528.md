# Issue 7528: Orientation of a graph with bounded out-degree

archive/issues_007528.json:
```json
{
    "body": "Assignee: rlm\n\nGiven an undirected graph and an integer k, it is possible to find through the flow algorithm an orientation of it such that any vertex has an out-degree of at most k ( or say that this is impossible )\n\nIssue created by migration from https://trac.sagemath.org/ticket/7528\n\n",
    "created_at": "2009-11-25T09:56:20Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Orientation of a graph with bounded out-degree",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7528",
    "user": "ncohen"
}
```
Assignee: rlm

Given an undirected graph and an integer k, it is possible to find through the flow algorithm an orientation of it such that any vertex has an out-degree of at most k ( or say that this is impossible )

Issue created by migration from https://trac.sagemath.org/ticket/7528





---

archive/issue_comments_063811.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-05T14:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63811",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063812.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-15T17:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63812",
    "user": "rlm"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_063813.json:
```json
{
    "body": "I'm ready to give this a positive review, except there is a conflict:\n\n\n```\nGiven a complete bipartite graph `K_{n,m}`, the minimum  \noutdegree of an orientation is  \n`\\left\\lceil \\frac {nm} {n+m}\\right\\rceil`:: \n\nsage: g = graphs.CompleteBipartiteGraph(3,4) \nsage: o = g.minimum_outdegree_orientation() # optional - requires GLPK or CBC \nsage: max(o.out_degree()) == ceil((4*3)/(3+4)) # optional - requires GLPK or CBC \nTrue\n```\n\n\nShould \"the minimum outdegree\" be \"the smallest possible maximum outdegree\", or something similar?",
    "created_at": "2009-12-15T17:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63813",
    "user": "rlm"
}
```

I'm ready to give this a positive review, except there is a conflict:


```
Given a complete bipartite graph `K_{n,m}`, the minimum  
outdegree of an orientation is  
`\left\lceil \frac {nm} {n+m}\right\rceil`:: 

sage: g = graphs.CompleteBipartiteGraph(3,4) 
sage: o = g.minimum_outdegree_orientation() # optional - requires GLPK or CBC 
sage: max(o.out_degree()) == ceil((4*3)/(3+4)) # optional - requires GLPK or CBC 
True
```


Should "the minimum outdegree" be "the smallest possible maximum outdegree", or something similar?



---

archive/issue_comments_063814.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-16T01:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63814",
    "user": "ncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063815.json:
```json
{
    "body": "Attachment\n\nIndeed ! ( corrected )",
    "created_at": "2009-12-16T01:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63815",
    "user": "ncohen"
}
```

Attachment

Indeed ! ( corrected )



---

archive/issue_comments_063816.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T03:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63816",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063817.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T21:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7528#issuecomment-63817",
    "user": "mhansen"
}
```

Resolution: fixed
