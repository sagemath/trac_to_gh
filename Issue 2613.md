# Issue 2613: Moving "all_paths()" to "GenericGraph"

Issue created by migration from https://trac.sagemath.org/ticket/2613

Original creator: vgermrk

Original creation time: 2008-03-20 14:29:48

Assignee: rlm

The class Graph has a method "all_paths", but DiGraph don't.


---

Attachment


---

Comment by vgermrk created at 2008-03-20 15:07:48

I moved all_paths() and interior_paths() (with modifications) to class GenericGraph


---

Comment by rlm created at 2008-03-20 20:17:02

The code looks sensible, but you haven't created any new doctests to demonstrate the case of a DiGraph in either function!


---

Attachment


---

Comment by vgermrk created at 2008-03-21 12:55:43

The second patch adds doctests for all_paths() and interior_paths() of DiGraphs.


---

Comment by rlm created at 2008-03-21 20:55:48

Looks good, all tests in `graph.py` pass.


---

Comment by mabshoff created at 2008-03-22 04:02:15

Merged in Sage 2.11.alpha0 - all doctests pass [except know issues]


---

Comment by mabshoff created at 2008-03-22 04:02:15

Resolution: fixed
