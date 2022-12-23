# Issue 7550: lapack ignores setting of SAGE_FORTRAN and uses 'gfortran'

Issue created by migration from https://trac.sagemath.org/ticket/7550

Original creator: drkirkby

Original creation time: 2009-11-28 21:58:16

Assignee: tbd

Many packages ignore CC and CXX, but lapack-20071123.p0 is ignoring SAGE_FORTRAN. 

With SAGE_FORTRAN set to a Sun Fortran compiler, 

export SAGE_FORTRAN=/opt/xxxsunstudio12.1/bin/f95

lapack builds with 'sage_fortran'


```
sage_fortran -fPIC  -c sgbbrd.f -o sgbbrd.o
sage_fortran -fPIC  -c sgbcon.f -o sgbcon.o
sage_fortran -fPIC  -c sgbequ.f -o sgbequ.o
```


It's not clear what compiler is being used here, but when checking what processes are running, I noted that 'gfortran' (the GNU fortran compiler) was running. I then killed that (pkill -9 gfortran) and so the build of lapack immediately stopped. 

This does not need to be reported upstream, as it is the file patches/make.inc which is setting the compiler to be 'sage_fortran' and not to whatever the environment variable SAGE_FORTRAN is set to. This file clearly shows that the fortran compiler is being set to 'sage_fortran'.


```
#  Modify the FORTRAN and OPTS definitions to refer to the
#  compiler and desired compiler options for your machine.  NOOPT
#  refers to the compiler options desired when NO OPTIMIZATION is
#  selected.  Define LOADER and LOADOPTS to refer to the loader and 
#  desired load options for your machine.
#
FORTRAN  = sage_fortran -fPIC
#OPTS     = -funroll-all-loops -O3

```



Dave 




---

Comment by drkirkby created at 2009-11-28 23:42:00

This was an error on my part. William's explanation is clear and correct. I will mark it as closed and invalid.

---

SAGE_FORTRAN is an environment variable that is ***ONLY*** supposed to
impact one spkg, and one spkg only -- the fortran spkg.  It is not
supposed to do anything at all ever to the lapack or any other spkg.
If it does, that is a mistake.    So in one sense lapack is ignoring
SAGE_FORTRAN, as it should.  However, it is making indirect use of the
fact that SAGE_FORTRAN was set when the fortran spkg was installed.

The SAGE_FORTRAN environment variable does not mean "build any spkg
that uses fortran using this fortran".  It means "when installing the
fortran spkg, setup the the sage_fortran script run the fortran
specified by the !SAGE_FORTRAN variable".

William


---

Comment by drkirkby created at 2009-11-28 23:42:00

Resolution: invalid
