# Issue 904: [with patch] graphs: clique-testing

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-10-15 22:19:21

Assignee: was

Keywords: graphs

This adds is_clique and is_indendent_set functions to undirected graphs.


---

Attachment


---

Comment by jason created at 2007-10-17 16:11:38

Updated patch clique_ind_set-2.patch.  Apply this instead of the first patch.

This adds an option to the is_clique to check if it is a directed clique (i.e., edges in each direction exist) in the case the graph is a directed graph.  This patch also puts both functions into GeneralGraph to make them available to directed graphs.  It also deletes the (now redundant) independent_set function in GeneralGraph.

This functionality now gives us the Combinatorica EmptyQ and CompleteQ functions, as well as the CliqueQ and IndependentSetQ functions.


---

Attachment

Replaces the first patch above.


---

Comment by rlm created at 2007-10-21 04:31:24

This patch looks ready for inclusion. Jason -- do you notice any other functions that could be moved to GeneralGraph?


---

Comment by malb created at 2007-10-23 22:17:43

Resolution: fixed


---

Comment by malb created at 2007-10-23 22:17:43

merged into 2.8.9.alpha0
