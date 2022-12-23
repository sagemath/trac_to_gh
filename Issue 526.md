# Issue 526: better support for parallel make

Issue created by migration from https://trac.sagemath.org/ticket/526

Original creator: dmharvey

Original creation time: 2007-08-30 04:30:52

Assignee: was

CC:  dmharvey@math.harvard.edu

a.k.a. `make -j`

See discussion at

http://groups.google.com/group/sage-devel/browse_thread/thread/a88d59dc35404507



---

Comment by mabshoff created at 2007-11-20 14:09:14

Changing keywords from "" to "package audit".


---

Comment by mabshoff created at 2007-11-20 14:09:14

The issue has been solved and needs to be properly documented. If you do

```
export MAKE="make -j4"
make
```

Sage will be build with up to 4 jobs in parallel. Spkgs like Singular which do not build properly with parallel make make sure that MAKE is reset while building themselves.

So somebody send us a patch for the manual. We also need to audit all packages and change make to $MAKE.

Cheers,

Michaek


---

Comment by gfurnish created at 2008-03-09 05:15:12

Changing assignee from was to gfurnish.


---

Comment by gfurnish created at 2008-03-09 05:15:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-26 09:18:25

Changing assignee from gfurnish to mabshoff.


---

Comment by mabshoff created at 2008-09-26 09:18:25

This has been fixed. Every spkg that can be build in parallel does get build that way.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 09:18:25

Changing status from assigned to new.


---

Comment by mabshoff created at 2008-09-26 09:18:33

Resolution: fixed
