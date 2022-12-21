# Issue 7035: R sends the correct Sun flags to C and C++ compilers, but not Fortran.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 15:16:37

Assignee: tbd

Keywords: solaris gfortran

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler and SAGE_FORTRAN to the Sun Fortran 95 compiler. While R sends the correct flags (-KPIC) to make position independent code to the Sun C and C++ compilers, it does not do so with the Fortran compiler. Instead it used the GNU flag -fPIC. R is however picking up the correct Fortran compiler (f95 and not gfortran)


```
/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c tabulate.c -o tabulate.o
/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c uncmin.c -o uncmin.o/opt/xxxsunstudio12.1/bin/cc -I. -I../../src/include -I../../src/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/inlcude -DHAVE_CONFIG_H   -KPIC  -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -L/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/lib/  -c zeroin.c -o zeroin.osage_fortran  -PIC  -g -c ch2inv.f -o ch2inv.o
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
sage_fortran  -PIC  -g -c chol.f -o chol.o
```



---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.


---

Comment by mkoeppe created at 2021-08-26 19:09:47

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2021-08-26 19:09:47

Outdated, should close


---

Comment by mjo created at 2021-10-04 22:57:59

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-10-04 23:44:13

Resolution: invalid
