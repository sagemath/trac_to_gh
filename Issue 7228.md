# Issue 7228: [with patch, need review] Generalized Petersen graph generator

Issue created by migration from https://trac.sagemath.org/ticket/7228

Original creator: AJonsson

Original creation time: 2009-10-15 15:29:31

Assignee: rlm

This patch introduces a generator for the generalized Petersen graphs.

http://mathworld.wolfram.com/GeneralizedPetersenGraph.html
http://en.wikipedia.org/wiki/Petersen_graph#Generalized_Petersen_graphs

The method used for plotting gives exactly the same result as the Petersen, Desargues, and the Moebius-Kantor graphs, so these functions have been simplified to just call GeneralizedPetersenGraph() with suitable parameter values and then change the graph's name to the named graph in question.

Patch is made against sage 4.1.2


---

Comment by AJonsson created at 2009-10-15 15:31:20

generator for generalized Petersen graphs


---

Comment by AJonsson created at 2009-10-15 15:33:12

Changing status from new to needs_review.


---

Attachment


---

Comment by ncohen created at 2009-10-18 13:39:30

This patch seems perfect to me ! I just modified the name of this graph so that it includes the values of n and k, and added some ` somewhere.

If you agree with these, you can set this ticket to positive review !


---

Attachment

Thanks for your review, I agree with all changes. I noticed however that my patch caused a test to fail in graph.py (a test that looks up the coordinates of all vertices of the Petersen Graph). The failure was trivial, the main reason was that I had placed the nodes at larger distance from (0,0) than before.

I have fixed these position issues in this new patch, which should be applied on top of trac_7228-reviewer.patch


---

Attachment

fixes failure of position test


---

Comment by ncohen created at 2009-10-20 14:28:09

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-10-20 14:28:09

good point !

Positive review !


---

Comment by mhansen created at 2009-10-21 04:47:31

Resolution: fixed
