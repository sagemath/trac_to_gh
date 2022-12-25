# Issue 2265: [with patch, positive review] fix shortest_path_all_pairs

archive/issues_002265.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\nsage: C = graphs.CubeGraph(4)\nsage: C.shortest_paths('0000')\n\n{'0000': ['0000'],\n...\n '1111': ['0000', '0100', '0110', '1110', '1111']}\nsage: C.shortest_path_all_pairs()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/rlmill/sage/<ipython console> in <module>()\n\n/Users/rlmill/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in shortest_path_all_pairs(self)\n   2245             for u in verts:\n   2246                 for v in verts:\n-> 2247                     if dist[u][v] > dist[u][w] + dist[w][v]:\n   2248                         dist[u][v] = dist[u][w] + dist[w][v]\n   2249                         pred[u][v] = pred[w][v]\n\n<type 'exceptions.TypeError'>: unsupported operand type(s) for +: 'int' and 'NoneType'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2265\n\n",
    "closed_at": "2008-02-24T18:14:47Z",
    "created_at": "2008-02-22T19:29:13Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, positive review] fix shortest_path_all_pairs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2265",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

```
sage: C = graphs.CubeGraph(4)
sage: C.shortest_paths('0000')

{'0000': ['0000'],
...
 '1111': ['0000', '0100', '0110', '1110', '1111']}
sage: C.shortest_path_all_pairs()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/rlmill/sage/<ipython console> in <module>()

/Users/rlmill/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in shortest_path_all_pairs(self)
   2245             for u in verts:
   2246                 for v in verts:
-> 2247                     if dist[u][v] > dist[u][w] + dist[w][v]:
   2248                         dist[u][v] = dist[u][w] + dist[w][v]
   2249                         pred[u][v] = pred[w][v]

<type 'exceptions.TypeError'>: unsupported operand type(s) for +: 'int' and 'NoneType'
```

Issue created by migration from https://trac.sagemath.org/ticket/2265





---

archive/issue_comments_014972.json:
```json
{
    "body": "This works for me on ubuntu 7.10, 32-bit, sage 2.10.1:\n\n```\nsage: C=graphs.CubeGraph(4)\nsage: C.shortest_paths('0000')\n\n{'0000': ['0000'],\n '0001': ['0000', '0001'],\n '0010': ['0000', '0010'],\n '0011': ['0000', '0001', '0011'],\n '0100': ['0000', '0100'],\n '0101': ['0000', '0100', '0101'],\n '0110': ['0000', '0100', '0110'],\n '0111': ['0000', '0100', '0110', '0111'],\n '1000': ['0000', '1000'],\n '1001': ['0000', '1000', '1001'],\n '1010': ['0000', '1000', '1010'],\n '1011': ['0000', '0001', '0011', '1011'],\n '1100': ['0000', '1000', '1100'],\n '1101': ['0000', '0100', '0101', '1101'],\n '1110': ['0000', '0100', '0110', '1110'],\n '1111': ['0000', '0100', '0110', '1110', '1111']}\n```",
    "created_at": "2008-02-22T19:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14972",
    "user": "https://github.com/jasongrout"
}
```

This works for me on ubuntu 7.10, 32-bit, sage 2.10.1:

```
sage: C=graphs.CubeGraph(4)
sage: C.shortest_paths('0000')

{'0000': ['0000'],
 '0001': ['0000', '0001'],
 '0010': ['0000', '0010'],
 '0011': ['0000', '0001', '0011'],
 '0100': ['0000', '0100'],
 '0101': ['0000', '0100', '0101'],
 '0110': ['0000', '0100', '0110'],
 '0111': ['0000', '0100', '0110', '0111'],
 '1000': ['0000', '1000'],
 '1001': ['0000', '1000', '1001'],
 '1010': ['0000', '1000', '1010'],
 '1011': ['0000', '0001', '0011', '1011'],
 '1100': ['0000', '1000', '1100'],
 '1101': ['0000', '0100', '0101', '1101'],
 '1110': ['0000', '0100', '0110', '1110'],
 '1111': ['0000', '0100', '0110', '1110', '1111']}
```



---

archive/issue_comments_014973.json:
```json
{
    "body": "Never mind, I see that the error was something different.  I get the same error.",
    "created_at": "2008-02-22T19:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14973",
    "user": "https://github.com/jasongrout"
}
```

Never mind, I see that the error was something different.  I get the same error.



---

archive/issue_comments_014974.json:
```json
{
    "body": "The problem was that we were blindly adding the labels to edges, so if an edge didn't have a label, things went boom.\n\nI added a default_weight option which will be applied when an edge doesn't have a weight.",
    "created_at": "2008-02-22T20:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14974",
    "user": "https://github.com/jasongrout"
}
```

The problem was that we were blindly adding the labels to edges, so if an edge didn't have a label, things went boom.

I added a default_weight option which will be applied when an edge doesn't have a weight.



---

archive/issue_comments_014975.json:
```json
{
    "body": "Attachment [shortest-paths.patch](tarball://root/attachments/some-uuid/ticket2265/shortest-paths.patch) by @jasongrout created at 2008-02-22 20:21:42\n\nI also added a by_weight option as vgermrk suggested to be consistent with the other shortest path functions.",
    "created_at": "2008-02-22T20:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14975",
    "user": "https://github.com/jasongrout"
}
```

Attachment [shortest-paths.patch](tarball://root/attachments/some-uuid/ticket2265/shortest-paths.patch) by @jasongrout created at 2008-02-22 20:21:42

I also added a by_weight option as vgermrk suggested to be consistent with the other shortest path functions.



---

archive/issue_comments_014976.json:
```json
{
    "body": "I haven't run doctests yet, but pending that, everything looks good.",
    "created_at": "2008-02-22T21:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14976",
    "user": "https://github.com/rlmill"
}
```

I haven't run doctests yet, but pending that, everything looks good.



---

archive/issue_comments_014977.json:
```json
{
    "body": "Testall passes with that patch, so with rml's review I am giving this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-24T18:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14977",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Testall passes with that patch, so with rml's review I am giving this a positive review.

Cheers,

Michael



---

archive/issue_events_005357.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-24T18:14:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2265#event-5357"
}
```



---

archive/issue_comments_014978.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T18:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14978",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014979.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-24T18:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2265#issuecomment-14979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.alpha0
