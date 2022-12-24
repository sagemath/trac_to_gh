# Issue 6238: possible failure in is_planar(set_embedding=True, set_pos=False)

archive/issues_006238.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  rlm ekirkman\n\n\n```\nsage: pari('v'), pari('w')\n(v, w)\nsage: w = QQ['w'].0\nsage: v = QQ['w']['v'].0\nsage: f = v^3 - (w^7 + w + 1)\n\nsage: rts = list(set(f.discriminant().roots(QQbar, multiplicities=False)))\nsage: rts = map(CDF, rts)\nsage: xs = map(real_part, rts)\nsage: ys = map(imag_part, rts)\n\nsage: import delaunay\nsage: DT = delaunay.Triangulation(xs, ys)\nsage: G = Graph(DT.node_graph())\nsage: G.set_pos(dict(enumerate(zip(xs, ys))))\nsage: G.is_planar(set_embedding=True, set_pos=False)\nTrue\nsage: G.get_embedding()\n{0: [2, 3, 6],\n 1: [5, 4, 2],\n 2: [6, 1, 4, 5, 3, 0],\n 3: [0, 2, 5],\n 4: [2, 1],\n 5: [3, 2, 1],\n 6: [0, 2]}\n```\n\n\nThe first face does not have vertices in clockwise order.  At least, not for me :)  Hard to see without show-ing the graph.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6238\n\n",
    "created_at": "2009-06-06T23:37:56Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "possible failure in is_planar(set_embedding=True, set_pos=False)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6238",
    "user": "@ncalexan"
}
```
Assignee: @rlmill

CC:  rlm ekirkman


```
sage: pari('v'), pari('w')
(v, w)
sage: w = QQ['w'].0
sage: v = QQ['w']['v'].0
sage: f = v^3 - (w^7 + w + 1)

sage: rts = list(set(f.discriminant().roots(QQbar, multiplicities=False)))
sage: rts = map(CDF, rts)
sage: xs = map(real_part, rts)
sage: ys = map(imag_part, rts)

sage: import delaunay
sage: DT = delaunay.Triangulation(xs, ys)
sage: G = Graph(DT.node_graph())
sage: G.set_pos(dict(enumerate(zip(xs, ys))))
sage: G.is_planar(set_embedding=True, set_pos=False)
True
sage: G.get_embedding()
{0: [2, 3, 6],
 1: [5, 4, 2],
 2: [6, 1, 4, 5, 3, 0],
 3: [0, 2, 5],
 4: [2, 1],
 5: [3, 2, 1],
 6: [0, 2]}
```


The first face does not have vertices in clockwise order.  At least, not for me :)  Hard to see without show-ing the graph.

Issue created by migration from https://trac.sagemath.org/ticket/6238





---

archive/issue_comments_049832.json:
```json
{
    "body": "Attachment [is_planar-example.png](tarball://root/attachments/some-uuid/ticket6238/is_planar-example.png) by @rlmill created at 2009-07-13 21:32:00\n\nThe problem is that you are never asking the graph to remember the embedding, so when you show the graph, you are just looking at some random embedding.\n\nThe way to do what you're trying to do is to ask the graph to remember the planar positioning:\n\n```\nsage: G.is_planar(set_embedding=True, set_pos=True)\n```\n\n\ni.e. change a 'False' to a 'True'. :)",
    "created_at": "2009-07-13T21:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6238#issuecomment-49832",
    "user": "@rlmill"
}
```

Attachment [is_planar-example.png](tarball://root/attachments/some-uuid/ticket6238/is_planar-example.png) by @rlmill created at 2009-07-13 21:32:00

The problem is that you are never asking the graph to remember the embedding, so when you show the graph, you are just looking at some random embedding.

The way to do what you're trying to do is to ask the graph to remember the planar positioning:

```
sage: G.is_planar(set_embedding=True, set_pos=True)
```


i.e. change a 'False' to a 'True'. :)



---

archive/issue_comments_049833.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-07-13T21:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6238#issuecomment-49833",
    "user": "@rlmill"
}
```

Resolution: invalid
