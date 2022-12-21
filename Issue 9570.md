# Issue 9570: Wrong LP solver ordering

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-07-22 02:55:20

Assignee: jason, jkantor

At the moment, GLPK is the solver used regardless of the presence of CBC or CPLEX. This is just because of a line written ten lines too high in the file !

Nathann


---

Comment by ncohen created at 2010-07-22 02:57:28

Changing status from new to needs_review.


---

Attachment


---

Comment by lsampaio created at 2010-07-23 08:19:16

Fixes the AttributeError that was returned when no mip solver was specified by the user


---

Attachment

I applied your patch, but while trying to solve an MIP without specifying a solver, I've got an AttributeError, since the attribute '_default_solver' was not defined.
I just fixed this by adding a line stating that _default_solver = None.
If you agree with my changes, I think the patch can be said to be reviwed.


---

Comment by ncohen created at 2010-07-23 09:09:38

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-07-23 09:09:38

Excellent ! Thank you very much for your help :-)

Both apply fine and in the end, it works... Now the annoying part is #8880 because CPLEX is called by next-to-any method in the LP library XD

Nathann


---

Comment by ddrake created at 2010-07-26 02:35:08

Resolution: fixed


---

Comment by ddrake created at 2010-07-26 02:35:08

Leonardo -- be sure to use informative commit messages for your patches. "fix" is not very helpful. :)  Always include a ticket number, too. I changed your commit message to "ticket 9570: insure _default_solver attribute exists".

both patches merged in 4.5.2.alpha1.


---

Comment by lsampaio created at 2010-07-26 02:47:00

ok, thanks for the advice =)
