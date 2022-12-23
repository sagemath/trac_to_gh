# Issue 5904: [with patch, needs review] improve doctest coverage for schemes/jacobians/abstract_jacobian.py

Issue created by migration from https://trac.sagemath.org/ticket/5904

Original creator: AlexGhitza

Original creation time: 2009-04-26 11:34:46

Assignee: was

Keywords: abstract jacobian doctest

The attached patch improves the doctest coverage of `abstract_jacobian.py` from 0% to 85% (6 of 7).



---

Attachment


---

Comment by AlexGhitza created at 2009-04-26 11:43:40

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-04-26 11:43:40

Changing assignee from was to AlexGhitza.


---

Comment by cremona created at 2009-04-27 19:49:53

Looks good, applies cleanly to 3.4.2.alpha0 and tests pass.  I guess there is no point in adding this to the reference manual as it has no actual functionality really.  (As admitted in notes.txt).


---

Comment by mabshoff created at 2009-04-30 01:55:18

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 01:55:18

Resolution: fixed
