# Issue 1298: [with spkg] To build atlas on osx, we need to actual build lapack on osx.

Issue created by migration from https://trac.sagemath.org/ticket/1298

Original creator: jkantor

Original creation time: 2007-11-28 09:47:57

Assignee: jkantor

The current lapack.spkg doesn't build on osx (because osx intel has one in /usr/lib)
Since we will buid atlas on all platforms, we need to build lapack on osx. 

http://sage.math.washington.edu/home/jkantor/spkgs/lapack-20071123.spkg 




               


---

Comment by mabshoff created at 2007-12-01 23:21:22

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-01 23:25:04

Resolution: fixed


---

Comment by mabshoff created at 2007-12-01 23:25:04

Merged in 2.8.15.alpha2.
