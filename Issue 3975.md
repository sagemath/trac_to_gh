# Issue 3975: Small mistake in the new plot() code.

Issue created by migration from https://trac.sagemath.org/ticket/3975

Original creator: anakha

Original creation time: 2008-08-28 14:42:56

Assignee: was

delta is computed with xmin and xmax in the wrong order resulting in a negative delta.

This makes the rest of the code go very slowly.




---

Attachment


---

Attachment

I posted a rebased patch which should apply with all of the new plotting patches applied.

Positive review.


---

Comment by mabshoff created at 2008-08-28 20:39:47

Resolution: fixed


---

Comment by mabshoff created at 2008-08-28 20:39:47

Merged in Sage 3.1.2.alpha2
