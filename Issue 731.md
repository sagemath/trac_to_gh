# Issue 731: graphs: set_boundary accepts integers

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-21 18:54:22

Assignee: was

Keywords: graphs


```
sage: g=Graph({0:[1,2],1:[2]})
sage: g.set_boundary(1)
sage: g._boundary()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-graphs2/sage/graphs/<ipython console> in <module>()

<type 'exceptions.TypeError'>: 'sage.rings.integer.Integer' object is not callable
```




---

Comment by jason created at 2007-09-21 18:57:32

The above behavior is consistent.  However, because _boundary is now an integer, we get other errors:


```
sage: enum(g)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-graphs2/sage/graphs/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in enum(graph, quick)
   6014                 enumeration += 1 << ((n-(i+1))*n + n-(j+1))
   6015         return enumeration
-> 6016     M = graph.am()
   6017     for i, j in M.nonzero_positions():
   6018         enumeration += 1 << ((n-(i+1))*n + n-(j+1))

/home/grout/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in am(self)
   1832
   1833         """
-> 1834         return self.adjacency_matrix()
   1835
   1836     def complement(self):

/home/grout/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in adjacency_matrix(self, sparse)
   3415         """
   3416         n = len(self._nxg.adj)
-> 3417         verts = self.vertices()
   3418         D = {}
   3419         for e in self.edge_iterator():

/home/grout/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in vertices(self)
    738         int_verts = []
    739         for v in self.vertex_iterator():
--> 740             if v in self._boundary:
    741                 bdy_verts.append(v)
    742             else:

<type 'exceptions.TypeError'>: argument of type 'sage.rings.integer.Integer' is not iterable
sage: g._boundary()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-graphs2/sage/graphs/<ipython console> in <module>()

<type 'exceptions.TypeError'>: 'sage.rings.integer.Integer' object is not callable
```



---

Comment by rlm created at 2007-10-22 01:33:48

The problem is that you are calling the property (not the function) with parentheses:

try

sage: g=Graph({0:[1,2],1:[2]})
sage: g.set_boundary(1)
sage: g.get_boundary()
[]


The source code is:

    def set_boundary(self, boundary):
        if isinstance(boundary,list):
            self._boundary = boundary

This is as of 2.8.8.1, so I think we can call this fixed.


---

Comment by rlm created at 2007-10-22 01:33:48

Resolution: worksforme


---

Comment by mabshoff created at 2007-10-22 07:02:17

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-22 07:02:17

Resolution changed from worksforme to 


---

Comment by mabshoff created at 2007-10-22 07:03:02

Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.

Cheers,

Michael


---

Comment by malb created at 2007-10-23 21:15:23

closing for good.


---

Comment by malb created at 2007-10-23 21:15:23

Resolution: invalid
