# Issue 1306: [with patch, positive review] Bundles of graphs

archive/issues_001306.json:
```json
{
    "body": "Assignee: @rlmill\n\nFrom Chris Godsil's wishlist (reply by Jason Grout, second reply by Robert Miller)\n\n```\n>>> (e) Bundles: Start with a base graph G with vertices {1, . . . , n}.\n>>> For each\n>>> vertex i we are given a graph Ci . For each edge ij we are given a\n>>> bipartite\n>>> graph joining V (Ci ) to V (Cj ). (There is an implicit orientation here.)\n>>> Some examples:\n>>> (i) The Petersen graph: n = 2, C1 is the 5-cycle, C2 is its complement\n>>> and the bipartite graph is a 5-matching.\n>>> (ii) The Hoffman-Singleton graph can be constructed with n = 2, where\n>>> C1 is an independent set on 15 vertices, C2 is a nice distance regular\n>>> graph on 35 vertices,. . .\n>>> (iii) Covering graphs. Here the graphs Ci are empty on r vertices, and\n>>> each bipartite graphs is either an r-matching or is empty.\n>> Huh, I used this idea extensively in my dissertation and a research\n>> paper. I used the \"blowup graph\" terminology, though, from extremal\n>> graph theory. Is anyone working on this? If not, I'll make a trac ticket.\n> Nobody I know of. If you did this type of stuff in your dissertation,\n> then I nominate you! Create a ticket.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1306\n\n",
    "closed_at": "2008-01-21T04:06:16Z",
    "created_at": "2007-11-28T19:53:26Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, positive review] Bundles of graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1306",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

From Chris Godsil's wishlist (reply by Jason Grout, second reply by Robert Miller)

```
>>> (e) Bundles: Start with a base graph G with vertices {1, . . . , n}.
>>> For each
>>> vertex i we are given a graph Ci . For each edge ij we are given a
>>> bipartite
>>> graph joining V (Ci ) to V (Cj ). (There is an implicit orientation here.)
>>> Some examples:
>>> (i) The Petersen graph: n = 2, C1 is the 5-cycle, C2 is its complement
>>> and the bipartite graph is a 5-matching.
>>> (ii) The Hoffman-Singleton graph can be constructed with n = 2, where
>>> C1 is an independent set on 15 vertices, C2 is a nice distance regular
>>> graph on 35 vertices,. . .
>>> (iii) Covering graphs. Here the graphs Ci are empty on r vertices, and
>>> each bipartite graphs is either an r-matching or is empty.
>> Huh, I used this idea extensively in my dissertation and a research
>> paper. I used the "blowup graph" terminology, though, from extremal
>> graph theory. Is anyone working on this? If not, I'll make a trac ticket.
> Nobody I know of. If you did this type of stuff in your dissertation,
> then I nominate you! Create a ticket.
```

Issue created by migration from https://trac.sagemath.org/ticket/1306





---

archive/issue_comments_008190.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8190",
    "user": "https://github.com/rlmill"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008191.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"\".",
    "created_at": "2007-12-17T15:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8191",
    "user": "https://github.com/rlmill"
}
```

Changing keywords from "graphs" to "".



---

archive/issue_comments_008192.json:
```json
{
    "body": "Changing assignee from @mwhansen to @rlmill.",
    "created_at": "2007-12-17T15:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8192",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @mwhansen to @rlmill.



---

archive/issue_comments_008193.json:
```json
{
    "body": "Attachment [graph_bundles.patch](tarball://root/attachments/some-uuid/ticket1306/graph_bundles.patch) by @rlmill created at 2008-01-21 03:56:29",
    "created_at": "2008-01-21T03:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8193",
    "user": "https://github.com/rlmill"
}
```

Attachment [graph_bundles.patch](tarball://root/attachments/some-uuid/ticket1306/graph_bundles.patch) by @rlmill created at 2008-01-21 03:56:29



---

archive/issue_comments_008194.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-21T03:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8194",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008195.json:
```json
{
    "body": "Depends on #1874.",
    "created_at": "2008-01-21T03:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8195",
    "user": "https://github.com/rlmill"
}
```

Depends on #1874.



---

archive/issue_comments_008196.json:
```json
{
    "body": "Applies and passes for me after 1874.",
    "created_at": "2008-01-21T04:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8196",
    "user": "https://github.com/mwhansen"
}
```

Applies and passes for me after 1874.



---

archive/issue_comments_008197.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T04:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8197",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_events_003416.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T04:06:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1306#event-3416"
}
```



---

archive/issue_comments_008198.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1306#issuecomment-8198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003417.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-01-21T18:20:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1306",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1306#event-3417"
}
```
