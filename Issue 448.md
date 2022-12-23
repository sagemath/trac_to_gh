# Issue 448: add spkg-check to all packages

Issue created by migration from https://trac.sagemath.org/ticket/448

Original creator: mabshoff

Original creation time: 2007-08-19 05:34:57

Assignee: was

spkg-check should be run upon demand after spkg-install has been run but before the build directory is deleted. In spkg-check any possible "make check" target the package offers should be run in order to catch bugs early on, especially on more exotic platforms.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-19 05:36:16

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2007-08-21 13:11:42

This is a duplicate of #299. Because the description in #299 is better than mine I will close this ticket and assign #299 to the Sage-3.0 milestone.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-21 13:11:42

Resolution: duplicate
