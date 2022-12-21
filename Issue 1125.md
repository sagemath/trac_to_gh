# Issue 1125: cvxopt fix completely breaks building Sage with gfortran

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-07 19:06:15

Assignee: was


```
> 
> Compiling from source using gcc-4.2.2, I get
> 
> ***
> x86-Linux, ia64-Linux
> ***
> While compiling cvxopt-0.8.2.p4, I get
> 
> gcc -pthread -shared build/temp.linux-i686-2.5/C/base.o
> build/temp.linux-i686-2.5/C/dense.o
> build/temp.linux-i686-2.5/C/sparse.o
> -L/home/kate/sage/sage-2.8.12-x86-Linux/local/lib
> -L/home/kate/sage/sage-2.8.12-x86-Linux/local/lib/gcc-lib/i686-pc-linux-gnu/4.0.3
> -lm -llapack -lblas -lf95 -o build/lib.linux-i686-2.5/cvxopt/base.so
> /usr/local/binutils-2.17/x86-Linux-gcc-4.1.1/bin/ld: cannot find -lf95

That's because you're using gfortran.  Evidently Josh's fix for cvxopt not fully working
fails for people using gfortran.  I'll open a trac ticket. 

```



This either has to be properly fixed, or cvxopt has to be removed or something.
We need to make sure we fully support using gfortran.  Perhaps we should just
completely switch to using gfortran and make having gfortran installed a requirement for building sage.  Tempting.  


---

Comment by was created at 2007-11-07 19:06:46

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2007-11-08 20:05:32

Waiting on feedbackk from Kate, but there is a new spkg by Josh:

http://sage.math.washington.edu/home/jkantor/spkgs/cvxopt-0.8.2.p5.spkg

Cheers,

Michael


---

Comment by jkantor created at 2007-11-17 01:16:40

The spkg in 1161 incorporates the fix for this and also upgrades cvxopt to a newer version.


---

Comment by mabshoff created at 2007-11-18 06:17:49

Resolution: fixed


---

Comment by mabshoff created at 2007-11-18 06:17:49

superseded by #1161, which also contains this fix.
