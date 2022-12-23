# Issue 6707: Sage will try to build on compilers known to be too old.

Issue created by migration from https://trac.sagemath.org/ticket/6707

Original creator: drkirkby

Original creation time: 2009-08-09 10:02:38

Assignee: tbd

ratpoints needs at least gcc 4.0.1, but the configure script will permit any gcc version of >= 3.0.0 from being used. 

See also trac #6701


---

Comment by drkirkby created at 2009-09-27 10:47:27

Changing component from algebra to build.


---

Comment by was created at 2009-10-07 15:42:59

Resolution: fixed
