# Issue 6493: new scipy-0.7.p2 spkg is broken on 64-bit OS X

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-09 03:45:17

Assignee: mabshoff

To replicate this on OS X:

 1. export SAGE64="yes"
 2. Try to build Sage, which will fail because of Fortran
 3. install the experimental fortran spkg:

```
sage -i fortran-OSX64-20090120
```

 4. fix ratpoints using the spkg in #6492
 5. continue the build and get the following error.  Note that scipy used to work, for sage-4.0.  So something got messed up when we ugpraded scipy.



```
...
Fortran f77 compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch i686 -fPIC -O3 -funroll-loops
Fortran f90 compiler: sage_fortran -Wall -fno-second-underscore -arch ppc -arch i686 -fPIC -O3 -funroll-loops
Fortran fix compiler: sage_fortran -Wall -ffixed-form -fno-second-underscore -Wall -fno-second-underscore -arch ppc -arch i686 -fPIC -O3 -funroll-loops
creating build/temp.macosx-10.3-i386-2.6
creating build/temp.macosx-10.3-i386-2.6/scipy
creating build/temp.macosx-10.3-i386-2.6/scipy/fftpack
creating build/temp.macosx-10.3-i386-2.6/scipy/fftpack/src
creating build/temp.macosx-10.3-i386-2.6/scipy/fftpack/src/dfftpack
compile options: '-I/Users/was/build/64bit/sage-4.1.rc1/local/lib/python2.6/site-packages/numpy/core/include -c'
sage_fortran:f77: scipy/fftpack/src/dfftpack/dcosqb.f
scipy/fftpack/src/dfftpack/dcosqb.f:0: error: CPU you selected does not support x86-64 instruction set
lipo: can't figure out the architecture type of: /var/tmp//cc7wivPN.out
scipy/fftpack/src/dfftpack/dcosqb.f:0: error: CPU you selected does not support x86-64 instruction set
lipo: can't figure out the architecture type of: /var/tmp//cc7wivPN.out
error: Command "sage_fortran -Wall -ffixed-form -fno-second-underscore -arch ppc -arch i686 -fPIC -O3 -funroll-loops -I/Users/was/build/64bit/sage-4.1.rc1/local/lib/python2.6/site-packages/numpy/core/include -c -c scipy/fftpack/src/dfftpack/dcosqb.f -o build/temp.macosx-10.3-i386-2.6/scipy/fftpack/src/dfftpack/dcosqb.o" failed with exit status 1
Error building scipy.

real    0m28.097s
user    0m26.180s
sys     0m1.497s
sage: An error occurred while installing scipy-0.7.p2
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/was/build/64bit/sage-4.1.rc1/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/was/build/64bit/sage-4.1.rc1/spkg/build/scipy-0.7.p2 and type 'make'.
Instead type "/Users/was/build/64bit/sage-4.1.rc1/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/was/build/64bit/sage-4.1.rc1/spkg/build/scipy-0.7.p2
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/scipy-0.7.p2] Error 1

real    39m40.718s
user    34m27.276s
sys     4m20.496s
Error building Sage.
wstein`@`bsd:~/build/64bit/sage-4.1.rc1$ 
```



---

Comment by was created at 2009-07-09 04:17:26

It turns out this is caused by a bug in numpy :-).    I commented out the not-needed line that is patched here http://projects.scipy.org/numpy/ticket/1087 and the build completes fine.  So here is a new numpy spkg.  

With this package and the patched ratpoints, sage builds completely 64-bit on OS X.

http://sage.math.washington.edu/home/wstein/patches/numpy-1.3.0.p0.spkg


---

Comment by mvngu created at 2009-07-17 08:49:38

Replying to [comment:1 was]:
> It turns out this is caused by a bug in numpy :-).    I commented out the not-needed line that is patched here http://projects.scipy.org/numpy/ticket/1087 and the build completes fine.  So here is a new numpy spkg.  
> 
> With this package and the patched ratpoints, sage builds completely 64-bit on OS X.
> 
> http://sage.math.washington.edu/home/wstein/patches/numpy-1.3.0.p0.spkg
I'm renaming this spkg to `numpy-1.3.0.p1.spkg` since there is already an spkg called `numpy-1.3.0.p0.spkg` in Sage 4.1. This is to prevent confusion later on: people might wonder why Sage 4.1 and (the upcoming) Sage 4.1.1 each has a numpy spkg with the same name as each other, but patched differently. The renamed spkg is up at

http://sage.math.washington.edu/home/mvngu/patch/numpy-1.3.0.p1.spkg


---

Comment by mvngu created at 2009-07-17 08:49:38

Resolution: fixed
