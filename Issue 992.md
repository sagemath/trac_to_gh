# Issue 992: Need an extra "sage -b" after an upgrade

Issue created by migration from https://trac.sagemath.org/ticket/992

Original creator: was

Original creation time: 2007-10-25 02:08:34

Assignee: was

When doing sage -ugprade, i.e., running SAGE_ROOT/devel/sage/spkg-install, there should be one extra "sage -b"  again at the end to ensure that the new versions of all .pyx files get copied to the build directory.


This is incredibly easy to fix.


---

Attachment

this probably fixes the problem, though it is hard to test.  time will tell.


---

Comment by was created at 2007-10-25 07:56:36

Resolution: fixed
