# Issue 2676: [with patch, needs easy review] is_equitable: flatten flattens too much!

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-03-26 17:41:40

Assignee: rlm

This is the problem, which is now a doctest:

```
sage: ss = (graphs.WheelGraph(5)).line_graph(labels=False)
sage: prt = [[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]
sage: ss.is_equitable(prt)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/rlmill/sage-2.11.alpha1/<ipython console> in <module>()

/Users/rlmill/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py in is_equitable(self, partition, quotient_matrix)
   5477         from sage.misc.misc import uniq
   5478         if sorted(flatten(partition)) != self.vertices() or any(len(cell)==0 for cell in partition):
-> 5479             raise TypeError("Partition (%s) is not valid for this graph."%partition)
   5480         if quotient_matrix:
   5481             from sage.matrix.constructor import Matrix

<type 'exceptions.TypeError'>: Partition ([[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]) is not valid for this graph.
```


Reported by Chris Godsil.


---

Attachment


---

Attachment

Apply this as well. Fixes a related problem in the next function down. Also reported by Chris Godsil.


---

Attachment

Oops. Apply this one too. Fixes the original problem in the other function.


---

Comment by ekirkman created at 2008-03-27 21:34:30

These 3 patches fix the bug, are documented and pass the doctests.  Ready for inclusion.


---

Comment by mabshoff created at 2008-03-28 07:21:43

Well, not that I am paranoid, but applying all three patches works for me, too.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-28 07:21:54

Resolution: fixed


---

Comment by mabshoff created at 2008-03-28 07:21:54

Merged in Sage 2.11.alpha2
