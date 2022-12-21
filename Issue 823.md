# Issue 823: make atlas standard in Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-04 15:56:26

Assignee: mabshoff




---

Comment by mabshoff created at 2007-10-04 16:07:56

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-10-27 06:39:57

What needs to be done:

 * update to 3.8.0
 * use sage_fortran to build the f77 wrapper, the flag --no-f77 doesn't work properly
 * build a complete Lapack by using netlib.org's F77 Lapack

Getting ATLAS into Sage will probably be a coding sprint project during SD6.

Cheers,

Michael


---

Comment by jkantor created at 2007-11-24 00:25:37

new package that should resolve all these issues. 

http://sage.math.washington.edu/spkgs/atlas-3.8.spkg

One important point. For atlas to build a correct lapack, we must have already built an lapack and then merge with atlas libs to get a full one. On OSX we don't build lapack  so the above package will fail. To use the above on OSX first install this spkg 

http://sage.math.washington.edu/spkgs/lapack-20071123.spkg

This will build lapack even on OSX. Then atlas can be installed.

Also on OSX even with atlas installed, numpy and scipy build against the accelerate framework still.


---

Comment by jkantor created at 2007-11-27 06:23:11

I just noticed that building the cvxopt package with this atlas causes a missing symbol error for the cvxopt package

_g95_ioparm

I'm mystified by this. Need to investigate.


---

Comment by jkantor created at 2007-11-28 06:05:55

Ignore the cvxopt package issue, it was a mistake on my part, I think atlas is ready to go.


---

Comment by jkantor created at 2007-11-28 22:37:38

the atlas3.8 package didn't have mabshoff's patch so that the shared objects are copied by make install 

http://sage.math.washington.edu/home/jkantor/spkgs/atlas-3.8.p1.spkg


---

Comment by jkantor created at 2007-11-28 22:40:52

Problem: 

Atlas does not build shared libraries on OSX. 

THis is because on OSX the atlas build script does 

ld -melf_i386 -shared -soname libatlas.so -o libatlas.so \
        --whole-archive libatlas.a --no-whole-archive -lc -lm
ld: unknown flag: -melf_i386


This is a problem with atlas not knowing that on osx we don't want elf, 

probably should be -dynamiclib or something.


---

Comment by jkantor created at 2007-11-29 02:26:01

On OSX the ld options --whole_archive don't exist. 

The following appears to produce a shared atlas from the static one

ld -dylib -o libatlas.dylib  -lm -lc -all_load libatlas.a

(-L must be set appropriately)


---

Comment by jkantor created at 2007-11-30 06:08:02

New package

http://sage.math.washington.edu/home/jkantor/atlas-3.8.p2.spkg

This package fixes problems with the shared libraries lapack creates on linux (the lapack.so doesn't not have the same symbols as lapack.a)

It also creates libatlas and libcblas shared on OSX using the trick in the previous comment, but I have not yet resolved how to make libf77blas or liblapack shared on OSX.  It might be best 
to not do this on OSX till we create the whole thing. Thoughts


---

Comment by mabshoff created at 2007-12-13 06:42:12

Resolution: fixed
