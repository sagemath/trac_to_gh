# Issue 2265: fix shortest_path_all_pairs

Issue created by migration from https://trac.sagemath.org/ticket/2265

Original creator: rlm

Original creation time: 2008-02-22 19:29:13

Assignee: rlm


```
sage: C = graphs.CubeGraph(4)
sage: C.shortest_paths('0000')

{'0000': ['0000'],
...
 '1111': ['0000', '0100', '0110', '1110', '1111']}
sage: C.shortest_path_all_pairs()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/rlmill/sage/<ipython console> in <module>()

/Users/rlmill/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in shortest_path_all_pairs(self)
   2245             for u in verts:
   2246                 for v in verts:
-> 2247                     if dist[u][v] > dist[u][w] + dist[w][v]:
   2248                         dist[u][v] = dist[u][w] + dist[w][v]
   2249                         pred[u][v] = pred[w][v]

<type 'exceptions.TypeError'>: unsupported operand type(s) for +: 'int' and 'NoneType'
```



---

Comment by jason created at 2008-02-22 19:32:45

This works for me on ubuntu 7.10, 32-bit, sage 2.10.1:


```
sage: C=graphs.CubeGraph(4)
sage: C.shortest_paths('0000')

{'0000': ['0000'],
 '0001': ['0000', '0001'],
 '0010': ['0000', '0010'],
 '0011': ['0000', '0001', '0011'],
 '0100': ['0000', '0100'],
 '0101': ['0000', '0100', '0101'],
 '0110': ['0000', '0100', '0110'],
 '0111': ['0000', '0100', '0110', '0111'],
 '1000': ['0000', '1000'],
 '1001': ['0000', '1000', '1001'],
 '1010': ['0000', '1000', '1010'],
 '1011': ['0000', '0001', '0011', '1011'],
 '1100': ['0000', '1000', '1100'],
 '1101': ['0000', '0100', '0101', '1101'],
 '1110': ['0000', '0100', '0110', '1110'],
 '1111': ['0000', '0100', '0110', '1110', '1111']}
```



---

Comment by jason created at 2008-02-22 19:33:35

Never mind, I see that the error was something different.  I get the same error.


---

Comment by jason created at 2008-02-22 20:04:48

The problem was that we were blindly adding the labels to edges, so if an edge didn't have a label, things went boom.

I added a default_weight option which will be applied when an edge doesn't have a weight.


---

Attachment

I also added a by_weight option as vgermrk suggested to be consistent with the other shortest path functions.


---

Comment by rlm created at 2008-02-22 21:22:40

I haven't run doctests yet, but pending that, everything looks good.


---

Comment by mabshoff created at 2008-02-24 18:11:45

Testall passes with that patch, so with rml's review I am giving this a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-24 18:14:47

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 18:14:47

Merged in Sage 2.10.3.alpha0
