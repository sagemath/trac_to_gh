# Issue 3093: [with patch; needs review] Debian lcalc package missing -DINCLUDE_PARI flag

Issue created by migration from https://trac.sagemath.org/ticket/3093

Original creator: tabbott

Original creation time: 2008-05-03 08:22:40

Assignee: tabbott

The Debian package for lcalc was missing the -DINCLUDE_PARI flag.  Also, it had a useless setting of CFLAGS.  This patch fixes these issues.


---

Attachment

Patch is correct, hence positive review. Slipped into lcalc-20080205.p0.spkg without bumping the release number.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 14:29:27

Merged in Sage 3.0.1.final


---

Comment by mabshoff created at 2008-05-03 14:29:27

Resolution: fixed
