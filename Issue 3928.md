# Issue 3928: multiedge graphs create an edge for each character of a label

archive/issues_003928.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\nSay, I want to define a multigraph with selfloops, and edge labels..\nOne way to do this is:\n\nimport networkx\nG=networkx.XDiGraph(selfloops=True,multiedges=True)\nfor i in range(3): G.add_node(i)\nfor i in [(1,1,'hola'),(1,1,'hi'),(1,2,'two'),(1,2,'dos'),\n(2,1,'one')]: G.add_edge(i)\nG=DiGraph(G)\n\nNow, I would be tempted to just do the following:\nG=DiGraph({1:{1:'hola',1:'hi',2:'two',2:'dos'},2:{1:'one'}},\nloops=True, multiedges=True)\n\nor trying\n\nimport networkx\nG=networkx.XDiGraph({1:{1:'hola',1:'hi',2:'two',2:'dos'},2:{1:'one'}},\nselfloops=True, multiedges=True)\n\nBut in each case  I get:\n\nG.edges()\n\n(1, 1, 'h'), (1, 1, 'i'), (1, 2, 'd'), (1, 2, 'o'), (1, 2, 's'), (2,\n1,\n'o'), (2, 1, 'n'), (2, 1, 'e')]\n\n\nWhich is not as intended for two reasons:  One is that the labels are\nwrong, and the other one is that it created three edges from 1 to 2.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3928\n\n",
    "created_at": "2008-08-22T17:58:49Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "multiedge graphs create an edge for each character of a label",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3928",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

```
Say, I want to define a multigraph with selfloops, and edge labels..
One way to do this is:

import networkx
G=networkx.XDiGraph(selfloops=True,multiedges=True)
for i in range(3): G.add_node(i)
for i in [(1,1,'hola'),(1,1,'hi'),(1,2,'two'),(1,2,'dos'),
(2,1,'one')]: G.add_edge(i)
G=DiGraph(G)

Now, I would be tempted to just do the following:
G=DiGraph({1:{1:'hola',1:'hi',2:'two',2:'dos'},2:{1:'one'}},
loops=True, multiedges=True)

or trying

import networkx
G=networkx.XDiGraph({1:{1:'hola',1:'hi',2:'two',2:'dos'},2:{1:'one'}},
selfloops=True, multiedges=True)

But in each case  I get:

G.edges()

(1, 1, 'h'), (1, 1, 'i'), (1, 2, 'd'), (1, 2, 'o'), (1, 2, 's'), (2,
1,
'o'), (2, 1, 'n'), (2, 1, 'e')]


Which is not as intended for two reasons:  One is that the labels are
wrong, and the other one is that it created three edges from 1 to 2.
```


Issue created by migration from https://trac.sagemath.org/ticket/3928





---

archive/issue_comments_028058.json:
```json
{
    "body": "This is an error in input. I don't know how well the documentation explains this, but a dict-of-dicts representing a graph with multi-edges requires that the entries of the inner dicts be lists. That is the syntax. So if the documentation doesn't explain this carefully, it needs to.\n\nThe behavior you are getting is *exactly* as intended.",
    "created_at": "2008-08-22T21:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28058",
    "user": "https://github.com/rlmill"
}
```

This is an error in input. I don't know how well the documentation explains this, but a dict-of-dicts representing a graph with multi-edges requires that the entries of the inner dicts be lists. That is the syntax. So if the documentation doesn't explain this carefully, it needs to.

The behavior you are getting is *exactly* as intended.



---

archive/issue_comments_028059.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-23T03:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28059",
    "user": "https://github.com/jasongrout"
}
```

Resolution: invalid



---

archive/issue_events_009011.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2008-08-23T03:56:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3928#event-9011"
}
```



---

archive/issue_comments_028060.json:
```json
{
    "body": "Indeed, the following works:\n\n```\nsage: G=DiGraph({1:{1:['hola','hi'], 2:['two','dos']},2:{1:['one']}}, loops=True, multiedges=True)\nsage: G.edges()\n[(1, 1, 'hi'), (1, 1, 'hola'), (1, 2, 'dos'), (1, 2, 'two'), (2, 1, 'one')]\n\n```",
    "created_at": "2008-08-23T03:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28060",
    "user": "https://github.com/jasongrout"
}
```

Indeed, the following works:

```
sage: G=DiGraph({1:{1:['hola','hi'], 2:['two','dos']},2:{1:['one']}}, loops=True, multiedges=True)
sage: G.edges()
[(1, 1, 'hi'), (1, 1, 'hola'), (1, 2, 'dos'), (1, 2, 'two'), (2, 1, 'one')]

```



---

archive/issue_comments_028061.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-08-26T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28061",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_comments_028062.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-08-26T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28062",
    "user": "https://github.com/jasongrout"
}
```

Changing status from closed to reopened.



---

archive/issue_events_009012.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2008-08-26T15:43:31Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3928#event-9012"
}
```



---

archive/issue_comments_028063.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-26T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28063",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_028064.json:
```json
{
    "body": "As per Robert's comment and the suggestion on sage-devel to add documentation, I'm reopening this to add the following to the documentation:\n\n```\nFor a digraph with multiple edges and labels, one must provide a list\nwithin the dictionary:\n\nsage: G=DiGraph({1:{1:['hola','hi'], 2:['two','dos']},2:{1:['one']}},\nloops=True, multiedges=True)\nsage: G.edges()\n[(1, 1, 'hi'), (1, 1, 'hola'), (1, 2, 'dos'), (1, 2, 'two'), (2, 1,\n'one')]\n```",
    "created_at": "2008-08-26T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28064",
    "user": "https://github.com/jasongrout"
}
```

As per Robert's comment and the suggestion on sage-devel to add documentation, I'm reopening this to add the following to the documentation:

```
For a digraph with multiple edges and labels, one must provide a list
within the dictionary:

sage: G=DiGraph({1:{1:['hola','hi'], 2:['two','dos']},2:{1:['one']}},
loops=True, multiedges=True)
sage: G.edges()
[(1, 1, 'hi'), (1, 1, 'hola'), (1, 2, 'dos'), (1, 2, 'two'), (2, 1,
'one')]
```



---

archive/issue_comments_028065.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-08-26T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28065",
    "user": "https://github.com/jasongrout"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_028066.json:
```json
{
    "body": "This is a *new* ticket - don't reopen closed tickets and reuse them for something related.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-26T16:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a *new* ticket - don't reopen closed tickets and reuse them for something related.

Cheers,

Michael



---

archive/issue_comments_028067.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-08-26T16:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3928#issuecomment-28067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_009013.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-26T16:53:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3928#event-9013"
}
```
