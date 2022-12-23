# Issue 5869: Fix libgpg-error shared library name on FreeBSD

Issue created by migration from https://trac.sagemath.org/ticket/5869

Original creator: pjeremy

Original creation time: 2009-04-23 07:04:38

Assignee: tbd

Ensure that a symlink is created from libgpg-error.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.



---

Attachment

I will work on integrating this tomorrow.

Cheers,

Michael


---

Comment by pjeremy created at 2009-04-23 08:51:41

Changing assignee from tbd to mabshoff.


---

Comment by pjeremy created at 2009-04-23 08:51:41

Changing component from algebra to freebsd.


---

Comment by mhansen created at 2009-06-20 07:02:23

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-06-20 07:02:23

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 07:02:23

Looks good to me.

The spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/libgpg_error-1.6.p1.spkg .


---

Comment by rlm created at 2009-07-02 22:37:59

Resolution: fixed
