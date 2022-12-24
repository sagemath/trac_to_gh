# Issue 7540: Speed up shortest_path_all_pairs() and update distance_graph

archive/issues_007540.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rbeezer\n\nAs mentionned in #7533 by Rob Beezer, the function shortest_path_all_pairs() is much slower than computing independently all the distances, which is a bit worrying. Easy explanation ( at least it is an explanation for me, though there may be a deeper one ), distance() is a function from NetworkX while the Floyd-Marshall algorithm is directly written in Python, hence the slowness.\n\nThis function is very fundamental and should be improved ! The difference is amazing :\n\n\n```\nsage: g=graphs.RandomGNP(200,.1)\nsage: time e=g.shortest_path_all_pairs()\nCPU times: user 16.51 s, sys: 0.06 s, total: 16.57 s\nWall time: 16.60 s\nsage: time a=[g.distance(i,j) for (i,j) in Subsets(g,2)]\nCPU times: user 1.06 s, sys: 0.00 s, total: 1.06 s\nWall time: 1.06 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7540\n\n",
    "created_at": "2009-11-27T12:16:45Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Speed up shortest_path_all_pairs() and update distance_graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7540",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  rbeezer

As mentionned in #7533 by Rob Beezer, the function shortest_path_all_pairs() is much slower than computing independently all the distances, which is a bit worrying. Easy explanation ( at least it is an explanation for me, though there may be a deeper one ), distance() is a function from NetworkX while the Floyd-Marshall algorithm is directly written in Python, hence the slowness.

This function is very fundamental and should be improved ! The difference is amazing :


```
sage: g=graphs.RandomGNP(200,.1)
sage: time e=g.shortest_path_all_pairs()
CPU times: user 16.51 s, sys: 0.06 s, total: 16.57 s
Wall time: 16.60 s
sage: time a=[g.distance(i,j) for (i,j) in Subsets(g,2)]
CPU times: user 1.06 s, sys: 0.00 s, total: 1.06 s
Wall time: 1.06 s
```


Issue created by migration from https://trac.sagemath.org/ticket/7540





---

archive/issue_comments_063988.json:
```json
{
    "body": "then... use networkx. More precisely,\n`networkx.all_pairs_shortest_path` and `networkx.all_pairs_shortest_path_length`.\n\nThey are not based on Floyd-Marshall (it is also in networkx but way slower)",
    "created_at": "2009-11-27T14:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7540#issuecomment-63988",
    "user": "ylchapuy"
}
```

then... use networkx. More precisely,
`networkx.all_pairs_shortest_path` and `networkx.all_pairs_shortest_path_length`.

They are not based on Floyd-Marshall (it is also in networkx but way slower)



---

archive/issue_comments_063989.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T06:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7540#issuecomment-63989",
    "user": "ncohen"
}
```

Resolution: duplicate



---

archive/issue_comments_063990.json:
```json
{
    "body": "Done in #7966",
    "created_at": "2010-01-19T06:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7540#issuecomment-63990",
    "user": "ncohen"
}
```

Done in #7966
