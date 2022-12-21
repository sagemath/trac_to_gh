# Issue 8672: SCIP support

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-04-11 12:32:06

Assignee: jason, jkantor

CC:  malb schilly r.gaia.cs

Based upon Harald Schilly's SPKG for SCIP, here is a patch to enable the use of this solver through the usual interface for LP.

Nathann


---

Comment by ncohen created at 2010-04-11 12:33:26

Changing status from new to needs_review.


---

Comment by schilly created at 2010-04-11 12:44:33

wow, thank you!! just one thing, is it possible to enable verbose output if enabled? i don't know which parameter you have to set in Sage's MIP interface, but it is  scip.solver(quiet=False) in scip.


---

Comment by ncohen created at 2010-04-11 12:54:53

Fixed ! The corresponding argument in sage is log=# in the solve method. 0 for no output, and integers to have progressdively more (only GLPk has different levels of output though, the others only understand 0/1 or none at all )

Nathann


---

Attachment


---

Comment by malb created at 2010-06-02 21:30:05

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-06-02 21:30:05

Hi Nathann,

two small things:

 * `solve_scip` has no documentation/doctests 
 * "the default solver is used (COIN if available, GLPK otherwise)" seems to be inaccurate since you also try SCIP whether it is available


---

Comment by ncohen created at 2010-09-06 11:13:10

Changing component from numerical to linear programming.


---

Comment by mkoeppe created at 2016-03-30 20:43:52

Duplicate of #10879, so I'm marking this one as "needs_review" so it can be closed -- hoping this is the correct procedure.


---

Comment by mkoeppe created at 2016-03-30 20:43:52

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2016-04-07 20:13:43

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
