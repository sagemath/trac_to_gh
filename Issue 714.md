# Issue 714: The line(s) in interfaces/* like this are bad.  Should kill -9: print "WARNING: -- unable to kill %s. You may have to do so manually."%self

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-20 18:36:19

Assignee: malb




---

Comment by malb created at 2007-09-20 19:01:36

The attached patch 'fixes' that by raising an exception instead. This way hopefully bugreports can be gathered to properly fix the problem.


---

Attachment


---

Comment by was created at 2007-09-20 19:05:52

Resolution: fixed
