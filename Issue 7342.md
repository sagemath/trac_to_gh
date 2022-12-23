# Issue 7342: installing kash3-2008-07-31 spkg fails on OS X

Issue created by migration from https://trac.sagemath.org/ticket/7342

Original creator: was

Original creation time: 2009-10-29 00:39:42

Assignee: tbd

CC:  dimpase

The kash3 optional spkg doesn't work at all on OS X:


```
x kash3-2008-07-31/src/KASH3-Linux-2008-07-31.tar.bz2
x kash3-2008-07-31/src/KASH3-Darwin-2008-07-31.tar.bz2
Finished extraction
****************************************************
Host system
uname -a:
Darwin d-69-91-159-10.dhcp4.washington.edu 10.0.0 Darwin Kernel Version 10.0.0: Fri Jul 31 22:47:34 PDT 2009; root:xnu-1456.1.25~1/RELEASE_I386 i386
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin10
Configured with: /var/tmp/gcc/gcc-5646~6/src/configure --disable-checking --enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.2/ --with-slibdir=/usr/lib --build=i686-apple-darwin10 --with-gxx-include-dir=/include/c++/4.2.1 --program-prefix=i686-apple-darwin10- --host=x86_64-apple-darwin10 --target=i686-apple-darwin10
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5646)
****************************************************
Usage:
  List:    tar -tf <archive-filename>
  Extract: tar -xf <archive-filename>
  Create:  tar -cf <archive-filename> [filenames...]
  Help:    tar --help
Error extracting kash.

real	0m0.050s
user	0m0.037s
sys	0m0.011s
sage: An error occurred while installing kash3-2008-07-31
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/wstein/s/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/Users/wstein/s/spkg/build/kash3-2008-07-31 and type 'make'.
Instead type "/Users/wstein/s/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/wstein/s/spkg/build/kash3-2008-07-31
(When you are done debugging, you can type "exit" to leave the
subshell.)
```



---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by slelievre created at 2020-08-22 07:17:20

Resolution: invalid
