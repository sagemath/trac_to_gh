# Issue 1775: clicking on 'search worksheets' can log you out.

Issue created by migration from https://trac.sagemath.org/ticket/1775

Original creator: bill.p

Original creation time: 2008-01-14 10:44:00

Assignee: boothby

I have just succeeded in creating a personal id on my sage server (as opposed to admin).
When I logged in I wondered what 'search worksheets' might do so I clicked on it
and found I had been logged out! An error message which left me logged in would be
much better.


---

Comment by was created at 2008-01-14 14:51:54

I can not replicate this.  You might have been confused about whether or not you were actually logged in or something?  Please give clear step-by-step directions that allow you to replicate tis problem every time.


---

Comment by bill.p created at 2008-01-14 15:17:33

William, I have just created a new user (charlie) via the 'Create new user' on
the login page method. Logged in as Charlie, then clicked on 'Search worksheets'
and it logged me out:
-------------------------------------------------------
Login failure
You have entered an invalid username. Please try again.

Valid login names:
admin,
charlie,
bill 
-------------------------------------------------------


---

Comment by was created at 2008-01-14 15:46:39

OK, I can definitely replicate this bug now, so we should easily be able to fix it.


---

Comment by TimothyClemans created at 2008-08-27 16:55:30

I can't reproduce this at https://sage.math.washington.edu:8102


---

Comment by mhansen created at 2009-01-23 12:43:32

I cannot duplicate this in Sage 3.2.3 either.  I'm going to mark it as invalid at this point.


---

Comment by mhansen created at 2009-01-23 12:43:32

Resolution: invalid
