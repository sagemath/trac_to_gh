# Issue 5571: fast_callable improvements (followup for #5093)

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-03-19 23:55:04

Assignee: somebody

The code at #5093 is very good and ready to go in, but there are several improvements that have been suggested and agreed work on at a later date. They are posted here so we can merge and close the other ticket. 

Specifically, 

Not fixed:

* Robert's suggestion: an option that uses a fast domain, if it's there, but ignores the domain parameter if it's not (I don't mind the idea, and the implementation is easy; what should the syntax be? Part of my problem picking a syntax is that I don't want to promise that a specialized interpreter is always faster than the Python-object interpreter, so I don't particularly want to use the word "fast" in any option names.)

* fast_callable on list,tuple,vector,matrix arguments

* any interaction with #5413 (my plan is to wait until either #5093 or #5413 gets a positive review, then fix the other one to match)

* fast_callable on constant arguments (waiting for a spec from Jason!)

* fast_callable of a zero multivariate polynomial returns a zero of the base ring, without paying attention to the types of the arguments




---

Comment by cwitty created at 2009-03-20 06:11:44

Duplicate of #5572


---

Comment by cwitty created at 2009-03-20 06:11:44

Resolution: duplicate
