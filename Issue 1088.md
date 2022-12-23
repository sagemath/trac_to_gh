# Issue 1088: [with patch] graphs: minimum spanning tree function

Issue created by migration from https://trac.sagemath.org/ticket/1088

Original creator: jason

Original creation time: 2007-11-03 20:45:05

Assignee: mhansen

Keywords: graphs

Here's an implementation of a minimum spanning tree function.  Well, actually 3 implementations, defaulting to Kruskal's algorithm.


---

Attachment


---

Attachment


---

Comment by was created at 2007-11-03 23:38:14

Resolution: fixed


---

Comment by jason created at 2007-11-06 22:36:49

Resolution changed from fixed to 


---

Comment by jason created at 2007-11-06 22:36:49

Changing status from closed to reopened.


---

Comment by jason created at 2007-11-06 22:36:49

I believe there is a bug in the code change of the doc_1088 patch above.  The third patch (1088-correct-bugs-improve-doctests.patch) reverses this change, reimplements the doctests, and makes the code faster by sorting using key instead of cmp.

The third doctest should be applied after the first two doctests.


---

Attachment


---

Comment by jason created at 2007-11-06 22:38:20

The third patch above also corrects a bug in the original code.


---

Comment by mabshoff created at 2007-11-06 23:54:16

Resolution: fixed
