# Issue 460: AttributeError: 'Graphics' object has no attribute 'append'

Issue created by migration from https://trac.sagemath.org/ticket/460

Original creator: mhansen

Original creation time: 2007-08-19 14:27:28

Assignee: was

Hello,

one of the graphics patches applied during Bug Day 1 causes the
following problem:

**********************************************************************
File "graph_isom.pyx", line 802:
   sage: SD.plot(pos=posn, vertex_size=400,
vertex_colors={'#FFFFFF':range(1,19)},
edge_labels=True).save('search_tree.png')
Exception raised:
   Traceback (most recent call last):
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/
doctest.py", line 1212, in __run
       compileflags, 1) in test.globs
     File "<doctest __main__.example_8[14]>", line 1, in <module>
       SD.plot(pos=posn, vertex_size=Integer(400),
vertex_colors={'#FFFFFF':range(Integer(1),Integer(19))},
edge_labels=True).save('search_tree.png')###line 802:
   sage: SD.plot(pos=posn, vertex_size=400,
vertex_colors={'#FFFFFF':range(1,19)},
edge_labels=True).save('search_tree.png')
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/graphs/graph.py", line 2330, in plot
       G = networkx_plot(self._nxg, pos=pos,
vertex_labels=vertex_labels, vertex_size=vertex_size,
vertex_colors=vertex_colors, edge_colors=edge_colors,
graph_border=graph_border, scaling_term=scaling_term)
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/plot/plot.py", line 2594, in networkx_plot
       g.append(NGP)
   AttributeError: 'Graphics' object has no attribute 'append'

This happens all over the code.

Cheers,

Michael



---

Comment by rlm created at 2007-08-19 16:45:06

Resolution: fixed


---

Comment by rlm created at 2007-08-19 16:45:06

Fix is here:

http://sage.math.washington.edu/home/rlmill/plot.patch
