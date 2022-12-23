# Issue 6233: remove the explain_picklejar function, since it is self contained and its test fails on all platforms

Issue created by migration from https://trac.sagemath.org/ticket/6233

Original creator: was

Original creation time: 2009-06-06 16:16:24

Assignee: tbd

The doctest for explain_picklejar fails on all platforms.  Thus the choice is to either remove explain_pickle entirely, fix the bug (needs cwitty), or remove that one function.  This ticket removes that one function explain_picklejar until cwitty fixes it. 


---

Attachment


---

Comment by was created at 2009-06-15 23:48:24

Note that I think this was merged into 4.0.1 already, over a week ago in order to get that release out.


---

Comment by mhansen created at 2009-06-20 01:59:36

Resolution: fixed


---

Comment by mhansen created at 2009-06-20 01:59:36

Yep.  I believe this was.
