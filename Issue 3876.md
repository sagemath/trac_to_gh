# Issue 3876: Add plotting to sigma function

Issue created by migration from https://trac.sagemath.org/ticket/3876

Original creator: kcrisman

Original creation time: 2008-08-15 17:54:23

Assignee: was

First attempt at adding plotting to sigma (sum-of-divisors) function.


---

Attachment


---

Attachment

Adds plotting to the Euler phi function


---

Comment by kcrisman created at 2008-08-24 04:00:19

Changing status from new to assigned.


---

Comment by kcrisman created at 2008-08-24 04:00:19

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2008-08-24 04:00:19

Two patches which turn sigma and euler_phi into classes Sigma and Euler_Phi, allowing addition of plot methods like that of the M/moebius function.


---

Comment by cswiercz created at 2008-09-16 23:18:53

Plotting of both function works great! All doctests pass!


---

Comment by cswiercz created at 2008-09-16 23:18:53

Resolution: fixed


---

Comment by mabshoff created at 2008-09-17 00:26:13

Ehh, somebody asleep here? Tickets get closed once they are merged :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-17 00:26:13

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-09-17 00:26:13

Changing status from closed to reopened.


---

Comment by cswiercz created at 2008-09-17 00:50:13

Oops. Sorry about that. I guess I was asleep!


---

Comment by mabshoff created at 2008-09-19 04:03:58

Merged both patches in Sage 3.1.3.alpha0


---

Comment by mabshoff created at 2008-09-19 04:03:58

Resolution: fixed
