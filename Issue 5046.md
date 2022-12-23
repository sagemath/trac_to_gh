# Issue 5046: converting between Graph and DiGraph naturally

Issue created by migration from https://trac.sagemath.org/ticket/5046

Original creator: jason

Original creation time: 2009-01-21 07:14:00

Assignee: rlm

This should work.  At the very minimum, there should be a sensible error message:


```
sage: DiGraph(graphs.PathGraph(4))                                             
---------------------------------------------------------------------------
NetworkXError                             Traceback (most recent call last)

/home/grout/.sage/<ipython console> in <module>()

/home/grout/sage-3.2.3/local/lib/python2.5/site-packages/sage/graphs/graph.pyc in __init__(self, data, pos, loops, format, boundary, weighted, implementation, sparse, vertex_labels, **kwds)
   8362             else:
   8363                 if implementation == 'networkx':
-> 8364                     self._backend = NetworkXGraphBackend(networkx.XDiGraph(data, selfloops=loops, **kwds))
   8365                 elif implementation == 'c_graph':
   8366                     if data is None:

/home/grout/sage-3.2.3/local/lib/python/networkx/xdigraph.py in __init__(self, data, name, selfloops, multiedges)
    118         self.multiedges=multiedges
    119         if data is not None:
--> 120             convert.from_whatever(data,create_using=self)
    121         self.name=name
    122 

/home/grout/sage-3.2.3/local/lib/python/networkx/convert.py in from_whatever(thing, create_using)
    114 
    115     raise networkx.NetworkXError, \
--> 116           "Input is not a known data type for conversion."
    117 
    118     return 

NetworkXError: Input is not a known data type for conversion.
sage: Graph(DiGraph({0:[1,2],1:[0,3]}))
---------------------------------------------------------------------------
NetworkXError                             Traceback (most recent call last)

/home/grout/.sage/<ipython console> in <module>()

/home/grout/sage-3.2.3/local/lib/python2.5/site-packages/sage/graphs/graph.pyc in __init__(self, data, pos, loops, format, boundary, weighted, implementation, sparse, vertex_labels, **kwds)
   7022                         self.add_vertices(xrange(data))
   7023                     else:
-> 7024                         self._backend = NetworkXGraphBackend(networkx.XGraph(data, selfloops=loops, **kwds))
   7025                 elif implementation == 'c_graph':
   7026                     if data is None:

/home/grout/sage-3.2.3/local/lib/python/networkx/xgraph.py in __init__(self, data, name, selfloops, multiedges)
    111         self.multiedges=multiedges
    112         if data is not None:
--> 113             self=convert.from_whatever(data,create_using=self)
    114         self.name=name
    115 

/home/grout/sage-3.2.3/local/lib/python/networkx/convert.py in from_whatever(thing, create_using)
    114 
    115     raise networkx.NetworkXError, \
--> 116           "Input is not a known data type for conversion."
    117 
    118     return 

NetworkXError: Input is not a known data type for conversion.
```




---

Comment by jason created at 2009-01-21 07:26:22

Currently, there are to_directed and to_undirected methods, but the above is the natural way to convert things in Sage.


---

Comment by jason created at 2009-01-21 07:27:14

Oh, and don't forget that you can specify whether loops are allowed or not.  That replaces the to_simple function.


---

Comment by rlm created at 2009-02-17 18:40:37

Fixed by the patch at #5171, I believe.


---

Comment by rlm created at 2009-02-17 18:43:45

I just checked this example:

```
sage: DiGraph(graphs.PathGraph(4))
Path Graph: Digraph on 4 vertices
```



---

Comment by mabshoff created at 2009-02-18 00:09:51

Resolution: fixed


---

Comment by mabshoff created at 2009-02-18 00:09:51

Fixed via #5171.

Cheers,

Michael
