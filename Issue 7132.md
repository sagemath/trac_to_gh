# Issue 7132: mpir-1.2.p7 fails to build as CXXFLAGS has no 64-bit option on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/7132

Original creator: drkirkby

Original creation time: 2009-10-06 00:04:42

Assignee: tbd

CC:  dimpase

I'm using the following hardware and software now.
    * A Sun Blade 2000 running Solaris 10 update 7
    * Sage 4.1.2.rc0
    * gcc 4.4.1
    * SAGE64 exported to "yes" 

mpir-1.2.p7 consists of both C and C++ code, but although the spkg-install is adding -m64 to CFLAGS, it is not doing this to CXXFLAGS on Solaris. Hence it attempts to build with a mix of 32 and 64-bit binaries, which gives the usual error:

ld: fatal: file .libs/dummy.o: wrong ELF class: ELFCLASS32
quired

A look at the object files, clearly shows some are built 32-bit, whilst others are 64-bit. 



```
./cxx/.libs/ismpf.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
./cxx/.libs/ismpq.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
./cxx/.libs/osfuns.o:   ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
./cxx/.libs/ismpz.o:    ELF 32-bit MSB relocatable SPARC32PLUS Version 1, V8+ Required
```


though others (not shown) are 64-bit as they are supposed to be. 

There are a number of packages in Sage building as 32-bit on Solaris, despite SAGE64 being set to "yes" This include, but are almost certainly not limited to:

 * zlib #7128
 * libgpg_error #7129
 * libpng #7130
 * libcliquer #7131

mpir fails to build at all, since it is trying to mix 32 and 64-bit objects. 

The fix to this will be quite easy, but I will wait until I've written a better sage-env, which will mean the correct flags for 64-bit will be generated on all platforms and compilers we can possibly envisage. Whilst -m64 works with Sun and GNU compilers, it will not work with native compilers on AIX or HP-UX. 



---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-07-14 16:30:34

Resolution: invalid
