# Issue 716: graph functions to_undirected and to_directed forget the loops and multiple edges

archive/issues_000716.json:
```json
{
    "body": "Assignee: was\n\nKeywords: graph, graphs\n\n\nWith a directed graph g\n* g.to_directed() forgets multiedges, remembers loops\n* g.to_undirected() forgets multiedges and loops\n\nWith an undirected graph g\n* g.to_directed() forgets multiedges and loops\n* g.to_undirected() forgets multiedges, remembers loops\n\n\nIn each of these cases, both multiedges and loops should be remembered.\n\n\n```\nsage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)\nsage: g.to_directed().multiple_arcs()\nFalse\nsage: g.to_directed().loops()\nTrue\nsage: g.to_undirected().multiple_edges()\nFalse\nsage: g.to_undirected().loops()\nFalse\nsage: g=Graph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)\nsage: g.to_directed().multiple_arcs()\nFalse\nsage: g.to_directed().loops()\nFalse\nsage: g.to_undirected().multiple_edges()\nFalse\nsage: g.to_undirected().loops()\nTrue\n```\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/716\n\n",
    "created_at": "2007-09-20T20:07:16Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "graph functions to_undirected and to_directed forget the loops and multiple edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/716",
    "user": "jason"
}
```
Assignee: was

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

archive/issue_comments_004157.json:
```json
{
    "body": "Apparently the copy doesn't preserve multiple edges settings.\n\n\n```\nsage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)\nsage: g==g.copy()\nFalse\nsage: g.multiple_arcs()\nTrue\nsage: g.copy().multiple_arcs()\nFalse\n```\n",
    "created_at": "2007-09-20T20:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4157",
    "user": "jason"
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

archive/issue_comments_004158.json:
```json
{
    "body": "The real problem is that the __init__ function tests for a superclass before a subclass.  The attached patch fixes it (and also adds a to_simple function that _does_ forget multiple edges, loops, and directions on edges).\n\nThe attached patch may break some of the doctests in graph.py, though.",
    "created_at": "2007-09-20T21:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4158",
    "user": "jason"
}
```

The real problem is that the __init__ function tests for a superclass before a subclass.  The attached patch fixes it (and also adds a to_simple function that _does_ forget multiple edges, loops, and directions on edges).

The attached patch may break some of the doctests in graph.py, though.



---

archive/issue_comments_004159.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-20T21:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4159",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_004160.json:
```json
{
    "body": "Attachment\n\nFixes doctest failures and other strangeness",
    "created_at": "2007-09-20T22:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4160",
    "user": "rlm"
}
```

Attachment

Fixes doctest failures and other strangeness



---

archive/issue_comments_004161.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-20T23:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4161",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_004162.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-21T00:12:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4162",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_004163.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-21T00:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4163",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_004164.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-09-21T02:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4164",
    "user": "rlm"
}
```

Resolution: worksforme



---

archive/issue_comments_004165.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-21T02:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4165",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_004166.json:
```json
{
    "body": "As a side note, the above patches which were applied also changed all \"arc\" functions to \"edge\" functions.  This, of course, broke backward compatibility.",
    "created_at": "2007-09-28T20:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4166",
    "user": "jason"
}
```

As a side note, the above patches which were applied also changed all "arc" functions to "edge" functions.  This, of course, broke backward compatibility.



---

archive/issue_comments_004167.json:
```json
{
    "body": "I am curious if all those patches really were applied. They are over a months old, so I would assume so, but I do not understand why this ticket wasn't closed then.\n\nMichael",
    "created_at": "2007-10-24T17:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4167",
    "user": "mabshoff"
}
```

I am curious if all those patches really were applied. They are over a months old, so I would assume so, but I do not understand why this ticket wasn't closed then.

Michael



---

archive/issue_comments_004168.json:
```json
{
    "body": "Resolution changed from worksforme to ",
    "created_at": "2007-10-24T19:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4168",
    "user": "mabshoff"
}
```

Resolution changed from worksforme to 



---

archive/issue_comments_004169.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-10-24T19:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4169",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_004170.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T19:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4170",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_004171.json:
```json
{
    "body": "From Robert:\n\n```\nMichael,\n\nRegarding ticket #716, these patches were incorporated a while ago,\nand I closed the ticket last month when that happened. It looks like\nthe ticket has been closed, but in a future milestone, ever since...\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-10-24T19:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/716#issuecomment-4171",
    "user": "mabshoff"
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
