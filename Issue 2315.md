# Issue 2315: Union of Graphs

archive/issues_002315.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe union function of graphs doesn't do what its docstring says.\n\nDocstring:\n\n\"union(self, other)\n\nReturns the union of self and other.\nIf there are common vertices to both, they will be renamed.\"\n\nExecuting the example from the docstring shows that the description is wrong. Here are the graphs:\n\n```\nsage: D = graphs.DodecahedralGraph();D\nDodecahedron: Graph on 20 vertices\nsage: P = graphs.PetersenGraph();P\nPetersen graph: Graph on 10 vertices\n```\n\nBut the union returns a graph on 20 vertices\n\n```\nsage: D.union(P)\nGraph on 20 vertices\n```\n\nbut i expect it should return a graph on 30 vertices.\n\nSo either the function or the dostring is wrong.\n\nThere are two possible ways to deal with this problem:\n\n1.) Keep this one but rename it to \"nondisjoint_union\" (and correct the docstring of course),\nand code the right \"union\" function.\n\n2.) Correct the docstring of this one, and code a \"disjoint_union\".\n\nIn #sage-devel mhansen and i agreed that this union function is supposed to do a disjoint union, so 1.) should be the way. But that's maybe up to discussion.\n\n-vgermrk-\n\nIssue created by migration from https://trac.sagemath.org/ticket/2315\n\n",
    "created_at": "2008-02-26T12:34:23Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Union of Graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2315",
    "user": "https://github.com/m-r-k"
}
```
Assignee: @rlmill

The union function of graphs doesn't do what its docstring says.

Docstring:

"union(self, other)

Returns the union of self and other.
If there are common vertices to both, they will be renamed."

Executing the example from the docstring shows that the description is wrong. Here are the graphs:

```
sage: D = graphs.DodecahedralGraph();D
Dodecahedron: Graph on 20 vertices
sage: P = graphs.PetersenGraph();P
Petersen graph: Graph on 10 vertices
```

But the union returns a graph on 20 vertices

```
sage: D.union(P)
Graph on 20 vertices
```

but i expect it should return a graph on 30 vertices.

So either the function or the dostring is wrong.

There are two possible ways to deal with this problem:

1.) Keep this one but rename it to "nondisjoint_union" (and correct the docstring of course),
and code the right "union" function.

2.) Correct the docstring of this one, and code a "disjoint_union".

In #sage-devel mhansen and i agreed that this union function is supposed to do a disjoint union, so 1.) should be the way. But that's maybe up to discussion.

-vgermrk-

Issue created by migration from https://trac.sagemath.org/ticket/2315





---

archive/issue_comments_015372.json:
```json
{
    "body": "Whenever I hear \"union\", I think \"disjoint union\" (at least as far as graphs go).  So I vote for making this the disjoint union and making another function the non-disjoint union.",
    "created_at": "2008-02-26T13:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15372",
    "user": "https://github.com/jasongrout"
}
```

Whenever I hear "union", I think "disjoint union" (at least as far as graphs go).  So I vote for making this the disjoint union and making another function the non-disjoint union.



---

archive/issue_comments_015373.json:
```json
{
    "body": "Attachment [graph_union.patch](tarball://root/attachments/some-uuid/ticket2315/graph_union.patch) by @jasongrout created at 2008-02-26 22:51:59",
    "created_at": "2008-02-26T22:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15373",
    "user": "https://github.com/jasongrout"
}
```

Attachment [graph_union.patch](tarball://root/attachments/some-uuid/ticket2315/graph_union.patch) by @jasongrout created at 2008-02-26 22:51:59



---

archive/issue_comments_015374.json:
```json
{
    "body": "Furthermore, I vote with a patch :)",
    "created_at": "2008-02-26T22:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15374",
    "user": "https://github.com/jasongrout"
}
```

Furthermore, I vote with a patch :)



---

archive/issue_comments_015375.json:
```json
{
    "body": "Recommendations:\n\n1. `_lmul_` implements multiplication on the left. There isn't any point to having `G*3` but not `3*G` since most people will go for the latter.\n\n2. There should be an error (maybe NotImplemented with an explanation) for any other kind of attempted multiplications - I'm not about to go into a big discussion on which of the many products this should be...",
    "created_at": "2008-02-26T23:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15375",
    "user": "https://github.com/rlmill"
}
```

Recommendations:

1. `_lmul_` implements multiplication on the left. There isn't any point to having `G*3` but not `3*G` since most people will go for the latter.

2. There should be an error (maybe NotImplemented with an explanation) for any other kind of attempted multiplications - I'm not about to go into a big discussion on which of the many products this should be...



---

archive/issue_comments_015376.json:
```json
{
    "body": "implementing __rmul__ makes it so that:\n\n\n```\nsage: G=graphs.CycleGraph(3)\nsage: int(3)*G\n```\n\n\nworks, but the following still doesn't.  I think it's because 3*G means Integer(3)*G in Sage, but the coercion model blows up instead of seeing if G has an __rmul__ method that can handle Integers.\n\n\n```\nsage: G=graphs.CycleGraph(3)\nsage: int(3)*G              \ndisjoint_union( disjoint_union( disjoint_union( , Cycle graph ), Cycle graph ), Cycle graph ): Graph on 9 vertices\nsage: 3*G     \n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/jason/sage/devel/sage-main/sage/graphs/<ipython console> in <module>()\n\n/home/jason/sage/devel/sage-main/sage/graphs/element.pyx in sage.structure.element.RingElement.__mul__()\n\n/home/jason/sage/devel/sage-main/sage/graphs/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Integer Ring' and '<class 'sage.graphs.graph.Graph'>'\n```\n",
    "created_at": "2008-02-27T20:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15376",
    "user": "https://github.com/jasongrout"
}
```

implementing __rmul__ makes it so that:


```
sage: G=graphs.CycleGraph(3)
sage: int(3)*G
```


works, but the following still doesn't.  I think it's because 3*G means Integer(3)*G in Sage, but the coercion model blows up instead of seeing if G has an __rmul__ method that can handle Integers.


```
sage: G=graphs.CycleGraph(3)
sage: int(3)*G              
disjoint_union( disjoint_union( disjoint_union( , Cycle graph ), Cycle graph ), Cycle graph ): Graph on 9 vertices
sage: 3*G     
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/jason/sage/devel/sage-main/sage/graphs/<ipython console> in <module>()

/home/jason/sage/devel/sage-main/sage/graphs/element.pyx in sage.structure.element.RingElement.__mul__()

/home/jason/sage/devel/sage-main/sage/graphs/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Integer Ring' and '<class 'sage.graphs.graph.Graph'>'
```




---

archive/issue_comments_015377.json:
```json
{
    "body": "apply on top of the first patch",
    "created_at": "2008-02-27T20:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15377",
    "user": "https://github.com/jasongrout"
}
```

apply on top of the first patch



---

archive/issue_comments_015378.json:
```json
{
    "body": "Attachment [graph-union2.patch](tarball://root/attachments/some-uuid/ticket2315/graph-union2.patch) by @jasongrout created at 2008-02-27 20:55:42\n\nThe graph-union2.patch takes care of the recommendations.  This now depends on the patch at #2283 to work correctly (otherwise 3*G will still return an error because 3 == Integer(3) at the Sage command line).",
    "created_at": "2008-02-27T20:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15378",
    "user": "https://github.com/jasongrout"
}
```

Attachment [graph-union2.patch](tarball://root/attachments/some-uuid/ticket2315/graph-union2.patch) by @jasongrout created at 2008-02-27 20:55:42

The graph-union2.patch takes care of the recommendations.  This now depends on the patch at #2283 to work correctly (otherwise 3*G will still return an error because 3 == Integer(3) at the Sage command line).



---

archive/issue_comments_015379.json:
```json
{
    "body": "Merged both patches in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15379",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 2.10.3.rc0



---

archive/issue_comments_015380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2315#issuecomment-15380",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
