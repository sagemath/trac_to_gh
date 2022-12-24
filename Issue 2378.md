# Issue 2378: graph animations

archive/issues_002378.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe ought to have a way to create animations like these:\n\nhttp://www.cs.sunysb.edu/~skiena/combinatorica/animations/\n\nSee the Mathematica function:\n\nhttp://reference.wolfram.com/mathematica/Combinatorica/ref/AnimateGraph.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/2378\n\n",
    "created_at": "2008-03-03T18:07:41Z",
    "labels": [
        "Cygwin",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "graph animations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2378",
    "user": "@jasongrout"
}
```
Assignee: mabshoff

We ought to have a way to create animations like these:

http://www.cs.sunysb.edu/~skiena/combinatorica/animations/

See the Mathematica function:

http://reference.wolfram.com/mathematica/Combinatorica/ref/AnimateGraph.html

Issue created by migration from https://trac.sagemath.org/ticket/2378





---

archive/issue_comments_016041.json:
```json
{
    "body": "See also the highlight function:\n\nhttp://reference.wolfram.com/mathematica/Combinatorica/ref/Highlight.html",
    "created_at": "2008-03-03T18:08:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16041",
    "user": "@jasongrout"
}
```

See also the highlight function:

http://reference.wolfram.com/mathematica/Combinatorica/ref/Highlight.html



---

archive/issue_comments_016042.json:
```json
{
    "body": "Changing assignee from mabshoff to @rlmill.",
    "created_at": "2008-03-03T18:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16042",
    "user": "@jasongrout"
}
```

Changing assignee from mabshoff to @rlmill.



---

archive/issue_comments_016043.json:
```json
{
    "body": "Changing component from Cygwin to graph theory.",
    "created_at": "2008-03-03T18:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16043",
    "user": "@jasongrout"
}
```

Changing component from Cygwin to graph theory.



---

archive/issue_comments_016044.json:
```json
{
    "body": "To do the above, I think it would be sufficient to add an option to graph.plot that would implement the \"Highlight\" functionality from Mma",
    "created_at": "2008-03-03T18:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16044",
    "user": "@jasongrout"
}
```

To do the above, I think it would be sufficient to add an option to graph.plot that would implement the "Highlight" functionality from Mma



---

archive/issue_comments_016045.json:
```json
{
    "body": "Changing assignee from @rlmill to @jasongrout.",
    "created_at": "2008-09-10T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16045",
    "user": "@rlmill"
}
```

Changing assignee from @rlmill to @jasongrout.



---

archive/issue_comments_016046.json:
```json
{
    "body": "Code for a highlight function:\n\n\n```\nnormal_vertex_color='#fec7b8'\nnormal_edge_color = 'black'\ndef highlight(g,vertices=[],edges=[],**kwds):\n    edges = [e[0:2] for e in edges]\n    normal_edges = list(set(g.edges(labels=False)).difference(set([e[0:2] for e in edges])))\n    normal_vertices = list(set(g.vertices()).difference(set(vertices)))\n    return g.plot(vertex_colors={'red': vertices, normal_vertex_color: normal_vertices}, edge_colors={'red': edges, normal_edge_color: normal_edges},**kwds)\ng=graphs.DodecahedralGraph()\nhighlight(g,[1,2],[(1,2),(2,6)],layout=\"spring\")\n```\n",
    "created_at": "2008-12-22T18:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16046",
    "user": "@jasongrout"
}
```

Code for a highlight function:


```
normal_vertex_color='#fec7b8'
normal_edge_color = 'black'
def highlight(g,vertices=[],edges=[],**kwds):
    edges = [e[0:2] for e in edges]
    normal_edges = list(set(g.edges(labels=False)).difference(set([e[0:2] for e in edges])))
    normal_vertices = list(set(g.vertices()).difference(set(vertices)))
    return g.plot(vertex_colors={'red': vertices, normal_vertex_color: normal_vertices}, edge_colors={'red': edges, normal_edge_color: normal_edges},**kwds)
g=graphs.DodecahedralGraph()
highlight(g,[1,2],[(1,2),(2,6)],layout="spring")
```




---

archive/issue_comments_016047.json:
```json
{
    "body": "This is now possible with the graph editor widget *phitigra*, added as a package in #30540.\nSee the demo notebook at https://github.com/jfraymond/phitigra for examples with DFS and Dijkstra's algorithm.\nTherefore I am changing the ticket status to \"duplicate/invalid/wontfix\".",
    "created_at": "2022-04-20T10:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16047",
    "user": "@jfraymond"
}
```

This is now possible with the graph editor widget *phitigra*, added as a package in #30540.
See the demo notebook at https://github.com/jfraymond/phitigra for examples with DFS and Dijkstra's algorithm.
Therefore I am changing the ticket status to "duplicate/invalid/wontfix".



---

archive/issue_comments_016048.json:
```json
{
    "body": "We can certainly close it",
    "created_at": "2022-04-21T12:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16048",
    "user": "@dcoudert"
}
```

We can certainly close it



---

archive/issue_comments_016049.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2022-04-21T12:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16049",
    "user": "@dcoudert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016050.json:
```json
{
    "body": "I just played with the Dijkstra's algorithm implemented with Phitigra. It works like a charm!",
    "created_at": "2022-04-22T05:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16050",
    "user": "@kwankyu"
}
```

I just played with the Dijkstra's algorithm implemented with Phitigra. It works like a charm!



---

archive/issue_comments_016051.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-04-22T05:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16051",
    "user": "@kwankyu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_016052.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-05-11T02:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2378#issuecomment-16052",
    "user": "@mkoeppe"
}
```

Resolution: invalid
