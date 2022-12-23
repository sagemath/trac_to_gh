# Issue 1540: lapack.spkg: remove elf binaries from src/INSTALL

Issue created by migration from https://trac.sagemath.org/ticket/1540

Original creator: mabshoff

Original creation time: 2007-12-16 20:26:33

Assignee: mabshoff

As discussed in http://groups.google.com/group/sage-devel/t/13109b350bd5876c  we should remove the Linux elf binaries in src/INSTALL. They seem to cause trouble with certain OSX compilers. An updated  lapack.spkg is at

http://sage.math.washington.edu/home/mabshoff/lapack-20071123.p0.spkg

Cheers,

Michael


---

Comment by rlm created at 2007-12-18 20:57:20

Resolution: fixed


---

Comment by rlm created at 2007-12-18 21:07:00

Merged in 2.9.1.alpha1
