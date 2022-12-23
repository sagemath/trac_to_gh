# Issue 5868: Fix libgcrypt shared library name on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/5868

Original creator: pjeremy

Original creation time: 2009-04-23 07:00:46

Assignee: mabshoff

Ensure that a symlink is created from libgcrypt.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.




---

Attachment


---

Comment by mabshoff created at 2009-04-23 07:31:17

I will work on integrating this tomorrow.

Cheers,

Michael


---

Comment by mhansen created at 2009-06-20 02:12:25

Looks good to me.

The spkg with this change can be found at http://sage.math.washington.edu/home/mhansen/libgcrypt-1.4.3.p1.spkg


---

Comment by mhansen created at 2009-06-20 02:12:25

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-20 02:12:25

Changing status from new to assigned.


---

Comment by rlm created at 2009-07-02 22:32:12

Resolution: fixed
