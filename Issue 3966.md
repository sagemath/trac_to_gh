# Issue 3966: The ode cython example gives errors

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-08-27 15:47:56

Assignee: jkantor

The gsl ode_solver Cython/Pyrex example gives errors because the jacobian isn't passed (and doesn't need to be!).  This patch fixes the code and also changes the %pyrex to %cython


---

Attachment


---

Comment by jwmerrill created at 2008-08-28 02:04:31

This looks good to me.  All doctests still pass, and the cython example in the docs now works, although it is still not automatically tested.


---

Comment by mabshoff created at 2008-08-29 03:20:36

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-29 03:20:36

Resolution: fixed
