# Issue 7860: sage_fortran builds 32-bit exuctabes when SAGE64=yes

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-06 22:25:37

Assignee: drkirkby

CC:  was jsp

I'm trying to make a 64-bit build of Sage on my Sun Ultra 27, but although I've sorted out many packages which do not honour SAGE64, the sage_fortran package is unique, and I don't have a clue how to fix it. 

I've also set FCFLAGS to -m64, but that is being ignored. 

I've marked this as critical, as it really will inhibit progress on Sage on Open Solaris if this bit insists on building 32-bit executables. Overall, it seems less hassle to build 64-bit on Open Solaris than 32-bit, due to the OpenSSL issues.

Dave 


```
sage_fortran -fPIC  -c sgerqf.f -o sgerqf.o
sage_fortran -fPIC  -c sgesc2.f -o sgesc2.o
sage_fortran -fPIC  -c sgesdd.f -o sgesdd.o
sage_fortran -fPIC  -c sgesv.f -o sgesv.o
sage_fortran -fPIC  -c sgesvd.f -o sgesvd.o
^Cmake: *** [all] Interrupt

drkirkby`@`hawk:~/sage-4.3.1.alpha1$ find . -name sgerfs.o
./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o
drkirkby`@`hawk:~/sage-4.3.1.alpha1$ file ./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o
./spkg/build/lapack-20071123.p0/src/SRC/sgerfs.o:	ELF 32-bit LSB relocatable 80386 Version 1
drkirkby`@`hawk:~/sage-4.3.1.alpha1$ echo $SAGE64
yes
```



---

Comment by jsp created at 2010-01-07 13:29:15

Not so strange if you have:


{{{#!/bin/sh

/usr/bin/gfortran -fPIC $`@`

```


this is my sage_fortran

Jaap


---

Comment by drkirkby created at 2010-01-10 04:09:31

At the very least you would have to add -m64 to that, but that does not solve the problems - still things are build 32-bit, so screw up.


---

Comment by jdemeyer created at 2012-04-30 10:06:29

Is this still  a problem?


---

Comment by jdemeyer created at 2014-04-12 12:04:14

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-04-12 12:04:14

Close as obsolete (`sage_fortran` is no longer used).


---

Comment by jdemeyer created at 2014-04-12 12:04:18

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-04-13 14:52:22

Resolution: wontfix
