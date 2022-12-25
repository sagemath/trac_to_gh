# Issue 716: graph functions to_undirected and to_directed forget the loops and multiple edges

archive/issues_000716.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graph, graphs\n\n\nWith a directed graph g\n* g.to_directed() forgets multiedges, remembers loops\n* g.to_undirected() forgets multiedges and loops\n\nWith an undirected graph g\n* g.to_directed() forgets multiedges and loops\n* g.to_undirected() forgets multiedges, remembers loops\n\n\nIn each of these cases, both multiedges and loops should be remembered.\n\n```\nsage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)\nsage: g.to_directed().multiple_arcs()\nFalse\nsage: g.to_directed().loops()\nTrue\nsage: g.to_undirected().multiple_edges()\nFalse\nsage: g.to_undirected().loops()\nFalse\nsage: g=Graph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)\nsage: g.to_directed().multiple_arcs()\nFalse\nsage: g.to_directed().loops()\nFalse\nsage: g.to_undirected().multiple_edges()\nFalse\nsage: g.to_undirected().loops()\nTrue\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/716\n\n",
    "created_at": "2007-09-20T20:07:16Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "graph functions to_undirected and to_directed forget the loops and multiple edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/716",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graph, graphs


With a directed graph g
* g.to_directed() forgets multiedges, remembers loops
* g.to_undirected() forgets multiedges and loops

With an undirected graph g
* g.to_directed() forgets multiedges and loops
* g.to_undirected() forgets multiedges, remembers loops


In each of these cases, both multiedges and loops should be remembered.

```
sage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)
sage: g.to_directed().multiple_arcs()
False
sage: g.to_directed().loops()
True
sage: g.to_undirected().multiple_edges()
False
sage: g.to_undirected().loops()
False
sage: g=Graph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)
sage: g.to_directed().multiple_arcs()
False
sage: g.to_directed().loops()
False
sage: g.to_undirected().multiple_edges()
False
sage: g.to_undirected().loops()
True
```




Issue created by migration from https://trac.sagemath.org/ticket/716





---

archive/issue_comments_004144.json:
```json
{
    "body": "Apparently the copy doesn't preserve multiple edges settings.\n\n```\nsage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)\nsage: g==g.copy()\nFalse\nsage: g.multiple_arcs()\nTrue\nsage: g.copy().multiple_arcs()\nFalse\n```",
    "created_at": "2007-09-20T20:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4144",
    "user": "https://github.com/jasongrout"
}
```

Apparently the copy doesn't preserve multiple edges settings.

```
sage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)
sage: g==g.copy()
False
sage: g.multiple_arcs()
True
sage: g.copy().multiple_arcs()
False
```



---

archive/issue_comments_004145.json:
```json
{
    "body": "The real problem is that the __init__ function tests for a superclass before a subclass.  The attached patch fixes it (and also adds a to_simple function that _does_ forget multiple edges, loops, and directions on edges).\n\nThe attached patch may break some of the doctests in graph.py, though.",
    "created_at": "2007-09-20T21:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4145",
    "user": "https://github.com/jasongrout"
}
```

The real problem is that the __init__ function tests for a superclass before a subclass.  The attached patch fixes it (and also adds a to_simple function that _does_ forget multiple edges, loops, and directions on edges).

The attached patch may break some of the doctests in graph.py, though.



---

archive/issue_comments_004146.json:
```json
{
    "body": "Attachment [init_and_to_simple.hg](tarball://root/attachments/some-uuid/ticket716/init_and_to_simple.hg) by @jasongrout created at 2007-09-20 21:29:46",
    "created_at": "2007-09-20T21:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4146",
    "user": "https://github.com/jasongrout"
}
```

Attachment [init_and_to_simple.hg](tarball://root/attachments/some-uuid/ticket716/init_and_to_simple.hg) by @jasongrout created at 2007-09-20 21:29:46



---

archive/issue_comments_004147.json:
```json
{
    "body": "Attachment [deep_copy.hg](tarball://root/attachments/some-uuid/ticket716/deep_copy.hg) by @rlmill created at 2007-09-20 22:49:31\n\nFixes doctest failures and other strangeness",
    "created_at": "2007-09-20T22:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4147",
    "user": "https://github.com/rlmill"
}
```

Attachment [deep_copy.hg](tarball://root/attachments/some-uuid/ticket716/deep_copy.hg) by @rlmill created at 2007-09-20 22:49:31

Fixes doctest failures and other strangeness



---

archive/issue_comments_004148.json:
```json
{
    "body": "Attachment [doc_changes.hg](tarball://root/attachments/some-uuid/ticket716/doc_changes.hg) by @jasongrout created at 2007-09-20 23:54:09",
    "created_at": "2007-09-20T23:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4148",
    "user": "https://github.com/jasongrout"
}
```

Attachment [doc_changes.hg](tarball://root/attachments/some-uuid/ticket716/doc_changes.hg) by @jasongrout created at 2007-09-20 23:54:09



---

archive/issue_comments_004149.json:
```json
{
    "body": "Attachment [arc_edges.hg](tarball://root/attachments/some-uuid/ticket716/arc_edges.hg) by @rlmill created at 2007-09-21 00:12:56",
    "created_at": "2007-09-21T00:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4149",
    "user": "https://github.com/rlmill"
}
```

Attachment [arc_edges.hg](tarball://root/attachments/some-uuid/ticket716/arc_edges.hg) by @rlmill created at 2007-09-21 00:12:56



---

archive/issue_comments_004150.json:
```json
{
    "body": "Attachment [change_arc_to_edge.hg](tarball://root/attachments/some-uuid/ticket716/change_arc_to_edge.hg) by @jasongrout created at 2007-09-21 00:37:37",
    "created_at": "2007-09-21T00:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4150",
    "user": "https://github.com/jasongrout"
}
```

Attachment [change_arc_to_edge.hg](tarball://root/attachments/some-uuid/ticket716/change_arc_to_edge.hg) by @jasongrout created at 2007-09-21 00:37:37



---

archive/issue_events_001926.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-09-21T02:06:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/716#event-1926"
}
```



---

archive/issue_comments_004151.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-09-21T02:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4151",
    "user": "https://github.com/rlmill"
}
```

Resolution: worksforme



---

archive/issue_comments_004152.json:
```json
{
    "body": "Attachment [combinat-arcs2edges.patch](tarball://root/attachments/some-uuid/ticket716/combinat-arcs2edges.patch) by @rlmill created at 2007-09-21 02:06:07",
    "created_at": "2007-09-21T02:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4152",
    "user": "https://github.com/rlmill"
}
```

Attachment [combinat-arcs2edges.patch](tarball://root/attachments/some-uuid/ticket716/combinat-arcs2edges.patch) by @rlmill created at 2007-09-21 02:06:07



---

archive/issue_comments_004153.json:
```json
{
    "body": "As a side note, the above patches which were applied also changed all \"arc\" functions to \"edge\" functions.  This, of course, broke backward compatibility.",
    "created_at": "2007-09-28T20:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4153",
    "user": "https://github.com/jasongrout"
}
```

As a side note, the above patches which were applied also changed all "arc" functions to "edge" functions.  This, of course, broke backward compatibility.



---

archive/issue_comments_004154.json:
```json
{
    "body": "I am curious if all those patches really were applied. They are over a months old, so I would assume so, but I do not understand why this ticket wasn't closed then.\n\nMichael",
    "created_at": "2007-10-24T17:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am curious if all those patches really were applied. They are over a months old, so I would assume so, but I do not understand why this ticket wasn't closed then.

Michael



---

archive/issue_events_001927.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T17:29:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/716#event-1927"
}
```



---

archive/issue_comments_004155.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2007-10-24T19:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_004156.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-24T19:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001928.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T19:04:22Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/716#event-1928"
}
```



---

archive/issue_comments_004157.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T19:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001929.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T19:04:31Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/716#event-1929"
}
```



---

archive/issue_events_001930.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T19:04:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/716#event-1930"
}
```



---

archive/issue_events_001931.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-24T19:04:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/716#event-1931"
}
```



---

archive/issue_comments_004158.json:
```json
{
    "body": "From Robert:\n\n```\nMichael,\n\nRegarding ticket #716, these patches were incorporated a while ago,\nand I closed the ticket last month when that happened. It looks like\nthe ticket has been closed, but in a future milestone, ever since...\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-10-24T19:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4158",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

From Robert:

```
Michael,

Regarding ticket #716, these patches were incorporated a while ago,
and I closed the ticket last month when that happened. It looks like
the ticket has been closed, but in a future milestone, ever since...
```

Cheers,

Michael
