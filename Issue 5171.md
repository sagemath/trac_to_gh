# Issue 5171: Bugs in the Graph constructor when input an adjacency matrix.

Issue created by migration from https://trac.sagemath.org/ticket/5171

Original creator: was

Original creation time: 2009-02-04 02:53:08

Assignee: rlm

1. The adjacency matrix of a graph constructed from an adjacency matrix should either be the same or one should get an error when constructing the graph:

```
sage: a = matrix(2,2,[1,0,0,1])
sage: Graph(a)
Graph on 2 vertices
sage: Graph(a).adjacency_matrix()  # I think Graph(a) should work or given an error
[0 0]
[0 0]
sage: Graph(a, loops=True).adjacency_matrix()
[1 0]
[0 1]
```


Another example -- this is WRONG, since multiple loops should not be ignored.

```
sage: a = matrix(2,2,[2,0,0,1])
sage: Graph(a,loops=True).adjacency_matrix()
[1 0]
[0 1]
```


Why not just make a graph with loops and multiple edges (or at least weighted edges) if and only if the adjacency matrix has diagonal entries or non-1 entries?  I'm guessing the Graph constructor just grew from a time when these constructions weren't allowed or that networkx is just poorly designed.  Either way, this needs to be fixed for Sage. 

2. When the input matrix is non-square, the error message is wrong in multiple ways:

```
sage: a = matrix([1,0,0,1])
sage: Graph(a)
Traceback (most recent call last):
...
AttributeError: Incidence Matrix must have one 1 and one -1 per column.
```


  * it should be "adjacency matrix". 

  * The exception should be ValueError, not AttributeError

  * The Graph constructor doesn't take only 1's or -1's as input (but see above)

  * The Graph constructor is perfectly fine with having multiple 1's per column!




---

Comment by jason created at 2009-02-04 03:28:02

William: when the matrix is non-square, we are assuming it is an incidence matrix; the error message is perfect.  See http://en.wikipedia.org/wiki/Incidence_matrix.

However, it's not the first time that I've been frustrated with the behavior completely being different when a small change in input happens.  In fact, I remember complaining about the adjacency matrix/incidence matrix assumptions a long time ago.  I think it was part of one of my grand re-architecting schemes, though, so it got abandoned eventually :).


---

Comment by rlm created at 2009-02-14 23:16:01

Patches here will depend on #3541 and its dependencies.


---

Comment by rlm created at 2009-02-14 23:19:05

This patch implements fixes for `Graph.__init__` but not `DiGraph.__init__`. It is not ready for review. It passes tests in `sage/graphs`.


---

Comment by rlm created at 2009-02-17 18:40:13

Changing status from new to assigned.


---

Comment by rlm created at 2009-02-17 18:40:13

This will allow us to close #5046 as well.


---

Comment by mabshoff created at 2009-02-17 19:01:25

With only the first patch some trouble:

```
	sage -t -long devel/sage/sage/graphs/graph.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/crystals.py # 94 doctests failed
	sage -t -long devel/sage/sage/combinat/posets/posets.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/fast_crystals.py # 64 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 110 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/letters.py # 68 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/spins.py # 64 doctests failed
```


Cheers,

Michael


---

Comment by rlm created at 2009-02-17 21:11:48

I believe this new patch addresses the issues above.


---

Comment by mabshoff created at 2009-02-17 21:25:27

The new version of the patch makes all doctests pass on sage.math.

Cheers,

Michael


---

Comment by was created at 2009-02-17 22:21:10

REPORT:

 * All doctests pass in the graphs directory

 * old doctests don't fail in too disturbing a way

 * I definitely do not like at all the new multiple_edges function.  It should be split into two functions: has_multiple_edges() and allows_multiple_edges() and the current multiple_edges should be deprecated.  I personally would expect a function named "multiple_edges" to return a list of all multiple edges, which no variant of the current function does!  Having a check parameter that determines the functionality is particularly bad, given that check is used elsewhere all over in sage in a way that never changes the meaning of the output (it is always for speed).

 
Otherwise I'm good with this patch.


---

Attachment


---

Comment by was created at 2009-02-17 23:33:33

This looks good. Excellent!


---

Comment by mabshoff created at 2009-02-17 23:45:53

This latest patch requires one trivial doctest fix:

```
sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc2/devel/sage-main/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx", line 808:
    sage: sage.groups.perm_gps.partn_ref.refinement_graphs.random_tests()
Expected:
    All passed: ... random tests on ... graphs.
Got:
    doctest:1: DeprecationWarning: The function loops is replaced by allow_loops and allows_loops.
    All passed: 560 random tests on 28 graphs.
**********************************************************************
```

I am posting a reviewer patch shortly.

Cheers,

Michael


---

Attachment

Mike suggested the reviewer fix.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-18 00:08:15

Merged both patches in Sage 3.3.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-18 00:08:15

Resolution: fixed


---

Comment by rlm created at 2009-02-18 00:16:45

Replying to [comment:12 mabshoff]:
> Mike suggested the reviewer fix.

+1
