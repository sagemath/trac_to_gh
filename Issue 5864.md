# Issue 5864: Correctly inherit build environment in eclib

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2009-04-23 06:35:45

Assignee: mabshoff

Change 'make' to ${MAKE} - is the recommended way to recursively invoke make to ensure that the subordinate make is the same as the parent make (and also ensures that the two make instances will communicate on things like '-jX').

Explicitly use gmake instead of make on FreeBSD.


---

Attachment


---

Comment by mhansen created at 2009-06-20 07:24:49

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 07:24:49

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-20 07:24:49

Looks good to me.

The spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/eclib-20080310.p8.spkg


---

Comment by cremona created at 2009-06-20 14:07:01

I am confused here.  I already have a .p8 version, dated 2009-01-07.  Now you have created a new .p8 which must be different!

Checking the SPKG.txt in my p8 I see this entry:
### eclib-20080310.p8 (John Cremona, January 6th, 2009)
 * Change to debugging output in procs/p2points.cc (not relevant for Sage)
 * Change to pdivs() in procs/marith.cc (not relevant for Sage)

I suggest that we syncronise, otherwise I will get even more confused.  For a start, this ticket should have had me in its CC list!  I don't see how I can be expected to be responsible for this spkg if people are changing it without even telling me!

Hence I have changed this back to "needs work".


---

Comment by pjeremy created at 2010-07-13 20:05:51

This ticket is no longer needed with eclib-20080310.p10


---

Comment by pjeremy created at 2010-07-13 20:05:51

Resolution: fixed
