# Issue 7564: graph theory: examples on degree sequences

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-11-30 20:07:28

Assignee: rlm

The degree sequence of a graph is a basic property that is studied in an introductory course on graph theory. There should be examples explaining how to compute the degree sequence of a given graph.


---

Comment by mvngu created at 2009-11-30 21:45:04

The patch `trac_7564-degree-sequences.patch` adds two examples to the method `GenericGraph.degree()`, showcasing how to obtain the degree sequence of a graph using that method.


---

Comment by mvngu created at 2009-11-30 21:45:04

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-11-30 22:08:03

I will ask for more, if it isn't too much trouble.  Could there be a small wrapper to (the better one) called degree_sequence as well?  I realize this is very low priority.  If the graph theory tour ever gets back up, this would be ideal to put in it as well.


---

Comment by kcrisman created at 2009-11-30 22:08:03

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2009-11-30 22:26:05

Replying to [comment:2 kcrisman]:
> Could there be a small wrapper to (the better one) called degree_sequence as well?

As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.




> If the graph theory tour ever gets back up, this would be ideal to put in it as well.

Nod.


---

Comment by kcrisman created at 2009-11-30 22:52:05

Replying to [comment:3 mvngu]:
> Replying to [comment:2 kcrisman]:
> > Could there be a small wrapper to (the better one) called degree_sequence as well?
> 
> As I mentioned in my [email](http://groups.google.com/group/sage-devel/browse_thread/thread/8edd29e9bddc67e5) to sage-devel, I'm unable to find a function or method in the graph theory module that computes the degree sequence of a given graph. So there is no function or method for wrapping, unless you can point me to such a method/function. On the other hand, are you suggesting that there be a method in the class `GenericGraph` called `degree_sequence()` that does exactly as its name implies? If so, then that could be done.

Yes, that is exactly what I meant - wrapping the examples you provide, as it were.  I don't have time to do this, unfortunately, though it should be pretty easy.


---

Comment by mvngu created at 2009-12-01 03:01:39

The (new) patch `trac_7564-degree-sequences.patch` defines the method `GenericGraph.degree_sequence()` for computing the degree sequence of a graph.


---

Comment by mvngu created at 2009-12-01 03:01:39

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2009-12-01 06:25:15

Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)


---

Comment by mvngu created at 2009-12-01 07:28:37

based on Sage 4.3.alpha0


---

Attachment

Replying to [comment:6 ncohen]:
> Could it be possible to define in the same patch functions outdegree_sequence and indegree_sequence for DiGraphs ? :-)

Y-E-S, yes! :-)



The patch `trac_7564-degree-sequences.patch` implements the following degree sequences:

 1. `degree_sequence()` --- the degree sequence of a (di)graph. This is implemented in the class `GenericGraph`.
 1. `in_degree_sequence()` --- the indegree sequence of a digraph. This is implemented in the class `DiGraph`.
 1. `out_degree_sequence()` --- the outdegree sequence of a digraph, also implemented in the class `DiGraph`.
 
I use the method names `in_degree_sequence()` and `out_degree_sequence()` to be consistent with how the graph theory module names the indegree and outdegree methods.


---

Comment by ncohen created at 2009-12-01 07:54:50

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-01 07:54:50

Excellent ! Approved :-)

Thank you for contributing to the Graph Section !! :-)


---

Comment by mhansen created at 2009-12-01 08:23:36

Resolution: fixed


---

Comment by ncohen created at 2009-12-01 08:36:08

A patch written, reviewed and merged in 11 hours ? O_O

God O_O
