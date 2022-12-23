# Issue 2315: Union of Graphs

Issue created by migration from https://trac.sagemath.org/ticket/2315

Original creator: vgermrk

Original creation time: 2008-02-26 12:34:23

Assignee: rlm

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


---

Comment by jason created at 2008-02-26 13:44:58

Whenever I hear "union", I think "disjoint union" (at least as far as graphs go).  So I vote for making this the disjoint union and making another function the non-disjoint union.


---

Attachment


---

Comment by jason created at 2008-02-26 22:52:58

Furthermore, I vote with a patch :)


---

Comment by rlm created at 2008-02-26 23:31:42

Recommendations:

 1. `_lmul_` implements multiplication on the left. There isn't any point to having `G*3` but not `3*G` since most people will go for the latter.

 2. There should be an error (maybe NotImplemented with an explanation) for any other kind of attempted multiplications - I'm not about to go into a big discussion on which of the many products this should be...


---

Comment by jason created at 2008-02-27 20:10:04

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

Comment by jason created at 2008-02-27 20:52:02

apply on top of the first patch


---

Attachment

The graph-union2.patch takes care of the recommendations.  This now depends on the patch at #2283 to work correctly (otherwise 3*G will still return an error because 3 == Integer(3) at the Sage command line).


---

Comment by mabshoff created at 2008-02-28 06:17:33

Merged both patches in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 06:17:33

Resolution: fixed
