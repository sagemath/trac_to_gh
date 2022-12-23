# Issue 4445: is_isomorphic throws an error when the graph is compared to itself

Issue created by migration from https://trac.sagemath.org/ticket/4445

Original creator: jason

Original creation time: 2008-11-05 15:04:17

Assignee: rlm

Consider:


```
sage: g=graphs.HeawoodGraph()
sage: g.is_isomorphic(g)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.5/site-packages/sage/graphs/graph.pyc in is_isomorphic(self, other, certify, verbosity, edge_labels)
   6540             G2 = other; partition2 = [other.vertices()]
   6541         from sage.misc.flatten import flatten
-> 6542         isom = isomorphic(G, G2, partition, flatten(partition2, max_level=1), (self._directed or self.loops()), 1)
   6543         if not isom and certify:
   6544             return False, None

/home/jason/sage/local/lib/python2.5/site-packages/sage/groups/perm_gps/partn_ref/refinement_graphs.so in sage.groups.perm_gps.partn_ref.refinement_graphs.isomorphic (sage/groups/perm_gps/partn_ref/refinement_graphs.c:9946)()

TypeError: 'NoneType' object is unsubscriptable
```


However, 

```
sage: g.is_isomorphic(graphs.HeawoodGraph())
True
```




---

Attachment

This does indeed seem to fix the problem.  Thanks for the speedy work!  doctests in graph.py pass.

Positive review.


---

Comment by mabshoff created at 2008-11-05 21:25:37

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-05 21:25:37

Resolution: fixed
