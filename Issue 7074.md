# Issue 7074: cvxopt-0.9.p8 sends GNU options to Sun Fortran compiler and has bad C code.

Issue created by migration from https://trac.sagemath.org/ticket/7074

Original creator: drkirkby

Original creation time: 2009-09-29 13:51:32

Assignee: tbd

CC:  dimpase

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha4
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used #7021 


```
cvxopt-0.9.p8/spkg-install
cvxopt-0.9.p8/.hgignore
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
f95: Warning: Option -fPIC passed to ld, if ld is invoked, ignored otherwise
f95: Warning: Option --version passed to ld, if ld is invoked, ignored otherwise
Usage: f95 [ options ] files.  Use 'f95 -flags' for details
Using gfortran
running install
running build
running build_py
creating build
creating build/lib.solaris-2.10-sun4u-2.6
creating build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/__init__.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/misc.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/cvxprog.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/modeling.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/info.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/coneprog.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
copying python/solvers.py -> build/lib.solaris-2.10-sun4u-2.6/cvxopt
running build_ext
building 'base' extension
creating build/temp.solaris-2.10-sun4u-2.6
creating build/temp.solaris-2.10-sun4u-2.6/C
/opt/xxxsunstudio12.1/bin/cc -DNDEBUG -O -xcode=pic32 -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include/python2.6 -c C/base.c -o build/temp.solaris-2.10-sun4u-2.6/C/base.o
"C/sun_complex.h", line 30: invalid type combination
"C/sun_complex.h", line 30: incomplete _Imaginary type specifier
"C/sun_complex.h", line 30: warning: useless declaration
"C/sun_complex.h", line 30: warning: typedef declares no type name
"C/misc.h", line 29: incomplete _Complex type specifier
```



---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mjo created at 2020-07-12 20:04:33

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by mjo created at 2020-07-12 20:04:33

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid
