# Issue 3331: [with patch, needs review] Disable --incref-local-binop in pbuild

Issue created by migration from https://trac.sagemath.org/ticket/3331

Original creator: gfurnish

Original creation time: 2008-05-29 19:18:27

Assignee: gfurnish

CC:  robertwb

Keywords: pbuild

The --incref-local-binop option in cython seems to be unneeded, and costs performance and readability.


---

Attachment


---

Comment by gfurnish created at 2008-05-29 19:19:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-31 06:11:00

Patch looks good to me. Positive review. 

Robert: I think we can apply the same patch to the current build system. Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-31 06:12:15

Merged in Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-05-31 06:12:15

Resolution: fixed


---

Comment by robertwb created at 2008-06-02 17:47:01

Yep, that's fine. The only reason it was there was to enable inplace operators, but there's issues with NumPy so it's already disabled in the code.
