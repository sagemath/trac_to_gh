# Issue 2791: [with patch; needs review] Build symmetrica with -fPIC on Debian

Issue created by migration from https://trac.sagemath.org/ticket/2791

Original creator: tabbott

Original creation time: 2008-04-03 06:15:23

Assignee: tabbott

Now that the linbox bug is fixed, I tried to build SAGE itself, and am running into more -fPIC problems.  Attached is a patch to make symmetric build with -fPIC.

Though really, we should fix the symmetrica build system.  


---

Attachment


---

Comment by mabshoff created at 2008-04-03 11:25:13

Patch looks good to me. The patch will be in the updated symmetrica-2.0.p2.spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-03 11:25:42

Resolution: fixed


---

Comment by mabshoff created at 2008-04-03 11:25:42

Merged in Sage 3.0.alpha1
