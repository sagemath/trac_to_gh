# Issue 4103: Delete the cmap option for vector field plots

Issue created by migration from https://trac.sagemath.org/ticket/4103

Original creator: jason

Original creation time: 2008-09-12 04:03:03

Assignee: was

The cmap argument for vector field plots is not used.  Does anyone know why it's there?  I don't think it's even valid matplotlib code.

This patch deletes the option.


---

Attachment


---

Comment by mabshoff created at 2008-09-19 02:22:12

Patch looks good to me. Assuming it passes doctests (which are running now) this is a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-19 03:13:52

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 03:13:52

Merged in Sage 3.1.3.alpha0
