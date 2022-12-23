# Issue 7025: givaro 3.2.13rc2 says GMP is not installed, even though MPIR is.

Issue created by migration from https://trac.sagemath.org/ticket/7025

Original creator: drkirkby

Original creation time: 2009-09-27 11:11:06

Assignee: tbd

CC:  dimpase

MPIR is supposed to be a substitute for GMP. When using the Sun compiler with sage-4.1.2.alpha2, givaro-3.2.13rc2 seems to think GMP is not installed, even though the substitute mpir is installed. See below. 

It works on Solaris if gcc is used, which is a bit odd. I checked to see if the mpir had created the header files and libraries, and see that local/include/gmp.h and local/lib/libgmp.* do in fact exist, so mpir really has been installed. 



```
givaro-3.2.13rc2/src/examples/Polynomial/pol_eval.C
givaro-3.2.13rc2/src/examples/Polynomial/pol_factor.C
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
Copying updated gmp++.h
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... ./install-sh -c -d
<SNIP>
checking for GMP >= 3.1.1... not found
*******************************************************************************
 ERROR: GMP not found!

 GMP version 3.1.1 or greater is required for this library to compile. Please
 make sure GMP is installed and specify its location with the option
 --with-gmp=<prefix> when running configure.
*******************************************************************************
Error configuring givaro

real    0m22.266s
user    0m7.925s
sys     0m13.148s
```



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

Comment by slelievre created at 2020-08-22 07:15:11

Resolution: invalid
