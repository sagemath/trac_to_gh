# Issue 7720: Digraph.reverse() should be rewritten more efficiently ( not hard )

archive/issues_007720.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm\n\nThis function should be rewritten much more efficiently :\n\nFirst, there should be a way to reverse the arcs \"in place\" ( without building a copy, by modifying the current graph -- I do not know if the expression used in frech translates in this case ). Such a function, for c_graphs, should be written in Cython and consist in the case of sparse graph in reverting the two copies kept of the graph.\nIn the end, this function should consist in an (optional) copy of the graph (=fast) and a call to the functionr reverting the arcs ( O(1) )\n\nIf possible and if deemed useful, the same should be made for NetworkX graphs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7720\n\n",
    "created_at": "2009-12-17T12:47:49Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Digraph.reverse() should be rewritten more efficiently ( not hard )",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7720",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  rlm

This function should be rewritten much more efficiently :

First, there should be a way to reverse the arcs "in place" ( without building a copy, by modifying the current graph -- I do not know if the expression used in frech translates in this case ). Such a function, for c_graphs, should be written in Cython and consist in the case of sparse graph in reverting the two copies kept of the graph.
In the end, this function should consist in an (optional) copy of the graph (=fast) and a call to the functionr reverting the arcs ( O(1) )

If possible and if deemed useful, the same should be made for NetworkX graphs.

Issue created by migration from https://trac.sagemath.org/ticket/7720





---

archive/issue_comments_066328.json:
```json
{
    "body": "In case of a `SparseGraph`, the `SparseGraphBackend` has `self._cg` and `self._cg_rev`. They can merely be swapped. In the case of a `NetworkX` graph, I believe their digraphs have `succ` and `pred` dictionaries storing the adjacency information. These could also be swapped. For `DenseGraphs`, this is equivalent to switching between row ordering and column ordering in bitsets, which is inevitably costly.",
    "created_at": "2009-12-18T22:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7720#issuecomment-66328",
    "user": "rlm"
}
```

In case of a `SparseGraph`, the `SparseGraphBackend` has `self._cg` and `self._cg_rev`. They can merely be swapped. In the case of a `NetworkX` graph, I believe their digraphs have `succ` and `pred` dictionaries storing the adjacency information. These could also be swapped. For `DenseGraphs`, this is equivalent to switching between row ordering and column ordering in bitsets, which is inevitably costly.



---

archive/issue_comments_066329.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7720#issuecomment-66329",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_066330.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7720#issuecomment-66330",
    "user": "ncohen"
}
```

Changing status from new to needs_work.
