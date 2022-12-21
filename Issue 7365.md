# Issue 7365: Petersen's 2-factor theorem

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-31 20:53:35

Assignee: rlm

Implement a function corresponding to Petersen's theorem on 2-factors.

This theorem says that any 2r-regular graphs can be decomposed in 2-factors. If the graph is not regular and is of maximum degree Delta, then it can be decomposed as an union of Delta/2 disjoints (<=2)-factors.


---

Comment by ncohen created at 2009-11-18 18:09:22

Changing status from new to needs_review.


---

Comment by rlm created at 2009-12-15 17:27:17

If you're introducing a new module in sage.graphs, the header of the file should be much more descriptive of what the module is for, etc... Take a look at some of the other files for examples.

I'm (personally) very curious about what else you plan on including in `graph_decompositions`...

The patch applies cleanly, and the code looks good. Once again, I'd like to see a little more examples in the documentation.


---

Comment by rlm created at 2009-12-15 17:27:17

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-18 08:51:02

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-18 08:51:02

Hello !!!

As mentionned, I moved this function toward graph.py, and will patiently wait for the splitting of graph.py to begin creating new files.. :-)

(please do not forget to install GLPK or CBC before testing it because of #7734)

Nathann


---

Attachment

I tried to find another example, but could not find any interesting/funny one (the theorem and its proof by themselves are enough to make me laugh :-) ). If you can think of a good one, just tell me and I'll add it :-)

Nathann


---

Attachment


---

Comment by rlm created at 2009-12-18 19:22:58

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2009-12-19 22:59:07

Resolution: fixed
