# Issue 6540: [with patch, needs review] g.add_edge((u,v), label=l) syntax unsupported for C graphs

Issue created by migration from https://trac.sagemath.org/ticket/6540

Original creator: rlm

Original creation time: 2009-07-16 00:53:02

Assignee: rlm

CC:  jason




---

Attachment


---

Comment by jason created at 2009-07-18 22:09:17

This looks good and passes tests in graph.py.

The function has a blanket except: statement, which should instead trap the specific error it is expecting.  But that is not this issue.

As a side note, I think there are too many syntax choices for creating edges, which not only creates obscure corner cases and parsing code like this, but also leads to code that goes against the python philosophy that there should be one way to do things ("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6540/trac_6540-edge_syntax.patch").  I don't have time to do anything about it, so this is just a hollow complaint now :).


---

Comment by mvngu created at 2009-07-19 14:04:11

Resolution: fixed
