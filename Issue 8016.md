# Issue 8016: graph_editor(p) should work for p a poset

Issue created by migration from https://trac.sagemath.org/ticket/8016

Original creator: rlm

Original creation time: 2010-01-20 20:21:57

Assignee: sage-combinat

CC:  saliola rkirov mpatel

Obviously `graph_editor(p)` doesn't work on its own, since `p` is not a graph. However, it should be possible to implement a few functions for `p` to make this work:


```
File "sage/graphs/graph_editor.py", line 111, in graph_editor
    if not isinstance(graph.get_pos(), dict):
AttributeError: 'FinitePoset' object has no attribute 'get_pos'
```


While wishing, it would also be nice if the graph editor could be adapted to remember vertex labels, at least in the case that the labels are strings.


---

Comment by jmantysalo created at 2015-10-21 07:09:21

If the name of variable to save the (undirected) graph is `P`, then it is easy to just say


```
d = DiGraph()
d.add_vertices(P.vertices())
pos = P.get_pos()
for e in P.edges(labels=False):
    if pos[e[0]][1] < pos[e[1]][1]:
        d.add_edge(e)
    else:
        d.add_edge([e[1], e[0]])
P = Poset(d).canonical_label()
```


to convert it to poset. But really somebody should expand the code to handle digraphs.


---

Comment by slelievre created at 2020-10-11 22:53:15

Somewhat related:

- #30214: Add to_digraph method to Permutation
