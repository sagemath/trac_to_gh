# Issue 9852: Enumerate Integer solution of a LP through new CPLEX interface

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-09-03 18:39:05

Assignee: jason, jkantor

CC:  nthiery

This tickets implements a new (and direct) interface to CPLEX, using its C library. We are now able to iterate over integer solutions of a MILP, which is a *very* good news (after quite a lot of work debugging Cython code) `:-D`

I also updated the method MixedIntegerLinearProgram.solve to show two different ways to use CPLEX. #8880 is not needed either anymore once this patch is merged.

Tips for the reviewer :

    * Do not read the parts of the .patch file related to the changes in files mip_cplex and mip_osi cplex. Here is what happened : the former file named mip_cplex has been renamed to mip_osi_cplex (as it uses CPLEX through the OSI library), and the mip_cplex file is brand new, and contains the new interface. Of course, I changed in the docstrings of mip_osi_cplex lines such as 
     {{{
     from sage.numerical.mip_cplex import [something]
     }}}
     to
     {{{
     from sage.numerical.mip_osi_cplex import [something]
     }}}
     So there is no need to deal with all these - and + lines.
   *  Please, pick an enumeration problem that you like, and check CPLEX is indeed returning ALL the solutions. It first "forgot" some of them, and I had to change a very badly documented parameter to get all the answers I wanted for my problems. Please check on some other examples `:-)`

Nathann


---

Comment by ncohen created at 2010-09-03 18:41:02

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-09-06 11:11:01

Changing component from numerical to linear programming.


---

Attachment


---

Comment by ncohen created at 2010-09-19 10:53:14

(just added a sage_free where I had forgotten it) `:-)`

Nathann


---

Comment by ncohen created at 2010-09-23 15:44:41

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-10-09 08:36:41

This ticket also modifies files which are deleted by #10043. I'll rewrite it using the new interface anyway !

Nathann


---

Comment by mpatel created at 2010-10-09 08:46:15

Resolution: invalid


---

Comment by nthiery created at 2012-01-04 23:29:04

Why was this ticket considered as invalid?


---

Comment by ncohen created at 2012-01-04 23:36:53

> Why was this ticket considered as invalid?

Because it worked on an ooooooold version of the LP backends, that have been totally rewritten since. But it is nice to have this code around, because I remember I went through hell to find the CPLEX methods that should be use to enumerate integer solutions.

This being said, we have a Gurobi backend too, now. Perhaps it can also enumerate integer solutions.


---

Comment by nthiery created at 2012-01-05 01:02:22

Replying to [comment:8 ncohen]:
> Because it worked on an ooooooold version of the LP backends, that have been totally rewritten since. But it is nice to have this code around, because I remember I went through hell to find the CPLEX methods that should be use to enumerate integer solutions.
> 
> This being said, we have a Gurobi backend too, now. Perhaps it can also enumerate integer solutions.

Ok, so it's more like the current patch is invalid. The feature would still be useful (be it implemented through CPLEX or other). So, unless there is another ticket for this feature, I would recommend to (have the release manager?) reopen this ticket.

Cheers,
                                Nicolas
