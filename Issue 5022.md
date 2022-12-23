# Issue 5022: Solaris 10: update libgcrypt to 1.4.3

Issue created by migration from https://trac.sagemath.org/ticket/5022

Original creator: mabshoff

Original creation time: 2009-01-19 10:16:45

Assignee: mabshoff

The update fixes two important issues:

 * padlock support has been fixed, so we don't need to disable it
 * gcrypt no longer needs huge amounts of entropy which made key generation a pain. The bug was introduced in gcrypt 1.4 and affected Solaris among other platforms.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 10:33:49

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-19 10:33:49

The updated spkg can be found at


http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/libgcrypt-1.4.3.spkg

Cheers,

Michael


---

Comment by mhansen created at 2009-01-19 10:37:53

Looks good to me.


---

Comment by mabshoff created at 2009-01-19 10:42:20

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 10:42:20

Merged in Sage 3.3.alpha0
