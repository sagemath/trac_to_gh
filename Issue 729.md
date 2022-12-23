# Issue 729: graphs: Implement __eq__ and __neq__ rather than __cmp__

Issue created by migration from https://trac.sagemath.org/ticket/729

Original creator: jason

Original creation time: 2007-09-21 17:56:12

Assignee: was

Keywords: graphs

The rich comparison operators __eq__ and __neq__ are preferred in Python.  See [http://docs.python.org/ref/customization.html](http://docs.python.org/ref/customization.html)


---

Comment by rlm created at 2007-10-22 01:36:10

This is actually crucial in the graph_isom code: there, not just equality comparison, but actually finding which graph is smaller is important. There is a specific enumeration of graphs coded, and under that enumeration, __cmp__ gives exactly what it means. This method cannot be removed.


---

Comment by rlm created at 2007-10-22 01:36:10

Resolution: invalid


---

Comment by mabshoff created at 2007-10-22 07:03:23

Please do not close tickets unless explicitly asked to do so. You can recommend to close a ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-22 07:03:51

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-22 07:03:51

Resolution changed from invalid to 


---

Comment by rlm created at 2007-10-22 16:30:30

Actually, I was wrong on two counts - count 1, the graph_isom code actually re-implements the enumeration, so it doesn't actually depend on __cmp__, and count 2, you're right about rich comparison, but instead of just __eq__ and __neq__, there should also be __lt__, __le__, etc. However, this would all be part of an overhaul on how graph enumeration is done in general, so this could be part of ticket #749.


---

Comment by malb created at 2007-10-23 18:01:14

This is duplicate because #749 takes care of it.


---

Comment by malb created at 2007-10-23 18:01:14

Resolution: duplicate
