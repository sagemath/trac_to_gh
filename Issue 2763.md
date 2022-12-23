# Issue 2763: [with patch; needs review] Debian amd64 fixes for rubiks

Issue created by migration from https://trac.sagemath.org/ticket/2763

Original creator: tabbott

Original creation time: 2008-04-01 22:14:11

Assignee: tabbott

Apparently my rubiks Debian package failed to distclean, and thus some i386 binaries managed to survive during the amd64 build, which produced a very confusing error from dpkh-shlibdeps.  The attached patch fixes this.


---

Attachment

Patch is good. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-01 23:26:44

Merged in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-04-01 23:26:44

Resolution: fixed
