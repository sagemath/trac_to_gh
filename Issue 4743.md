# Issue 4743: [with spkg; needs review] change genus2reduction to include GPL copyright file and email from liu making the program GPL'd

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-08 21:11:57

Assignee: mabshoff

The new spkg is here:

  http://sage.math.washington.edu/home/was/patches/genus2reduction-0.3.p4.spkg

I am upstream for this program.  I modified the src/ subdirectory to include the GPL COPYING file, along with an email Liu sent me where he officially GPL'd genus2reduction. 

This change was caused by a request from Karl Meyer who is packaging sage for Fedora. 


---

Comment by mabshoff created at 2008-12-10 06:36:53

Looks good to me. One change that was missing was the addition of an SPKG.txt entry which I have added.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 06:37:05

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-10 06:37:05

Resolution: fixed
