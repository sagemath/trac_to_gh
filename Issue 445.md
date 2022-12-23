# Issue 445: serious issue with how interupting subprocesses sometimes behaves.

Issue created by migration from https://trac.sagemath.org/ticket/445

Original creator: was

Original creation time: 2007-08-18 21:09:45

Assignee: was


 1. Start a hard calc in magma, e.g., ask if polynomial is irreducible.
 2. interrupt in notebook.
 3. OK get sage back, but magma is not really interupted!  it's still running.

This is BAD.



---

Comment by was created at 2007-09-20 18:19:57

Resolution: fixed
