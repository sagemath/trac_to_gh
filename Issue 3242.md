# Issue 3242: [with patch, needs review] Fix little bug in G.relabel() for G a graph...

Issue created by migration from https://trac.sagemath.org/ticket/3242

Original creator: rlm

Original creation time: 2008-05-17 19:14:18

Assignee: rlm

Reported by Chris Godsil:

```
"""
bad4.txt

Created by Chris Godsil on 2008-05-14.

"""

I construct a graph P on 8 vertices from the Petersen graph.

PROBLEMS:
	(1) The command P.relabel() raises an error as shown, but seems to work.
	(2) An attempt to get the automorphism group again raises an error, as shown.
	(3) P.is_planar() raises an exceptions.KeyError.
	(4) Attempting to get the group before relabelling raises an error too.
	(5) Ditto for P.girth()
	
VERSION:
	sage: version()
	'SAGE Version 3.0, Release Date: 2008-04-21'

GRAPH CONSTRUCTION:
P = graphs.PetersenGraph()
P.delete_edge([0,1])
P.add_edge([4,5])
P.add_edge([2,6])
P.delete_vertices([0,1])

sage: P.degree()  
[3, 3, 3, 3, 3, 3, 3, 3]

sage: P.vertices()
[2, 3, 4, 5, 6, 7, 8, 9]


ERRORS:
sage: P.relabel()
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call last)

/Users/chrisgodsil/Documents/sgwork/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in relabel(self, perm, inplace, return_map)
   5791             new_pos = {}
   5792             for v in self._pos:
-> 5793                 new_pos[perm[v]] = self._pos[v]
   5794             self._pos = new_pos
   5795         self._boundary = [perm[v] for v in self._boundary]

<type 'exceptions.KeyError'>: 0

sage: P.vertices()
[0, 1, 2, 3, 4, 5, 6, 7]


sage: P.automorphism_group()
---------------------------------------------------------------------------
<type 'exceptions.KeyError'>              Traceback (most recent call last)

/Users/chrisgodsil/Documents/sgwork/<ipython console> in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in automorphism_group(self, partition, translation, verbosity, edge_labels, order, return_group, orbits)
   6159                     a,b = A
   6160             else:
-> 6161                 a = search_tree(self, partition, dict_rep=False, lab=False, dig=dig, verbosity=verbosity, order=order)
   6162                 if order:
   6163                     a,c = a

/Users/chrisgodsil/Documents/sgwork/graph_isom.pyx in sage.graphs.graph_isom.search_tree (sage/graphs/graph_isom.c:8990)()

/Applications/sage/local/lib/python2.5/site-packages/sage/graphs/graph.py in relabel(self, perm, inplace, return_map)
   5791             new_pos = {}
   5792             for v in self._pos:
-> 5793                 new_pos[perm[v]] = self._pos[v]
   5794             self._pos = new_pos
   5795         self._boundary = [perm[v] for v in self._boundary]

<type 'exceptions.KeyError'>: 8
```



---

Attachment


---

Comment by jason created at 2008-05-22 17:11:33

looks good to me, passes doctests in graph/


---

Comment by mabshoff created at 2008-05-22 20:13:10

Resolution: fixed


---

Comment by mabshoff created at 2008-05-22 20:13:10

Merged in Sage 3.0.2.rc0
