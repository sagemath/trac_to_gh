# Issue 7033: libfplll can't find _gmpz_init in -lgmp

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 14:51:48

Assignee: tbd

CC:  dimpase

Keywords: solaris gmp

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021

CC was set to the Sun C compiler, and CXX to the Sun C++ compiler, 


```
checking whether we are using the GNU C++ compiler... (cached) no
checking whether /opt/xxxsunstudio12.1/bin/CC accepts -g... (cached) yes
checking dependency style of /opt/xxxsunstudio12.1/bin/CC... (cached) none
checking for gcc... (cached) /opt/xxxsunstudio12.1/bin/cc
checking whether we are using the GNU C compiler... (cached) no
checking whether /opt/xxxsunstudio12.1/bin/cc accepts -g... (cached) yes
checking for /opt/xxxsunstudio12.1/bin/cc option to accept ISO C89... (cached) none needed
checking dependency style of /opt/xxxsunstudio12.1/bin/cc... (cached) none
checking whether make sets $(MAKE)... (cached) yes
checking for __gmpz_init in -lgmp... no
configure: error: GNU MP not found, see http://gmplib.org
Error configuring libfplll

real    0m45.568s
user    0m10.239s
sys     0m25.294s
```


mpir is insalled ok - all the gmp headers and libraries have been built. I suspect some programs not to accept mpir as being the same as gmp when the compiler is not gcc.


---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by slelievre created at 2020-08-22 07:15:47

Resolution: invalid
