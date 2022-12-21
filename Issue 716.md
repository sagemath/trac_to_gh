# Issue 716: graph functions to_undirected and to_directed forget the loops and multiple edges

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-20 20:07:16

Assignee: was

Keywords: graph, graphs


With a directed graph g
 * g.to_directed() forgets multiedges, remembers loops
 * g.to_undirected() forgets multiedges and loops

With an undirected graph g
 * g.to_directed() forgets multiedges and loops
 * g.to_undirected() forgets multiedges, remembers loops


In each of these cases, both multiedges and loops should be remembered.


```
sage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)
sage: g.to_directed().multiple_arcs()
False
sage: g.to_directed().loops()
True
sage: g.to_undirected().multiple_edges()
False
sage: g.to_undirected().loops()
False
sage: g=Graph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)
sage: g.to_directed().multiple_arcs()
False
sage: g.to_directed().loops()
False
sage: g.to_undirected().multiple_edges()
False
sage: g.to_undirected().loops()
True
```






---

Comment by jason created at 2007-09-20 20:12:46

Apparently the copy doesn't preserve multiple edges settings.


```
sage: g=DiGraph({0:[0,1,1,2],1:[0,1]},loops=True,multiedges=True)
sage: g==g.copy()
False
sage: g.multiple_arcs()
True
sage: g.copy().multiple_arcs()
False
```



---

Comment by jason created at 2007-09-20 21:29:12

The real problem is that the __init__ function tests for a superclass before a subclass.  The attached patch fixes it (and also adds a to_simple function that _does_ forget multiple edges, loops, and directions on edges).

The attached patch may break some of the doctests in graph.py, though.


---

Attachment


---

Attachment

Fixes doctest failures and other strangeness


---

Attachment


---

Attachment


---

Attachment


---

Comment by rlm created at 2007-09-21 02:06:07

Resolution: worksforme


---

Attachment


---

Comment by jason created at 2007-09-28 20:52:50

As a side note, the above patches which were applied also changed all "arc" functions to "edge" functions.  This, of course, broke backward compatibility.


---

Comment by mabshoff created at 2007-10-24 17:29:59

I am curious if all those patches really were applied. They are over a months old, so I would assume so, but I do not understand why this ticket wasn't closed then.

Michael


---

Comment by mabshoff created at 2007-10-24 19:04:22

Resolution changed from worksforme to 


---

Comment by mabshoff created at 2007-10-24 19:04:22

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-24 19:04:31

Resolution: fixed


---

Comment by mabshoff created at 2007-10-24 19:08:48

From Robert:

```
Michael,

Regarding ticket #716, these patches were incorporated a while ago,
and I closed the ticket last month when that happened. It looks like
the ticket has been closed, but in a future milestone, ever since...
```


Cheers,

Michael
