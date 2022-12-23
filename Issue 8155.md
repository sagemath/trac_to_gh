# Issue 8155: add sig_on/sig_off to sage.schemes.elliptic_curves.descent_two_isogeny

Issue created by migration from https://trac.sagemath.org/ticket/8155

Original creator: rlm

Original creation time: 2010-02-02 19:02:30

Assignee: cremona

Otherwise a KeyboardInterrupt will be ignored during the call to ratpoints.


---

Comment by rlm created at 2010-02-02 19:04:09

Changing status from new to needs_review.


---

Comment by cremona created at 2010-02-06 17:27:19

Changing status from needs_review to positive_review.


---

Attachment

I applied the patch successfully to 4.3.2 with the spkg and patches at #8184 already applied, with no problem.

Testing the whole library (without -long):  all test pass.   Positive review!


---

Comment by mpatel created at 2010-02-11 14:30:53

Resolution: fixed
