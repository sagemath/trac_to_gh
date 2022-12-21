# Issue 1045: [with patch] graphs: add eulerian testing and circuit-finding

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-10-31 21:47:58

Assignee: was

Keywords: graphs

This patch adds is_eulerian to graphs and digraphs and adds an eulerian_circuit function which uses Fleury's algorithm to find an eulerian circuit in a graph.


---

Attachment

Just some bookkeeping...


---

Comment by mabshoff created at 2007-11-01 09:59:02

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 09:59:02

applied to 2.8.11.alpha0
