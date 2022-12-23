# Issue 3508: gmp-4.2.2.spkg is severly broken

Issue created by migration from https://trac.sagemath.org/ticket/3508

Original creator: mabshoff

Original creation time: 2008-06-25 02:06:47

Assignee: mabshoff

There are various issues at play here:

 * configure from patches is from GMP 4.2.1
 * the Core2 patches do not apply since Jason's script detects the version mismatch
 * GMP 4.2.2 in general misdetects some very new Core2 Quads and Core2 Xeons as 32 bit Intel CPUs

Fix all those issues!

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-25 02:06:56

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-07 06:04:16

We put the old gmp-4.2.1.p14.spkg into Sage 3.0.4.alpha2 and will deal with this issue later.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 02:57:01

Resolution: invalid


---

Comment by mabshoff created at 2008-08-30 02:57:01

We will switch to eMPIRe anyway, so let's invalidate this ticket.

Cheers,

Michael
