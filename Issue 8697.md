# Issue 8697: Add basic generic test methods

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-04-16 21:37:32

Assignee: tbd

Keywords: generic tests

In SageObject:

 - _test_eq: tests self == self, (self != self) == False, (self == None) == False, self != None (this would have caught #8695)

 - _test_hash: test that the result of __hash__ is an int or that it raises an appropriate exception

 - Please Florent, add here what we had thought about


---

Comment by hivert created at 2010-04-16 23:37:29

>  - Please Florent, add here what we had thought about

This looks like a duplicate of #8402... and should be closed.


---

Comment by nthiery created at 2010-04-18 10:02:26

Resolution: duplicate


---

Comment by nthiery created at 2010-04-18 10:02:26

Replying to [comment:1 hivert]:
> >  - Please Florent, add here what we had thought about
> 
> This looks like a duplicate of #8402... and should be closed.

Oops, right. Sorry.
