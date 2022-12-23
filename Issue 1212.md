# Issue 1212: make gfortran mandatory on OSX 10.5

Issue created by migration from https://trac.sagemath.org/ticket/1212

Original creator: mabshoff

Original creation time: 2007-11-20 00:36:10

Assignee: was

scipy and cvxopt still fail to build on 10.5 with the binary g95 compiled for 10.4. So on 10.5 make gfortran mandatory and otherwise error out early.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 09:39:01

Updated spkg at http://sage.math.washington.edu/home/mabshoff/fortran-20071120.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-20 09:39:21

Merged in 2.8.13.rc0.


---

Comment by mabshoff created at 2007-11-20 09:39:21

Resolution: fixed
