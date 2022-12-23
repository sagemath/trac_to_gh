# Issue 2846: [with patch] no need for bitset.h with new Cython

Issue created by migration from https://trac.sagemath.org/ticket/2846

Original creator: robertwb

Original creation time: 2008-04-07 18:36:43

Assignee: cwitty

I've modified the .pxi file


---

Attachment


---

Comment by mabshoff created at 2008-04-07 20:49:22

Patch looks good to me, passes a {{-ba}} followed by a successful `testall long`. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 20:50:30

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-07 20:50:30

Resolution: fixed
