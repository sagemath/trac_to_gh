# Issue 7358: Strong orientations of 2-connected graphs

Issue created by migration from https://trac.sagemath.org/ticket/7358

Original creator: ncohen

Original creation time: 2009-10-31 08:44:40

Assignee: rlm

A special case of #7303 ( which is much easier and efficient to implement ) is to find a strongly connected orientation of the edges of a bridgeless connected graph.

This can be done using the short algorithm given in :
Schriver Combinatorial optimization
Volume B 
page 1037


---

Comment by ncohen created at 2009-11-01 19:56:27

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-11-01 19:56:27

Here it is !!!


---

Comment by rlm created at 2009-12-15 17:22:17

1. You need to describe what a strongly connected orientation is in your docstrings.

2. You also need to clearly describe the output, i.e. what type of object is it...

3. The function shouldn't assume but rather check whether the necessary conditions are met, and print a helpful error message if they aren't. If you're concerned about speed, then you can make use of a `check=False` option.

Other than these minor issues, the patch applies and passes tests, and looks good.


---

Comment by rlm created at 2009-12-15 17:22:17

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-12-16 01:03:10

I added a definition of both "orientation" and "strong", plsu a reference to the wikipedia page, and described the output. This function is actually useful in both situations ( when the graph is not 2-connected, or when it is ), so I removed "of a 2-connected graph" in the first sentence of the docstring : it is explicitely written later that if the graph is not 2-connected, the result will be "as best as can be hoped for" in this situation ( and I assure you this part of the function is useful by itself :-) )


---

Comment by ncohen created at 2009-12-16 01:03:10

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by rlm created at 2009-12-16 03:11:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 21:54:50

Resolution: fixed
