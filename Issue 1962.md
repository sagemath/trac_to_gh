# Issue 1962: set_edge_label creates edges when multiple edges are allowed

archive/issues_001962.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nsage: g = Graph({0: [0,1,1,2]}, loops=True, multiedges=True)\nsage: g.set_edge_label(0,0,'test')\nsage: g.edges()\n\n[(0, 0, 'e'),\n (0, 0, 's'),\n (0, 0, 't'),\n (0, 0, 't'),\n (0, 1, None),\n (0, 1, None),\n (0, 2, None)]\n```\n\n\nI suggest that set_edge_labels should *never* create an edge or the function name should be changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1962\n\n",
    "created_at": "2008-01-28T19:49:16Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "set_edge_label creates edges when multiple edges are allowed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1962",
    "user": "jason"
}
```
Assignee: rlm


```
sage: g = Graph({0: [0,1,1,2]}, loops=True, multiedges=True)
sage: g.set_edge_label(0,0,'test')
sage: g.edges()

[(0, 0, 'e'),
 (0, 0, 's'),
 (0, 0, 't'),
 (0, 0, 't'),
 (0, 1, None),
 (0, 1, None),
 (0, 2, None)]
```


I suggest that set_edge_labels should *never* create an edge or the function name should be changed.

Issue created by migration from https://trac.sagemath.org/ticket/1962





---

archive/issue_comments_012670.json:
```json
{
    "body": "This is not a bug in `set_edge_label` itself:\n\n```\nsage: g._nxg.adj\n{0: {0: 'test', 1: [None, None], 2: [None]},\n 1: {0: [None, None]},\n 2: {0: [None]}}\n```\n\nIt is in fact a bug in NetworkX's `edges` function:\n\n```\nsage: g._nxg.edges()\n[(0, 0, 't'),\n (0, 0, 'e'),\n (0, 0, 's'),\n (0, 0, 't'),\n (0, 1, None),\n (0, 1, None),\n (0, 2, None)]\n```\n",
    "created_at": "2008-02-17T00:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12670",
    "user": "rlm"
}
```

This is not a bug in `set_edge_label` itself:

```
sage: g._nxg.adj
{0: {0: 'test', 1: [None, None], 2: [None]},
 1: {0: [None, None]},
 2: {0: [None]}}
```

It is in fact a bug in NetworkX's `edges` function:

```
sage: g._nxg.edges()
[(0, 0, 't'),
 (0, 0, 'e'),
 (0, 0, 's'),
 (0, 0, 't'),
 (0, 1, None),
 (0, 1, None),
 (0, 2, None)]
```




---

archive/issue_comments_012671.json:
```json
{
    "body": "My mistake: when multiple edges is True, the representation is slightly different:\n\n```\nsage: G = Graph({0:[1]})\nsage: G._nxg.adj\n{0: {1: None}, 1: {0: None}}\nsage: G = Graph({0:[1]}, multiedges=True)\nsage: G._nxg.adj\n{0: {1: [None]}, 1: {0: [None]}}\n```\n",
    "created_at": "2008-02-17T00:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12671",
    "user": "rlm"
}
```

My mistake: when multiple edges is True, the representation is slightly different:

```
sage: G = Graph({0:[1]})
sage: G._nxg.adj
{0: {1: None}, 1: {0: None}}
sage: G = Graph({0:[1]}, multiedges=True)
sage: G._nxg.adj
{0: {1: [None]}, 1: {0: [None]}}
```




---

archive/issue_comments_012672.json:
```json
{
    "body": "In fact, `set_edge_label` only makes sense when there is only one possible edge whose label is to be set: if there is more than one, which label to set?",
    "created_at": "2008-02-17T00:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12672",
    "user": "rlm"
}
```

In fact, `set_edge_label` only makes sense when there is only one possible edge whose label is to be set: if there is more than one, which label to set?



---

archive/issue_comments_012673.json:
```json
{
    "body": "Attachment [1962.patch](tarball://root/attachments/some-uuid/ticket1962/1962.patch) by rlm created at 2008-02-17 00:24:54",
    "created_at": "2008-02-17T00:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12673",
    "user": "rlm"
}
```

Attachment [1962.patch](tarball://root/attachments/some-uuid/ticket1962/1962.patch) by rlm created at 2008-02-17 00:24:54



---

archive/issue_comments_012674.json:
```json
{
    "body": "Attachment [1962-ref.patch](tarball://root/attachments/some-uuid/ticket1962/1962-ref.patch) by ncalexan created at 2008-02-26 01:06:04\n\nAfter discussion on IRC, this looks good to me.  Apply.  Needs both patches, -ref second.",
    "created_at": "2008-02-26T01:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12674",
    "user": "ncalexan"
}
```

Attachment [1962-ref.patch](tarball://root/attachments/some-uuid/ticket1962/1962-ref.patch) by ncalexan created at 2008-02-26 01:06:04

After discussion on IRC, this looks good to me.  Apply.  Needs both patches, -ref second.



---

archive/issue_comments_012675.json:
```json
{
    "body": "Merged both patches in Sage 2.10.3.alpha0",
    "created_at": "2008-02-26T01:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12675",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.10.3.alpha0



---

archive/issue_comments_012676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-26T01:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1962",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1962#issuecomment-12676",
    "user": "mabshoff"
}
```

Resolution: fixed
