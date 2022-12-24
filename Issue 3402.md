# Issue 3402: Digraph.incoming_edges forgets labels

archive/issues_003402.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage: dg = DiGraph({0 : [1], 1 : [0]})\nsage: dg.set_edge_label(0,1,5)\nsage: dg.set_edge_label(1,0,9)\nsage: dg.edges()\n[(0, 1, 5), (1, 0, 9)]\nsage: dg.outgoing_edges([1])\n[(1, 0, 9)]\nsage: dg.incoming_edges([1])\n[(0, 1, None)]\nsage: dg.outgoing_edges(0)\n[(0, 1, 5)]\nsage: dg.incoming_edges(0)\n[(1, 0, None)]\n```\n\n\nAs you can see, outgoing_edges remembers the labels but incoming_edges does not.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3402\n\n",
    "created_at": "2008-06-12T05:48:36Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "Digraph.incoming_edges forgets labels",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3402",
    "user": "bump"
}
```
Assignee: tbd


```
sage: dg = DiGraph({0 : [1], 1 : [0]})
sage: dg.set_edge_label(0,1,5)
sage: dg.set_edge_label(1,0,9)
sage: dg.edges()
[(0, 1, 5), (1, 0, 9)]
sage: dg.outgoing_edges([1])
[(1, 0, 9)]
sage: dg.incoming_edges([1])
[(0, 1, None)]
sage: dg.outgoing_edges(0)
[(0, 1, 5)]
sage: dg.incoming_edges(0)
[(1, 0, None)]
```


As you can see, outgoing_edges remembers the labels but incoming_edges does not.

Issue created by migration from https://trac.sagemath.org/ticket/3402





---

archive/issue_comments_023868.json:
```json
{
    "body": "Changing assignee from tbd to rlm.",
    "created_at": "2008-06-12T05:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3402#issuecomment-23868",
    "user": "mhansen"
}
```

Changing assignee from tbd to rlm.



---

archive/issue_comments_023869.json:
```json
{
    "body": "Changing component from algebra to graph theory.",
    "created_at": "2008-06-12T05:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3402#issuecomment-23869",
    "user": "mhansen"
}
```

Changing component from algebra to graph theory.



---

archive/issue_comments_023870.json:
```json
{
    "body": "Attachment [trac3402-set_edge_label.patch](tarball://root/attachments/some-uuid/ticket3402/trac3402-set_edge_label.patch) by rlm created at 2008-06-12 19:19:09",
    "created_at": "2008-06-12T19:19:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3402#issuecomment-23870",
    "user": "rlm"
}
```

Attachment [trac3402-set_edge_label.patch](tarball://root/attachments/some-uuid/ticket3402/trac3402-set_edge_label.patch) by rlm created at 2008-06-12 19:19:09



---

archive/issue_comments_023871.json:
```json
{
    "body": "The incoming edge iterator depends on self._backend._nxg which is a NetworkX XDigraph. This digraph has separate iterators for incoming and outgoing edges that depend on dictionaries self._backend._nxg.succ and self._backend._nxg.pred. Before the patch, self._backend._nxg.pred was not getting initialized.\n\nThe patch is obviously correct and I've also tested it.",
    "created_at": "2008-06-13T14:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3402#issuecomment-23871",
    "user": "bump"
}
```

The incoming edge iterator depends on self._backend._nxg which is a NetworkX XDigraph. This digraph has separate iterators for incoming and outgoing edges that depend on dictionaries self._backend._nxg.succ and self._backend._nxg.pred. Before the patch, self._backend._nxg.pred was not getting initialized.

The patch is obviously correct and I've also tested it.



---

archive/issue_comments_023872.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-16T04:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3402#issuecomment-23872",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_023873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T04:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3402#issuecomment-23873",
    "user": "mabshoff"
}
```

Resolution: fixed
