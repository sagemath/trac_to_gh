# Issue 944: "sage -t ." does not run doctests in the current directory

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-20 17:05:01

Assignee: failure

"sage -t ." should run the doctests in the current directory, but it doesn't.  It looks like maybe it fails when the directory name starts with a period:


```
cwitty`@`magnetar:~/sage/devel/sage/sage/rings/polynomial$ ~/sage/sage -t .
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds
cwitty`@`magnetar:~/sage/devel/sage/sage/rings/polynomial$ ~/sage/sage -t ../polynomial/
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds
```




---

Comment by gfurnish created at 2008-03-21 14:18:21

Resolution: fixed


---

Comment by gfurnish created at 2008-03-21 14:18:21

Fixed in sage-ptest
