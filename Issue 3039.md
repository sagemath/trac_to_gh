# Issue 3039: [with patch; needs review] Improve auto-generated version numbers for Debian packages

Issue created by migration from https://trac.sagemath.org/ticket/3039

Original creator: tabbott

Original creation time: 2008-04-27 02:36:29

Assignee: tabbott




---

Attachment


---

Comment by tabbott created at 2008-04-27 02:39:04

Oops, forgot the text.

This patch changes the auto-generated versions for Debian packages so that 
1) alpha and rc versions are lower than the final versions (by appending ~ before them)
2) the Debian revisions start with 0 (so that if Debian comes out with its own version of the same version of the package, the Debian version number will be higher)
3) the Debian version numbers include sage in them so that it's obvious from the version number that this is a package that may have been modified for use with SAGE.


---

Comment by mabshoff created at 2008-04-27 02:48:04

Patch looks good to me and applies cleanly. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-27 02:48:19

Merged in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-27 02:48:19

Resolution: fixed
