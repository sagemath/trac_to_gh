# Issue 7672: topological_sort in c_graphs

Issue created by migration from https://trac.sagemath.org/ticket/7672

Original creator: ncohen

Original creation time: 2009-12-12 18:14:14

Assignee: rlm

The function topological_sort uses Networkx for the moment. As c_graphs are to become the standard implementation of graphs in Sage, this function should be rewritten in Cython.


---

Comment by ncohen created at 2010-06-06 11:00:45

Changing status from new to needs_work.


---

Comment by ncohen created at 2011-01-01 13:25:38

Resolution: fixed


---

Comment by ncohen created at 2011-01-01 13:25:38

Done at #10432
