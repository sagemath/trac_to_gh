# Issue 8132: fix documentation related to ODE solvers

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-01-31 00:32:02

Assignee: mvngu

The documentation to ODE solvers is not written in harmony with Sage developers guide and the Sage Constructions are outdated. 


---

Attachment


---

Comment by robert.marik created at 2010-01-31 00:38:00

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-01-31 00:58:12

this patch

* fixes indentation in sage/gsl/ode.pyx from 3 spaces to 4 spaces

* fixes documentation


---

Attachment

fixes one failed doctest, apply on the top of previous poatch


---

Comment by wdj created at 2010-01-31 14:59:05

This seems to be an excellent and extremely welcomed collection of docstring fixes related to solving differential equations in Sage.

 Am I missing something or is it odd that calculus/desolver is not listed http://www.sagemath.org/doc/reference/modindex.html? Using
http://www.sagemath.org/doc/developer/sage_manuals.html#building-the-manuals
I see how to rebuild the manual but how do I see what the changes in the patch look like if 
desolver isn't even in the manual in the first place?

Can a patch be added to include desolver in the manual?


---

Comment by robert.marik created at 2010-01-31 16:27:50

Fixed thanks. Thanks for the links how to do it.
Two new chapters are at the end of Symbolic Calculus.

PDF manual does not build, partly due to #8036, patly due to another problem not related to this ticket (unknown command \cross used in some file related to polynomials). The ODE part of PDF manual looks good, anyway.

Html version looks good for me.


---

Comment by robert.marik created at 2010-01-31 16:28:28

apply on the top of the previous two patches


---

Attachment

btw: the second problem which caused pdf not to build has been fixed by #8021


---

Comment by wdj created at 2010-01-31 22:31:17

Three patches apply fine to 4.3.2.a0 and passes sage -testall, except for apparently unrelated failures already reported, on a mac 10.6.2.

Very nice docstring patch Robert!

Positive review.


---

Comment by wdj created at 2010-01-31 22:31:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-02 02:21:30

Resolution: fixed


---

Comment by mvngu created at 2010-02-02 02:21:30

Merged in the following order:

 1. [trac_8132.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132.patch)
 1. [trac_8132_fixed_doctests.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132_fixed_doctests.patch)
 1. [trac_8132_fixed_reference_manual.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8132/trac_8132_fixed_reference_manual.patch)
