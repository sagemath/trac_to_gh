# Issue 3301: Fix POSIX issues in gmp's spkg-install

Issue created by migration from https://trac.sagemath.org/ticket/3301

Original creator: mabshoff

Original creation time: 2008-05-25 20:26:39

Assignee: mabshoff


```
Ubuntu 8.04, 64-bit.

Fails to build GMP.  All before this seems to work ok.

First message that looks suspect in "install.log" is:

Patching gmp-h.in (fixes OSX 10.5 issues and gcc 4.3 problems)
Do we have a Core2 CPU?... No
[: 220: ==: unexpected operator
```




---

Comment by mabshoff created at 2008-07-31 01:13:45

The issue has been resolved in Sage 3.0.6.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 01:13:45

Resolution: fixed
