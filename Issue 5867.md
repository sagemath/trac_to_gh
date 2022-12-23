# Issue 5867: Fix gd build on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/5867

Original creator: pjeremy

Original creation time: 2009-04-23 06:56:11

Assignee: mabshoff

On FreeBSD, libiconv will be installed in /usr/local/lib - which is not searched by default.  Explicitly add /usr/local/lib to LDFLAGS to ensure it is correctly detected by the gd configure script.


---

Attachment


---

Comment by mabshoff created at 2009-04-23 07:30:57

I will work on integrating this tomorrow.

Cheers,

Michael


---

Comment by mhansen created at 2009-06-20 02:07:31

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 02:07:31

Looks good to me.

The spkg with this fix is at http://sage.math.washington.edu/home/mhansen/gd-2.0.35.p2.spkg


---

Comment by mhansen created at 2009-06-20 02:07:31

Changing assignee from mabshoff to mhansen.


---

Comment by rlm created at 2009-07-02 22:26:58

Resolution: fixed
