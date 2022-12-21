# Issue 5870: Detect blas and atlas libraries for linbox on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2009-04-23 07:12:05

Assignee: mabshoff

spkg-install for linbox uses OS-specific code to detect and use the BLAS and Atlas libraries.  Add code to support FreeBSD.


---

Attachment


---

Comment by mabshoff created at 2009-04-23 07:32:08

I will work on integrating this tomorrow.

Cheers,

Michael


---

Comment by mhansen created at 2009-06-20 07:29:21

Looks good to me.

An spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/linbox-1.1.6.p0.spkg


---

Comment by mhansen created at 2009-06-20 07:29:21

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-20 07:29:21

Changing status from new to assigned.


---

Comment by rlm created at 2009-07-02 22:47:41

Resolution: fixed
