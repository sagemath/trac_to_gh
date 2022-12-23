# Issue 3513: modular symbols -- remove the compute_dual option to decomposition

Issue created by migration from https://trac.sagemath.org/ticket/3513

Original creator: was

Original creation time: 2008-06-26 03:14:28

Assignee: craigcitro

This is broken and shouldn't be used anyways.


---

Attachment


---

Comment by AlexGhitza created at 2008-07-03 17:28:35

See the attached trivial patch.  I doctested everything under sage/modular.


---

Comment by AlexGhitza created at 2008-07-03 17:28:35

Changing component from algebra to modular forms.


---

Comment by mabshoff created at 2008-07-06 10:57:47

Since Craig promised to take care of the review I am making him editor :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 10:57:47

Changing keywords from "" to "editor_craigcitro".


---

Comment by craigcitro created at 2008-07-06 21:32:45

Looks good. The changes make sense, and testing `sage/modular/` works fine.


---

Comment by mabshoff created at 2008-07-07 01:38:33

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-07 01:38:33

Resolution: fixed
