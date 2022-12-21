# Issue 5253: Make a jacobian function which computes the jacobian matrix

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-02-13 05:08:19

Assignee: burcin

Attached patch computes the Jacobian matrix, the matrix of partial derivatives of a multivariable function from R^n to R^m.


---

Attachment


---

Comment by jason created at 2009-02-13 05:49:18

Changing status from new to assigned.


---

Comment by jason created at 2009-02-13 05:49:18

Changing assignee from burcin to jason.


---

Comment by cwitty created at 2009-02-13 18:52:41

Does what it says, code looks reasonable, all doctests pass.  (I'm not sure if the set of special cases controlling which types it will handle is "right", but that can be fixed later if somebody has specific complaints.)

Positive review.


---

Comment by jason created at 2009-02-13 19:45:23

FYI, the special casing is because there is no good way right now to represent a function from R<sup>n</sup> to R<sup>m</sup>.  I think people would naturally use either a list, tuple, or vector of symbolic expressions.  The Matrix special case is so that you can do nested jacobians to compute the hessian matrix, like what is illustrated in the doctests.


---

Comment by mabshoff created at 2009-02-14 09:03:39

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 09:03:39

Resolution: fixed
