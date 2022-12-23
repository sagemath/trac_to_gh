# Issue 6238: possible failure in is_planar(set_embedding=True, set_pos=False)

Issue created by migration from https://trac.sagemath.org/ticket/6238

Original creator: ncalexan

Original creation time: 2009-06-06 23:37:56

Assignee: rlm

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


---

Attachment

The problem is that you are never asking the graph to remember the embedding, so when you show the graph, you are just looking at some random embedding.

The way to do what you're trying to do is to ask the graph to remember the planar positioning:

```
sage: G.is_planar(set_embedding=True, set_pos=True)
```


i.e. change a 'False' to a 'True'. :)


---

Comment by rlm created at 2009-07-13 21:32:00

Resolution: invalid
