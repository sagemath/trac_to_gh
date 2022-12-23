# Issue 6632: Bug in blocks_and_cut_vertices() of a graph that occurs when vertex 0 is a cut vertex

Issue created by migration from https://trac.sagemath.org/ticket/6632

Original creator: hartke

Original creation time: 2009-07-26 22:10:42

Assignee: rlm

CC:  rlm

There is a bug in the blocks_and_cut_vertices() function for graphs such that an incorrect result is returned if the vertex 0 is a cut vertex.


```
sage: G=Graph()
sage: G.add_vertices(range(5))
sage: G.add_edges([(0,1),(0,2),(1,2),(2,3),(2,4),(3,4)])
sage: print G.blocks_and_cut_vertices()
([[0, 1, 2]], [])
```


The bug arises because the algorithm as presented in the referenced book uses 0 to indicate a vertex not in the graph.  However, in Sage, we number the vertices of a graph starting at 0.

A patch will be attached below.



---

Attachment

Patch to fix bug in blocks_and_cut_vertices() in graph.py


---

Comment by mvngu created at 2009-07-26 22:38:00

Stephen: If you want people to review your patch, you should mark the subject of the ticket with "needs review". That way, the ticket would be picked up by the relevant trac report and people can easily identify those tickets that need review.


---

Comment by hartke created at 2009-07-27 15:28:07

Minh:  Thanks for fixing the summary!  This was my first submitted patch, so I'm trying to learn the ropes.


---

Comment by mvngu created at 2009-07-28 03:19:22

Replying to [comment:3 hartke]:
> Minh:  Thanks for fixing the summary!  This was my first submitted patch, so I'm trying to learn the ropes.
No worries. We all have to start somewhere :-)


---

Comment by jason created at 2009-07-31 06:54:56

Thanks for looking at this!

How about we trade reviews?  I'd like to get #6659 reviewed and in 4.1.1 :).

Could you also just initialize p to [None]*G.num_verts()?  Then the check at the bottom becomes `p[v] is None`.

I'm a little concerned about you taking out the last B.append(S) statement.  Can you comment on it?  I don't have Jungnickel handy, so forgive me if the answer is easy.

I noticed a few other things with this function, but I'll open up another ticket to address these.  For one, it totally ignores the original vertex labeling in the answer.  For example, you can't make sense of the following output.

```
sage: g=graphs.CubeGraph(2)
sage: g.blocks_and_cut_vertices()
([[2, 3, 1, 0]], [])
sage: g
2-Cube: Graph on 4 vertices
sage: g.vertices()
['00', '01', '10', '11']
```


Second: there seems to be a serious error (in the old implementation too) in the case of a star graph.  Look at the cut vertices returned here.


```
sage: g=graphs.StarGraph(8)      
sage: g.blocks_and_cut_vertices() # current implementation

([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [0]],
 [0, 0, 0, 0, 0, 0, 0])
```


Your implementation corrects at least one problem: the last [0] is gone (probably as an effect of you taking out that last append() statement, right?):


```
sage: g=graphs.StarGraph(8)      
sage: g.blocks_and_cut_vertices() # your implementation

([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
 [0, 0, 0, 0, 0, 0, 0])
```



---

Attachment

Apply both patches.


---

Comment by mvngu created at 2009-08-03 02:02:00

Resolution: fixed
