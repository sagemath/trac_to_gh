# Issue 1354: [with patch] Solaris modp 64 bit fix

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-01 21:22:23

Assignee: mabshoff

We are currently only compiling Solaris in 32 bit mode. Then a 64 int has to be a long long. Fix that so that all the modp doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-01 21:25:49

Resolution: fixed


---

Attachment

Merged in 2.8.15.alpha2.
