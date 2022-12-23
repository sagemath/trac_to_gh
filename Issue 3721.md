# Issue 3721: [with patch; needs review] Use SAGE_TESTDIR for dsage unit tests

Issue created by migration from https://trac.sagemath.org/ticket/3721

Original creator: tabbott

Original creation time: 2008-07-25 05:31:34

Assignee: yi

dsage tests currently ignore the SAGE_TESTDIR environment variable, resulting in permission denied errors for users who don't have write access to their Sage install.

I've attached a patch to fix this.


---

Attachment


---

Comment by mabshoff created at 2008-07-31 00:56:42

Patch looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 00:58:36

Merged in Sage 3.1.alpha0


---

Comment by mabshoff created at 2008-07-31 00:58:36

Resolution: fixed
