# Issue 6533: sage >= 4.1.rc1 doesn't build on cleo (ia64-Linux-rhel5)

Issue created by migration from https://trac.sagemath.org/ticket/6533

Original creator: was

Original creation time: 2009-07-14 18:39:01

Assignee: tbd

The Sage library fails to build (when linking symmetrica) on  ia64-Linux-rhel5.  I am investigating this. Note that sage-4.1.rc0 built fine, and there are minimal changes between rc0 and rc1. 


---

Comment by was created at 2009-11-11 17:43:16

According to the sysadmin, this appears to be a problem with the binutils and compiler setup on that computer.  So I'm closing this as invalid for now.


---

Comment by was created at 2009-11-11 17:43:16

Resolution: invalid
