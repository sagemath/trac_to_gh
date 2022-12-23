# Issue 955: Singular interface (and possibly others) can lose synchronization due to GC

Issue created by migration from https://trac.sagemath.org/ticket/955

Original creator: cwitty

Original creation time: 2007-10-21 03:50:22

Assignee: was

I'm going to describe the problem in terms of the Singular interface, but I think probably at least some other interfaces are similarly vulnerable.

The bad sequence of events is:

 1) Some Singular computation is requested, by calling Singular.eval().

 2) Singular.eval() calls Expect.eval().

 3) Expect.eval() sends a command to Singular, to perform the requested computation.

 4) A Python garbage collection is triggered.

 5) One of the collected objects is a Singular wrapper object (of type SingularElement).

 6) Singular.clear() is called on this object.

 7) Singular.clear() calls Singular.eval() to kill the Singular variable corresponding to this object.

 8) Singular.eval() calls Expect.eval().

 9) Expect.eval() sends the kill command to Singular.

 10) Expect.eval() waits for a response from Singular.  Unfortunately, the next response it sees from Singular is the response to the command sent in step 3), from the mathematical computation.

 11) Expect.eval() returns this response to Singular.eval().

 12) Singular.eval() returns this response to Singular.clear().

 13) Singular.clear() discards the response.

 14) Garbage collection completes.

 15) Expect.eval() waits for a response from Singular.  Unfortunately, the next response it sees from Singular is the null response from the kill command.

 16) Expect.eval() returns this response to Singular.eval().

 17) Singular.eval() returns this null response as the result of the requested computation.

I'll attach two log files to this ticket; log7027 shows the interface working, and log7028 shows the interface failing because the print(sage10); command is interrupted by the command to kill sage7.


---

Attachment


---

Attachment


---

Comment by was created at 2007-10-21 06:22:23

See rings/morphism.pyx for an example of this that is # not tested right now.


---

Comment by cwitty created at 2007-10-25 05:34:04

Changing status from new to assigned.


---

Comment by cwitty created at 2007-10-25 05:34:04

Changing assignee from was to cwitty.


---

Comment by cwitty created at 2007-10-25 05:41:28

Release 2.8.8 had a patch for this that fixed most or all of the issues with Singular.  However, other interfaces are still vulnerable to the same problem.  All interfaces should be audited and fixed.


---

Attachment

I've fixed several places that looked slightly dubious, although I could have missed something.

The attached patch will be in 2.8.10.


---

Comment by cwitty created at 2007-10-27 18:02:30

Resolution: fixed
