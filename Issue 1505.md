# Issue 1505: make M4RI a shared library

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-12-14 12:41:26

Assignee: malb

We are not the only ones anymore who use M4RI, PolyBoRi (which deputs in Sage 2.9) also uses M4RI. Thus we should make M4RI a shared library to not duplicate code/memory.


---

Comment by malb created at 2007-12-16 15:02:50

spkg here:

   http://sage.math.washington.edu/home/malb/pkgs/libm4ri-20071216.spkg

stand-alone shared lib:

   http://sage.math.washington.edu/home/malb/pkgs/libm4ri-1.0.0.tar.gz

patch for Sage:

   attached


---

Attachment


---

Comment by malb created at 2007-12-16 15:03:45

oh, 'make test' passes on 64-bit Linux.


---

Comment by rlm created at 2007-12-22 18:53:22

Resolution: fixed


---

Comment by rlm created at 2007-12-22 18:53:22

merged in 2.9.1 rc0
