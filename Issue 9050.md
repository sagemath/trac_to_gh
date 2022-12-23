# Issue 9050: libntl.dll should be libntl.dll.a on Cygwin

Issue created by migration from https://trac.sagemath.org/ticket/9050

Original creator: mhansen

Original creation time: 2010-05-25 22:54:28

Assignee: tbd

This is so that Cygwin will find the shared library before it finds the static library; otherwise, there are lots of segfaults in Sage under Cygwin


---

Comment by mhansen created at 2010-05-25 22:57:53

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-05-25 22:57:53

There is an spkg for this at http://sage.math.washington.edu/home/mhansen/ntl-5.4.2.p12.spkg


---

Comment by was created at 2010-05-26 01:08:21

Resolution: fixed
