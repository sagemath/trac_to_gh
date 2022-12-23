# Issue 5358: major bug in missing import of escape in twist.py

Issue created by migration from https://trac.sagemath.org/ticket/5358

Original creator: was

Original creation time: 2009-02-24 14:44:39

Assignee: boothby

twist.py uses escape but doesnt' import it.  This is a bug introduced in #5258 by bad refereeing. 


---

Attachment


---

Comment by jason created at 2009-02-24 15:22:59

With all due respect, the bug was introduced by the author of the patch (me), not the reviewer (you).  You take too much credit :).

This patch looks good, but I haven't applied it or doctested it.  I'm upgrading to 3.3 now to be able to try that.

Really, this should have been caught in a doctest, so another +1 towards getting notebook doctesting working!


---

Comment by was created at 2009-02-24 18:39:47

I caught it by watching the server log on sagenb.org and seeing a traceback.  That's definitely not an ideal way to find something like this ;-)


---

Comment by jason created at 2009-02-24 22:08:16

The patch applies cleanly and I don't see any errors running the notebook with it applies.  It certainly seems like it would cause errors not to have it applied. Positive review.


---

Comment by mabshoff created at 2009-02-28 15:56:36

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 15:56:36

Merged in Sage 3.4.rc0.

Cheers,

Michael
