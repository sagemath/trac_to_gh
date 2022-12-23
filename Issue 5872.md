# Issue 5872: [with patch, needs review] Explicitly pass -fPIC into ntl shared object build.

Issue created by migration from https://trac.sagemath.org/ticket/5872

Original creator: pjeremy

Original creation time: 2009-04-23 08:06:35

Assignee: mabshoff

The ntl makefile appears to rely on compiler flags specified as a target dependency being passed to the compiler.  This fails on at least FreeBSD, resulting in an attempt to include non-PIC objects in a shared library.

Instead, explicitly pass -fPIC to the sub-make used for the shared object build.



---

Attachment

Looks good to me.

The spkg incorporating this patch can be found at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p8.spkg


---

Comment by mhansen created at 2009-06-20 07:13:30

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-20 07:13:30

Changing assignee from mabshoff to mhansen.


---

Comment by rlm created at 2009-07-02 22:58:58

Resolution: fixed
