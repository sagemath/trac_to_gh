# Issue 784: quotient spaces of vector spaces

Issue created by migration from https://trac.sagemath.org/ticket/784

Original creator: nbruin

Original creation time: 2007-10-02 13:38:11

Assignee: was

If V is a subspace of W then W.quotient(V) should give the quotient space U=W/V.

Left TODO:
  - overload "/" constructor ?
  - provide a section map U->W ?
  - install appropriate coercions ?


---

Comment by nbruin created at 2007-10-02 13:39:24

implementation


---

Attachment

implementation


---

Comment by nbruin created at 2007-10-02 13:44:56

use fix.patch; not 6540.patch.


---

Comment by nbruin created at 2007-10-02 13:46:02

Resolution: duplicate
