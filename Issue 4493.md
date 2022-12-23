# Issue 4493: derivative and integral of a matrix

Issue created by migration from https://trac.sagemath.org/ticket/4493

Original creator: jason

Original creation time: 2008-11-11 18:22:50

Assignee: burcin

It would be handy in differential equations to be able to do differentiation and integration of matrices and vectors, with the exact same answer as obtained by using the apply_map method.


---

Comment by jason created at 2008-12-05 06:45:03

Changing status from new to assigned.


---

Comment by jason created at 2008-12-05 06:45:03

Changing assignee from burcin to jason.


---

Comment by jason created at 2008-12-05 08:14:51

This depends on #4713

I guess the integral of a matrix doesn't come up that often, so I'm changing my request.  Besides, the integral can calculated using the apply_map function at #4713 for vectors or the existing apply_map function for matrices.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-12-07 09:59:29

Resolution: fixed


---

Comment by mabshoff created at 2008-12-07 09:59:29

Merged both patches in Sage 3.2.2.alpha1
