# Issue 7047: lapack sends GNU option -fPIC to Sun fortran compiler.

Issue created by migration from https://trac.sagemath.org/ticket/7047

Original creator: drkirkby

Original creation time: 2009-09-28 09:13:11

Assignee: tbd

CC:  dimpase

Using
    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha4
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021 

I tried to build Sage with Sun Studio and see:


```
lapack-20071123.p0/spkg-install~
lapack-20071123.p0/spkg-install
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
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/lapack-20071123.p0/src'
( cd INSTALL; make; ./testlsame; ./testslamch; \
  ./testdlamch; ./testsecond; ./testdsecnd; ./testversion )
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/lapack-20071123.p0/src/INSTALL'
sage_fortran -fPIC  -c lsame.f -o lsame.o
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
sage_fortran -fPIC  -c lsametst.f -o lsametst.o
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
sage_fortran  -o testlsame lsame.o lsametst.o
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
ld: fatal: option -f and building a dynamic executable are incompatible
ld: fatal: Flags processing errors
make[3]: *** [testlsame] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/lapack-20071123.p0/src/INSTALL'
/bin/sh: ./testlsame: not found
/bin/sh: ./testslamch: not found
/bin/sh: ./testdlamch: not found
/bin/sh: ./testsecond: not found
/bin/sh: ./testdsecnd: not found
/bin/sh: ./testversion: not found
make[2]: *** [lapack_install] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/lapack-20071123.p0/src'
Error compiling lapack.

real    0m0.415s
user    0m0.150s
sys     0m0.215s
```



---

Comment by drkirkby created at 2009-11-09 14:07:41

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2011-05-25 07:22:46

Are you sure this is not an upstream problem? You appear to have set a number of tickets to N/A, but that might not be the case. 

Dave


---

Comment by ltw created at 2011-05-25 17:57:46

Replying to [comment:3 drkirkby]:
> Are you sure this is not an upstream problem? You appear to have set a number of tickets to N/A, but that might not be the case. 
> 
> Dave 

I simply modified the descriptions so that tickets would be referenced as "#NNNN" rather than by URL (see: http://groups.google.com/group/sage-devel/browse_thread/thread/a97f1a4473848617). I could not figure out why Trac kept thinking that I set the upstream field, even though I never touched it. My apologies if I ruined something!


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mjo created at 2020-07-12 20:05:25

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by mjo created at 2020-07-12 20:05:25

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
