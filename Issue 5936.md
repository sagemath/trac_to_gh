# Issue 5936: result of graph query should be iterable -- make more pythonic

archive/issues_005936.json:
```json
{
    "body": "Assignee: @rlmill\n\nCurrently we have this:\n\n```\nsage: Q = GraphQuery(\n       display_cols=['graph6','num_vertices','degree_sequence'],\n       num_edges=['<=',5],min_degree=1)\nsage: for G in Q: print G\n```\n\noutputs\n\n```\nTraceback (click to the left for traceback)\n...\nTypeError: 'GraphQuery' object is not iterable\n```\n\n\nWhy not have it Q.__iter__() return an iterator over `Q.get_graphs_list()`, which would easily work?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5936\n\n",
    "created_at": "2009-04-29T15:59:37Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "result of graph query should be iterable -- make more pythonic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5936",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

Currently we have this:

```
sage: Q = GraphQuery(
       display_cols=['graph6','num_vertices','degree_sequence'],
       num_edges=['<=',5],min_degree=1)
sage: for G in Q: print G
```

outputs

```
Traceback (click to the left for traceback)
...
TypeError: 'GraphQuery' object is not iterable
```


Why not have it Q.__iter__() return an iterator over `Q.get_graphs_list()`, which would easily work?


Issue created by migration from https://trac.sagemath.org/ticket/5936





---

archive/issue_comments_046844.json:
```json
{
    "body": "Patch covers docstring updates (see #5935) and adds an iterator for GraphQuery.",
    "created_at": "2009-05-21T22:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5936#issuecomment-46844",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Patch covers docstring updates (see #5935) and adds an iterator for GraphQuery.



---

archive/issue_comments_046845.json:
```json
{
    "body": "Attachment [trac5936_graphdatabase.patch](tarball://root/attachments/some-uuid/ticket5936/trac5936_graphdatabase.patch) by @rlmill created at 2009-05-21 22:27:00\n\nReferee edit of Emily's patch",
    "created_at": "2009-05-21T22:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5936#issuecomment-46845",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac5936_graphdatabase.patch](tarball://root/attachments/some-uuid/ticket5936/trac5936_graphdatabase.patch) by @rlmill created at 2009-05-21 22:27:00

Referee edit of Emily's patch



---

archive/issue_events_013911.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-01T04:57:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5936",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5936#event-13911"
}
```



---

archive/issue_comments_046846.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T04:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5936#issuecomment-46846",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_046847.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T04:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5936",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5936#issuecomment-46847",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
