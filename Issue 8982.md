# Issue 8982: Fix jacobian for ode_solver example.

Issue created by migration from https://trac.sagemath.org/ticket/8982

Original creator: lfousse

Original creation time: 2010-05-17 11:33:57

Assignee: burcin

The jacobian used for the Van der Pol oscillator in the gsl/ode.pyx file has wrong dimensions 3x2. The example runs fine as the last line is ignored. The attached patch corrects that.


---

Attachment

You should mark the ticket as `needs_review` when you submit a patch. This will put it on the relevant trac reports http://trac.sagemath.org/sage_trac/report/30 and http://trac.sagemath.org/sage_trac/report/10.


---

Comment by burcin created at 2010-05-22 11:54:55

Changing status from new to needs_review.


---

Comment by burcin created at 2010-05-22 11:57:01

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-05-22 11:57:01

Looks good to me.


---

Comment by mhansen created at 2010-06-06 01:30:18

Resolution: fixed
