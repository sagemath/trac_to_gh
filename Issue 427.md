# Issue 427: backslash infix operator does not print properly in documentation

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-08-13 20:50:31

Assignee: was

CC:  mhansen

The infix operator '\' does not print properly in the notebook
when used in the examples of solve_right (for a matrix)
(file:
`local/lib/python/site-packages/sage/matrix/matrix2.pyx`)
I suspect that these backslashes simply end up escaping the space after them. Some more preprocessing may be needed to escape backslashes occurring in examples in documentation?



---

Comment by nbruin created at 2007-08-13 20:50:56

Changing component from algebraic geometry to user interface.


---

Comment by nbruin created at 2007-08-13 20:50:56

Changing priority from major to minor.


---

Comment by mabshoff created at 2008-10-26 02:33:40

What is the status here?

Cheers,

Michael


---

Comment by mhansen created at 2009-01-22 13:57:45

This behaves fine in the Sphinx documentation.


---

Comment by mhansen created at 2009-01-22 13:57:45

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2009-01-22 13:57:45

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-02-21 23:41:21

Yes, please close this.


---

Comment by mabshoff created at 2009-02-21 23:45:47

Replying to [comment:5 jhpalmieri]:
> Yes, please close this.

Thanks John, this will be closed once the ReST patches are in.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:57:21

Fixed by the ReST merge in 3.4.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 19:57:21

Resolution: fixed
