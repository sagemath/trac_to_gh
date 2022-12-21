# Issue 2131: disable "padlock" support in libgcrypt

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-02-09 20:39:06

Assignee: mabshoff

On some OS/compiler variants, the "Padlock" support fails to compile.

See http://groups.google.com/group/sage-devel/browse_thread/thread/9d4b39e961c24e4f/89bfb1cd2822ffd2?lnk=gst&q=rijndael#89bfb1cd2822ffd2 for details.

The easy fix is to add "--disable-padlock-support" in the call to configure.


---

Comment by mabshoff created at 2008-02-14 11:20:35

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.2/alpha0/libgcrypt-1.4.0.p0.spkg

adds the option Paul suggested. It passes compile tests on 32 and 64 bit Linux boxen.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 11:20:35

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-02-14 11:21:30

Merged in Sage 2.10.2.alpha0

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-14 11:21:30

Resolution: fixed
