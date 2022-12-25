# Issue 5248: edge_colors does not work on loops

archive/issues_005248.json:
```json
{
    "body": "Assignee: @rlmill\n\nKeywords: graphs\n\nThe following example illustrates the problem.  Loops are treated seperately, and not correctly colored (they are always black).\n\n\n```\ng = graphs.CompleteGraph(3)\ng.loops(True)\ng.add_edge(0,0)\nc_dict = {\"red\":[(0,0)], \"blue\":[(0,1),(1,2),(0,2)]}\nshow(g.plot(edge_colors = c_dict))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5248\n\n",
    "created_at": "2009-02-12T16:53:34Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "edge_colors does not work on loops",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @rlmill

Keywords: graphs

The following example illustrates the problem.  Loops are treated seperately, and not correctly colored (they are always black).


```
g = graphs.CompleteGraph(3)
g.loops(True)
g.add_edge(0,0)
c_dict = {"red":[(0,0)], "blue":[(0,1),(1,2),(0,2)]}
show(g.plot(edge_colors = c_dict))
```


Issue created by migration from https://trac.sagemath.org/ticket/5248





---

archive/issue_comments_040145.json:
```json
{
    "body": "Ticket #3541 is going to contain an overhaul of the graph plotting code. Since I'm refereeing, I'll make sure that this is fixed in that patch.",
    "created_at": "2009-02-12T17:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5248#issuecomment-40145",
    "user": "https://github.com/rlmill"
}
```

Ticket #3541 is going to contain an overhaul of the graph plotting code. Since I'm refereeing, I'll make sure that this is fixed in that patch.



---

archive/issue_comments_040146.json:
```json
{
    "body": "This ticket will be fixed by #3541, so let's move it to 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5248#issuecomment-40146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket will be fixed by #3541, so let's move it to 3.3.

Cheers,

Michael



---

archive/issue_comments_040147.json:
```json
{
    "body": "This is now fixed by #3541.  Cheers.",
    "created_at": "2009-02-14T03:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5248#issuecomment-40147",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

This is now fixed by #3541.  Cheers.



---

archive/issue_events_005504.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/ekirkman",
    "created_at": "2009-02-14T03:48:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5248#event-5504"
}
```



---

archive/issue_comments_040148.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-02-14T03:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5248#issuecomment-40148",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Resolution: duplicate
