# Issue 7904: is_gallai_tree

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-01-12 08:16:07

Assignee: rlm

From the docstring : 
A graph is a Gallai tree if and only if it is connected and its `2`-connected components are all isomorphic to complete graphs or odd cycles.

This patch also slightly touches the function is_clique, which was unnecessarily copying the whole graph 2 times :
* Firstly, using the subgraph method
* Secondly, using the to_simple method


---

Attachment


---

Comment by ncohen created at 2010-01-12 08:16:42

Changing status from new to needs_review.


---

Comment by jason created at 2010-03-17 05:27:20

Changing type from defect to enhancement.


---

Comment by ncohen created at 2010-05-20 20:07:56

Changing priority from major to minor.


---

Comment by rlm created at 2010-06-18 23:56:51

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-29 16:46:57

Resolution: fixed
