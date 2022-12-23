# Issue 6110: [with patch, needs review] implement a "decorator" to allow pickling nested classes

Issue created by migration from https://trac.sagemath.org/ticket/6110

Original creator: cwitty

Original creation time: 2009-05-21 09:10:24

Assignee: cwitty

CC:  craigcitro

The nested_pickle decorator modifies nested classes to be picklable.  (In Python 2.6 it should be usable as a decorator, although that hasn't been tested; Python 2.5 doesn't support class decorators, so you can't use that syntax in Sage until it upgrades.)


---

Attachment

Reviewer patch, with demo of metaclass


---

Attachment

I just uploaded a super patch (for sage 3.4.2) which:
 - Demonstrates the use a metaclass call nested_pickle automatically on a class, *and all derived subclasse*. Potential application: put this on Category, and all categories would be handled properly. Same thing on Parent? Hmm.
 - Fix nested_pickle to handle old-style classes


---

Comment by was created at 2009-05-28 07:15:51

Perfect for 4.0.1.


---

Comment by robertwb created at 2009-06-10 08:46:49

Looks and works well for me. Lets get this pickle stuff in.


---

Comment by ncalexan created at 2009-06-13 21:53:38

Resolution: fixed
