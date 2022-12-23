# Issue 2473: [with patch, needs review] BipartiteGraph.__init__ does not properly initialize for some inputs

Issue created by migration from https://trac.sagemath.org/ticket/2473

Original creator: rhinton

Original creation time: 2008-03-11 22:03:53

Assignee: rlm

BipartiteGraph.__init__ does not call the base class __init__ for some inputs, leaving the object unusable.  For example, 

```
sage: B = BipartiteGraph(None)
sage: B
```

will throw an exception because the base class attributes have not been initialized.  The attached patch ensures the base class __init__ is called.


---

Comment by rlm created at 2008-03-12 00:23:06

The problem with this approach is it allows one to construct graphs which are not bipartite, but they will be instances of BipartiteGraph. What should be done instead is to raise a NotImplementedError, so that the user knows that the initialization failed. This problem is a small part of the much bigger task in ticket #1941, which is one of the next things I'll be doing. Watch for a patch in the next few days, perhaps...


---

Attachment

try #2


---

Attachment

The updated patch, I believe, addresses your concerns.  It also fixes several more bugs.


---

Comment by rlm created at 2008-03-12 19:40:15

Is patch 2 supposed to replace patch 1?


---

Comment by rlm created at 2008-03-13 02:23:50

Some notes:

1. "TESTS" should actually be labeled "EXAMPLE" or "EXAMPLES". This is just the convention.

2. Comments in the examples don't need "#"; see many other doctests for examples of the formatting.

3. I've moved the networkx import further down so it only happens if it needs to. This import, if it hasn't been done before, takes several seconds... (I know this doesn't seem to make much sense now, but soon we won't be importing networkx by default whenever we have a graph, so it will make sense eventually.)


---

Attachment

Apply bipartite_graph_input.2.patch, then this.


---

Comment by mabshoff created at 2008-03-13 12:45:52

Resolution: fixed


---

Comment by mabshoff created at 2008-03-13 12:45:52

Merged in Sage 2.10.4.alpha0
