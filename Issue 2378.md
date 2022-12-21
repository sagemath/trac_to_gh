# Issue 2378: graph animations

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-03 18:07:41

Assignee: mabshoff

We ought to have a way to create animations like these:

http://www.cs.sunysb.edu/~skiena/combinatorica/animations/

See the Mathematica function:

http://reference.wolfram.com/mathematica/Combinatorica/ref/AnimateGraph.html


---

Comment by jason created at 2008-03-03 18:08:37

See also the highlight function:

http://reference.wolfram.com/mathematica/Combinatorica/ref/Highlight.html


---

Comment by jason created at 2008-03-03 18:08:48

Changing assignee from mabshoff to rlm.


---

Comment by jason created at 2008-03-03 18:08:48

Changing component from Cygwin to graph theory.


---

Comment by jason created at 2008-03-03 18:19:41

To do the above, I think it would be sufficient to add an option to graph.plot that would implement the "Highlight" functionality from Mma


---

Comment by rlm created at 2008-09-10 03:01:01

Changing assignee from rlm to jason.


---

Comment by jason created at 2008-12-22 18:31:06

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

Comment by @jfraymond created at 2022-04-20 10:12:42

This is now possible with the graph editor widget _phitigra_, added as a package in #30540.
See the demo notebook at https://github.com/jfraymond/phitigra for examples with DFS and Dijkstra's algorithm.
Therefore I am changing the ticket status to "duplicate/invalid/wontfix".


---

Comment by dcoudert created at 2022-04-21 12:22:32

We can certainly close it


---

Comment by dcoudert created at 2022-04-21 12:22:32

Changing status from new to needs_review.


---

Comment by klee created at 2022-04-22 05:25:03

I just played with the Dijkstra's algorithm implemented with Phitigra. It works like a charm!


---

Comment by klee created at 2022-04-22 05:25:03

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-05-11 02:14:43

Resolution: invalid
