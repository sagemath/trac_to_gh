# Issue 8467: move the document "Linear Programming in Sage" to "Sage HOWTOs"

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-03-07 02:18:58

Assignee: mvngu

CC:  ncohen jason

Keywords: linear programming

Move the document "Linear Programming in Sage", found [here](http://www.sagemath.org/doc/constructions/linear_programming.html) and [here](http://www-sop.inria.fr/members/Nathann.Cohen/tut/LP/), to the classification "Sage HOWTOs". The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).


---

Comment by ncohen created at 2010-03-09 12:52:47

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-03-09 12:52:47

Here is where I have for the moment. I still need to rewrite LP examples for some problems, but at least I reformatted everything for Sphinx.

It will require the new LP patch enabling a new syntax for constraints #7311

Nathann


---

Comment by ncohen created at 2010-03-09 12:55:07

Oh yes, and there is also something to take care of : the new patch for CPLEX support brings changes to the current LP document in the Constructions manual... Only a few lines concerning CPLEX at the end of it, and some fixes, but we should not lose it when deleting the current document and replacing it with this one in the HOWTO manual :-)

Nathann


---

Comment by ncohen created at 2010-03-16 11:37:40

this version passes doctests !

Nathann


---

Comment by ncohen created at 2010-03-16 23:46:56

Here it is ! :-)


---

Comment by ncohen created at 2010-03-16 23:46:56

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by pang created at 2010-07-20 16:03:46

I've read up to the "Maximum average degree" problem, and I have some found some errata:

 * line 63: Errata on example LP
 * line 161: maximization instead of minimization
 * line 177: missing objective function
 * line 200-204: problem not written properly
 * line 204: alternative formulation with only one variable for each edge

I adjoint a rst file with corrections. The example on "Maximum average degree" is correct but I find it harder to follow than the previous ones, for a non-expert in graph-theory. I don't know which is the target audience...


---

Attachment

Thank you very much for reading it until then !!! Actually, I will need to change some parts of it now that GLPK is a standard SPKG. I will also update the end of it, to give more natural examples :-)

I am setting it to "needs work" until this is done !!

Nathann


---

Comment by ncohen created at 2010-07-21 02:29:03

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-07-28 01:37:37

When this is ready, could you produce it as a Mercurial patch file?


---

Comment by ncohen created at 2010-07-28 02:44:03

Of course of course ! :-)


---

Comment by ncohen created at 2010-09-04 11:30:19

This ticket should be closed as a duplicate of #9836 `:-)`

Nathann


---

Comment by mvngu created at 2010-09-10 12:50:52

Close as duplicate of #9836.


---

Comment by mvngu created at 2010-09-10 12:50:52

Resolution: duplicate
