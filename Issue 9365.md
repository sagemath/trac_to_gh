# Issue 9365: sage-4.5.alpha0: R fails to build on OS X 10.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-28 21:08:45

Assignee: GeorgSWeber

See

  http://sage.math.washington.edu/home/wstein/tmp/install-4.5.alpha0.log

and 

  http://sage.math.washington.edu/home/justin/logs/install-4.5.a0.log

for potentially two different issues with building R on OS X 10.6


---

Comment by drkirkby created at 2010-06-28 21:17:09

I suspect it is related to this - #9346 

Dave


---

Comment by rlm created at 2010-06-30 01:11:08

The fix for Justin's problem is up at #9388.

I suspect the fixes to fortran in 4.5.alpha1 will fix William's, so once we see a successful R build on bsd.math, we can close this ticket.


---

Comment by rlm created at 2010-06-30 22:10:17

This has been fixed by the fortran spkg updates in sage-4.5.alpha1.


---

Comment by rlm created at 2010-06-30 22:10:17

Resolution: worksforme
